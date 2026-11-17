# 1. Create a list of 10 numbers and print all elements using a for loop.

# number = [10,20,30,40,50,60,70,80,90,100]

# for i in number:
#     print(i)

# 2. Print only even and odd numbers from a list.

# number = [1,2,3,4,5,6,7,8,9,10]

# print("Even no.s are")
# for num in number:
#     if num % 2 == 0:
#         print(num)

# print("Odd no.s are")
# for num in number:
#     if num % 2 != 0:
#             print(num)

# 3. Find the largest and smallest numbers in a list using a loop.

# numbers = [45, 12, 89, 23, 5, 67]

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)

# 4. Count how many times a particular number appears in a list.

# numbers = [10, 20, 30, 10, 40, 10, 50]

# target = 10
# count = 0

# for num in numbers:
#     if num == target:
#         count += 1

# print("Count:", count)

# 5. Write a function to calculate the sum of all elements without using sum().

# def calculate_sum(numbers):
#     total = 0

#     for num in numbers:
#         total += num

#     return total


# numbers = [10, 20, 30, 40, 50]

# print("Sum:", calculate_sum(numbers))

# 6. Find the second-largest number without using sort() or max().

# numbers = [10, 50, 30, 80, 60]

# largest = float('-inf')
# second = float('-inf')

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num

#     elif num > second and num != largest:
#         second = num

# if second == float('-inf'):
#     print("Second largest does not exist")
# else:
#     print("Second largest:", second)

# 7. Remove duplicate elements without using set().


# numbers = [10, 20, 10, 30, 20, 40, 50]

# new_list = []

# for num in numbers:
#     if num not in new_list:
#         new_list.append(num)

# print(new_list)


# 8. Separate positive, negative and zero values into three different lists.

# numbers = [10, -5, 0, 20, -15, 0, 30, -8]

# positive = []
# negative = []
# zero = []

# for num in numbers:
#     if num > 0:
#         positive.append(num)

#     elif num < 0:
#         negative.append(num)

#     else:
#         zero.append(num)

# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)

# 9. Find common elements between two lists without using intersection().

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]

# common = []

# for num in list1:
#     if num in list2 and num not in common:
#         common.append(num)

# print("Common elements:", common)


# 10. Write a function to check whether a list is a palindrome.

# def is_palindrome(numbers):
#     left = 0
#     right = len(numbers) - 1

#     while left < right:
#         if numbers[left] != numbers[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# numbers = [1, 2, 3, 2, 1]

# if is_palindrome(numbers):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# TUPLE

# 1. Create a tuple of 10 numbers and print all elements using a for loop.

# numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# for num in numbers:
#     print(num)


# 2. Print all elements along with their index using enumerate().

# numbers = (10, 20, 30, 40, 50)

# for index, value in enumerate(numbers):
#     print(index, value)

# 3. Find the largest and smallest numbers using a loop.

# numbers = (45, 12, 89, 23, 5, 67)

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)

# 4. Count how many times a particular number appears using count().

# numbers = (10, 20, 30, 10, 40, 10, 50)

# target = 10

# result = numbers.count(target)

# print("Count:", result)

# 5. Calculate the sum of all tuple elements without using sum().

# def calculate_sum(numbers):
#     total = 0

#     for num in numbers:
#         total = total + num

#     return total


# numbers = (10, 20, 30, 40, 50)

# print("Sum:", calculate_sum(numbers))


# 6. Find the second-largest number without using sort() or max().

# numbers = (10, 50, 30, 80, 60)

# largest = float('-inf')
# second = float('-inf')

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num

#     elif num > second and num != largest:
#         second = num

# if second == float('-inf'):
#     print("Second largest does not exist")
# else:
#     print("Second largest:", second)


# 7. Find all duplicate elements in a tuple.

# numbers = (10, 20, 30, 10, 40, 20, 50, 30)

# duplicates = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate elements:", duplicates)

# 8. Check whether a tuple is a palindrome without using slicing.

# numbers = (1, 2, 3, 2, 1)

# left = 0
# right = len(numbers) - 1

# is_palindrome = True

# while left < right:

#     if numbers[left] != numbers[right]:
#         is_palindrome = False
#         break

#     left += 1
#     right -= 1

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 9. Find the common elements between two tuples using loops.

# tuple1 = (10, 20, 30, 40, 50)
# tuple2 = (30, 40, 50, 60, 70)

# common = []

# for num in tuple1:
#     if num in tuple2 and num not in common:
#         common.append(num)

# print("Common elements:", common)

# 10. Separate even and odd numbers into two different lists.

# numbers = (10, 15, 20, 25, 30, 35, 40, 45)

# even = []
# odd = []

# for num in numbers:

#     if num % 2 == 0:
#         even.append(num)

#     else:
#         odd.append(num)

# print("Even numbers:", even)
# print("Odd numbers:", odd)


# SET

# 1. Create a set of 10 numbers and print all elements using a for loop.

# numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

# for num in numbers:
#     print(num)

# 2. Create two sets and find their union.

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# result = set1.union(set2)

# print("Union:", result)


# 3. Find common elements between two sets using intersection().

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# result = set1.intersection(set2)

# print("Common elements:", result)

# 4. Find the difference between two sets using difference().

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# result = set1.difference(set2)

# print("Difference:", result)

# 5. Find the largest and smallest numbers in a set using a loop.


# numbers = {45, 12, 89, 23, 5, 67}

# largest = float('-inf')
# smallest = float('inf')

# for num in numbers:

#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)

# 6. Find common elements between two sets without using intersection().

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# common = set()

# for num in set1:
#     if num in set2:
#         common.add(num)

# print("Common elements:", common)

# 7. Find the union of two sets without using union().

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# result = set()

# for num in set1:
#     result.add(num)

# for num in set2:
#     result.add(num)

# print("Union:", result)


# 8. Check whether two sets are equal without using the == operator.

# set1 = {10, 20, 30, 40}
# set2 = {40, 30, 20, 10}

# if len(set1) != len(set2):
#     print("Sets are not equal")

# else:
#     if set1.issubset(set2) and set2.issubset(set1):
#         print("Sets are equal")
#     else:
#         print("Sets are not equal")

# 9. Find elements that are present in exactly one of three sets.

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
# set3 = {40, 60, 70, 80}

# result = set()

# for num in set1:
#     if num not in set2 and num not in set3:
#         result.add(num)

# for num in set2:
#     if num not in set1 and num not in set3:
#         result.add(num)

# for num in set3:
#     if num not in set1 and num not in set2:
#         result.add(num)

# print("Exactly one set:", result)

# 10. Find common characters between two strings using sets.

# str1 = "python"
# str2 = "programming"

# set1 = set(str1)
# set2 = set(str2)

# common = set1.intersection(set2)

# print("Common characters:", common)