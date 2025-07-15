from app import app, db

@app.post("/")
async def root():
    collection = await db.users.find_one({"email": "jhon@dmail.com"})
    print(collection)
    return {"message": "Hello Wor1ld"}