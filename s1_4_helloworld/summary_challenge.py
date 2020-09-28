message = """Please choose an option from the list: 
1. Learn Python
2. Speak Spanish
3. Order Pizza
4. Drink Coffee 
0. Exit
"""
ans = '-'
while ans != "0":
    if ans in "1234":
        print("You typed {}".format(ans))
    else:
        print(message)
    ans = input()
