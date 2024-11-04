from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'title1', 'price': 500, 'auth': 'arif'},
    {'title': 'title2', 'price': 1500, 'auth': 'asif'},
    {'title': 'title3', 'price': 5100, 'auth': 'arif khan'},
    {'title': 'title4', 'price': 5000, 'auth': 'rupu'}
]

@app.get("/")
async def getbook():
    return {'message':'welcome'}

@app.get('/books')
async def booklist():
    return BOOKS

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

