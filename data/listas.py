primos = [2,3,5,7,11,13,17,19,23,29]
for num in primos:
    print(num)

primos.append(31)
print(primos)

primos.insert(0, 1)
print(primos)

primos.insert(5, 37)
print(primos)

ultimo= primos.pop()
print(f'ultimo: {ultimo}')
print(primos)

primos.remove(37)
print(primos)

del primos[4]
print(primos)

print(primos[0:7])

print(primos[2:8])

sub_primos = primos[1:5]
print(sub_primos)