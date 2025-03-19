from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki, search_wiki, phrase  # Import the search function

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "World"}


@app.get("/search/{name}")
async def search_wiki_endpoint(name: str):
    search_result = search_wiki(name)  # Call the imported search function first
    if search_result:  # Proceed only if search_result is valid
        return {"message": search_result}
    return {"error": "Search failed or no results found"}  # Handle search failure


@app.get("/wiki/{name}/{length}")
async def get_wiki(name: str, length: int):
    search_result = search_wiki(name)  # Call the search function first
    if search_result:  # Proceed only if search_result is valid
        return {"message": wiki(name, length)}
    return {"error": "Search failed or no results found"}  # Handle search failure


@app.get("/phrase/{name}")
async def get_phrase(name: str):
    search_result = search_wiki(name)  # Call the search function first
    if search_result:  # Proceed only if search_result is valid
        return {"message": phrase(name)}
    return {"error": "Search failed or no results found"}  # Handle search failure


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
