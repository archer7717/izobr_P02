

def generator_num(list_1:int):
    for i in list_1:
        yield i


l_num = [1,2,3,4,5]

print(generator_num(l_num))

for i in generator_num(l_num):
    print(i)


# Генератор выражения 
n = 5 


square_generator = (i*i for i in range(n+1))
print(type(square_generator))

for square in square_generator:
    print(square)