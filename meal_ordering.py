class CustomSandwich:
    def __init__(self):
        self.meat = None
        self.cheese = None
        self.lettuce = None
        self.tomato = None
        self.type_of_bread = None
        self.make = None

    def __str__(self):
        return f'{self.make}, {self.meat = }, {self.cheese = }, {self.lettuce = }, {self.tomato = }, {self.type_of_bread = }'

class CustomSalad:
    def __init__(self):
        self.lettuce = None
        self.tomato = None
        self.cheese = None
        self.make = None

    def __str__(self):
        return f'{self.make}, {self.lettuce = }, {self.tomato = }, {self.cheese = }'

class CustomSandwichBuilder:
    def __init__(self):
        self._sandwich = CustomSandwich()

    def set_meat(self, meat):
        self._sandwich.meat = meat
        return self

    def set_cheese(self, cheese: str):
        self._sandwich.cheese = cheese
        return self

    def set_lettuce(self, lettuce: str):
        self._sandwich.lettuce = lettuce
        return self

    def set_tomato(self, tomato: str):
        self._sandwich.tomato = tomato
        return self

    def set_type_of_bread(self, bread_type: str):
        self._sandwich.type_of_bread = bread_type
        return self

    def set_make(self, make: str):
        self._sandwich.make = make
        return self

    def build(self):
        return self._sandwich

class CustomSaladBuilder:
    def __init__(self):
        self._salad = CustomSalad()

    def set_cheese(self, cheese: str):
        self._salad.cheese = cheese
        return self

    def set_tomato(self, tomato: str):
        self._salad.tomato = tomato
        return self

    def set_lettuce(self, lettuce: str):
        self._salad.lettuce = lettuce
        return self

    def set_type_of_bread(self, bread_type: str):
        self._salad.type_of_bread = bread_type
        return self

    def set_make(self, make: str):
        self._salad.make = make
        return self

    def build(self):
        return self._salad

if __name__ == "__main__":
    custom_sandwich_builder = (CustomSandwichBuilder().
                                set_make('Big Large Sandwich').
                                set_meat('meat').
                                set_cheese('cheese').
                                set_lettuce('lettuce').
                                set_tomato('tomato').
                                set_type_of_bread('bread').
                                build())
    custom_salad_builder = (CustomSaladBuilder().
                            set_make('Big Large Salad').
                            set_cheese('cheese').
                            set_tomato('tomato').
                            set_lettuce('lettuce').
                            set_type_of_bread('bread').
                            build())
    print(custom_sandwich_builder,'\n' ,custom_salad_builder)