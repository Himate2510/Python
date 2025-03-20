s1 = {2, 5, 7, 9}
s2 = {2, 5, 8, 3}
print(s2, "\n")
print(s1, "\n")
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [100, 200, 300, 400, 500]
list2 = [1000, 2000, 3000, 4000, 5000]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

stocks = ["Microsoft", "Google", "Apple", "Amazon"]
prices = [100, 200, 300, 400]
new_dict = {stocks: prices for stocks, prices in zip(prices, stocks)}
print(new_dict)