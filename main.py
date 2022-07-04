from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'data': {"message": "Hello "}}


'''
If we use dictionary in value part of data then it gets converted to list in JSON
example: {'data':{'ayush','singhal'}} the {'ayush','singhal'} part gets converted to ['ayush','singhal']
'''


@app.get('/about')
async def about():
    return {'data': {'ayush', 'singhal'}}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
