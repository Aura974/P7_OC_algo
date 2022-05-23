import bruteforce as bf
import optimized as opt

if __name__ == "__main__":
    actions_table = bf.read_csv("dataset2_Python+P7.csv",
                                "nom", "cout", "benefice")

    # (best_comb_list_bf,
    #     best_comb_t_cost_bf,
    #     best_comb_t_profit_bf) = bf.brute_force_algo(actions_table)

    # bf.display_bf_result(best_comb_list_bf,
    #                      best_comb_t_cost_bf,
    #                      best_comb_t_profit_bf)

    (best_comb_list_opt,
        best_comb_list_names_opt,
        best_comb_t_cost_opt,
        best_comb_t_profit_opt,
        nb_of_combinations) = opt.optimized_algo(actions_table, 500)

    opt.display_opt_result(best_comb_list_opt,
                           best_comb_list_names_opt,
                           best_comb_t_cost_opt,
                           best_comb_t_profit_opt)
