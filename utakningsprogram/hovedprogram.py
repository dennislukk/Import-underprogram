# Her importerer jeg alt fra bakprogrammet, slik at jeg kan bruke funksjonene her.
import bakprogram

# Her viser jeg til at jeg skal plukke funksjoner og variabler med å bruke bakprogram. før hver ting. Deretter viser jeg at den skal skrive i obj_Systeminfo som da er en tekst fil som har blitt opprettet
# Deretter viser jeg til alt den skal legge til, derfor plukker jeg opp alle funksjonene etterfulgt av (), slik at den skal fylle ut informasjonen selv, basert på variabelen.
bakprogram.obj_SystemInfo.write(bakprogram.funk_hostname() + bakprogram.funk_OsInformasjon() + bakprogram.funk_LedigDiskplass() + bakprogram.funk_brukernavn() + bakprogram.funk_HentIpAdresse() + bakprogram.funk_InstillertProgramvare())
# Her sier jeg at filen skal bli lukket, slik at den ikke står å går. Det kan skape error
bakprogram.obj_SystemInfo.close() #Lukker filen