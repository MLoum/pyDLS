from lmfit import Model
import numpy as np

def update_param_vals(pars, prefix, **kwargs):
    """Update parameter values with keyword arguments."""
    for key, val in kwargs.items():
        pname = "%s%s" % (prefix, key)
        if pname in pars:
            pars[pname].value = val
    return pars

class Cumulant(Model):
    """ with four Parameters ``B``, ``betz``, ``Gamma``, ''mu2'', ''mu3''  and ``mu4``.

    Defined as:

    .. math::

        f(t; , t0, amp, tau, cst) = B + beta*np.exp(-2*Gamma*t)*((1 + mu2/2*t**2/Gamma**2 - mu3/6*t**3/Gamma**3 +  mu4/24*t**4/Gamma**4)**2)

    """

    def __init__(self, independent_vars=['t'], prefix='', nan_policy='propagate',
                 **kwargs):
        kwargs.update({'prefix': prefix, 'nan_policy': nan_policy,
                       'independent_vars': independent_vars})

        def cumulant(t, B, beta, gamma, mu2, mu3, mu4):
            # return B + beta*np.exp(-t*gamma)*((1 + mu2/2*t**2/tau**2 - mu3/6*t**3/tau**3 +  mu4/24*t**4/tau**4)**2)
            return B + beta * np.exp(-2*t*gamma) * ((1 + mu2/2*t**2- mu3/6*t**3 + mu4/24*t**4)** 2)

        super(Cumulant, self).__init__(cumulant, **kwargs)

    def guess(self, data, x=None, **kwargs):
        B, beta, gamma, mu2, mu3, mu4 = 0., 0., 0., 0., 0., 0.

        # TODO form the polynomial expression
        # with B assumed as 1 (or else we can form ln(G-B/B)
        # ln(G - 1) = ln (beta/2) - Gamma * t + mu2/2 * t**2 - mu3/6 * t**3 + mu4/24 * t**4
        # Is there some numerical procedure for fitting a polynome without initial value
        # To a mathematician, polynomial models are very special. Strictly speaking, polynomial models are not 'nonlinear'. Even though a graph of X vs. Y is curved (in all but some special cases), the derivative of Y with respect to the parameters is linear.
        #
        # Because polynomial models are not nonlinear, it is possible (but not with Prism) to fit polynomial models without fussing with initial values. And the fit can be in one step, rather than the iterative approach used for nonlinear models.
        # Il va donc falloir deriver la courbe et donc faire avant/en même temps un filtre passe-bas.

        error_bar = kwargs["error_bar"]

        if x is not None:
            # FIXME 1/sigma ou 1/sigma²
            w = error_bar
            # FIXME
            data_ = np.copy(data)
            data_[data_ < 1] = 1
            p, residuals, rank, singular_values, rcond = np.polyfit(x, np.ln(np.sqrt(data_-1)), deg=4, w=w, full=True)
            gamma = - p[3]
            mu3 = -6*p[1]
            mu2 = 2*p[2]
            k4 = 24*[0]
            mu4 = k4 + 3*mu2**2
            # Better estimation with the initial point (! afterpulsing !)
            beta = 2*np.exp(p[5])
            #FIXME mean of the last point.
            B = 1
            # TODO analyse SVD etc for estimation of the good polynomial order.

        pars = self.make_params(B=B, beta=beta, gamma=gamma, mu2=mu2, mu3=mu3, mu4=mu4)
        return update_param_vals(pars, self.prefix, **kwargs)

    # __init__.__doc__ = COMMON_INIT_DOC
    # guess.__doc__ = COMMON_GUESS_DOC
    __init__.__doc__ = "TODO"
    guess.__doc__ = "TODO"