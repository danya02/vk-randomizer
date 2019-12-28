import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
try:
    from . import temp_file
except:
    import temp_file

def plot_random_polynominal(degree=random.randint(3,7), max_coeff=random.randint(10,20)):
    x = x = np.linspace(-3, 3, 20000)
    val=0
    print(degree)
    for i in range(degree,-1,-1):
        val=val + random.randint(1 if i==degree else 0,max_coeff)*(x**i)
    plt.plot(x, val)
    path = temp_file.TemporaryFile.generate_new('png')
    plt.savefig(path)
    return path

if __name__=='__main__':
    print(plot_random_polynominal().persist())
