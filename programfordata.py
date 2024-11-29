import os
import socket
import platform
import shutil

obj_SystemInfo = open("systeminfo.txt", "w") #Oppretter en fil som heter systeminfo.txt

var_Hostname = socket.gethostname() #Henter maskinnavnet

var_OsInformasjon = f"{platform.system()} {platform.version()}" #Henter OS-informasjon

var_LedigDiskplass = shutil.disk_usage("/") #Henter ledig diskplass

var_brukernavn = os.getlogin() #Henter brukernavn

var_HentIpAdresse = socket.gethostbyname(var_Hostname) #Henter IP-adresse



obj_SystemInfo.write(f"Maskinnavn: {var_Hostname}\n")
obj_SystemInfo.write(f"OS-informasjon: {var_OsInformasjon}\n")
obj_SystemInfo.write(f"Ledig diskplass: {var_LedigDiskplass}\n")
obj_SystemInfo.write(f"Brukernavn: {var_brukernavn}\n")
obj_SystemInfo.write(f"IP-adresse: {var_HentIpAdresse}\n")

obj_SystemInfo.close() #Lukker filen