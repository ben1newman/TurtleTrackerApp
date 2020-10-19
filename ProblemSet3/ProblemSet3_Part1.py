#-------------------------------------------------------------
# Problem set 3 - PART I
# Author: Ben Newman (ben.newman@duke.edu)
# NetID:  bfn3
# Date:   Fall 2020
#--------------------------------------------------------------

#/*-PS3: Task 1

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (mountain + ", formerly\nknown as \"" + nickname+"\"")
print ("is " + str(elevation) +  '\' above sea level.' )

#%% Task 2

dataFolder = "W:\\859_data\\tri_state"

dataList = ['roads.shp','road_types.dbf','naip_imagery.tif']

userItem = "streams.shp"

#Append userItem to the end of dataList
dataList.append(userItem)

#Use the FOR loop to iterate over each object in dataList
for state in dataList:
    print(dataFolder+'\\'+state)
    
#%% Task3

#Create an empty list
userNumbers = []

#Iterate 3 times using FOR loop and append real integer value to the empty list
for random in range(3):
    
    my_integer = input("Enter an integer")
    
    #Convert my_integer to a real_integer
    real_integer = int(my_integer)
    
     #Append to list
    userNumbers.append(real_integer)
    
#sort the list by ascending order
userNumbers.sort()

#Print the highest value 
print(userNumbers[-1])


#%% Task 3 (Challenge Question)

#Create an empty list
userNumbers = []

#Iterate 3 times using FOR loop and append real integer value to the empty list
for random in range(3):
    my_integer = input("Enter an integer")
    
    #Convert my_integer to a real_integer
    real_integer = int(my_integer)
    
    #Append to list
    userNumbers.append(real_integer)
    
#Sort the list by descending order
userNumbers.sort(reverse = True)

#Print numbers in descending order
print(userNumbers)
