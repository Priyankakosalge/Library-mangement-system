# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:25:31 2021

@author: WINDOWS
"""

class library:
    list_of_admins={'username':'admin','password':'admin'}
    def admin():
        username=input('enter the username')
        password=input('enter the password')
        if (username in library.list_of_admins['username']) and (password in library.list_of_admins['password']):
            print("you logged in sucessfully")
        else:
              print("Please enter the correct data")
    
import random
class Book:
    list_of_book=[]
    
         
    def addbook():
        title=input('enter the title of book')
        author=input ('enter the author of book')
        pages=input('enter the no.of pages of book')
        copies=input ('enter the no.of copies of book')
        isbn=input('enter the isbn no.of book')
        published_year=input('enter the published year of book')
        key=['bookid','title','author','pages','copies','isbn','publishedyear']
        values=[random.randint(1,9999),title,author,pages,copies,isbn,published_year]
        
        Book.list_of_book.append(dict(zip(key,values)))
        print('book is sucessfully added to the library')
    def printlistofbook():
        print(Book.list_of_book)
    def deletebook():
        list1=Book.list_of_book
        bookid=input('enter the book Id which you want to delete')
        for book in list1:
            for key,value in book.items():
                if book['bookid']==bookid:
                    list1.remove(book)
                    print('book is deleted')
                else:
                    print('you entered wrong book ID')
    
class borrower:
    list_of_borrower=[]
    history=[]
    def borrower_registation():
        info=[]
        name=input('enter the full name')
        info.append(name)
        dob=input('enter the DOB')
        info.append(dob)
        contactno=input('enter the contact no.')
        info.append(contactno)
        emailid=input('enter the email ID')
        info.append(emailid)
        password=input('enter the password')
        info.append(password)
        borrower.list_of_borrower.append(info)
        print('registation is sucessfull')
    
    def listofborrower():
        print(borrower.list_of_borrower)
        
    def login():
        emailid=input('enter the email Id')
        password=input('enter the password')
        list1=borrower.list_of_borrower
        for i in range(len(list1)): 
            
            if (emailid in list1[i] ) and (password in list1[i] ):
                    print("Login successful")
            else:
                    print("Incorrect login email and password")
    
    def listofborrowedbook():
        pass
class Admin:
    books= Book()
    borrower=borrower()
    import datetime
    
    issuebook=[]
    def detailsofborrower():
        for i in borrower.list_of_borrower:
            print(""'details of borrower' and 'history'"",borrower.list_of_borrower[i],borrower.history[i])
    
    def issuebook():
        import datetime
       
        bookid=input('enter the book id which to be issued')
        emailid=input('enter the email id of boorrower')
        for i in range(len(Book.list_of_book)):
            if bookid in Book.list_of_book:
                Admin.issuebook.append(bookid,emailid,datetime.datetime.now())
                print('book is issued')
            else:
                print('book is not available in library')
    def returnbook():
          import datetime
          bookid=input('enter the bookid which you want to return')
          ct_date=datetime.datetime.now()
          for i in range(len(Admin.issuebook)):
                if Admin.issuebook[i][0] ==bookid:
                    ct_date -  Admin.issuebook[i][2]==15
                    print('book is returned ')
                else:
                    print('you have Charge fine of INR 100')
        
if __name__ == '__main__':
        ans = True
        print("\nEnter the number corresponding to what you want to choose:")
        while ans:                   
                choice=int(input('/n1.admin /n2.borrower'))
                print(choice)
                if choice==1:
                    library.admin()
                    print('welcome admin')
                    ans=True
                    while ans:
                
                        print("\nEnter the number corresponding to what you want to choose:")
                        choice=int(input('/n1. for add book /n2.delete book /n3.list of all borrower /n4.issue book /n5.return book/n6.list of all book/n7.exit'))
          
              
                        if choice == 1:
                            Book.addbook()
                        elif choice==2:
                            Book.deletebook()
                        elif choice==3:
                            borrower.listofborrower()
                        elif choice==4:
                            Admin.issuebook()
                        elif choice==5:
                            Admin.returnbook()
                        elif choice==6:
                            Book.printlistofbook()
                        elif choice==7:
                            ans=False
                        else:
                            print('you entered wrong choice')
                elif choice==2:
                        print("\nEnter the number corresponding to what you want to choose:")
                        no= int(input("/n1.for registation /n2.for login"))
                        if no==1:
                                borrower.borrower_registation()
                        elif no==2:
                                borrower.login()
                                ans=True
                                while ans:
                                    print('enter the no.cooreesponding to what you want to choose')
                                    choice=int(input('1.view list of book /n2.borrowing history/n3.exit'))
                                    
                                    if choice==1:
                                             borrower.listofborrowedbook()
                                    elif choice==2:
                                             borrower.history()
                                    elif choice==3:
                                        ans=False
                                    else:
                                         
                                             print('you enterd wrong input')
                        else:
                            print('you enterd wrong input')
                else:
                            print('you enterd wrong input')
           
                            
                   
    
         