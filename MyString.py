class MyString(str):
    def __new__(cls, string):
        if isinstance(string, str):
            return str.__new__(cls, string)
        else:
            return string

    def add(self, value):
        return self + value



# my_string = MyString("123456")
# my_string = my_string.add("123")

my_string = MyString(123)

print(type(my_string))