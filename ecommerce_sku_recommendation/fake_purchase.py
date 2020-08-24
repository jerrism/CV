import random

with open('jd_i.csv')as f:
    skus = f.read().splitlines()
for i in range(10000000):
    uid = str(i).zfill(8)
    purchase_times = random.randrange(1, 101)
    purchased_skus = random.sample(skus, purchase_times)
    print('\n'.join(['%s,%s' % (uid, purchased_sku) for purchased_sku in purchased_skus]))
