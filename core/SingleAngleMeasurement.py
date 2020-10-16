import os
from core.importFormat import nist_fpga
import numpy as np

from core.CumulantModel import Cumulant

import multiprocessing as mp

from lmfit import minimize, Parameters, Model
import matplotlib.pyplot as plt
from lmfit.models import LinearModel, ExponentialModel

from core.pycorrelate import pcorrelate, correlate_whal

class SingleAngleMeasurement():

    def __init__(self, full_measurement, angle, raw_data):
        self.full_measurement = full_measurement
        self.angle = angle
        self.raw_data = raw_data
        self.correlation_curve = None
        self.error_bar = None
        self.time_axis = None
        self.cumulants = {}

    def import_data(self, file_path):
        if (os.path.isfile(file_path)) is False:
            print("File does not exist")
            return "File does not exist"

        filename, file_extension = os.path.splitext(file_path)
        if file_extension == ".txt":
            # TODO create format for correlation curve text file
            pass

        elif file_extension == ".ttt":
            timestamps, detectors, nanotimes, timestamps_unit, meta = nist_fpga.load_ttt(file_path)
            # self.exp_param.fill_with_ttt_meta_data(meta)

        # The photons (i.e clock tick) are not ordered by detectors but by arrival time.
        unique, return_index, unique_inverse, unique_counts = np.unique(detectors, return_index=True,

        # FIXME check data
                                                                        return_inverse=True, return_counts=True)
        # FIXME ? Hardcoded value
        minimum_nb_of_tick_per_channel = 5

        num_channel = 0
        nb_of_channel = 0
        for value in unique:
            # "minimum_nb_of_tick_per_channel" is arbiratry, we do this to filter false count on some detector.
            if unique_counts[num_channel] > minimum_nb_of_tick_per_channel and value >= 0:
                nb_of_channel += 1
            num_channel += 1

        self.full_measurement.nb_of_channel = nb_of_channel

        num_channel = 0
        soft_channel_value = 0
        self.ticks = []
        for value in unique:
            # 50 is arbiratry, we do this to filter false count on some detector.
            if unique_counts[num_channel] < minimum_nb_of_tick_per_channel or value < 0:
                num_channel += 1
                soft_channel_value += 1
                continue

            # On créé un masque et on fait une copie des elements non masqués vers le channel.
            m_ = np.ma.masked_where(detectors != value, timestamps)
            timestampsMasked = np.ma.compressed(m_)

            # self.ticks = np.empty(unique_counts[soft_channel_value], np.uint64)

            self.ticks.append(timestampsMasked)

        return "OK"

    def correlate_raw_data(self, timestamps_1, timestamps_2, max_correlation_time_in_tick, start_correlation_time_in_tick, nb_of_point_per_cascade_aka_B, tick_duration_micros, algo="Whal"):
        """
        :param timestamps_1:
        :param timestamps_2:
        :param max_correlation_time_in_tick:
        :param start_correlation_time_in_tick:
        :param nb_of_point_per_cascade_aka_B:
        :param tick_duration_micros:
        :return:
        """
        self.tick_duration_micros = tick_duration_micros

        # TODO nb_of_workers based on user preference.
        nb_of_workers = 4

        # Split the timeStamps in array
        self.max_time_in_tick_1 = timestamps_1[-1]
        self.max_time_in_tick_2 = timestamps_2[-1]

        # Arbitrary statement : In order to compute lag at time time, we need at least ratio_lag_vs_file_duration time
        # of data

        # TODO minimum number of photon in a chunk ?
        chunk_boundaries = []
        ratio_lag_vs_file_duration = 6

        # nb_of_chunk = int(self.max_time_in_tick_1/(max_correlation_time_in_tick*ratio_lag_vs_file_duration))

        nb_of_max_cor_time = self.max_time_in_tick_1 / max_correlation_time_in_tick

        i = 0
        N = timestamps_1.size
        # chunk_time_limit = i * ratio_lag_vs_file_duration * max_correlation_time_in_tick
        # boundary = np.searchsorted(timestamps_1, chunk_time_limit)
        boundary = 0
        while boundary != N:
            chunk_boundaries.append(boundary)
            i += 1
            chunk_time_limit = i * ratio_lag_vs_file_duration * max_correlation_time_in_tick
            boundary = np.searchsorted(timestamps_1, chunk_time_limit)

        nb_of_chunk = len(chunk_boundaries)
        #FIXME hardcoded
        if nb_of_chunk > 15:
            nb_of_chunk = 15

        # FIXME Log
        # self.log("nb of chunk : %d\n" % nb_of_chunk)

        # FIXME set minimum value for nb_of_chunk
        # if nb_of_chunk > 10:
        #     nb_of_chunk = 10
        # elif nb_of_chunk < 10:
        #     # diminish the max correlation_time ?
        #     pass

        chunks_of_timestamps_1 = []
        chunks_of_timestamps_2 = []

        for i in range(len(chunk_boundaries) - 1):
            b1_1 = chunk_boundaries[i]
            b2_1 = chunk_boundaries[i + 1]
            chunks_of_timestamps_1.append(timestamps_1[b1_1:b2_1])
            b1_2 = min(b1_1, timestamps_2.size - 1)
            b2_2 = min(b2_1, timestamps_2.size - 1)
            chunks_of_timestamps_2.append(timestamps_2[b1_2:b2_2])

        # TODO fix cross-correlation
        # The last photon is the one that can be correlated with the last point of the correlation curve (max_correlation_time_in_tick)
        self.num_last_photon = np.searchsorted(timestamps_1, self.max_time_in_tick_1 - max_correlation_time_in_tick)
        self.end_time_correlation_tick = timestamps_1[self.num_last_photon]

        self.time_axis = self.create_list_time_correlation(start_correlation_time_in_tick,
                                                           max_correlation_time_in_tick,
                                                           point_per_decade=nb_of_point_per_cascade_aka_B)

        # self.correlation_curve = np.zeros(self.nb_of_correlation_point, dtype=np.int)

        #self.log("Creating a pool of %d workers\n" % nb_of_workers)
        p = mp.Pool(nb_of_workers)
        #self.log("Calculating Correlation \n")
        if algo == "Laurence":
            # Gs = [p.apply(pcorrelate, args=(chunks_of_timestamps_1[i], chunks_of_timestamps_2[i], self.time_axis, True)) for i in range(nb_of_chunk-1)]
            results = [p.apply_async(pcorrelate, args=(
            chunks_of_timestamps_1[i], chunks_of_timestamps_2[i], self.time_axis, True)) for i in
                       range(nb_of_chunk - 1)]
            Gs = [p.get() for p in results]
        elif algo == "Whal":
            results = [p.apply_async(correlate_whal,
                                     args=(
                                     chunks_of_timestamps_1[i], chunks_of_timestamps_2[i],
                                    self.time_axis, 10, True, True)) for i
                       in range(nb_of_chunk - 1)]
            Gs = [p.get() for p in results]

        elif algo == "F2Cor":
            pass
        elif algo == "lin":
            pass

        self.sub_correlation_curves = np.vstack(Gs)

        self.correlation_curve = np.mean(self.sub_correlation_curves, axis=0)
        self.error_bar = np.std(self.sub_correlation_curves, axis=0)

        # self.normalize_correlation()
        self.scale_time_axis()

        if algo == "Laurence":
            # FIXME why ??
            self.time_axis = self.time_axis[:-1]
        # self.log("Calculation complete !\n")

    def scale_time_axis(self):
        self.time_axis = self.tick_duration_micros * self.time_axis.astype(np.float64)


    def create_list_time_correlation(self, start_correlation_time_in_tick, max_correlation_time_tick, point_per_decade):
        B = self.point_per_decade = point_per_decade
        # How many "cascade" do we need ?
        # maxCorrelationTime_tick =  2^(n_casc - 1/B)
        # then ln (maxCorrelationTime_tick) = (n_casc - 1/B) ln 2
        self.nb_of_cascade = int(np.log(max_correlation_time_tick) / np.log(2) + 1 / B)

        """
                 |
                 | 1                                si j = 1
         tau_j = |
                 |                  j - 1
                 | tau_(j-1) + 2^( -------)         si j > 1      ATTENTION division entre integer
                                      B                           i.e on prend la partie entiere !!

        """
        # TODO Total vectorisation ? Numba ?
        self.nb_of_correlation_point = int(self.nb_of_cascade * B)  # +1 ?
        taus = np.zeros(self.nb_of_correlation_point, dtype=np.uint32)
        taus[:B] = np.arange(B) + 1
        for n in range(1, self.nb_of_cascade):
            taus[n * B:(n + 1) * B] = taus[:B] * np.power(2, n) + taus[n * B - 1]
        i = -1
        while taus[i] > max_correlation_time_tick:
            taus[i] = 0
            i -= 1
        taus = np.trim_zeros(taus)
        taus += start_correlation_time_in_tick
        self.nb_of_correlation_point = taus.size
        self.time_axis = taus
        return taus


    def fit_cumulants(self, is_error_bar_for_fit=True):

        # Set data boundaries
        if self.full_measurement.correlation_time_start != 0:
            idx_start = np.searchsorted(self.time_axis, self.full_measurement.correlation_time_start)
        else:
            idx_start = 0
        if self.full_measurement.correlation_time_end != -1:
            idx_end = np.searchsorted(self.time_axis, self.full_measurement.correlation_time_end)
        else:
            idx_end = -1

        y = self.correlation_curve[idx_start:idx_end]
        x = self.time_axis[idx_start:idx_end]

        if is_error_bar_for_fit:
            error_bar = self.error_bar[idx_start:idx_end]
        else:
            error_bar = None

        # Set model and params
        self.model = Cumulant()
        self.params = self.model.make_params(B=1, beta=1, gamma=100, mu2=0, mu3=0, mu4=0)
        #TODO limite pour les parametres (positif par exmeple).
        self.model.guess(y, x, error_bar=error_bar)

        # fitting

        self.fit_results_method1 = self.fit_results = self.model.fit(y, self.params, t=x, weights=error_bar,
                                                                     method=self.full_measurement.fitting_method1)

        if self.full_measurement.fitting_method2 != "None":
            self.fit_results = self.model.fit(y, self.fit_results.params, weights=error_bar, t=x,
                                              method=self.full_measurement.fitting_method2)

        self.best_fit = self.fit_results.best_fit
        self.fit_x, self.residual_x  = x

        self.residuals = self.fit_results.residual

        self.cumulants = self.fit_results.best_values
        return self.fit_results.fit_report()

    def fit_contin(self):
        pass