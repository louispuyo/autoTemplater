from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from uvicorn import run
from typing import List
import requests
import os

# PATH :
base_path = os.path.abspath(os.path.curdir)
current_wd = 'templates'
# TEMPLATES :
templates = Jinja2Templates(directory="/Users/snowden/Programmation/python/webProgrammation/templates/core/templates")
# API :
api = FastAPI(debug=True)
api.mount("/static", StaticFiles(directory=base_path+"/static"), name="static")

# ROUTES :
@api.get('/')
async def root(request:Request):    
    tem = templates.get_template('index.html')
    return templates.TemplateResponse(tem, {'request':request})
    # return {"code":"hello world"}



if __name__ == "__main__":
    run(api)