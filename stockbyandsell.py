def Profits(arr,arr_size):
    profit = 0
    for i in range(1, arr_size):

        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit
prices = [100, 180, 260, 310, 40, 535, 695]

profit = Profits(prices, len(prices))
print("Max Profit: ", profit)