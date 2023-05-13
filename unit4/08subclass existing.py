
class MyString(str):
    def __init__(self,a):
        super().__init__()
        pass
    def print_content(self):
        print(self.content)

def run_test1():
    s1 = MyString(14.5)
    s1.content = 'abcABC'

    print(s1)
    print(s1[0], s1[-1])
    print(s1.content)
    s1.print_content()

if __name__ == '__main__':
    run_test1()
