from scipy.stats import chi2

buckets = 30

rv = chi2(3)
cdf = rv.cdf
top = 10.0

bucket_size = top/buckets
epsilon = bucket_size/10
x_caps = []
cur = bucket_size
while cur < top + epsilon:
    x_caps.append(cur)
    cur = cur+bucket_size

vals = [cdf(x) - cdf(x-bucket_size) for x in x_caps]

for i,x in enumerate(vals):
    print('%i:%f' % (i,x))
