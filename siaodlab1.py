#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Сурова Мария Андреевна БСТ2201
#Задание 1
print("Hello, World!")


# In[20]:


#Задание 2
import random
user_m = int(input("Количество строк: "))
user_n = int(input("Количество столбцов: "))
user_min_limit = int(input("Минимальное значение: "))
user_max_limit = int(input("Максимальное значение: "))
def create_matrix(user_m,user_n,user_min_limit,user_max_limit):
    m =[]
    for i in range (user_m):
        irr = []
        for j in range(user_n):
            irr.append(random.randint(user_min_limit,user_max_limit))
        m.append(irr)
    return(m)
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
create_matrix(user_m,user_n,user_min_limit,user_max_limit)
for i in range(len(matrix)):
    print(matrix[i])


# In[21]:


#Задание 3
#Сортировка выбором
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
print("Изначальная матрица:")
for n in range(len(matrix)):
    print(matrix[n])
import time
import timeit
#start_time = timeit.default_timer()
def selection_sort(matrix):
    for i in range(len(matrix)):
        min_idex = i
        for j in range(i+1, len(matrix)):
            if matrix[j] < matrix[min_idex]:
                min_idex = j
        matrix[min_idex], matrix[i] = matrix[i], matrix[min_idex]
                
    return matrix
print("\nОтсортированная матрица:")
for num in range(len(matrix)):
    selection_sort(matrix[num])
    print(matrix[num])
#print(timeit.default_timer() - start_time)


# In[8]:


#Сортировка вставкой
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
print("Изначальная матрица:")
for n in range(len(matrix)):
    print(matrix[n])
def insertion_sort(matrix):
    for i in range(len(matrix)):
        cursor = matrix[i]
        pos = i
        while pos > 0 and matrix[pos-1] > cursor:
            matrix[pos] = matrix[pos-1]
            pos = pos-1
        matrix[pos]=cursor
    return matrix
print("\nОтсортированная матрица:")
for row in range(len(matrix)):
    insertion_sort(matrix[row])
    print(matrix[row])
        


# In[9]:


#Сортировка пузырьком
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
print("Изначальная матрица:")
for n in range(len(matrix)):
    print(matrix[n])
def bubble_sort(matrix):
    is_change = True
    while is_change:
        is_change = False
        for i in range(len(matrix)-1):
            if matrix[i] > matrix[i+1]:
                matrix[i], matrix[i+1] = matrix[i+1], matrix[i]
                is_change = True
    return matrix
print("\nОтсортированная матрица:")
for st in range(len(matrix)):
    bubble_sort(matrix[st])
    print(matrix[st])
    


# In[10]:


# Сортировка Шеллa
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
print("Изначальная матрица:")
for n in range(len(matrix)):
    print(matrix[n])
def shell_sort(matrix):
    gap = len(matrix) // 2
    
    while gap > 0:
        for value in range(gap, len(matrix)):
            current_value = matrix[value]
            position = value
            
            while position >= gap and matrix[position - gap] > current_value:
                matrix[position] = matrix[position - gap]
                position -= gap
                matrix[position] = current_value
        gap //= 2
    return matrix
print("\nОтсортированная матрица:")
for st in range(len(matrix)):
    shell_sort(matrix[st])
    print(matrix[st])


# In[11]:


# Быстрая сортировка
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
print("Изначальная матрица:")
for n in range(len(matrix)):
    print(matrix[n])
def quick_sort(matrix):
    quick_sort_helper(matrix, 0, len(matrix) - 1) 
    return matrix
def quick_sort_helper(matrix, low, high):
    if low < high:
        split_point = partition(matrix, low, high) 
        quick_sort_helper(matrix, low, split_point - 1)
        quick_sort_helper(matrix, split_point + 1, high)
def partition(matrix, low, high):
    pivot_value = matrix[low]
    left_mark = low + 1
    right_mark = high
    done = False
    while not done:
        while left_mark <= right_mark and matrix[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and matrix[right_mark] >= pivot_value: 
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            matrix[left_mark], matrix[right_mark] = matrix[right_mark], matrix[left_mark]
    matrix[low], matrix[right_mark] = matrix[right_mark], matrix[low] 
    return right_mark
print("\nОтсортированная матрица:")
for row in range(len(matrix)):
    quick_sort(matrix[row])
    print(matrix[row])


# In[19]:


#Турнирная сортировка
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
print("Изначальная матрица:")
for n in range(len(matrix)):
    print(matrix[n])
print("\nОтсортированная матрица:")
def heap(matrix, heap_size, root_index):
    largest = root_index
    left = (2*root_index)+1
    right = (2*root_index)+2
    if left < heap_size and matrix[left] > matrix[largest]:
        largest = left
    if right < heap_size and matrix[right] > matrix[largest]:
        largest = right
    if largest != root_index:
        matrix[root_index], matrix[largest] = matrix[largest], matrix[root_index]
        heap(matrix, heap_size, largest)
def t_sort(matrix):
    n = len(matrix)
    for i in range(n, -1, -1):
        heap(matrix, n, i)
    for i in range(n - 1, 0, -1):
        matrix[i], matrix[0] = matrix[0], matrix[i]
        heap(matrix, i, 0)
    return matrix
for st in range(len(matrix)):
    t_sort(matrix[st])
    print(matrix[st])
    


# In[14]:


#Встроенная сортировка
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
print("Изначальная матрица:")
for n in range(len(matrix)):
    print(matrix[n])
print("\nОтсортированная матрица:")
for st in range(len(matrix)):
    matrix[st].sort()
    print(matrix[st])


# In[27]:


#Оценка времени работы алгоритмов сортировки
import timeit
matrix = create_matrix(user_m,user_n,user_min_limit,user_max_limit)
#Сортировка выбором
start_time = timeit.default_timer()
selection_sort(matrix)
selection_time = timeit.default_timer() - start_time
print("Сортировка выбором: ",selection_time)
#Сортировка вставкой
start_time = timeit.default_timer()
insertion_sort(matrix)
insertion_time = timeit.default_timer() - start_time
print("Сортировка вставкой: ", insertion_time)
#Сортировка пузырьком
start_time = timeit.default_timer()
bubble_sort(matrix)
bubble_time = timeit.default_timer() - start_time
print("Сортировка пузырьком: ", bubble_time)
#Сортировка Шелла
start_time = timeit.default_timer()
shell_sort(matrix)
shell_time = timeit.default_timer() - start_time
print("Сортировка Шелла: ", shell_time)
#Быстрая сортировка
start_time = timeit.default_timer()
quick_sort(matrix)
quick_time = timeit.default_timer() - start_time
print("Быстрая сортировка: ", quick_time)
#Стандартная сортировка
start_time = timeit.default_timer()
matrix.sort()
standard_time = timeit.default_timer() - start_time
print ("Стандартная сортировка: ", standard_time)


# In[ ]:





# In[ ]:





# In[ ]:




