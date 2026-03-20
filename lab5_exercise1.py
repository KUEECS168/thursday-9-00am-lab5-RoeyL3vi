'''
Author: Roey Levi
KUID: 3200438
Date: 3/5/2026
Lab: lab05
Last modified: 3/5/2026
Purpose: be able to create and manipulate lists
'''
choice = 0
my_list = []
while choice != 4:
    print("Welcome to your Shopping List!")
    print('1) Add item')
    print('2) Check off item')
    print('3) Print list')
    print('4) Exit ')
    choice = int(input('Enter a choice: '))

    if choice == 1:
        my_list.append(input('What item do you want to add? '))

    if choice == 2:
        i = int(input('Which item will you check off? ')) - 1
        item = my_list[i]
        my_list[i] = item[0] + "-" * (len(item) - 2) + item[-1]

    if choice == 3:
        for num in range(len(my_list)):
            print(f"{num+1}) {my_list[num]}")

    print()

print('Program exiting...')