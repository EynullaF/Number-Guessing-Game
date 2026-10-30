print("\033[94mNumber Guessing Game\033[0m")
d=input("\033[31mSelect the difficulty level (Easy(E),Medium(M),Hard(H)): \033[0m")
if d=="E":
    print("\033[94mThe interval is between 1 and 100\033[0m]")
    a=list(range(1,101))
    import random
    b=int(random.choice(a))
    c=0
    while c != b:
        c=int(input("Guess The Number: "))
        if c>b:
            print("\033[92mYou said a higher number.\033[0m")
        if c<b:
            print("\033[92mYou said a lower number.\033[0m")
        if c==b:
            print("\033[91mYOU WON\033[0m")
            break
if d=="M":
    print("\033[94mThe interval is between 1 and 1000\033[0m")
    a=list(range(1,1001))
    import random
    b=int(random.choice(a))
    c=0
    while c != b:
        c=int(input("Guess The Number: "))
        if c>b:
            print("\033[92mYou said a higher number.\033[0m")
        if c<b:
            print("\033[92mYou said a lower number.\033[0m")
        if c==b:
            print("\033[91mYOU WON\033[0m")
            break
if d=="H":
    print("\033[94mThe interval is between 1 and 10000\033[0m")
    a=list(range(1,10001))
    import random
    b=int(random.choice(a))
    c=0
    while c != b:
        c=int(input("Guess The Number: "))
        if c>b:
            print("\033[92mYou said a higher number.\033[0m")
        if c<b:
            print("\033[92mYou said a lower number.\033[0m")
        if c==b:
            print("\033[91mYOU WON\033[0m")
            break