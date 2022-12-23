from ..application.response import ResponseBot
from .mysql import MysqlBots


class BotsController():
    def __init__(self):
        self.mysql = MysqlBots()
        self.responseData = ResponseBot()

    def controllerBotsPlaca(self):
        bots = self.mysql.statusBots()
        list = self.responseData.parsedRespondBot(bots)
        return list
