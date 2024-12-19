import numpy.testing as npt
import numpy as np
import miller

def test_flux_surface():
    A = 1    # Aspect ratio
    kappa = 1
    delta = 0
    R0 = 1
    theta = np.linspace(0,2*np.pi)
    x = (1+np.cos(theta))
    y = (np.sin(theta))

    r,z = miller.flux_surface(A,kappa,delta,R0)
    print(r,z)
    print(x,y)
    return npt.assert_allclose([r,z], [x,y])

test_flux_surface()