#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (mountain + ", formerly\nknown as \"" + nickname+"\"")
print ("is " + str(elevation) +  '\' above sea level.' )

#%% Task 2

dataFolder = "W:\\859_data\\tri_state"

dataList = ['roads.shp','road_types.dbf','naip_imagery.tif']

userItem = "streams.shp"

dataList.append(userItem)

for state in dataList:
    print(dataFolder+'\\'+state)
    
#%% Task3

userNumbers = []

for random in range(3):
    my_integer = input("Enter an integer")
    real_integer = int(my_integer)
    userNumbers.append(real_integer)
userNumbers.sort()
print(userNumbers[-1])

#Task 3- Challenge

userNumbers = []

for random in range(3):
    my_integer = input("Enter an integer")
    real_integer = int(my_integer)
    userNumbers.append(real_integer)
userNumbers.sort(reverse = True)
print(userNumbers)
