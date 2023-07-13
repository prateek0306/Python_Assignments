class A:
    def __init__(self, a, b, c):
        self.__a = a  # private member
        self._b = b   # protected member
        self.c = c    # public member

    def display_A(self):
        print("Values of a, b, and c:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)  

    def display_B(self):
        print('public member: ',self.c)
        print('protectec member: ',self._b)
        try:
            print("private member: ", self.__a)  
        except AttributeError:
            print("Cannot access private member a from class B")

obj = B(365,265,165)
obj.display_A()
obj.display_B()

