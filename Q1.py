class a:
    def sample():
        print("In A")
class b(a):
    #Here we are over ride the parent class method
    def sample():
        print("In B")
obj = b()
b.sample()