#Dette programmet leser inn fila navn.txt 1 linje av gangen

obj_FilInn = open("navn.txt", "r")

print (obj_FilInn.readline())
print (obj_FilInn.readline())

obj_FilInn.close()

