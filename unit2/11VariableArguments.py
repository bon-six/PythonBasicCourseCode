

def foo(a, b, c,*args, **kwargs):
    print(a,b,c)
    print(args)
    print(kwargs)


my_list = ['a','b','c']
my_dict = {'A':'aaa', 'B':'bbb'}

foo(1, 2, 10, *my_list, **my_dict)
foo(1, 2, *my_list, **my_dict)
foo(1, *my_list, **my_dict)


def foo(a, b, c, A, B):
    print(a,A,b,B,c)

foo(1,2,3,**my_dict)
foo(*my_list, **my_dict)
