import sys 

number = len(sys.argv)

dict = {1:'One', 2: 'Two', 3:'Three', 4:'Four',5:'Five', 6:'Six',
7:'Seven', 8:"eight", 9:'Nine'}
output = ''
res = []
for i in range(1, number):
    a = sys.argv[i]
    for j in a:
        string = str(dict.get(int(j)))
        output = output + string
    res.append(output)
print(res)