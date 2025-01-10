from dataclasses import dataclass

@dataclass
class customer():
    name: str
    birth: str
    age: str

    def __init__(self, name, birth, age):
        self.name = name
        self.birth = birth
        self.age = age
        
    # def create_customer():
        