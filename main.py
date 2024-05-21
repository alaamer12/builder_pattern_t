from vehicle_assembly import vehicle_assembly
from house_constraction import SimpleHouseBuilder, LuxuryHouseBuilder
from meal_ordering import CustomSaladBuilder, CustomSandwichBuilder




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    match i:=int(input('1. vehicle_assembly\n2. house_constraction\n3. meal_ordering\n your choice: ')):
        case 1:
            vehicle_assembly()
        case 2:
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
        case 3:
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
            print(custom_sandwich_builder, '\n', custom_salad_builder)
        case _:
            print('invalid input')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
