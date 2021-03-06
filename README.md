# Arduino Twitter

This is a script that uses the Twitter API to look for tweets from a user with a specific hashtag.
Right now I'm using it to turn an LED on or off, but that's just an example. Get a [Power Switch Tail](http://www.powerswitchtail.com/) to interface with AC voltage and make this more useful.

## Setup:

1. Clone this repository.
2. Create a [Twitter application](http://apps.twitter.com) and enter the following information into a file named `auth.py` in the manner below:

```
consumer_key='YOUR_CONSUMER_KEY'
consumer_secret='YOUR_CONSUMER_SECRET'
access_token_key='YOUR_ACCESS_TOKEN'
access_token_secret='YOUR_ACCESS_TOKEN_SECRET'
screen_name='YOUR_TWITTER_HANDLE'
```
3. Install the [Python Twitter API](https://github.com/sixohsix/twitter)
4. Configure your port on line 14 of `connect.py` if necessary.

## Usage:

1. Connect your Arduino and upload the `twitter.ino` file onto your board.
2. Run `python connect.py` in the terminal.
3. Tweet starting with the hashtag `#twt` from the account specified in `auth.py`. The LED should turn on.
5. Tweet starting with the hashtag `#twtoff` from the account specified in `auth.py`. The LED should turn off.
