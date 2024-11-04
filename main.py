def add_sum(a:int,b:int)->int:
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("the values must be int")
    return a+b


add1=add_sum(1,2)
print(add1)