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


n = len(actions_table)
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
            comb_cost += cost(actions_table[i])
            comb_profit += profit(actions_table[i])
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
        best_comb_total_cost.append(actions_table[i]["cout"])
        best_comb_total_profit.append(profit(actions_table[i]))

print(f"La meilleur combinaison est la liste de "
      f"{len(best_comb_list)} actions : {best_comb_list}"
      f" pour un coût total de {sum(best_comb_total_cost)} €"
      f" et pour un profit total de "
      f"{round(sum(best_comb_total_profit), 2)} €.")
