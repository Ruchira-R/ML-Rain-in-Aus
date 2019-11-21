from scipy.stats import norm
from math import sqrt

def one_sided_hypo(sample_mean, pop_mean, std_dev, sample_size, alpha):
    actual_z = abs(norm.ppf(alpha))
    hypo_z = (sample_mean - pop_mean) / (std_dev/sqrt(sample_size))
    print('actual z value :', actual_z)
    print('hypothesis z value :', hypo_z, '\n')
    if hypo_z <= actual_z:
        return True
    else:
        return False

alpha = 0.05
sample_mean = 551.95
pop_mean = 502.22
sample_size =  366
std_dev = 3.88

print('H0 : μ >=', pop_mean)
print('H1 : μ <', pop_mean)
print('alpha value is :', alpha, '\n')

reject = one_sided_hypo(sample_mean, pop_mean, std_dev, sample_size, alpha)
if reject:
    print('Reject NULL hypothesis')
else:
    print('Failed to reject NULL hypothesis')