#Dette er hovedprogrammet
import underprogram
underprogram.funk_skrivUT("Fra hovedprogram")

#importere bare funk
from underprogram import funk_skrivUT
funk_skrivUT("importert bare den ene funksjonen")

#importere som noe annet
from underprogram import funk_skrivUT as ut
ut("korteste")