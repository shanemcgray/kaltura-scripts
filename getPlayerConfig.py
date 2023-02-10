'''
This script will download the configurations of Kaltura players
and save them into txt files. These can be applied to newly-created players,
allowing the admin to copy/paste player configs across PIDs.

How to use:
This script uses a companion file "getPlayerConfig_playerList.txt"
The txt file shall contain one player ID per line.
Each of these player ID's configs will be downloaded.
'''

#----------------------------------------------------

# Import the startSession script for authentication
import startSession
# Import the Kaltura API
from KalturaClient import *
from KalturaClient.Plugins.Core import *
# Start the Kaltura session
startSession.client.setKs(startSession.StartSession())
#----------------------------------------------------

# Open the companion txt file and place each player ID into a list playersToGrab
listFile = open("getPlayerConfig-playerList.txt", 'r')
playersToGrab = listFile.read().split("\n")

# For every player ID in our playerList:
print ("Players found within list:")
for play in playersToGrab:
	# Display the player IDs to the user
	print (play)
	# Get the player using the ID
	result = startSession.client.uiConf.get(play)

	# Create the text file
	# It will be named using the format "playerId - playerName.txt"
	filename = str(play) + " - " + (result.name.replace("/", " ") + ".txt")
	outFile = open(filename, 'w')

	# Write the player's config into the file and close. Move to the next ID in our list.
	outFile.write(str(result.config)) 
	outFile.close()