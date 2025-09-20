from persona import *
import json
persona_1 = Persona()
persona_1.Name = "Jazmin"
persona_1.Last = "Banda"
persona_1.Mail = "jazmin.bandav@gmail.com"
persona_1.Phone = "+52880269369"


print(persona_1.dict_persona())

with open("data.json", "w") as file:
    json.dump(persona_1.dict_persona(), file)