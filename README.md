# CLI Text To Speech (REALISM UPDATE)

More voices have been added, with improved speech and hyper realism.


# Setting Up
To begin using the CLI Text To Speech, open your terminal and navigate to the directory of the "Text-To-Speech" folder or if you renamed it just go to the directory where it's located.

Linux: cd /home/(YOUR_USER)/Downloads/Text-To-Speech/Audio

Windows: cd /d C:\Users\(YOUR_USER)\Downloads\Text-To-Speech\Audio

MacOS: cd ~/Downloads/Text-To-Speech/Audio


# System & Environment Requirements

Python 3.8+: Required for asyncio and modern package support.

Active Internet Connection: edge-tts streams speech online from Microsoft Azure's neural engine.

xdg-utils (Linux): Provides xdg-open to automatically play output audio files with your default media player.

Python Packages:

edge-tts (only external dependency)

Built-in standard library packages: argparse, asyncio, os, subprocess, sys


# IMPORTANT DEPENDENCIES!!

## 1. Create and activate virtual environment

python3 -m venv .venv

source .venv/bin/activate

## 2. Upgrade pip and install edge-tts

pip install --upgrade pip

pip install edge-tts

## 3. Install xdg-utils (Linux only, if not already installed)

sudo dnf install xdg-utils (Fedora)

sudo apt install xdg-utils (Ubuntu/Debian)


# Commands
"-h" or "--help" (Gives you useful info on how each command works.)

"-t" or "--text" (Stores the string to convert into audio)

"-f" or "--file" (Path to a text file of your choosing)

"-i" or "--interactive" (Launches a live typing mode in the terminal)

"-v" or "--voice" (Specifies which voice you would like to use default is gb-male)

"-r" or "--rate" (How fast or slow the voice is, default is +0%)

"-o" or "--output" (Outputs the file, example Banger.mp3)

# Voices

 ## -- Realistic voices --
 ava 
    
 andrew
    
 brian
 
 emma

 ## --- US Accents ---
 
 us-aria
 
 us-guy
 
 us-jenny
 
 us-chris
 
 us-steffan

 ## --- UK Accents ---
 
 uk-ryan
 
 uk-sonia
 
 uk-thomas
 
 uk-maisie

 ## --- Australian Accents ---
 
 au-natasha
 
 au-william

 ## --- Canadian Accents ---
 
 ca-clara
 
 ca-liam

 ## --- Irish & South African ---
 
 ie-emily
 
 ie-connor
 
 za-leah

 ## --- Indian English ---
 
 in-neerja
 
 in-prabhat


# Usage
To make your very own text to speech file simply type:

python Text-To-Speech.py -t "Type whatever you want in here" -o Name-This-Whatever-You-Want.mp3

## If you want to change the voice add the -v or --voice command:

python Text-To-Speech.py -t "Type whatever you want in here" -v brian -o Name-This-Whatever-You-Want.mp3

## If you want to increase or decrease the speed of the voice add the -r or --rate command:

python Text-To-Speech.py -t "Type whatever you want in here" -v ava -r +20 -o Name-This-Whatever-You-Want.mp3

# Interactive Mode
To use the interactive mode simply type:

python Text-To-Speech.py -i

In order to exit type exit or quit.

## Change the interactive mode voice by adding the -v or --voice command.

python Text-To-Speech.py -i -v uk-guy

## Increase or Decrease the interactive mode voice speed by adding the -r or --rate command

python Text-To-Speech.py -i -v ca-liam -r -10%

# File Reading Mode
To convert the text from a text file into audio first put the text file you would like to be read out in the Audio folder. and proceed to type the following in your terminal:

python Text-To-Speech.py -f TXT.txt

## To change the file reading voice.

python Text-To-Speech.py -f TXT.txt -v za-leah

## To change the rate.

python Text-To-Speech.py -f TXT.txt -v ie-connor -r +30%








