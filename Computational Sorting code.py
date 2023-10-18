#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt


# In[63]:


data = pd.read_csv('Dataset.csv', low_memory=False)


# In[64]:


data.head()


# In[65]:


specific_data = data.select_dtypes(include=['number'])
specific_data


# In[66]:


specific_data.isnull().sum()


# In[67]:


specific_data = specific_data.fillna(specific_data.median())
specific_data


# In[68]:


specific_data.isnull().sum()


# In[69]:


insertionsort_nonincreasing_times = []
insertionsort_nondecreasing_times = []
mergesort_nonincreasing_times = []
mergesort_nondecreasing_times = []


# In[70]:


def insertion_sort_nonincreasing(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# In[71]:


def insertion_sort_nondecreasing(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# In[72]:


current_amount = specific_data['Current Loan Amount']
credit_score = specific_data['Credit Score']
annual_income = specific_data['Annual Income']
credit_history = specific_data['Years of Credit History']
Months_since_last_delinquent = specific_data['Months since last delinquent']
account_open = specific_data['Number of Open Accounts']
credit_problem = specific_data['Number of Credit Problems']
credit_balance = specific_data['Current Credit Balance']
Bankruptcies = specific_data['Bankruptcies']
Tax_Liens = specific_data['Tax Liens']

#arr = specific_data['Current Loan Amount'], specific_data['Credit Score'], specific_data['Annual Income'], specific_data['Years of Credit History'], specific_data['Months since last delinquent'], specific_data['Number of Credit Problems'], specific_data['Current Credit Balance'], specific_data['Bankruptcies'], specific_data['Tax Liens']
#arr = specific_data['Current Loan Amount'], specific_data['Credit Score']
arr = list(zip(current_amount, credit_score, annual_income, credit_history, Months_since_last_delinquent, account_open, credit_problem, credit_balance, Bankruptcies, Tax_Liens))


# In[12]:


for _ in range(10):
    start_time = time.process_time()
    insertion_sort_nonincreasing(arr.copy())
    end_time = time.process_time()
    insertionsort_nonincreasing_times.append(end_time - start_time)
print(insertionsort_nonincreasing_times)
for _ in range(10):
    start_time = time.process_time()
    insertion_sort_nondecreasing(arr.copy())
    end_time = time.process_time()
    insertionsort_nondecreasing_times.append(end_time - start_time)
print(insertionsort_nondecreasing_times)


# In[74]:


def merge_sort_nonincreasing(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_nonincreasing(left_half)
        merge_sort_nonincreasing(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# In[75]:


def merge_sort_nondecreasing(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_nondecreasing(left_half)
        merge_sort_nondecreasing(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# In[76]:


for _ in range(10):
    start_time = time.process_time()
    merge_sort_nonincreasing(arr)
    end_time = time.process_time()
    mergesort_nonincreasing_times.append(end_time - start_time)
print(mergesort_nonincreasing_times)

for _ in range(10):
    start_time = time.process_time()
    merge_sort_nondecreasing(arr)
    end_time = time.process_time()
    mergesort_nondecreasing_times.append(end_time - start_time)
print(mergesort_nondecreasing_times)


# In[77]:


plt.figure(figsize=(20, 10))
plt.bar(specific_data.columns, insertionsort_nonincreasing_times, label='Insertion Sort', width=0.4)
plt.bar(specific_data.columns, mergesort_nonincreasing_times, label='Merge Sort', width=0.4, align='edge')
plt.xlabel('Specific_data')
plt.ylabel('Computational Time (seconds)')
plt.title('Running Time of Non-Increasing Insertion Sort vs. Merge Sort')
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[78]:


plt.figure(figsize=(20, 10))
plt.bar(specific_data.columns, insertionsort_nondecreasing_times, label='Insertion Sort', width=0.4)
plt.bar(specific_data.columns, mergesort_nondecreasing_times, label='Merge Sort', width=0.4, align='edge')
plt.xlabel('Specific_data')
plt.ylabel('Computational Time (seconds)')
plt.title('Running Time of Non-descreasing Insertion Sort vs. Merge Sort')
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

