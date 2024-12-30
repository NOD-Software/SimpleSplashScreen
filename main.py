##################################################
### EXAMPLE FILE TO SHOW HOW TO USE THE MODULE ###
##################################################

import sys
from SimpleSplashScreen import SplashScreen
import time

splash = SplashScreen("resources/NOD.png")

# simulating the loading process and parsing the percentage loaded to the splash screen
# replace this with actual data from your program

for simulated_percentage_done in range(101):
    splash.update_progress(simulated_percentage_done)
    time.sleep(0.01)

# if there is nothing to load and you want to show the splash screen then
# keep an eye out for updates on github, it's in my todo list for this project

###
### this is where you would put the code that you want to run after the splash screen is done
###

# exit the program
sys.exit()
