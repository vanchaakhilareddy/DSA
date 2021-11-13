#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def getPairsCount(arr, n, sum):
 
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))


# In[2]:


#1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# In[3]:


#3. Write a program to check if two strings are a rotation of each other?

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return 0
    temp = string1 + string1
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

string1 = "AACD"
string2 = "ACDA"
 
if areRotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")


# In[5]:


#4. Write a program to print the first non-repeated character from a string?
NO_OF_CHARS = 256
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count

def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 
string = "AkhilaReddyVancha"
index = firstNonRepeating(string)
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is " + string[index])


# In[6]:


#5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')


# In[ ]:




