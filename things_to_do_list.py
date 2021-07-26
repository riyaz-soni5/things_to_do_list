things_to_do_list = []

while True:
  


    enter_work = input("enter the you want to do : ")

    print("THINGS TO DO LIST -------------")
    things_to_do_list.append(enter_work)
    print(",".join(things_to_do_list))
    
    if enter_work == "close":
        print("make sure to the things on things to do list !")
        break