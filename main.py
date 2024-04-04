#!/usr/bin/python3

import time
import subprocess
import os
import sys
import instaloader

# Check if Colorama has been already installed or not
try:
    from colorama import init, Fore
    print(Fore.LIGHTMAGENTA_EX + "Colorama has been already installed, We have initialized it for you :)")
    time.sleep(5)
except ImportError:
    print(Fore.RED + "Colorama has not been installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore
    print(Fore.LIGHTMAGENTA_EX + "Done, Colorama has been installed.")
    time.sleep(3)

# Clear the terminal screen
    os.system("clear")
    time.sleep(1)

def create_3d_banner():
    # Banner text
    banner_text = "InstaHashFinder"

    try:
        # Use figlet to create ASCII art with mono9 font
        figlet_process = subprocess.Popen(
            ["figlet", "-w", "27", "-f", "mono9", "-c", banner_text],
            stdout=subprocess.PIPE
        )
        figlet_output, _ = figlet_process.communicate()

        # Use lolcat to add color to the ASCII art
        lolcat_process = subprocess.Popen(["lolcat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        banner_output, _ = lolcat_process.communicate(input=figlet_output)

        # Print the result
        print(banner_output.decode())

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "Error: Make sure 'figlet' and 'lolcat' are installed on your system. (Hint: Run ./setup.sh)")
        time.sleep(2)

def search_hashtag(hashtag):
    L = instaloader.Instaloader()

    # Login if you need to access private profiles
    # L.interactive_login("your_username")

    posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()

    for post in posts:
        print(post.url)

def main():
    hashtag = input(Fore.LIGHTMAGENTA_EX + "Enter the hashtag to search: ")
    search_hashtag(hashtag)

if __name__ == "__main__":
    main()