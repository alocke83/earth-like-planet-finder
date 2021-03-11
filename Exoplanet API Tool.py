#Adam Locke 2021
#NASA Exoplanet API tool
#This script calls to nasa and uses the exoplanet API to obtain information about exoplanets  based upon user selected parameters.
#Please feel free to use this script, so long as you mention who wrote it :)


'''IMPORTANT NOTES
The NASA exoplanet archive uses SQL so the api requests have to include valid SQL statements.  The database returns CSV as the default file format.

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
https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_letter,pl_name,pl_discmethod,pl_orbper,pl_bmass, pl_rad, pl_dens, pl_notes, 
        '''
#import statements
import requests
import csv 
import tkinter

#global variables


#functions
define pull_earth_values():
#this function pre-fills the search variables with values equal to the earth and allos the variation of those values by 15%, then queries the database for records that fit the requirements.

define pull_current_values:
    #this function queries the database for the current value of the star and planet fiels provided in the interface, if there is no value provided a wildcard is used.
    
define  reset():
    #a function to reset the values in the interface
    
define test_pull():
    #a function for debugging that tests that the API request works and that values are returned.
    
define open_encyclopedia():
    #a function that scrapes the explanet encyclopedia using the field returned, with exception handling for planets with no entry.  The information is presented in the interface as a text string.
       
define display_values():
    #a function that uses the interface to display the values returned by a pull function in columns that can be scrolled.  
    
'''bonus content functions for if there is extra time'''
    
define export results():
    #a function that exports the results of a pull function to a csv that is stored in a local folder.  The export includes a copy of the search parameters that were submitted.
    
define narrow_search():
    #a function that uses the results to search them again, using new parameters entered by the user, but using only the current search returns.  This will clear the information pulled from the database and present the narrowed results as the new results set, which can then be narrowed again.  As with the pull, where no value is entered a wildcard is used.  Narrow is a sensible efficiency solution because it allows the user to work with the local data set instead of hitting the database over and over again.
    
define load_from_CSV():
    #a function that lets the user load the information from a locally located CSV instead of hittin the NASA database, so that data can be sorted when internet connectity is not available.
 
'''Mainline Logic for testing'''    
    
    
'''interace design area, remember to include the main loop'''    
       