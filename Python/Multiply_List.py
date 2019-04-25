def multiply_list(l):
    nw_list = []
    for i in range(len(l)):
        tmp = 1
        for n in l:
            if l[i] == n:
                pass
            else:
                tmp = tmp * n
        nw_list.append(tmp)

    print(nw_list)

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    multiply_list(l1)
    l2 = [3,2,1]
    multiply_list(l2)
