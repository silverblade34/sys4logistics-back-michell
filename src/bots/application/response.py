from datetime import datetime
from time import gmtime, strftime

import json
import requests

class ResponseBot():
    def __init__(self):
        pass

    def parsedResponsePlaca(self,name):
        data = {"name": name,"flag":1}
        dataJson = json.dumps(data)
        response = requests.post('http://67.207.87.64:8000/api/v1/bot/data',dataJson)
        raw = response.json()
        result = raw['data'][-1]['nm']
        placa = result[0:6]
        return placa

    def arrayNames(self):
        arrayNames = ["SECURITAS","COMSATEL"]
        return arrayNames

    def parsedRespondBot(self, bots):
        ListBots = []
        for bot in bots:
           dicBot = {}
           placa = self.parsedResponsePlaca(bot[0])
           dicBot['name']=bot[0]
           dicBot['status']=bool(bot[1])
           dicBot['lateplate'] = placa
           dicBot['date'] = bot[2]
           ListBots.append(dicBot)
        return ListBots


