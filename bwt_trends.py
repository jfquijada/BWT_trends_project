###################################
# ------------ MAIN ---------------
###################################


######################################################################
# XML APPROACH #
import requests

# get rss feed into object
URL = "https://bwt.cbp.gov/api/bwtRss/rssbyportnum/HTML/POV/250301"
page = requests.get(URL)

# write page into xml file
with open('bwt_trends.xml', 'wb') as f:
    f.write(page.content)




######################################################################
# HTML PARSER APPROACH #

# import requests
# URL = "https://bwt.cbp.gov/api/bwtRss/rssbyportnum/HTML/POV/250301"
# page = requests.get(URL)

# # print(page.text)
# print('\n')
# # print(page.text[444:459])
# # print("\n")
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)
# results = soup.find_all('item', attrs={'description':'br/'})
# print(results)
# results = soup.find(_ngcontent-c2="", class())

# <div _ngcontent-c2="" class="col-sm-12 col-md-12 col-lg-12">
#     <span _ngcontent-c2="" class="text-primary" style="display:inline-block;margin-right:10px;margin-left:-3px; font-size:22px;"> 
#         Current Wait: <!---->
#     <span _ngcontent-c2="" style="padding:0 3px; background-color: rgb(246, 229, 229);border-right:5px solid #cc0033;color:black">
#         90 min</span>
#     <!---->
#         <!----></span>
# <!---->
#     <span _ngcontent-c2="" class="text-default nw m10">
#         At 2:00 pm PST,  3 lanes open </span>
#         <!---->
# </div>



# first_result = results[0]
# second_result = results[1]

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


# print("\nfirst result contents:")
# print(first_result.contents)
# print("\nfirst result contents 10-14:")
# print(first_result.contents[10:14])

# print("\nsecond result contents:")
# print(second_result.contents)
# print("\nsecond result contents 10-13:")
# print(second_result.contents[10:13])

# def printBorderWaitTime(result):



#########################################################################################
################################# EAST PORT OF ENTRY ####################################
#########################################################################################

# print("\nEast Port of Entry Wait Times")
# first result = east port
# second result = west port

################ STANDARD LANE ####################

# eastMaxLanes = first_result.contents[3]
# print("\nMax Lanes:",eastMaxLanes)

# print("\nStandard Lane:")
#second square bracket determines the range of the string that will be returned
# standardLaneTime = first_result.contents[6][0:-2]
# print("time:" , standardLaneTime)

# standardWaitTime = first_result.contents[7].text
# print("wait time:" , standardWaitTime)

# standardLanesOpen = first_result.contents[8][2:]
# print("lanes open:" , standardLanesOpen)


################ READY LANE ####################

# print("\nReadyLane:")
#second square bracket determines the range of the string that will be returned
# readyLaneTime = first_result.contents[11][0:-2]
# print("time:" , readyLaneTime)

# readyWaitTime = first_result.contents[12].text
# print("wait time:" , readyWaitTime)

# readyLanesOpen = first_result.contents[13][2:]
# print("lanes open:" , readyLanesOpen)

################ SENTRI LANE ####################

# print("\nSentri Lane:")
#second square bracket determines the range of the string that will be returned
# sentriLaneTime = first_result.contents[16][0:-2]
# print("time:" , sentriLaneTime)

# sentriWaitTime = first_result.contents[17].text
# print("wait time:" , sentriWaitTime)

# sentriLanesOpen = first_result.contents[18][2:]
# print("lanes open:" , sentriLanesOpen)

########################################################################################
############################### WEST PORT OF ENTRY #####################################
########################################################################################

# print("\n\nWest Port of Entry Wait Times")

# westMaxLanes = second_result.contents[3]
# print("\nMax Lanes:",westMaxLanes)

################ STANDARD LANE ####################

# print("\nStandard Lane:")
#second square bracket determines the range of the string that will be returned
# westStandardLaneTime = second_result.contents[6][0:-2]
# print("time:" , westStandardLaneTime)

# westStandardWaitTime = second_result.contents[7].text
# print("wait time:" , westStandardWaitTime)

# westStandardLanesOpen = second_result.contents[8][2:]
# print("lanes open:" , westStandardLanesOpen)


################ READY LANE ####################

# print("\nReadyLane:")
# print("N/A on West Port of Entry")

################ SENTRI LANE ####################

# print("\nSentri Lane:")
#second square bracket determines the range of the string that will be returned
# westSentriLaneTime = second_result.contents[14][0:-2]
# print("time:" , westSentriLaneTime)

# westSentriWaitTime = second_result.contents[15].text
# print("wait time:" , westSentriWaitTime)

# westSentriLanesOpen = second_result.contents[16][2:]
# print("lanes open:" , westSentriLanesOpen)


################ BUILDING THE DATASET #############
# East Standard Lane Records

