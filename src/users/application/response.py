
class UserResponse():
    @staticmethod
    def parsedUser(raw):
        if raw is not None:
            if len(raw['bearer_token'])>0:
                message = "Usuario Válido"   
                return raw, message
            else:
                raise Exception("Token Invalido")
        else:
            raise Exception("Usuario no válido")