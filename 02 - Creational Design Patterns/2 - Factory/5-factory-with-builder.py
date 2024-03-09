# Factory to get the right builder
class HomeBuilderFactory:
    def get_home_builder(home_type):
        if home_type == 'apartment':
            return ApartmentBuilder()
        elif home_type == 'detached':
            return DetachedHouseBuilder()
        # Add more types as necessary
        else:
            raise ValueError("Unknown home type")

# Abstract builder class
class HomeBuilder:
    def add_floor(self):
        pass
    def add_roof(self):
        pass
    # Additional methods for customization
    def build(self):
        pass

class ApartmentBuilder(HomeBuilder):
    # Implement the steps specific to apartments
    def build(self):
        return "Apartment built with custom features"

class DetachedHouseBuilder(HomeBuilder):
    # Implement the steps specific to detached houses
    def build(self):
        return "Detached House built with custom features"

# Client code
home_type = 'apartment'  # This could come from user input
builder = HomeBuilderFactory.get_home_builder(home_type)
# Use the builder to customize the home
custom_home = builder.add_floor().add_roof().build()