"""
Beginner Python Project using input, print, and conditionals by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 

How to run:
    python login.py

Credentials are read from environment variables (no plaintext secrets in code):
    export LOGIN_USERNAME=kylie
    export LOGIN_PASSWORD=secretpassword

If either variable is not set, the script will print instructions and exit.
"""
import getpass
import os
import sys
# Time module offers time values, timestamps, delays, 
# and performance measurements. 
import time

# login function for more modularity.
# expected_username and expected_password receive the credentials at call time.
# username_input_fn and password_input_fn can be replaced in unit tests
# to avoid interactive prompts.
def login(expected_username, expected_password,
          username_input_fn=input, password_input_fn=getpass.getpass):
    # Two user inputs for Username and Password
    username_input = username_input_fn('Username: ')
    password_input = password_input_fn('Password: ')
    # if user input (Username) is exact to defined username variable and
    # if user input (Password) is exact to defined password variable
    # proceed with if statement.
    if username_input == expected_username and password_input == expected_password:
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
    elif username_input == expected_username and password_input != expected_password:
        print('Password incorrect')
    # else if statement for incorrect username input prints Username incorrect.
    elif username_input != expected_username and password_input == expected_password:
        print('Username incorrect')
    # else (lastly) let user know username and password are incorrect.
    else:
        print('You might wanna check both fields...')

def main(username, password):
    # Introduction to secret mainframe to identify username and
    # password.
    print("==============================================") 
    print(" WELCOME TO THE ASTRAL MAINFRAME v3.7") 
    print("==============================================") 
    time.sleep(1) 
    print("\nBefore you lies a terminal rumored to guard the") 
    print("ancient secrets of the digital realm. Only those") 
    print("who can decipher the clues may enter.") 
    time.sleep(2) 
    print("\nA whisper echoes from the machine:") 
    print('"The key is hidden in plain sight… if you can') 
    print(' read between the lines, you already know."') 
    time.sleep(3) 
    print("\nA faint note appears on the screen:") 
    print(" - The guardian favors a name that starts with 'k' and ends with 'ylie'.") 
    print(" - The password? Well… some say it's the most *secret* thing of all.") 
    time.sleep(3) 
    print("\nType the credentials to prove your worth.\n")
    login(username, password)

# Execute program
if __name__ == "__main__":
    # Load credentials from environment variables (no plaintext secrets in source).
    # Verify they are set before starting the interactive session.
    _username = os.environ.get('LOGIN_USERNAME')
    _password = os.environ.get('LOGIN_PASSWORD')
    if not _username or not _password:
        print("Error: credentials not configured.")
        print("Please set the LOGIN_USERNAME and LOGIN_PASSWORD environment variables:")
        print("  export LOGIN_USERNAME=<your_username>")
        print("  export LOGIN_PASSWORD=<your_password>")
        sys.exit(1)
    main(_username, _password)