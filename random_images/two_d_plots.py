import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
try:
    from . import temp_file
except:
    import temp_file

def plot_random_polynominal(degree=random.randint(10,20), max_coeff=random.randint(10,20)):
    def get_poly_and_range(roots, shift, chance_delete=0.5):
        val=0
        maxv = 0
        minv = 0
        new_roots = []
        for v in roots:
            v += (random.random()-0.5) * shift
            if random.random()>chance_delete:
                new_roots.append(v)
        new_roots.sort()
        maxv = new_roots[-1]
        minv = new_roots[0]

        poly = np.polynomial.polynomial.polyfromroots(new_roots)
        poly = np.polynomial.polynomial.Polynomial(poly)
        return poly, minv, maxv 

    gminv = 0
    gmaxv = 0
    polys = []
    roots = []
    for i in range(10):
        roots.append((random.random()-0.5)*10)

    for _ in range(random.randint(3,7)):
        poly, minv, maxv = get_poly_and_range(roots, 0.1)
        gminv = min(gminv, minv)
        gmaxv = max(gmaxv, maxv)
        polys.append(poly)

    
    x = np.linspace(gminv, gmaxv, 20000)

    axes = plt.gca()
    axes.set_ylim([-300, 300])

    for p in polys:
        plt.plot(x, p(x))


    path = temp_file.TemporaryFile.generate_new('png')
    plt.savefig(path)
    return path

if __name__=='__main__':
    print(plot_random_polynominal().persist())
