# FASTAPI
from fastapi import FastAPI 
from src.bots.domain.bot import bot  
from src.users.domain.bot import bot 

app = FastAPI()
app.include_router(bot)


