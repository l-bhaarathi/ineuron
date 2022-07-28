# i want to extract 234 from the list

l=[3,4,5,6,7,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,6657,6),{"key1" :"sudh",234:[23,45,656]}]

# I was able to extract this way

def get_num(l,n):
    for i in l:
        if type(i)==int:
            if i==n:
                print(i)
        elif type(i)==list or type(i)==set or type(i)==tuple:
            get_list(i,n)
        elif type(i)==dict:
            get_list(i.keys(),n)
            get_list(i.values(),n)
get_list(l,234)

# I want the operation done inside a class I dont how to do that.


class data:
    def __init__(self):
        self.l=[3,4,5,6,7,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,6657,6),{"key1" :"sudh",234:[23,45,656]}]
