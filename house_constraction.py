class SimpleHouse:
    def __init__(self) -> None:
        self.bedrooms = 0
        self.bathrooms = 0
        self.kitchen = 0
        self.living_room = 0
        self.garage = 0
        self.make = None

    def __str__(self):
        return f'{self.make}, {self.bedrooms = }, {self.bathrooms = }, {self.kitchen = }, {self.living_room = }, {self.garage = }\n'


class LuxuryHouse:
    def __init__(self) -> None:
        self.bedrooms = 0
        self.bathrooms = 0
        self.kitchen = 0
        self.living_room = 0
        self.garage = 0
        self.make = None

    def __str__(self):
        return f'{self.make}, {self.bedrooms = }, {self.bathrooms = }, {self.kitchen = }, {self.living_room = }, {self.garage = }\n'


class SimpleHouseBuilder:
    def __init__(self) -> None:
        self._house = SimpleHouse()

    def set_make(self, make: str):
        self._house.make = make
        return self

    def set_bedrooms(self, bedrooms: int):
        self._house.bedrooms = bedrooms
        return self

    def set_bathrooms(self, bathrooms: int):
        self._house.bathrooms = bathrooms
        return self

    def set_kitchen(self, kitchen: int):
        self._house.kitchen = kitchen
        return self

    def set_living_room(self, living_room: int):
        self._house.living_room = living_room
        return self

    def set_garage(self, garage: int):
        self._house.garage = garage
        return self

    def build(self) -> SimpleHouse:
        return self._house


class LuxuryHouseBuilder:
    def __init__(self) -> None:
        self._house = LuxuryHouse()

    def set_make(self, make: str):
        self._house.make = make
        return self

    def set_bedrooms(self, bedrooms: int):
        self._house.bedrooms = bedrooms
        return self

    def set_bathrooms(self, bathrooms: int):
        self._house.bathrooms = bathrooms
        return self

    def set_kitchen(self, kitchen: int):
        self._house.kitchen = kitchen
        return self

    def set_living_room(self, living_room: int):
        self._house.living_room = living_room
        return self

    def set_garage(self, garage: int):
        self._house.garage = garage
        return self

    def build(self) -> LuxuryHouse:
        return self._house


if __name__ == "__main__":
    simple_house_builder = (SimpleHouseBuilder().
                            set_make('House').
                            set_bedrooms(3).
                            set_bathrooms(3).
                            set_kitchen(3).
                            set_living_room(3).
                            set_garage(3)
                            .build()
                            )
    luxury_house_builder = (LuxuryHouseBuilder()
                            .set_make('Luxury House')
                            .set_garage(3)
                            .set_living_room(3)
                            .set_kitchen(3)
                            .set_bathrooms(3)
                            .set_bedrooms(3)
                            .build()
                            )
    print(simple_house_builder, luxury_house_builder)
