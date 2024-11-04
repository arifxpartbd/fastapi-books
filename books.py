from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'title1', 'price': 500, 'auth': 'arif'},
    {'title': 'title2', 'price': 1500, 'auth': 'asif'},
    {'title': 'title3', 'price': 5100, 'auth': 'arif'},
    {'title': 'title4', 'price': 5000, 'auth': 'rupu'}
]

@app.get("/")
async def getbook():
    return {'message':'welcome'}

@app.get('/books')
async def booklist():
    return BOOKS

@app.get('/booklistbyauth/{nameofauth}')
async def booklistbyauth(nameofauth: str):
    returnBooks = []
    for book in BOOKS:
        if book.get('auth').casefold() == nameofauth.casefold():
            returnBooks.append(book)

    return returnBooks        

@app.get('/books/{title}')
async def searchbook(title: str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book  
        else:
            return {'message': 'no data found'} 

@app.post("/books/create")
async def createBook(newbook = Body()):
    BOOKS.append(newbook)
    return {"message":"new book created", "data": newbook}        

@app.put("/books/update")
async def updateBook(updateBook = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updateBook.get('title').casefold():
            BOOKS[i] = updateBook

            return {'message':'book updated', 'data': updateBook} 

    else:
            return {'message': 'updated failed'}  
    
@app.delete("/books/delete")
async def deleteBook(title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == title.casefold():
            BOOKS.pop(i)  # Remove the book from the list
            return {'message': 'book deleted'}

    # If no matching book is found
    return {'message': 'delete failed'}
   