import csv


def read_csv(csv_file, name, cost, profit):
    content = []

    with open(csv_file, newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader, None)
        fieldnames = [name, cost, profit]

        for row in reader:
            row_data = {key: value for key, value in zip(fieldnames, row)}
            content.append(row_data)
    return content


actions_table = read_csv("actions.csv", "nom", "cout", "benefice")


def profit(action):
    profit_int = int(action['benefice'])
    profit_result = int(action["cout"]) * profit_int/100
    return profit_result


def cost(action):
    return int(action["cout"])


def brute_force_algo(table):
    n = len(table)
    int_tab = [i for i in range(2**n)]
    binary_tab = [bin(i)[2:] for i in int_tab]
    combinations = ['0'*(n-len(k)) + k for k in binary_tab]

    max_cost = 500
    valid_combinations = []

    for comb in combinations:
        comb_cost = 0
        comb_profit = 0
        for i in range(n):
            if comb[i] == "1":
                comb_cost += cost(table[i])
                comb_profit += profit(table[i])
        if comb_cost <= max_cost:
            valid_combinations.append((comb, comb_profit))

    best_combination = valid_combinations[0][0]
    max_profit = valid_combinations[0][1]

    for comb in valid_combinations:
        if comb[1] > max_profit:
            max_profit = comb[1]
            best_combination = comb[0]

    best_comb_list = []
    best_comb_total_cost = []
    best_comb_total_profit = []

    for i in range(len(best_combination)):
        if best_combination[i] == "1":
            best_comb_list.append(actions_table[i]["nom"])
            best_comb_total_cost.append(cost(actions_table[i]))
            best_comb_total_profit.append(profit(actions_table[i]))

    return best_comb_list, best_comb_total_cost, best_comb_total_profit


def display_bf_result(list, cost, profit):
    print(f"La meilleure combinaison est la liste de "
          f"{len(list)} actions : {list}"
          f" pour un coût total de {sum(cost)} €"
          f" et pour un profit total de "
          f"{round(sum(profit), 2)} €.")
