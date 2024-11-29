import os
import socket
import platform
import shutil

obj_SystemInfo = open(f"{socket.gethostname()}_info.txt", "w") #Oppretter en fil som heter systeminfo.txt


def funk_hostname():
    try:
        var_Hostname = socket.gethostname()
    except Exception as e:
        var_Hostname = f"Feil ved henting av maskinnavn: {e}"

    return f"Maskinnavn: {var_Hostname}\n"

def funk_OsInformasjon():
    try:
        var_OsInformasjon = f"{platform.system()} {platform.version()}"
    except Exception as e:
        var_OsInformasjon = f"Feil ved henting av OS-informasjon: {e}"

    return f"OS-informasjon: {var_OsInformasjon}\n"

def funk_LedigDiskplass():
    try:
        var_LedigDiskplass = shutil.disk_usage("/")
        var_tilgjengelig_plass_gb = var_LedigDiskplass.free // (1024**3)
    except Exception as e:
        var_LedigDiskplass = f"Feil ved henting av ledig diskplass: {e}"

    return f"Ledig diskplass: {var_tilgjengelig_plass_gb} GB\n"

def funk_brukernavn():
    try:
        var_brukernavn = os.getlogin()
    except Exception as e:
        var_brukernavn = f"Feil ved henting av brukernavn: {e}"

    return f"Brukernavn: {var_brukernavn}\n"

def funk_HentIpAdresse():
    try:
        var_Hostname = socket.gethostname()
        var_HentIpAdresse = socket.gethostbyname(var_Hostname)
    except Exception as e:
        var_HentIpAdresse = f"Feil ved henting av IP-adresse: {e}"
    
    return f"Ip adresse: {var_HentIpAdresse}\n"


obj_SystemInfo.write(funk_hostname() + funk_OsInformasjon() + funk_LedigDiskplass() + funk_brukernavn() + funk_HentIpAdresse())
obj_SystemInfo.close() #Lukker filen