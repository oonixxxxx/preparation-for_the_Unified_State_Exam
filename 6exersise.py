def to_bin(n):
     return bin(n)[2:]


def get_summ(n):
    result = 0
    for i in range(len(n)):
        result = result + int(n[i])
        
    return result


def get_to_10(n):
    return (int(n, 2))

lst = []    
for i in range(0, 1000):
    result = ''
    result = result + to_bin(i)
    result = result + str(get_summ(result) % 2)
    result = result + str(get_summ(result) % 2)

    lst.append(get_to_10(result))
    
print(lst)


minnn = 9999999999999

for j in range(len(lst)):
    if int(lst[j]) > 170:
        if int(lst[j]) < minnn:
            minnn = int(lst[j])


print(minnn)