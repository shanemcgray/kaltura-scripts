'''
This script will be run at the beginning of every other script.
It handles the authentication with the Kaltura environment.
It also allows the user to select which PID/account to work in if the admin manages multiple PIDs.
The admin will sign in with their KMC username and password.
'''

# Import the Kaltura API and a password-entry library
from KalturaClient import *
from KalturaClient.Plugins.Core import *
import pwinput

# Ask the user which PID to work in
partner_id = input('Enter PID:')
config = KalturaConfiguration(partner_id)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
# Ask the user for their KMC username
user_id = input('Enter KMC username:')
# Use pwinput to securely store the user's password in cms_password
cms_password = pwinput.pwinput(prompt='Password: ')
otp = ""
# Use the username and password to get the admin secret
partner = client.partner.getSecrets(partner_id, user_id, cms_password, otp) 
secret = partner.adminSecret
k_type = KalturaSessionType.ADMIN
expiry = 86400
privileges = "disableentitlement"

# This is the function all other scripts will call with startSession.StartSession()
def StartSession():
	result = client.session.start(secret, user_id, k_type, partner_id, expiry, privileges)
	if result:
		print("Kaltura session started. Expiry is " + str(expiry) + " seconds.")
		return result	# Return the Kaltura session to the script that called this function
	else:
		print("Something has gone wrong.\nDid you use the correct PID, username, and password?")