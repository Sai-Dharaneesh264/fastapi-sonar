from fastapi import FastAPI

from cruds import login_message

app = FastAPI()



@app.get('/login')
async def get_login_message():
    response = await login_message()
    return response


@app.get('/home')
def get_home_page():
    return "this is home page"


@app.get('/careers')
def get_careers_page():
    return "This is careers page"