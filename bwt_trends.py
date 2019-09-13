###################################
# ------------ MAIN ---------------
###################################
import requests
r = requests.get('https://apps.cbp.gov/bwt/mobile.asp?action=n&pn=2503')
# print(r.text[0:500])
# print("\n")
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class':'pass_details'})

first_result = results[0]
second_result = results[1]

# EastStandardLaneRecords = []
# EastReadyLaneRecords = []
# EastSentriLaneRecords = []

# WestStandardLaneRecords = []
# #WestSentriLaneRecords = n/a
# WestSentriLaneRecords = []

############## NOTES #################
# find_all(): searches for all matching tags, and returns a ResultSet object
# find(): searches for the first matching tag, and returns a Tag object:
    # to extract information from a Tag object use these two attributes:
        # text: extracts the text of a Tag, and returns a string
            # i.e. first_result.find('b').text
        # contents: extracts the children of a Tag, and returns a list of Tags and strings
            # i.e. first_result.contents
#######################################

# print("length of results:" , len(results))
# print("\n results:\n")
# print(results)
# print("\n first result\n")
# # print(results[0])
# print("\n second result\n")
# print(results[1])



# print("\n first result\n")
# print(first_result)
# print("\nword in first result with tag<b>:")
# print(first_result.find('b').text)


print("\nfirst result contents:")
print(first_result.contents)
# print("\nfirst result contents 10-14:")
# print(first_result.contents[10:14])

print("\nsecond result contents:")
print(second_result.contents)
# print("\nsecond result contents 10-13:")
# print(second_result.contents[10:13])

# def printBorderWaitTime(result):



#########################################################################################
################################# EAST PORT OF ENTRY ####################################
#########################################################################################

print("\nEast Port of Entry Wait Times")
# first result = east port
# second result = west port

################ STANDARD LANE ####################

eastMaxLanes = first_result.contents[3]
print("\nMax Lanes:",eastMaxLanes)

print("\nStandard Lane:")
#second square bracket determines the range of the string that will be returned
standardLaneTime = first_result.contents[6][0:-2]
print("time:" , standardLaneTime)

standardWaitTime = first_result.contents[7].text
print("wait time:" , standardWaitTime)

standardLanesOpen = first_result.contents[8][2:]
print("lanes open:" , standardLanesOpen)


################ READY LANE ####################

print("\nReadyLane:")
#second square bracket determines the range of the string that will be returned
readyLaneTime = first_result.contents[11][0:-2]
print("time:" , readyLaneTime)

readyWaitTime = first_result.contents[12].text
print("wait time:" , readyWaitTime)

readyLanesOpen = first_result.contents[13][2:]
print("lanes open:" , readyLanesOpen)

################ SENTRI LANE ####################

print("\nSentri Lane:")
#second square bracket determines the range of the string that will be returned
sentriLaneTime = first_result.contents[16][0:-2]
print("time:" , sentriLaneTime)

sentriWaitTime = first_result.contents[17].text
print("wait time:" , sentriWaitTime)

sentriLanesOpen = first_result.contents[18][2:]
print("lanes open:" , sentriLanesOpen)

########################################################################################
############################### WEST PORT OF ENTRY #####################################
########################################################################################

print("\n\nWest Port of Entry Wait Times")

westMaxLanes = second_result.contents[3]
print("\nMax Lanes:",westMaxLanes)

################ STANDARD LANE ####################

print("\nStandard Lane:")
#second square bracket determines the range of the string that will be returned
westStandardLaneTime = second_result.contents[6][0:-2]
print("time:" , westStandardLaneTime)

westStandardWaitTime = second_result.contents[7].text
print("wait time:" , westStandardWaitTime)

westStandardLanesOpen = second_result.contents[8][2:]
print("lanes open:" , westStandardLanesOpen)


################ READY LANE ####################

print("\nReadyLane:")
print("N/A on West Port of Entry")

################ SENTRI LANE ####################

print("\nSentri Lane:")
#second square bracket determines the range of the string that will be returned
westSentriLaneTime = second_result.contents[14][0:-2]
print("time:" , westSentriLaneTime)

westSentriWaitTime = second_result.contents[15].text
print("wait time:" , westSentriWaitTime)

westSentriLanesOpen = second_result.contents[16][2:]
print("lanes open:" , westSentriLanesOpen)


################ BUILDING THE DATASET #############
# East Standard Lane Records

