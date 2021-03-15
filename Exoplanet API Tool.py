#Adam Locke 2021
#NASA Exoplanet API tool
#This script calls to nasa and uses the exoplanet API to obtain information about exoplanets  based upon user selected parameters.
#Please feel free to use this script, so long as you mention who wrote it :)


'''IMPORTANT NOTES
The NASA exoplanet archive uses SQL so the api requests have to include valid SQL statements.  The database returns CSV as the default file format.  I have coded it for json.

The masses of planets are measured in comparison to Jupiter.  The earth has a mass of .00314 Jupiter Mass, so the code should be written to pick planets in this mass cateogry as earth-like.  The same is true of. the radii of planets, the earth has .091 Jupiter radius.

pl_dens measures planet density as g/cm^3; the earth has 5.51 density.

pl_notes tells how many notes nasa has taken about the planet on their Confirmed Planet Overview page, maybe a scraping target.

st_dist measures the distance to the star in parsecs, each parsec is equal to 3.26 lightyears.

st_optmag measures star optical magnitude on the V Johnson or Kepler band units.  the field st_optband clarifies which is used.

st_teff tells the effective temperature of the star in kelvins as modeled but a black body emitting the same amount of radiation.

st_mass tells the mass of the star in solar masses, so stars close to 1 solar mass are liable to be yellow dwarfs like Sol.

st_rad tells the radius of the star, again in solar units so we want one pretty close to 1.

rowupdate column tells when the data in the entry was most recently updated, that is to say, how old the data is.

pl_imgflag tells if the planet has been observed with imaging techniques, that is to say that we have a picture or not.

pl_ratdor measures the distance between the planet and the star  at mid transit divided by the stellar radius.

pl_disc tells the year the planet was discovered
pl_locale tells where on earth or orbit the discovery of the planet was made
pl_instrument tells the instrument that was used to discover the planet
pl_status tells the review status of the planet with NASA, 1 is announced, 2 is submitted, 3 is accepted, and 0 is retracted.  Our code should screen out retracted records and show the status of those still under consideration.

pl_mnum tells how many moons were detected around the planet

pl_pelink provides a link to the exoplanet encyclopedia page for the planet in question.  Sagan's Encyclopedia Galactica as it were.

The required base URL for NASA exoplanet API requests:
    https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?
    
    for the exoplent table:
        https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets
        
        for the exoplanet table with a query; queries use the syntax &select=parameter1,parameter2,etc:
            '''
            
'''
            PRIMARY QUERY BUILD FOR THE PULL FUNCTION
https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_name,pl_discmethod,pl_orbper,pl_bmass, pl_rad, pl_dens, pl_notes
        '''
#import statements
import requests
import csv 
import json
'import tkinter'

#global variables
'''these variables will be used by different functions to define the value of the data pulled from the NASA API

planet_mass -- pl_bmass
planet_density -- pl_dens
planet_distance_lightyears -- st_dist
star_temperature -- st_teff
star_mass -- st_mass
planet_star_distance (planet to star during transit) -- pl_ratdor
nasa_status -- pl_status
'''

planet_mass=0.0
planet_density=0.0
planet_distance_lightyears=0.0
star_temperature=0
star_mass= 0.0
planet_star_distance= 0.0

#earth_mass = 5.97219*10^24
earth_density = 5.51
#earth_to_sol_distance = 149600000
sol_temperature  = 5778.0
sol_mass = 1.0

#functions
def math_test():
    global sol_mass
    global sol_temperature
    permass = sol_mass*0.15+sol_mass
    perheat = sol_temperature*0.15+sol_temperature
    print("The mass of the sun is",sol_mass,"and the temperature of the sun is ",sol_temperature)
    print("with a 15% increase the stellar mass allowed for is",permass," and the stellar temperature allowed for is",perheat)

def pull_earth_like():
    query='https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_name,pl_orbper,pl_ratdor,pl_dens,pl_status,st_dist,st_teff,st_mass&format=json'
    response = requests.get(query)
    sample = response.json()
    #if the the density is correct and the distance to star is correct and the temperature of the star is correct and the mass of the star is correct then return the planet name, the host star, these data points, the lightyears distance and the nasa review code; for metrics accept results that are within 15% of earth values
    qualifying_planets = []
    earth_value = 0.0
    comparison_value = 0.0
    for items in sample:
        for properties in items:
            if  items =='pl_dens':
                comparison_value=items.get('pl_dens')
                comparison_value=float(comparison_value)
                earth_value = 5.51
                targettop= earth_value*0.15+earth_value
                targetbottom= earth_value-earth_value*0.15
                if comparison_value <targettop and comparison_value >targetbottom:
                    if items == 'st_teff':
                        comparison_value=items.get('st_teff')
                        comparison_value=float(comparison_value)
                        earth_value=5778.0
                        targettop=earth_value+earth_value*0.15
                        targetbottom=earth_value-earth_value*0.15
                        if comparison_value <targettop and comparison_value >targetbottom:
                            if items == 'st_mass':
                                comparison_value=items.get('st_mass')
                                comparison_value=float(comparison_value)
                                earth_value=1.0
                                targettop=earth_value+earth_value*0.15
                                targetbottom=earth_value-earth_value*0.15
                                if comparison_value <targettop and comparison_value >targetbottom:
                                    new_entry=items.get('pl_name')
                                    qualifying_planets.append(new_entry)
    print(qualifying_planets)                            
#this function pre-fills the search variables with values equal to the earth and allos the variation of those values by 15%, then queries the database for records that fit the requirements.

'def pull_current_values:'
    #this function queries the database for pthe current value of the star and planet fiels provided in the interface, if there is no value provided a wildcard is used.
    
'define  reset():'
    #a function to reset the values in the interface
    
def test_pull():
    query='https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_name,pl_orbper,pl_ratdor,pl_dens,pl_status,st_dist,st_teff,st_mass&format=json'
    response = requests.get(query)
    print('status: ',response.status_code)
    print('header: ',response.headers['content-type'])
    print('encoding: ',response.encoding)
    #print('text: /p',response.text)
    #print('json version: /p',response.json())
    data_dictionary= response.json()
    print(type(data_dictionary))
    print(len(data_dictionary))
    print("type of entries in the list is ", type(data_dictionary[0]))
    #print(data_dictionary)
    #data_dictionary = data_dictionary[0]
    #print(type(data_dictionary))
    #print(data_dictionary)
    name_records=[]
    parameter = "pl_name"
    #****
    #this is the code portion for pulling the data for analysis that works
    #****
    for entries in data_dictionary:
        name=entries.get(parameter)
        name_records.append(name)
    '''for entries in data_dictionary:
        record = data_dictionary[entries]
        #print(len(record))
        for key in record:
            #print(key)
            #temp_list=[data_dictionary[name_counter]]
            if parameter == key:
                print(get(record[key]))
                entry = get(record[key])
                name_records.append(entry) 
                #name_counter = '''
    print(name_records)
    #data_dictionary = data_dictionary[0]
    #print(type(data_dictionary))
    #print(data_dictionary["pl_name"])
    #i need a loop to hit a list and pull the names
    #i'll try a for loop and a while loop

#a function for debugging that tests that the API request works and that values are returned.
    
'def open_encyclopedia():'
    #a function that scrapes the explanet encyclopedia using the field returned, with exception handling for planets with no entry.  The information is presented in the interface as a text string.
       
'def display_values():'
    #a function that uses the interface to display the values returned by a pull function in columns that can be scrolled.  
    
'''bonus content functions for if there is extra time'''
    
'def export results():'
    #a function that exports the results of a pull function to a csv that is stored in a local folder.  The export includes a copy of the search parameters that were submitted.
    
'def narrow_search():'
    #a function that uses the results to search them again, using new parameters entered by the user, but using only the current search returns.  This will clear the information pulled from the database and present the narrowed results as the new results set, which can then be narrowed again.  As with the pull, where no value is entered a wildcard is used.  Narrow is a sensible efficiency solution because it allows the user to work with the local data set instead of hitting the database over and over again.
    
'def load_from_CSV():'
    #a function that lets the user load the information from a locally located CSV instead of hittin the NASA database, so that data can be sorted when internet connectity is not available.
 
'''Mainline Logic for testing'''    
#test_pull()
pull_earth_like()
math_test()
    
'''interace design area, remember to include the main loop'''    
       