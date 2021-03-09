#2020 7/6, Adam Locke
#stellar analysis and exoplanet tool

#import statements
import csv
import tkinter

#global variables
dataset = []


#csv import process to get data from NASA's exoplanet archive
'version one can use the local CSV that I downloaded, version two must use the NASA api'
path = r'C:\Users\qtc1097\Desktop\python\non-business projects\star systems catalogue\compositepars_2020.06.30_06.13.15.csv'
print(path,"\n")



def loadfromcsv():
    global dataset
    global path
    holder =[]
    holder2 =[]
    file = open(path, newline='', mode = 'r')
    hubble = csv.reader(file)
    for lines in hubble:
    


#functions to organize the data in tables or dictionaries

#functions to recall data about stars

#functions to recall data about planets
def findearthlikes():
    global dataset
    earthsize = []
    minsize = float(.95)
    maxsize= float(1.05)
    for items in dataset:
        items[22]= float(items[22])
        if items[22]> minsize and dataset[5]< maxsize:
            earthsize.append(items)
    starmass = []
    for items in earthsize:
        if items[85] == 1:
            starmass.append(items)
    planetdense = []
    for items in starmass:
        if items[37] >5 and items[37] < 6:
            planetdense.append(items)
    planethot = []
    for items in planetdense:
        if items[70] > 230 and items[70] <300:
            planethot.append(items)
    print("similar plent mass\n", earthsize,"\nsimilar stellar mass\n", starmass, "\nsimilar planet density\n", planetdense, "\nsimilar planet temperature in Kelvin\n", planethot)
            

#functions to perform comparisons

#functions to allow the user to define the parameters of a search

#functions to measure the distance between stars

#functions to calculate the probability of earth similarity based on distance from galactic core, star data, planet data

#functions to calculate the travel time necessary to reach a star

#csv export functions

#pdf export functions

#tkinter interface to allow users to enter variables for search, to present results, and to allow the user to export results into a CSV or PDF report

        ##########mainline process###########
loadfromcsv()
display = []
holder = []
display.append(dataset)
holder.append(display[0])
    
    
    
#findearthlikes()
