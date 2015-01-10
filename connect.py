# Imports
from twitter import *
import serial
import time
import auth
import json

# Twitter Auth (Gets auth_values variable from a file named auth.py with these four variables)
api = Twitter(
    auth=OAuth(auth.access_token_key, auth.access_token_secret, auth.consumer_key, auth.consumer_secret)
    )

# Set and check serial port
ser = serial.Serial(port='/dev/tty.usbmodem1421', baudrate=9600)

def checkokay():
    ser.flushInput()
    time.sleep(3)
    line = ser.readline()
    time.sleep(3)

    if line == '':
        line = ser.readline()
    print 'here'

# Welcome Message
print "It's a go!"

# Gets Tweets!
def getTweets():
    tweets = []
    x = 0

    tweets = api.statuses.user_timeline(screen_name=auth.screen_name) # Get users Tweets
    checkTweets = [s.get('text') for s in tweets] # Puts the Tweets in an array
    tweet = checkTweets[0].split() # Split first tweet into two words

    # Check and match Tweets
    if tweet[0] == '#twt':
        print 'Tweet recieved, turning LED on.'
        ser.write('1')
    elif tweet[0] == '#twtoff':
        print 'Tweet recieved, turning LED off.'
        ser.write('0')
    else:
        print 'Awaiting Tweet'
        ser.write('0')

while 1:
    getTweets() # Call the getTweets function
    time.sleep(15) # Call only every 15 seconds to prevent rate limiting. (Twitter API GET requests: 15 calls every 15 minutes, and 180 calls every 15 minutes.)
