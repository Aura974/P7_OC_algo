import csv


def read_csv(csv_file):
    content = []

    with open(csv_file, newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader, None)
        fieldnames = ["nom", "cout", "benefice"]

        for row in reader:
            row_data = {key: value for key, value in zip(fieldnames, row)}
            content.append(row_data)
    return content


actions_table = read_csv("actions.csv")


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


def best_combination(actions_table, max_cost):
    sorted_table = sorted(actions_table, key=cost, reverse=True)
    t_cost = 0
    best_comb_list = []

    for action in sorted_table:
        if cost(action) + t_cost <= max_cost:
            best_comb_list.append(action)
            t_cost += cost(action)
    return best_comb_list


best_comb_list = best_combination(actions_table, 500)
best_comb_list_names = []
best_comb_list_costs = []
best_comb_list_profits = []

for action in best_comb_list:
    best_comb_list_names.append(action["nom"])
    best_comb_list_costs.append(cost(action))
    best_comb_list_profits.append(profit(action))

print(f"La meilleur combinaison est la liste de "
      f"{len(best_comb_list)} actions : {best_comb_list_names}"
      f" pour un coût total de {sum(best_comb_list_costs)} €"
      f" et pour un profit total de "
      f"{round(sum(best_comb_list_profits), 2)} €.")
