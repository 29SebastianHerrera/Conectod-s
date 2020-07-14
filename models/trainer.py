class Trainer():

    def __init__(self, name: str, lastName: str, age: int):
        self.name = name
        self.lastName = lastName
        self.age = age

        return {
            'name': self.name,
            'lastName': self.lastName,
            'age': self.age

        }
