class library:
  def __init__(self,booklist):
    self.book=booklist
  def display(self):
    print(f"Books present in library are: {"\n ".join(self.book)}")
  def borrow(self,studentname,bookname):
    if bookname in self.book:
      self.book.remove(bookname)
      print(f"{studentname} has borrowed {bookname} book from library")
    else:
      print(f"book {bookname} is not available in library")

  def returnbook(self,bookname):
    self.book.append(bookname)
    print(f"Thanks for returning {bookname} book to library")  

  def receivebook(self,bookname):
    self.book.append(bookname)
    print(f"thanks for sponsering a {bookname} to the library")    

class student:
  def __init__(self):
    self.book=""
    self.name=input("enter your name: ")
  def requestbook(self):
    self.book=input("enter the book you want to borrow: ")
    return self.book
  def returnbook(self):
    self.book=input("enter the book you want to return: ")
    return self.book
  def sponcerbook(self):
    booksponcered=input("enter the book you want to sponser: ")
    return booksponcered


  #main


central_library = library([' ','python','c++','java','html','css','c'])


current_student = student()


if __name__=="__main__":


  while True:
    welcomemsg=f"WELCOME TO CENTRAL LIBRARY {current_student.name}"
    print(welcomemsg)
    selectanyoption=input("1. Display Books\n2. Request a Book\n3. Return a Book\n4. Sponser a Book\n5. Exit the Library\n")
    " ".join(selectanyoption)
    if selectanyoption not in ['1','2','3','4','5']:
      print("please select a valid option")
    elif selectanyoption=='5':
      print("thanks for visiting the library")
      break
    elif selectanyoption=='1':
      central_library.display()
    elif selectanyoption=='2':  
      requested_book = current_student.requestbook()
      central_library.borrow(current_student.name, requested_book)
    elif selectanyoption=='3':
      retrunbook=current_student.returnbook()
      central_library.returnbook(retrunbook)  
    elif selectanyoption=='4':
      sponceredbook=current_student.sponcerbook()
      central_library.receivebook(sponceredbook)
      
    else:
      print("invalid option")

