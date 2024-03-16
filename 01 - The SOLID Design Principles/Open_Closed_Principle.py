"""
Open-Close principle (OCP): open for expansion closed for modification
"""

# without OCP: product with size and color
from enum import Enum
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:

    def __init__(self, name, color: str, size: str):
        self.name = name
        self.size = Size[size]
        self.color = Color[color]

    def __str__(self):
        return self.name


class ProductFilter:

    @staticmethod
    def by_color(products: List[Product], color: str):
        color = Color[color]
        for product in products:
            if color == product.color:
                yield product

    # after deploy this app, it has been required to add filter by size, so we will edit this class again to add filter
    # this violate OCP
    # else what about adding filter by 'size and color' or filter by 'size or color'
    # so this called will be edited for every forever , for every new property added to class will change alot in filter

    @staticmethod
    def by_size(products: List[Product], size: str):
        size = Size[size]
        for product in products:
            if size == product.size:
                yield product


# let's build collect one ###########################################################################################
class Specification:
    def is_satisfied(self, item: Product): ...


class Filter:
    def filter(self, items: List[Product], spec: Specification): ...


# generic product filter


class ProductFilter(Filter):

    def filter(self, items: List[Product], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


# now we can inherit from  Specification to add all condition and user ProductFilter2 to be work with all filter


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = Color[color]

    def is_satisfied(self, item: Product):
        return self.color == item.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = Size[size]

    def is_satisfied(self, item: Product):
        return self.size == item.size


# what about 'and' Specification


class AndSpecification(Specification):
    def __init__(self, *specs: Specification):
        self.specs = specs

    def is_satisfied(self, item: Product):
        return all(map(lambda spec: spec.is_satisfied(item), self.specs))


class OrSpecification(Specification):
    def __init__(self, *specs: Specification):
        self.specs = specs

    def is_satisfied(self, item: Product):
        return any(map(lambda spec: spec.is_satisfied(item), self.specs))


if __name__ == "__main__":
    apple = Product(name="apple", color="RED", size="SMALL")
    tree = Product(name="tree", color="GREEN", size="LARGE")
    water = Product(name="water", color="BLUE", size="MEDIUM")
    products = [apple, tree, water]
    filter_manger = ProductFilter()
    color_filter = ColorSpecification("RED")
    size_filter = SizeSpecification("SMALL")
    color_and_size_filter = AndSpecification(color_filter, size_filter)
    color_or_size_filter = OrSpecification(color_filter, size_filter)

    for product in filter_manger.filter(products, color_filter):
        print(product)
    for product in filter_manger.filter(products, size_filter):
        print(product)
    for product in filter_manger.filter(products, color_and_size_filter):
        print(product)
    for product in filter_manger.filter(products, color_or_size_filter):
        print(product)
