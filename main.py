import pysqlite3


class BookStore:
    def __init__(self, name):
        self.name = name
        self.con=pysqlite3.connect("mainBookStore.db")
        self.cur=self.con.cursor()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS books (title TEXT NOT NULL)''')
    
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Lenddickt(user_name TEXT NOT NULL, book_title TEXT NOT NULL)''')
        
        self.con.commit()

    def display_lenddickt(self):
        print("Lender-Book Database")
        self.cur.execute("SELECT * FROM Lenddickt")
        rows=self.cur.fetchall()
        for i in rows:
            print(f"Book: {i[1]}  user: {i[0]}")
        

    def displaybooks(self):
        print(f"Books present in our Store are ")
        self.cur.execute("SELECT * FROM Books")
        books=self.cur.fetchall()
        for (i,) in books:
            print(f"Title: {i}")

    def lendbook(self, user, book):
        self.cur.execute(f"SELECT * FROM Books WHERE title='{book}'")
        result = self.cur.fetchall()
        if result:
            self.cur.execute(f"INSERT INTO Lenddickt(user_name, book_title) VALUES('{user}', '{book}')")
            self.cur.execute(f"DELETE FROM Books WHERE title='{book}'")
            self.con.commit()
            print(f"Successfully lent {book}")


        else:
            print(f"Sorry the book {book} is not available in our store")


    def addbook(self,book):
        self.cur.execute(f"INSERT INTO Books(Title) VALUES('{book}')")
        self.con.commit()
        print(f"Thank you for Donating {book}")
    
    def returnBook(self, retbook, userName):
        self.cur.execute(f"SELECT * FROM Lenddickt WHERE book_title='{retbook}' AND user_name='{userName}'")
        ifBookInLend=self.cur.fetchall()
        if ifBookInLend:
            self.cur.execute(f"DELETE FROM Lenddickt WHERE book_title='{retbook}' AND user_name='{userName}'")
            self.cur.execute(f"INSERT INTO Books(Title) VALUES('{retbook}')")
            self.con.commit()
            print(f"{retbook} returned successfully")
        else:
            print(f"{retbook} not found in lenderBook datatbase")
    

if __name__ == '__main__':
    StoreName=input("Enter the name of the store: ")
    ProgramingBookStore = BookStore(StoreName)
    print(f'Welcome to {ProgramingBookStore.name} store. Enter your choice to continue')
    while True:
        print(f'1 to Display book')
        print(f'2 to Display Lender-Book Database')
        print(f'3 to Lend a book')
        print(f'4 to Add book')
        print(f'5 to return book')
        print("------------------YOUR CHOICE------------")

        try:
        
            choice=int(input())
        

            if choice==1:
                ProgramingBookStore.displaybooks()
            
            elif choice==2:
                    ProgramingBookStore.display_lenddickt()

            elif choice==3:
                book=input("Enter the name of the book: ")
                name=input("Enter your name: ")
                ProgramingBookStore.lendbook(name, book)

            elif choice==4:
                book=input("Enter the name of the book: ")
                ProgramingBookStore.addbook(book)
            
            elif choice==5:
                book=input("Enter the book u want to return: ")
                name=input("Enter your name: ")
                ProgramingBookStore.returnBook(book, name)

            else:
                print("Wrong input")

            print("press q to quit c to continue")
            choice2=""
            while(choice2 !="c" and choice2 !="q"):
                choice2=input()
                choice2=choice2.lower()
                if choice2=="q":
                    print(f"Thank you for visiting {ProgramingBookStore.name}")
                    exit(0)

                elif choice2=='c':
                    continue
        
        except ValueError:
            print("Enter a valid number")
        except pysqlite3.Error as e:
            print(f"Database error: {e}")