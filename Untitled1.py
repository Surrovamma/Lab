#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 2
import random
user_m = int(input("Количество строк: "))
user_n = int(input("Количество столбцов: "))
user_min_limit = int(input("Минимальное значение: "))
user_max_limit = int(input("Максимальное значение: "))
#user_m, user_n, user_min_limit, user_max_limit
matrix = []
for i in range(user_m):
    row = []
    for j in range(int(user_n)):
        num = random.randint(int(user_min_limit), int(user_max_limit))
        row.append(num)
    matrix.append(row)
    
for im  in range(int(user_m)):
    for jn in range(int(user_n)):
        if jn == int(int(user_n)-1):
            print (matrix[im][jn])
        else:
            print (matrix[im][jn],end = ' ')


# In[ ]:


def selection_sort(matrix):
    # Берем каждую строку матрицы
    for i in range(len(matrix)):
        # Предполагаем, что текущий элемент является минимальным
        min_idx = i
        # Перебираем оставшиеся элементы строки
        for j in range(i+1, len(matrix[i])):
            # Если находим элемент, который меньше текущего минимального, обновляем индекс минимального элемента
            if matrix[i][j] < matrix[i][min_idx]:
                min_idx = j
        # Меняем местами текущий элемент со найденным минимальным
        matrix[i][min_idx], matrix[i][i] = matrix[i][i], matrix[i][min_idx]
    return matrix

sorted_matrix = selection_sort(matrix)
print(sorted_matrix)


# In[ ]:





# In[ ]:





# In[ ]:




