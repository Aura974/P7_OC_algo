from matplotlib import pyplot as plt
import numpy as np
import bruteforce as bf
import optimized as opt
import time

actions_table = bf.read_csv("actions.csv", "nom", "cout", "benefice")

bf_timings = []
opt_timings = []

for i in range(len(actions_table)):
    sub_table = actions_table[:i]
    start_time = time.time()
    bf.brute_force_algo(sub_table)
    end_time = time.time()
    elapsed_time = end_time - start_time
    bf_timings.append(elapsed_time)

for i in range(len(actions_table)):
    sub_table = actions_table[:i]
    start_time = time.time()
    opt.optimized_algo(sub_table, 500)
    end_time = time.time()
    elapsed_time = end_time - start_time
    opt_timings.append(elapsed_time)

print(bf_timings, opt_timings)
plt.plot(range(20), bf_timings)
plt.plot(range(20), opt_timings)
plt.xlabel("nb of actions")
plt.ylabel("time (s)")
plt.xticks(np.arange(0, 20, step=2))

plt.show()
