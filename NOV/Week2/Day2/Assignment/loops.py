# 1. Print numbers from 1 to 10 using a for loop.

# for i in range(1, 11):
#     print(i)


# 2. Print numbers from 10 to 1 using a while loop.

# i = 10

# while i >= 1:
#     print(i)
#     i -= 1

# 3. Print even numbers from 2 to 20.

# for i in range(2, 21, 2):
#     print(i)

# 4. Print odd numbers from 1 to 20.

# for i in range(1, 20, 2):
#     print(i)

# 5. Print the multiplication table of any number.

# num = 3

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# 6. Print numbers from 5 to 25 with a step of 5.

# for i in range(5, 26, 5):
#     print(i)

# 7. Print numbers in reverse order from 5 to 1.

# for i in range(5, 0 , -1):
#     print(i)


# 8. Calculate the sum of numbers from 1 to 10.

# total = 0

# for i in range(1, 11):
#     total = total + i
# print("sum =", total)


# 9. Print the pattern 1 to 5

# for i in range(1,6,1):
#     print(i)


# 10. Print the pattern of star pyramid

for i in range(1, 6):
    for j in range(i):
        print("*",end ="")
    print()    