from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is no needed, it's dynamic created", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=10, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra" :{
            "example":{
                "title":"a new book title",
                "author":"write a author name of the book",
                "description":"a new book description",
                "rating": 5
            }
        }
    }



BOOKS = [
    book(1, 'computer science and eng', 'arif','very nice book', 5),
    book(2, 'computer science and eng 2', 'asif','very nice book', 5),
    book(3, 'computer science and eng 3', 'lamia','very nice book', 2),
    
]

@app.get("/")
async def books():
    return BOOKS

@app.get("/books/{book_id}")
async def bookById(book_id:int):
    for book in BOOKS:
        if book.id == book_id:
            return book
        
@app.get("/books/")
async def bookByRating(rating: int):
    bookList = []
    for ragintbook in BOOKS:
        if ragintbook.rating == rating:
            bookList.append(ragintbook)   
    return bookList  


@app.post("/createbook")
async def bookrequest(requestbook: BookRequest):
    newbook = book(**requestbook.dict())
    BOOKS.append(findBookId(newbook))
    return newbook

def findBookId(books: book):
    books.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return books

@app.put("/books/update")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/{book_id}")
async def deletebook(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break    
    
 