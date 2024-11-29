#Dette programmet printer ut fila navn.txt for linje med løkke

obj_FilInn = open("navn.txt", "r")

for linje in obj_FilInn:
    print(obj_FilInn.readline())

obj_FilInn.close()