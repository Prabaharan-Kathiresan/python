
print("Welcome",'to Python')


def greet() -> None:
    # with type hints
    print("Welcome to Day1")

def greet2():
    # with out the type hints
    print("Welcome to Day1")    
    return None #this line does not require since the python return when the last line reached



if __name__ == "__main__":
    print("you are running this module directly")
    greet()
    greet2()

"""
-------------basic print statements-----------------
1. print function by default adds end="\n" if not specified
"""
print("Hi","Hello")                             #Hi Hello #on the same line
print("Hi","Hello",sep="-")                     #Hi-Hello #on the same line
print("Hi","Hello","welcome",sep="-")           #Hi-Hello-welcom #on the same line

print("Hi","Hello",1,2.5,sep='-')                                       #Hi-Hello-1-2.5
print("hi","hello",sep="\n")                    #prints hello in new line
print("Hi","Hello",end="!")                     #Hi Hello!
print()                                         #adds new line, with out this line, above and below are combine, with this line, second prints in the new line
print("Welcome",'to','hello','world Python',end="!",sep=" ")
print()


"""
---------below prints are different types of string -------------------
1. single quote, 2. double quotes, 3. triple quotes
"""
print('Do u see "double quotes" are enclosed')
print("Do u see 'single quotes' are enclosed")
print("""First Line
Second Line""")

"""
-------------variables------------------------------
"""
a=10
b=20
print(a,b)
c,d = 30,40
print(c,d)
a=50;b=60;c=70;d=80 #dicouraged in python
print(a,b,c,d)
print()
var1,var2,var3 = 10,"Prabaharan",3.14
print(var1,var2,var3)
print()
print(f"var1={var1}\nvar2={var2}\nvar={var3}")
print()
print(f"var1={var1}",f"var2={var2}",f"var3={var3}",sep="\n")
print()
print(f"{var1=}\n{var2=}\n{var3=}")
var1_fl = 3.1
var2_fl = 3.2
print(f"{var1_fl:.2f}") #3.10
print(f"{var1_fl:06.2f}") #003.10
print(var1_fl+var2_fl)

