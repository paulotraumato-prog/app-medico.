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

@app.get('/login',response_class=HTMLResponse)
async def login_page(request:Request):
 ...
