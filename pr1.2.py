data = dict()
with open('C:\Python\слайды\text.2.txt', 'r') as file:
    for i in file.readlines():
        linedata = i.split()
        data[linedata[0]] = linedata[1]
months = ['May', 'June', 'July','November']
res = 0
for i in months:
    res += int(data[i])
print(res / len(months))