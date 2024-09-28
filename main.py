import time

specialcharacters = "~`!@#$%^&*()_-+=/{/}[]|:;<>,.?"
digits = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def word_generator(characters,length):
    if length == 0:
        return [""]
    strings = []
    for char in characters:
        for string in word_generator(characters,length-1):
            strings.append(char+string)
    return strings

def password_generator(bl,el,characters):
    strings = []
    total = sum(len(word_generator(characters,i))for i in range(bl,el+1))
    curr = 0
    while bl<=el:
       strings += word_generator(characters,bl)
       curr += len(word_generator(characters,bl))
       progress = (curr/total)*100
       print(f"Progress: {progress:.2f}%",end='\r')
       time.sleep(0.1)
       bl += 1
    strings = set(strings)
    return list(strings)

values = {"lc":True,"uc":True,"d":False,"sc":False}

main_flag = True
while (main_flag==True):
    print("""\n---OPTIONS--- 
    [1] CREATE WORDLIST
    [2] EXIT""")
    try:
        n = int(input("YOUR OPTION : "))
        if n==1:
            sub_flag = True
            while(sub_flag==True):    
                print("\nENTER NUMBER TO TOGGLE VALUES\n[1] LOWER CASE            {lc}\n[2] UPPER CASE            {uc}\n[3] SPECIAL CHARACTERS    {sc}\n[4] DIGITS                {d}\n[5] CUSTOM CHARACTERS\n[6] BUILD\n[7] EXIT".format(lc=values["lc"],uc=values["uc"],sc=values["sc"],d=values["d"]))
                try:
                    m = int(input("YOUR OPTION : "))
                    if m==1:
                        values["lc"] = not values["lc"]
                    elif m==2:
                        values["uc"] = not values["uc"]
                    elif m==3:
                        values["sc"] = not values["sc"]
                    elif m==4:
                        values["d"] = not values["d"]
                    elif m==5:
                        chars = str(input("ENTER ALL THE CHARACTERS YOU WANT TO USE : "))
                        filename = str(input("ENTER THE NAME OF YOUR WORDLIST : "))
                        sl = int(input("ENTER STARTING LENGTH OF THE PASSWORD : "))
                        el = int(input("ENTER END LENGTH OF THE PASSWORD : "))
                        lop = password_generator(sl,el,chars)
                        lop.sort()
                        lop.sort(key=lambda x:len(x))
                        with open(file=(filename+".txt"),mode="w") as f:
                            for i in lop:
                                f.write(i+"\n")
                        print("\n---DONE---")
                    elif m==6:
                        chars = ""
                        if values["lc"]==True:
                            chars += lowercase
                        if values["uc"]==True:
                            chars += uppercase
                        if values["sc"]==True:
                            chars += specialcharacters
                        if values["d"]==True:
                            chars += digits
                        filename = str(input("ENTER THE NAME OF YOUR WORDLIST : "))
                        sl = int(input("ENTER STARTING LENGTH OF THE PASSWORD : "))
                        el = int(input("ENTER END LENGTH OF THE PASSWORD : "))
                        lop = password_generator(sl,el,chars)
                        lop.sort()
                        lop.sort(key=lambda x:len(x))
                        with open(file=(filename+".txt"),mode="w") as f:
                            for i in lop:
                                f.write(i+"\n")
                        print("\n---DONE---")
                    elif m==7:
                        print("\n---BYE---")
                        main_flag = False
                        sub_flag = False
                    else:
                        print("\nPLEASE ENTER A VALID OPTION")
                except ValueError:
                    print("\nPLEASE ENTER A VALID OPTION")
        elif n==2:
            print("\n---BYE---")
            main_flag = False
        else:
            print("\nPLEASE ENTER A VALID OPTION")
    except ValueError:
        print("\nPLEASE ENTER A VALID OPTION")
