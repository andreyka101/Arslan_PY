
# создание списка
# arr_num = [2,5,7,9]

# print(arr_num)
# print(type(arr_num))



# получаем элемент по индексу
# print(arr_num[0] , arr_num[1])



# длина списка и строки
# num_s = "eifeifeihfif"
# print(len(num_s))
# print(len(arr_num))



# перебор списка с помощью цикла for range
# for i in range(len(arr_num)):
#     print("i =" , i)
#     print("arr_num[i] =" , arr_num[i])
#     print("-")



# получаем символ строки в списке
# arr_2 = ["qwerrt","3454y4y", "knkbnkgbk"]
# print(arr_2)
# print(arr_2[2][4])



# список в списке
# arr_3 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(arr_3)
# print(arr_3[0])
# print(arr_3[0][2])



# перебор списка с помощью цикла for
# for el in arr_num:
#     print(el)

# arr_num[0] + arr_num[1] + arr_num[2] + arr_num[3] + arr_num[4]

# перебор строки с помощью цикла for
# for el in num_s:
#     print(el)



# перебор списка в списке с помощью цикла for
# for en_x in arr_3:
#     print(en_x)
#     for en_y in en_x:
#         print(en_y)



# двух мерный цикл
# for x in range(10):
#     num_f = ""
#     for y in range(10):
#         num_f+= str(x) + str(y) + "  "

#     print(num_f)




# изменение элемента по индексу 






arr_dz_1 = [None , None , None , None , None]
num = 0
for i in range(5):
    arr_dz_1[i] = input("--")

print(arr_dz_1)



arr_num=[0,56,3,56,1,2]
for i in range(len(arr_num) -1 , -1 , -1):
    print("i =", i)
    print("arr_num[i] =",arr_num[i])
    print("-")




