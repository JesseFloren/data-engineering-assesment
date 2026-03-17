class Country:
    name: str
    iso_code: str

    def __init__(self, name: str, iso_code: str):
        self.name = name
        self.iso_code = iso_code

    def __str__(self):
        return "Country {name: " + self.name + ", iso_code: " + self.iso_code + "}"
    
    def __repr__(self):
        return self.__str__()