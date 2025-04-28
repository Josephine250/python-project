class book:
    def __init__(self,author_name,page):

        self.author_name = author_name
        self.page = page
    def writting (self):
        print("write on page four")
class history(book):
        def __init__(self,author_name,page,price):
            super().__init__(author_name,page)
            self.price = price
        def display(self):
            print(f"The book is {name}and {price}")
b1 = history("Johnbee",1023,20000)
b2 = history("Jackson",2355,10000)
b2.writting()
b2.display
print("name of write:",b2.author_name)
print("page of book",b2.page)
print("price of book",b2.price)
                 

   

    