from voluptuous import Schema, ALLOW_EXTRA

SUCCESSFUL = 200

login = Schema({
    "username": str,
    "password": str
},
     extra=ALLOW_EXTRA)

