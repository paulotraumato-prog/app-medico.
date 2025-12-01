from fastapi import FastAPI,Depends,HTTPException,Request,Form,UploadFile,File
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import timedelta
import mercadopago
from .database import get_db,init_db,User,Case,Certificate
from .auth import get_password_hash,verify_password,create_access_token,get_current_user
from .config import *
import os

app=FastAPI(title='App Médico')
templates=Jinja2Templates(directory='app/templates')
mp=mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN) if MERCADOPAGO_ACCESS_TOKEN else None

@app.get('/',response_class=HTMLResponse)
async def home(request:Request):
 return templates.TemplateResponse('index.html',{'request':request})

@app.get('/setup-db')
async def setup_database():
 try:
  init_db()
  return {'message':'Database initialized'}
 except Exception as e:
  return {'error':str(e)}
