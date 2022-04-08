from bruteforce import read_csv

actions_table = read_csv("actions.csv", "nom", "cout", "benefice")


def profit(action):
    profit_int = int(action['benefice'])
    profit_result = int(action["cout"]) * profit_int/100
    return profit_result


def cost(action):
    return int(action["cout"])


def total_profit(actions_table):
    t_profit = 0
    for action in actions_table:
        t_profit += profit(action)
    return t_profit


def total_cost(actions_table):
    t_cost = 0
    for action in actions_table:
        t_cost += cost(action)
    return t_cost


def optimized_algo(actions_table, max_cost):
    sorted_table = sorted(actions_table, key=cost, reverse=True)
    t_cost = 0
    best_comb_list = []
    best_comb_list_names = []
    best_comb_list_costs = []
    best_comb_list_profits = []

    for action in sorted_table:
        if cost(action) + t_cost <= max_cost:
            best_comb_list.append(action)
            t_cost += cost(action)

    for action in best_comb_list:
        best_comb_list_names.append(action["nom"])
        best_comb_list_costs.append(cost(action))
        best_comb_list_profits.append(profit(action))

    return (best_comb_list,
            best_comb_list_names,
            best_comb_list_costs,
            best_comb_list_profits)


def display_opt_result(list, names, cost, profit):
    print(f"La meilleure combinaison est la liste de "
          f"{len(list)} actions : {names}"
          f" pour un coût total de {sum(cost)} €"
          f" et pour un profit total de "
          f"{round(sum(profit), 2)} €.")
