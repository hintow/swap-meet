import uuid


class Item:
    def __init__(self, id=None, condition=0, age=0):
        if id is not None and not isinstance(id, int):
            raise ValueError(f"id={id}, expected int")
        if not isinstance(condition, int) and not isinstance(condition, float):
            raise ValueError(f"condition={id}, expected number")
        self.id = uuid.uuid4().int if not id else id
        self.condition = condition
        self.age = age

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return self.__class__.__name__

    def condition_description(self):
        if self.condition >= 4:
            return "Excellent!"
        if 2 <= self.condition < 4:
            return "Good!"
        return "Not the best!"
