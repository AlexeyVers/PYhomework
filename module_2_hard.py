main_list = []
decision_list = {}
for i in range(3, 21):
    main_list.append(i)

for i in main_list:
    list_ = []
    for j in range(1, i+1):
        for u in range(1, i+1):
            if i >= j + u and (j + u) % i == 0:
                list_.append([j, u])
    decision_list[i] = list_
print(decision_list)
