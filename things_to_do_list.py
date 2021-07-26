things_to_do_list = []

while True:
  


    enter_work = input("enter the work you want to do : ")
    things_to_do_list.append(enter_work)
    
    if enter_work == "close":
        print("THINGS TO DO LIST -------------")
        things_to_do_list.pop()
        print(",".join(things_to_do_list))
        print("make sure to the things on things to do list !")
        break
