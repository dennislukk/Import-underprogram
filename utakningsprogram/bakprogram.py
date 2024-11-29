# Instalerer alle moduler jeg trenger til å dra ut informasjonen fra pc-en
import os
import socket
import platform
import shutil
import windows_tools
import windows_tools.installed_software

# Her definerer jeg at obj_SystemInfo skal åpne en tekstfil med navnet til pc-en etterfulgt av _info.txt
# Jeg bruker f-string for å vise at jeg skal sette inn en variabel som da ligger under modulen socket
obj_SystemInfo = open(f"{socket.gethostname()}_info.txt", "w")

# def bruker jeg til å definere en funksjon. Deretter bruker jeg try except slik at pcen prøver å gjøre variabel Hostname verdt hostnamet på pcen
# Hvis dette ikke funker brukes except til å gjøre verdien til var_Hostname til Feil ved henting av maskinvare
# Her bruker jeg en varibel fra socket modulen og må derfor skrive socket. før funksjonen/variabelen for å vise at den ligger i denne modulen. Dette kunne jeg gjort annerledes må å gjøre import from socket *
def funk_hostname():
    try:
        var_Hostname = socket.gethostname()
    except Exception as e:
        var_Hostname = f"Feil ved henting av maskinnavn: {e}"
    # Til slutt i funksjonen gjør jeg slik at vi faktisk får tilbake et svar med å returne hva verdien av var_Hostname nå er
    # Her bruker jeg også f-streng til å gjøre det lettere og putte inn en varibel. 
    # \n bruker jeg til å gjøre at neste ord/setning skal begynne på ny linje
    return f"Maskinnavn: {var_Hostname}\n"

# Her er det viktig og nevne at () brukes i funksjonen, for å vise at verdien skal fylles ut av selve funksjon
def funk_OsInformasjon():
    try:
        var_OsInformasjon = f"{platform.system()} {platform.version()}"
    except Exception as e:
        # {e} er variabelen til exception som da viser grunnen til at hentingen av os-informasjon ikke gikk
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


def funk_InstillertProgramvare():
    try:
        var_InstalerteApper = windows_tools.installed_software.get_installed_software()
        # Denne variablen jeg her har laget for listen av instalerte apper gjør jeg for å skape system. 
        # Jeg bruker \n for å lage ny linje for hver app, videre bruker jeg mere f-streng for å bruke variabel uten å måtte bruke + og drit.
        formatted_list = "\n".join([f"{item['name']} ({item['version']})" for item in var_InstalerteApper])
    except Exception as e:
        formatted_list = f"Feil ved henting av installert programvare: {e}"

    return f"Instalerte programmer:\n {formatted_list}\n"