from fastapi import APIRouter
from src.users.insfrastructure.controller import UserController
from validations.validators import hasErrorMsg, parsedRespond, checkArgs

import requests


bot = APIRouter()

#MOSTRAR DATOS
@bot.get("/api/v1/login")
async def setUserParsed(user: str, pasw: str):
    try:
        _userCL = UserController()  
        raw = _userCL.validarUsuario(user, pasw) 
        return parsedRespond(raw)
    except Exception as err:
        return hasErrorMsg(err)
    