from fastapi import Body, FastAPI
from pydantic import BaseModel

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
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    book(1, 'computer science and eng', 'arif','very nice book', 5),
    book(2, 'computer science and eng 2', 'asif','very nice book', 5),
    book(3, 'computer science and eng 3', 'lamia','very nice book', 5),
    
]

@app.get("/")
async def books():
    return BOOKS


@app.post("/createbook")
async def bookrequest(requestbook: BookRequest):
    BOOKS.append(requestbook)
    return requestbook