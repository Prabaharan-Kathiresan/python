
"""
---------------objectives-----------------
1. starred expression
2. multiple arguments and multiple return values
3. data type conversion 
4. type hints
5. parameter ordering def function_name(a, b, *args, option=True, **kwargs)
6. Kwargs
"""


def addition(a: int, b: int) -> int:
    # with type hints
    return a+b

def subtraction(a: int, b: int):
    # with out the type hints
    return a-b

def multiplication(a:int, b:float) -> float: #type hints are labels, they dont actualy does conversion
    return a*b

def division(a:int=40, b:int=20) -> int:
    return a/b


"""
------------------Private function----------------------------
1. private or internal functions are prefixed with double underscores __
"""
def __division_multi_returns(a: int, b:int) -> int | None :
    if(b == 0):
        return None
    return a/b


"""
------------------Package Private----------------------------
1. Package private are prefixed with single underscores
"""
def _type_conversion(a:str, b:str) -> tuple[int, int]:
    #returns 2 values
    return int(a),int(b)

"""
----------- Multi arguments and multi returns-------------------
1. to receive multiple arguments use *var_name: <data_type>
2. to return multiple return values use type hints like tuple[int,int,int]
3. use ... when variable number of returns, ie. tuple[int,...]
"""
def _type_conversion_input(*inputs: str) -> tuple[int,...]:
    return tuple(int(value) for value in inputs)


"""
---------------kwargs----------------------------------
1. kwargs is a dictionary
"""
def print_users(**user_inputs:str):
    print(user_inputs)

   
if __name__ == "__main__":
    print(addition(10,20))
    print(subtraction(10,20))
    print(multiplication(10,20.5))
    print(division())
    print("------------User Input--------------------")
    # var1 = int(input("Enter the first number")) #input returns string, convert it 
    # var2 = int(input("Enter the second number"))
    # print()
    # print("Addition=",addition(var1,var2))
    # print("Subtraction=",subtraction(var1,var2))
    # print("Multiply=",multiplication(var1,var2))
    # print("Division=",division(var1,var2))
    # print("------------Multi inputs at the same line--------------------")
    # var3, var4=input("Enter the two numbers").split() #split returns the list, when it sees the left side of = with multiple variable name it unpacks it.
    # print(var3,var4)
    print("------------Handle multiple type hints--------------------")
    print(__division_multi_returns(10,0))
    print(__division_multi_returns(10,2))
    print("------------Handle multiple return values--------------------")
    print(_type_conversion("10","20"))
    a,b = _type_conversion("10",21.2)
    print(a, b)
    a,b = _type_conversion(float("10.5"),21.2) #int("10.5") throws error, we need to convert the value to float and send
    print(a, b)
    nums = _type_conversion_input(*input("Enter numbers with spaces ").split()) #here *input is unpacking the list to separate string values
    print(nums) #prnt the values as tuple
    print(*nums) #prints the vlaues as separate values, this is known as starred expression
    name, age = input("Enter name and age").split()
    print_users(name=name, age=age)



    





    
    
    
    
    


    

    
