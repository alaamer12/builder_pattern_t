# Procedures
1. create the classes that will be build later or the classes the u want to provide
   1. inside this class define two main methods,
   `__init__`, and `__str__`
   the init method for giving the concrete methods that will be used [setters] in the builder class and also give them initial values
   and the str method for printing the values
2. create the builder class
   1. inside this class will have `__init__` methods and all setters methods and data validations methods and helper methods and the main method: `build` method
   NOTE: inside the init method u would make variable of the class u want to build or u can inherit from it
3. create the builder methods
4. then u would call the builder class not the main class and call the chain-methods and with the last method `build`
e.g. `builder =
```python
sandwich = (CustomSandwichBuilder().set_make('Big Large Sandwich').set_meat('meat').set_cheese('cheese').set_lettuce('lettuce').set_tomato('tomato').set_type_of_bread('bread').build())
```