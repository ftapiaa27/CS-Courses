my_list = ["dogoasdf", "dogoloco", "dogoheehee"]
prefix = my_list[0]
for i in range (1, len(my_list)):
    while (my_list[i].find(prefix) != 0):
        prefix = prefix[:len(prefix)-1]
        print(prefix)
print(prefix)
##print(my_list[2].find("dogo"))
##print(len(prefix))
##my_list[0] = my_list[0][:3]
##print(my_list[0])
