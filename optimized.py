actions_table = [{"nom": "Action-1", "cout": 20, "benefice": "5%"},
                 {"nom": "Action-2", "cout": 30, "benefice": "10%"},
                 {"nom": "Action-3", "cout": 50, "benefice": "15%"},
                 {"nom": "Action-4", "cout": 70, "benefice": "20%"},
                 {"nom": "Action-5", "cout": 60, "benefice": "17%"},
                 {"nom": "Action-6", "cout": 80, "benefice": "25%"},
                 {"nom": "Action-7", "cout": 22, "benefice": "7%"},
                 {"nom": "Action-8", "cout": 26, "benefice": "11%"},
                 {"nom": "Action-9", "cout": 48, "benefice": "13%"},
                 {"nom": "Action-10", "cout": 34, "benefice": "27%"},
                 {"nom": "Action-11", "cout": 42, "benefice": "17%"},
                 {"nom": "Action-12", "cout": 110, "benefice": "9%"},
                 {"nom": "Action-13", "cout": 38, "benefice": "23%"},
                 {"nom": "Action-14", "cout": 14, "benefice": "1%"},
                 {"nom": "Action-15", "cout": 18, "benefice": "3%"},
                 {"nom": "Action-16", "cout": 8, "benefice": "8%"},
                 {"nom": "Action-17", "cout": 4, "benefice": "12%"},
                 {"nom": "Action-18", "cout": 10, "benefice": "14%"},
                 {"nom": "Action-19", "cout": 24, "benefice": "21%"},
                 {"nom": "Action-20", "cout": 114, "benefice": "18%"}]


def profit(action):
    profit_str = action['benefice']
    profit_int = int(profit_str[:-1])
    profit_res = action["cout"] * profit_int/100
    return profit_res


def cost(action):
    return action["cout"]


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
