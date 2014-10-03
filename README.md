#Shodan_Data

###Shodan JSON Parser

This is parser that was built to pull some of the information from the JSON files that Shodan will export as.
The python script will write the information out as a common seperated value, but that is easy enough to change if needed. 

Feel free to add other options or point out better ways to code sections as i'm not a python expert. 

###This script requires simplejson
sudo easy_install simplejson

### Execution
>python shodan_data.py <flags> <file> 
