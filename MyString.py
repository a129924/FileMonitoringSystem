class MyString(str):
    def __new__(cls, string):
        return str.__new__(cls, string)

    def add(self, value):
        return self + value



my_string = MyString("123456")
my_string = my_string.add("123")

print(my_string)