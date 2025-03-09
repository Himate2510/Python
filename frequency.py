d = {"Name": "Aryan", "Age": 12, "Grade": "Seventh" ,"School": "Agakhan"}
k = "Aryan"

result = 0
for i in d:
    if d[i] == k:
        result += 1
print(result)