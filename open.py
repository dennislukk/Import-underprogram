#Det vi skal gjøre nå er å åpne en fil og printe det ut

obj_FillInn = open("navn.txt", "a")

var_Navn = input("Skriv inn fornavn og etternavnet ditt: ")

var_Fødseldato = input("Skriv inn fødselsdatoen din: ")

obj_FillInn.write(var_Navn+" " + var_Fødseldato+"\n")

obj_FillInn.close()



