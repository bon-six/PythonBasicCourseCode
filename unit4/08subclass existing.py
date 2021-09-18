

class MyString (str):
    def __init__(self,a):
        super().__init__()
        pass
    def print_content(self):
        print(self.content)


s1 = MyString(14.5)

s1.content = 'abcABC'

print(s1)
print(s1.content)
