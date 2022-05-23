from matplotlib import pyplot as plt
import bruteforce as bf
import optimized as opt
import time

actions_table = bf.read_csv("dataset2_Python+P7.csv",
                            "nom", "cout", "benefice")

# bf_timings = []
# opt_timings = []
# n = 20

# for i in range(n):
#     sub_table = actions_table[:i]
#     start_time = time.time()
#     bf.brute_force_algo(sub_table)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     bf_timings.append(elapsed_time)

# for i in range(n):
#     sub_table = actions_table[:i]
#     start_time = time.time()
#     opt.optimized_algo(sub_table, 500)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     opt_timings.append(elapsed_time)

# print(bf_timings)
# plt.plot(range(n), bf_timings)
# plt.plot(range(n), opt_timings)
# plt.xlabel("nb of actions")
# plt.ylabel("time (s)")

# plt.title("Complexité temporelle")
# plt.savefig("time_analysis")
# plt.show()


bf_nb_of_combinations = []
opt_nb_of_combinations = []
n = 20

for i in range(n):
    sub_table = actions_table[:i]
    brute_force_algo = bf.brute_force_algo(sub_table)
    bf_nb_of_combinations.append(brute_force_algo[3])

for i in range(n):
    sub_table = actions_table[:i]
    optimized_algo = opt.optimized_algo(sub_table, 500)
    opt_nb_of_combinations.append(optimized_algo[4])

plt.plot(range(n), bf_nb_of_combinations)
plt.plot(range(n), opt_nb_of_combinations)

plt.xlabel("nb of actions")
plt.ylabel("nb of combinations")

plt.xticks(range(0, 20, 5))

plt.title("Analyse de la mémoire")

plt.savefig("space_analysis")
plt.show()
