import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI application instance
app = FastAPI()

# Model definitions
class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

#origins that are allowed to access our API, in this case react frontend
origins = [
    "http://localhost:5173"
]

#CORS middleware, CORS = Cross-Origin Resource Sharing, prohibits requests from other origins, cors will block out requests from other origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #define origins that are allowed to access our API
    allow_credentials=True, #allow credentials
    allow_methods=["*"], #allow all methods
    allow_headers=["*"], #allow all headers, can block if needed
)

#in memory database that will not persist when server shuts down
memory_db = {"fruits": []}

@app.get("/fruits", response_model=Fruits) #define root endpoint returns list of fruits from db in JSON
def get_fruits():
    return Fruits(fruits=memory_db["fruits"]) #returns an instance of the Fruits model

@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit): #take in a fruit object
    memory_db["fruits"].append(fruit) #add fruit to db
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) #run on all valid IP addresses on port 8000

""" sample app

class Item(BaseModel): #define item model for todo list, so we get a object that's modeled after this class
    text: str #required field for validation for server
    is_done: bool = False #optional field

# List to store items
items = [] 

@app.get("/")
def read_root(): #root dir, this is the function that will be called when the path is accessed
    return {"Hello": "World"}

@app.post("/items") #new endpoint
def create_item(item: Item): #pass item model directly, modeled object, item data now is json
    items.append(item)
    return items

@app.get("/items", response_model=list[Item]) #easy to work with frontend frameworks like react
def list_items(limit: int =10): #take limite query parameter
    return items[0:limit] #return first 10 items, if don't have 10 items, return all items; if don't specfiy limit, return all items

@app.get("/items/{item_id}", response_model=Item) #new endpoint
def get_item(item_id: int) -> Item: #path parameter, specifiy type
    if item_id < len(items):
        return items[item_id]
    else: 
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found") #return error message """