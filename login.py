"""
Beginner Python Project using input, print, and conditionals by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""
# Time module offers time values, timestamps, delays, 
# and performance measurements. 
import time

# Define username and password variables
username = 'kylie'
password = 'secretpassword'

# Two user inputs for Username and Password
username_input = input('Username: ')
password_input = input('Password: ')

# if user input (Username) is exact to defined username variable and
# if user input (Userpassword) is exact to defined password variable
# proced with if statement.
if username_input == username and password_input == password:
    print('Access granted')         # Print shown statements with pauses inbetween
    print('Please wait')
    time.sleep(5)                   # Pause program execution for 5 seconds
    print('Ok... Loading...')
    time.sleep(1)                   # Pause program execution for 1 second
    print('...')
    time.sleep(1)                   # Pause program execution for 1 second
    print('...')                    # Gain access to "secret mainframe"
    print('Alright you have security clearance. Pulling up the secret mainframe.')
# else if statement for incorrect password input prints Password incorrect.
elif username_input == username and password_input != password:
    print('Password incorrect')
# else if statement for incorrect username input prints Username incorrect.
elif username_input != username and password_input == password:
    print('Username incorrect')
# else (lastly) let user know username and password are incorrect.
else:
    print('You might wanna check both fields...')