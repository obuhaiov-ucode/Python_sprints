def bubble_sort(lst: list):
    n = len(lst)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
