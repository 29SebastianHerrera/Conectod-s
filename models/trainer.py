class Trainer():

    def __init__(self, name: str, lastName: str, age: int):
        self.name = name
        self.lastName = lastName
        self.age = age

    def to_json(self):

        return {
            'name': 'Sebastian',
            'lastName': 'Herrera',
            'age': 21,
        }


