class Star:

    type ='Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)


print('x is ', Star.x)  # o
Star.change()  # o
print('x is ', Star.x)

star = Star()  # o
print('x is ', star.x)  # o
star.change()  # Err

