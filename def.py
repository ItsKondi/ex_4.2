def addition(x,y):
    print(x+y)

addition(5,2)

a = 1

def scope_demo():
    a = 2
    print(a)

scope_demo()
print(a)

def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

print(shopping())

def no_result_function():
    print("I am just printing I love you")
    print("and returning nothing to you!")

print(type(no_result_function()))