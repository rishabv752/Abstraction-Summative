class gen():

    def asciiart(self):
        print('''
        
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗                                                                   
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗                                                               
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║                                                               
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║                                                               
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝                                                               
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝                                                                
                                                                                                                                                   
████████╗██╗  ██╗███████╗     █████╗ ██╗     ██╗███████╗███╗   ██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║     ██║██╔════╝████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   ███████║█████╗      ███████║██║     ██║█████╗  ██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
   ██║   ██╔══██║██╔══╝      ██╔══██║██║     ██║██╔══╝  ██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
   ██║   ██║  ██║███████╗    ██║  ██║███████╗██║███████╗██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                           ''')
        gen.start()


    def start(self):
        vname=input("Please enter your alien's name = ")
        if vname == "":
            print("Please type a name for your alien!")
            gen.start()
        else:
            gen.age()


    def age(self):
        vage=(input("Please enter your alien's age =  "))

        if vage.isdigit():
            gen.gender()
        else:
            print("Please use a number not a letter/word")
            gen.age()




    def gender(self):

        vgender=str(input("What gender is your alien? Type B for Boy, or G for Girl"))

        if vgender == "B" or vgender == "b":
            print("Your alien is a Boy!")
            gen.part_customize()

        elif vgender == "G" or vgender == "g":
            print("Your alien is a Girl!")
            gen.part_customize()

        else:
            print("Please choose one of the 2 genders!")
            gen.gender()

    def part_customize(self):

        vpart_customize=input("Press: 1 - Customize face, 2 - Customize upperbody, 3 - Customize lower body")

        if vpart_customize == 1:
            gen.face_customize()
        elif vpart_customize == 2:
            gen.upper_customize()
        elif vpart_customize == 3:
            gen.lower_customize()
        else:
            print("Please press 1, 2 or 3 to customize your alien")
            gen.part_customize()

    def face_customize(self):

        vchoice = input("Press the number to customize that part of the face: 1-Hair, 2-Nose, 3-Structure ")
        if vchoice == 1:
            gen.hair_customize()
        elif vchoice == 2:
            gen.nose_customize()
        elif vchoice == 3:
            gen.structure_customize()

        else:
            print("Please press 1, 2 or 3 to customize your alien")
            gen.face_customize()













gen = gen()
gen.asciiart()

