class Persona:
    def __init__(self, name:str="John", last:str="Doe", mail:str="mail@mail.com", phone:str="8180000000"):
        self._name = name
        self._last = last
        self._mail = mail
        self._phone = phone

    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, value):
        self._name = value
    @property
    def Last(self):
        return self._last
    @Last.setter
    def Last(self, value):
        self._last = value
    @property
    def Mail(self):
        return self._mail
    @Mail.setter
    def Mail(self, value):
        self._mail = value
    @property
    def Phone(self):
        return self._phone
    @Phone.setter
    def Phone(self, value):
        self._phone = value

    def __str__(self):
        return f"Persona=[name:{self._name} {self._last}, mail:{self._mail}, phone:{self._phone}]"

    def dict_persona(self):
        return {
            "Person Information": {
                "Name": self._name,
                "Last": self._last
            },
            "Contact Information": {
                "Mail": self._mail,
                "Phone": self._phone
            },
        }