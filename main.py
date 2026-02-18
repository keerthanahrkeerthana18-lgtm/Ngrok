from fastapi import FastAPI
import uvicorn
from db import engine, Base
from routes import user_routes

# Initialize Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routes we defined above
app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)