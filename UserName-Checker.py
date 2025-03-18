# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 03/18/2025
# Script Purpose : To check the availability of usernames across various platforms.
# Description    : This script checks whether a given username exists on supported 
#                  platforms by making HTTP requests to platform-specific URLs.
# Features       : 
#                  1. Displays a clear and user-friendly banner.
#                  2. Supports multiple platforms including YouTube, Instagram, and GitHub.
#                  3. Implements special handling for Reddit API requests.
# Requirements   : 
#                  1. Python 3.x
#                  2. Requests library
#                  3. Colorama library for colored console output.
# ===================================================================================

import os
import requests
from colorama import Fore, init

init()
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
w = Fore.RESET
r = Fore.RED

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    if os.name == 'nt':  
        os.system('title Username Checker')
    print(f'''
{c}==========================================
Username Checker 
Check if usernames exist on various sites
=========================================={w}
''')

def check_username(platform, url, special_handling=False):
    print(f'{c}[{platform}]{w} Checking...')
    try:
        if special_handling and platform == "Reddit":
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200 and response.json() is False:
                print(f'  {c}{un}{g} - exists on https://reddit.com/u/{un}')
            else:
                print(f'  {c}{un}{r} - does not exist on Reddit!')
        else:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'  {c}{un}{g} - exists on {url}')
            else:
                print(f'  {c}{un}{r} - does not exist on {platform}!')
    except requests.exceptions.RequestException:
        print(f'  {c}{un}{r} - Error checking {platform}!')

def main():
    while True:
        clear_screen()
        banner()
        
        print(f'{w}-{c}-' * 26)
        print(f'{w}Supported platforms:')
        print(f'{w} ')
        print(f'{c}YouTube, Instagram, GitHub, SoundCloud, Linktree,')
        print(f'Pastebin, Reddit, Snapchat, Medium, Quora')
        print(f'{w}-{c}-' * 26)
        
        global un
        print(f'{w} ')
        un = input(f'{w}Enter the username you want to search:{c} ').strip()
        clear_screen()
        print(f'{c}Searching for username: {g}{un}{w}\n')
        
        platforms = {
            "YouTube": f'https://youtube.com/@{un}',
            "Instagram": f'https://www.instagram.com/{un}',
            "GitHub": f'https://github.com/{un}',
            "SoundCloud": f'https://soundcloud.com/{un}',
            "Linktree": f'https://linktr.ee/{un}',
            "Pastebin": f'https://pastebin.com/u/{un}',
            "Reddit": f'https://www.reddit.com/api/username_available.json?user={un}',
            "Snapchat": f'https://www.snapchat.com/add/{un}',
            "Medium": f'https://medium.com/@{un}',
            "Quora": f'https://www.quora.com/profile/{un}'
        }
        
        for platform, url in platforms.items():
            if platform == "Reddit": 
                check_username(platform, url, special_handling=True)
            else:
                check_username(platform, url)
        
        end()

def end():
    print(f'\n{c}------------------------------------------{w}')
    while True:
        restart = input(f'{w}Do you want to check another username? ({c}y{w}/{c}n): ').strip().lower()
        if restart == 'y':
            clear_screen()
            break
        elif restart == 'n':
            print(f'\n{g}Thank you for using the Username Checker!{w}')
            print(f'{g}Goodbye and have a great day!{w}')
            exit()
        else:
            print(f'{r}Invalid input. Please enter "y" to restart or "n" to exit.{w}')

if __name__ == '__main__':
    main()
