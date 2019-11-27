# standard importing
import my_module


# specific imports
import my_package
from my_package.sub_module import car1, greeting


if __name__ == "__main__":
    # using module
    a = my_module.divide(10, 2)
    b = my_module.multipy(20, 3)

    # from package
    brand = car1['brand']
    text = greeting('Metin')

    # lets print it all
    print(a, b, brand, text)


