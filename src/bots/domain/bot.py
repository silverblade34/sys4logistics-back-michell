from fastapi import APIRouter   
from src.bots.infrastructure.controller import BotsController
from validations.validators import hasErrorMsg, parsedRespondData, parsedRespond


bot = APIRouter()

#ENDPOINT PARA VERIFICAR EL ESTADO DEL BOT Y LA ULTIMA PLACA ANALIZADA
@bot.get("/api/v1/list/bots")
async def setDataParsed():
    try:
        _controller = BotsController()
        raw = _controller.controllerBotsPlaca()
        result = parsedRespondData(raw)
        return result
    except Exception as err:
        return hasErrorMsg(err)


