class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
        
    def displaybooks(self):
        print("Books present in the library are :")
        for book in self.books:
            print("*"+book)

    def LibbookRequest(self,name):
        if name in self.books:
            print("Book requested is {}".format(name))
            print(" This book is available and you can take it")
            print("But please , Return it back in 30 days")
            self.books.remove(name)
            return True
        else:
            print(" Book requested is not available in college library at present!!!")
            return False

    def LibbookReturn(self,name):
        print("Book returned  back by student is {}".format(name))
        self.books.append(name)
        return True 

class Student:
    def BookRequest(self):
        self.b=input("Enter name of book from all available books:")
        return self.b

    def BookReturn(self):
        self.z=input("Enter name of book you want to return back: ")
        return self.z

if __name__ == "__main__":
    Collegelib=Library(["Engineering Maths","Basic electronics","Python","Workshop","Physics"])
    student=Student()
    while(True):
        LibraryPc=''' Welcome to our College Library 
        ENTER 1  to view all books present in library
        ENTER 2  to request a book
        ENTER 3  to return a book
        ENTER 4  to exit() 
        '''
        print(LibraryPc)
        a=(input("Please enter your option (only an integer please): "))

        if  (int(a)==1):
            Collegelib.displaybooks()
        elif (int(a)==2):
            Collegelib.LibbookRequest(student.BookRequest()) 
        elif (int(a)==3):
            Collegelib.LibbookReturn(student.BookReturn())
        elif (int(a)==4):
            print("Thankyou ")
            exit()
        else :
            print("You entered wrong option!!!")
            exit()
            

