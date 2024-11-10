# цикл while работает когда значение True
# while (True):
#     print("run")



# цикл работает пока (num == 5)
# num = 2
# while(num == 5):
#     print("круг цикла")
#     num = int(input("введите 5__"))
# print("ok")



# условные операторы в while
# num = 5
# while(num == 5 and True):
#     print("круг цикла")
#     num = int(input("введите 5__"))
# print("ok")




# к num_x1 прибавляем 5 и сохраняем в num_x1
# num_x1 = 3
# print(num_x1)
# num_x1 = num_x1 + 5
# print(num_x1)


# тоже самое но короче
# num_x2 = 3
# print(num_x2)
# num_x2 += 5
# print(num_x2)


# Операторы присваивания:
# num_x2 += 5
# num_x2 -= 5
# num_x2 /= 5
# num_x2 *= 5
# num_x2 **= 5
# num_x2 //= 5
# num_x2 %= 5




# цикл работает пока (num_2 > 1)
# num_2 = 10
# while(num_2 > 1):
#     print(num_2)
#     num_2 -= 1

# print("end " , num_2)





# цикл for работает какое то количество раз

# цикл работает от 0 до 9
# for i in range(10):
#     print(i)



# цикл работает от 5 до 10
# for index in range(5,11):
#     print(index)



# цикл работает от 3 до 20 с шагом 3
# for index in range(3 , 20+1 , 3):
#     print(index)


# range(a , b , s)
# a - начало
# b - конец
# s - шаг


# шаг может быть отрицательным 
# for index in range(300 , 20+1 , -3):
#     print(index)




# сумма всех чисел переменной index
# num_3 = 0
# for index in range(6):
#     # print("s _" , num_3)
#     num_3 += index
#     print("e _" , num_3)
# print("end" , num_3)



# print(range(10))



# длина строки
# num_str = "qwertyuio"
# print(len(num_str))



# получаем индекс каждого символа
# for index in range(len(num_str)):
#     # print(index)
#     print(num_str[index])



# разворачиваем строку
# str_revers = ""
# for i in range(len(num_str) - 1 , -1 , -1):
#     # print(num_str[i])
#     str_revers += num_str[i]
#     # print(i)
# print(str_revers)



# получаем каждый символ
# str_super = ""
# for symbol in num_str:
#     str_super += symbol + "."
#     print(symbol)

# print(str_super)


