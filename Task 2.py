print('welcome to the slab ordering program')
cchoice = 0
dchoice = 0
slabshape = 0
size = 0
cchoiceconfirmed = 0
dchoiceconfirmed = 0
slabshapeconfirmed = 0
slabshapeconfirmedfinal = 0
sizeconfirmed = 0
sizeconfirmedfinal = 0
amountconfirmed = 0
m = 1
n = 0

while True:
    choice = input(
        "press c to assign a color to the slab;\n press d to define the depth of the slab;\n press s to define the size and shape of the slab;\n press k if you are done\n")
    if choice == "c":
        cchoice = input(
            'type grey if you want the color grey;\n type red for red;\n green for green;\n and if you want a custom color press c\n')
        if cchoice == "grey":
            cchoiceconfirmed = "grey"
        elif cchoice == "red":
            cchoiceconfirmed = "red"
        elif cchoice == "green":
            cchoiceconfirmed = "green"
        elif cchoice == "c":
            cchoiceconfirmed = "custom color"
        else:
            print("invalid input")
    elif choice == "d":
        dchoice = input('what slab depth would you desire 38 or 45? ')
        if dchoice == "38":
            dchoiceconfirmed = "38"
        elif dchoice == "45":
            dchoiceconfirmed = "45"
        else:
            print("invalid input")
    elif choice == "s":
        slabshape = input('what shape of slab would you prefer: square, rectangle or circle')
        if slabshape == "square":
            slabshapeconfirmed = "square"
            slabshapeconfirmedfinal = 1
            size = input("what size would you prefer, 600x600 or 450x450")
            if size == "600x600":
                sizeconfirmed = "600x600"
                sizeconfirmedfinal = 1
            elif size == "450x450":
                sizeconfirmed = "450x450"
                sizeconfirmedfinal = 1
            else:
                print("invalid input")
        elif slabshape == "rectangle":
            slabshapeconfirmed = "rectangle"
            slabshapeconfirmedfinal = 1
            size = input("what size would you prefer 600x700 or 600x450")
            if size == "600x700":
                sizeconfirmed = "600x700"
                sizeconfirmedfinal = 1
            elif size == "600x450":
                sizeconfirmed = "600x450"
                sizeconfirmedfinal = 1
        elif slabshape == "circle":
            slabshapeconfirmed = "circle"
            slabshapeconfirmedfinal = 1
            size = input("Diameter 300 or 450?")
            if size == "300":
                sizeconfirmed = "300"
                sizeconfirmedfinal = 1
            elif size == "450":
                sizeconfirmed = "450"
                sizeconfirmedfinal = 1
            else:
                print("invalid input")
        else:
            print("Invalid input")
    elif choice == "k":
        if cchoiceconfirmed == 0:
            print("you have not assigned a color to the slab yet")
        elif dchoiceconfirmed == 0:
            print("you have not assigned a depth to the slab yet")
        elif slabshapeconfirmedfinal == 0:
            print("you have not assigned the slab shape")
        elif sizeconfirmedfinal == 0:
            print("you have not assigned the size of the slab")
        else:
            print("ok we are good to go")
            print("So here are your slab details \n The color choice is " + str(cchoiceconfirmed))
            print("\n The depth of the slab is " + str(dchoiceconfirmed))
            print("\n The slab shape is " + str(slabshapeconfirmed))
            print("\n The size of the slab is " + str(sizeconfirmed) + "mm")
            # calculating volume for price
            if slabshapeconfirmed == "circle":
                radius = int(sizeconfirmed) / 2
                volume = 3.14 * int(radius) * int(radius) * int(dchoiceconfirmed)
                volumeforbatch = int(volume) * 20
                priceforgrey = int(volumeforbatch) / 100000
                if cchoiceconfirmed == "grey":
                    print("Your order costs $" + str(priceforgrey))
                elif cchoiceconfirmed == "custom color":
                    calculation = 5 + int(priceforgrey)
                    price = 115 / 100 * int(calculation)
                    print("price is $" + str(price))
                else:
                    price = 110 / 100 * int(priceforgrey)
                    print("price is $" + str(price))
            else:
                firstside = sizeconfirmed[:3]
                secondside = sizeconfirmed[:-4]
                volume = int(firstside) * int(secondside) * dchoiceconfirmed
                volumeforbatch = int(volume * 20)
                priceforgrey = int(volumeforbatch) / 100000
                if cchoiceconfirmed == "grey":
                    print("The price is $" + str(priceforgrey))
                elif cchoiceconfirmed == "custom color":
                    calculation = 5 + int(priceforgrey)

                    price = 115 / 100 * int(calculation)
                    print("The price is $" + str(price))
                else:
                    price = 110 / 100 * int(priceforgrey)
                    print("The price is $" + str(price))
            print("The price if for a order of 20 slabs and")


            break
    else:
        print("invalid input")
while True:
    amountofslabs = input("Please enter the amount of slabs you want to order between 20 to 100")
    if int(amountofslabs) > 100:
        print("you cannot order greater than 100 slabs")
    elif int(amountofslabs) < 20:
        print("you cannot order less than 20 slabs")
    else:
        break
print("your order will be rounded off to the nearest multiple of twenty")
while int(amountofslabs) > int(n):
    n = 20 * int(m)
    m = m + 1
if int(n) - 10 > int(amountofslabs):
    amountconfirmed = int(n) - 20
elif int(n) - 10 < int(amountofslabs):
    amountconfirmed = int(n)
print("the amount rounded is " + str(amountconfirmed))

finalprice = int(price)/20*int(amountconfirmed)
print("The final price is $" + str(finalprice))
