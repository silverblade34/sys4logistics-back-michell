def parsedRespondData(data):
    temp = {
        'data': data,
        'status': True,
        'message': 'ok',
    }
    return temp

def parsedRespond(data):
    temp = {
        'data': data[0],
        'status': True,
        'message': data[1]
    }
    return temp

def hasErrorMsg(err):
    temp = {
        'message': str(err),
        'status': False
    }
    return temp

def checkArgs(list, argsx):
    for item in list:
        if item in argsx:
            pass
        else:
            temp = '''No se encuentra el argumento: %s''' % (item)
            raise Exception(temp)