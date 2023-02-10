'''
This script will take downloaded configs from getPlayerConfig.py
and apply them to other players.

Example use case:
The admin manages multiple PIDS. They want to copy a number of players from one PID to another.

How to use:
This should be used after downloading configs using getPlayerConfig.py
This script uses a companion file called "applyPlayerConfig-playerList.txt"
The txt file should contain player IDs of the players we want to copy INTO.
One player ID per line.
The config files to be copied from must be in the same directory as this script,
named with the convention playerIdString-config.txt (Example: "123456-config.txt")
'''

#----------------------------------------------------
# Import the startSession script which handles authentication and PID selection
import startSession
# Import the Kaltura API
from KalturaClient import *
from KalturaClient.Plugins.Core import *

# Start the Kaltura session
startSession.client.setKs(startSession.StartSession())
#----------------------------------------------------

# Get list of players to apply to from a file called applyPlayerConfig-playerList.txt
# Place each ID into a list playersToConfig
listFile = open("applyPlayerConfig-playerList.txt", 'r')
playersToConfig = listFile.read().split("\n")

# Display the IDs to the user
print("Players found within list:")
for play in playersToConfig:
	print(play)

# Ask the user to verify all files are in place and named correctly.
print("Make sure that you have one config file for each player in the list. Each one should be named [playerIdString]-config.txt (Example: 123456-config.txt).")
input("Press the enter key to continue or CTRL-C to quit.")

for play in playersToConfig:
	# Get txt file that is named with player ID. If we don't have a config file in place we'll get an error.
	playerIdString = str(play)
	configFileName = playerIdString + "-config.txt"
	configFile = open(configFileName, 'r')

	if configFile:
		# Read the config file and update selected player with its contents
		ui_conf = KalturaUiConf()
		ui_conf.config = file.read(configFile)
		startSession.client.uiConf.update(playerIdString, ui_conf)
	else:
		print "Could not find config file. Make sure file is named according to getPlayerConfig.py"

