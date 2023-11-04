import copy

def Change(y):
    main_list = [*set(y)]
    for x in main_list:
        if x in y:
            y.remove(x)
    for x in y:
        b = x
        while b in main_list:
            b = str(b) + str(x)
        main_list.append(b)
    print(set(main_list))

List1 = [1, 1, 3, 3, 1]
List2 = [5, 5, 5, 5, 5, 5, 5]
List3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

Change(copy.deepcopy(List1))
Change(copy.deepcopy(List2))
Change(copy.deepcopy(List3))