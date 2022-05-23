from bruteforce import read_csv

actions_table = read_csv("actions.csv", "nom", "cout", "benefice")


def profit(action):
    profit_float = float(action['benefice'])
    profit_result = float(action["cout"]) * profit_float/100
    return profit_result


def cost(action):
    return float(action["cout"])


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
    sorted_table = sorted(actions_table, key=profit, reverse=True)
    t_cost = 0
    best_comb_list = []
    best_comb_list_names = []
    best_comb_list_costs = []
    best_comb_list_profits = []
    nb_of_comb = 0

    for action in sorted_table:
        if (cost(action) + t_cost <= max_cost and cost(action) > 0):
            best_comb_list.append(action)
            t_cost += cost(action)
            nb_of_comb += 1

    for action in best_comb_list:
        best_comb_list_names.append(action["nom"])
        best_comb_list_costs.append(cost(action))
        best_comb_list_profits.append(profit(action))

    return (best_comb_list,
            best_comb_list_names,
            best_comb_list_costs,
            best_comb_list_profits,
            nb_of_comb)


def display_opt_result(list, names, cost, profit):
    print(f"La meilleure combinaison est la liste de "
          f"{len(list)} actions : {names}"
          f" pour un coût total de {round(sum(cost), 2)} €"
          f" et pour un profit total de "
          f"{round(sum(profit), 2)} €.")
