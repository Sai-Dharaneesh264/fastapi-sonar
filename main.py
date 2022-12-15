from fastapi import FastAPI

from cruds import home_page, login_message

app = FastAPI()



@app.get('/login')
def get_login_message():
    response = login_message()
    return response


@app.get('/home')
def get_home_page():
    response = home_page()
    return response


@app.get('/careers')
def get_careers_page():
    return "This is careers page"