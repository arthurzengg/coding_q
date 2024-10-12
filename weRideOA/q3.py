def getFinalPrice(price, queries):
    # Write your code here

    n = len(price)
    for query in queries:
        if query[0] == 2:
            for i in range(n):
                if price[i] < query[1]:
                    price[i] = query[2]
        elif query[0] == 1:
            x = query[1] - 1
            v = query[2]
            price[x] = v
        # print(price)

    return price



print(getFinalPrice([7,5,4], [[2,6,6],[1,2,9],[2,8,8]]))
print(getFinalPrice([1,2,3,4,5], [[1,3,4],[1,5,1],[2,3,3],[1,1,1]]))
print(getFinalPrice([9,6,3,1], [[2,8,8],[2,11,11]]))