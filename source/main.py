""" 
MAIN SERVICES
"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from route import mongo
app = FastAPI()

@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse("/docs")

app.include_router(mongo.app, prefix="/mongo", tags=['mongo'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9001, reload=True)
