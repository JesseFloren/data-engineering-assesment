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
    
    def __eq__(self, value):
        try:
            return self.name == value.name and self.iso_code == value.iso_code
        except:
            return False