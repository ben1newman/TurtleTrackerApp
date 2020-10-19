#-------------------------------------------------------------
# Problem set 3 - PART II
# Author: Ben Newman (ben.newman@duke.edu)
# NetID:  bfn3
# Date:   Fall 2020
#--------------------------------------------------------------

#%% Task 4.1 

#Create a Python file object to link the file's contents
fileObj = open(file='transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects and close the file
fileObj.close() 

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLineString
print(headerLineString)

#%% Task 4.2

#Split the headerLineString by comma into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsa, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the value of each index variable
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3

#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for line in lineList:
    if line[0] in ("m"):
        continue
    
    #Split the data into values
    realData = line.split(",")
    
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = realData[mmsi_idx]
    
    #Extract the fleet value
    fleet = realData[fleet_idx]
    
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet

#Print the values
print(len(vesselDict))

#%% Task 4.4

vesselID = "258799000"
value = vesselDict[vesselID] 
print (f"Vessel # {vesselID} flies the flag of {value}")
        

#%% Task 5

#Create a Python file object to link the file's contents
fileObj = open(file='loitering_events_20180723.csv',mode='r')

#Construct a list of all lines
lineList = fileObj.readlines()

#Loop through each data line in lineList
for line in lineList:
    if line[0] in ("t"):
        continue
    
    #Split the data into items
    realData = line.split(",")
    
    #Store the transshipment_mmsi, starting and ending latitude, and starting longitude values into their own respective variables
    transhipment_mmsi = realData[0]
    start_lat = float(realData[1])
    start_lon = float(realData[2])
    end_lat = float(realData[3])
    end_lon = float(realData[4])
    
    #To check if a vessel is passing from the southern to northern hemisphere, see if the starting latitude is a negative value and ending latitude is a positive value
    #In the IF statement, latitude and longitude vlaues were converted to float to compare with numeric values
    #To meet the longitude condition, start_lon must be more than 165 and less than 170
    if start_lat < 0 and end_lat > 0 and start_lon > 165 and start_lon < 170:  
        print (f"Vessel # {transhipment_mmsi} flies the flag of {vesselDict[transhipment_mmsi]}")
    
    #Print vessels that did not meet criteria
    else: 
        print("No vessels met criteria")