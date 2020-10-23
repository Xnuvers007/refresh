import webbrowser
from time import time
from time import sleep

url = input ("Masukan Url yang ingin di refresh (https://) = ")

while True:
    print ("Sedang Merefresh...")
    webbrowser.open(url) #new=0
    sleep(20) #30
