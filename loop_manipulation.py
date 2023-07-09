p = 'Prateek'

def for_else_loop(choice):
    for i in p:
        if choice == 'pass':
            if i == 't':
                pass
            else:
                print(i)
        elif choice == 'break':
            if i == 't':
                break
            else:
                print(i)
        elif choice == 'continue':
            if i == 't':
                continue
            else:
                print(i)
        elif choice == 'all':
            if i == 'a':
                pass
            elif i == 't':
                continue
            elif i == 'k':
                break
            else:
                print(i)
    else:
        print("For loop run successfully")

def while_else_loop(choice):
    a = 0
    while a < 15:
        if choice == 'pass':
            if a == 3:
                pass
            else:
                print(a)
            a+=1
        elif choice == 'continue':
            a+=1
            if a == 3:
                continue
            else:
                print(a)
        elif choice == 'break':
            if a == 3:
                break
            else:
                print(a)
            a+=1
        elif choice == 'all':
            if a == 2:
                pass
            elif a == 3:
                a+=1
                continue
            elif a == 9:
                break
            else:
                print(a)
            a += 1
    else:
        print('While loop run successfully')

loop_choice = input("Enter your choice for loop type (for/while): ")
action_choice = input("Enter your choice for action (pass/break/continue/all): ")

if loop_choice == 'for':
    for_else_loop(action_choice)
elif loop_choice == 'while':
    while_else_loop(action_choice)
else:
    print("Invalid choice for loop type!")
