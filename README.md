# CLI Text To Speech <REALISM UPDATE>

More voices have been added, with improved speech and hyper realism.


# Setting Up
To begin using the CLI Text To Speech, open your terminal and navigate to the directory of the "Text-To-Speech" folder or if you renamed it just go to the directory where it's located.

Linux: cd /home/(YOUR_USER)/Downloads/Text-To-Speech/Audio

Windows: cd /d C:\Users\(YOUR_USER)\Downloads\Text-To-Speech\Audio

MacOS: cd ~/Downloads/Text-To-Speech/Audio

Ensure you have a valid internet connection, it is needed for the audio files to be output.



# Commands
"-h" or "--help" (Gives you useful info on how each command works.)

"-t" or "--text" (Stores the string to convert into audio)

"-f" or "--file" (Path to a text file of your choosing)

"-i" or "--interactive" (Launches a live typing mode in the terminal)

"-v" or "--voice" (Specifies which voice you would like to use default is gb-male)

"-r" or "--rate" (How fast or slow the voice is, default is +0%)

"-o" or "--output" (Outputs the file, example Banger.mp3)

# Voices

gb-male(Britsh guy voice)

gb-female(British woman voice)

us-male(American dude)

us-female(American Woman)

au-male(Australian Guy)

All voices are taken from the Google Text To Speech Library.


# Usage
To make your very own text to speech file simply type:

python Text-To-Speech.py -t "Type whatever you want in here" -o Name-This-Whatever-You-Want.mp3

## If you want to change the voice add the -v or --voice command:

python Text-To-Speech.py -t "Type whatever you want in here" -v us-male -o Name-This-Whatever-You-Want.mp3

## If you want to increase or decrease the speed of the voice add the -r or --rate command:

python Text-To-Speech.py -t "Type whatever you want in here" -v us-male -r +20 -o Name-This-Whatever-You-Want.mp3

# Interactive Mode
To use the interactive mode simply type:

python Text-To-Speech.py -i

In order to exit type exit or quit.

## Change the interactive mode voice by adding the -v or --voice command.

python Text-To-Speech.py -i -v us-female

## Increase or Decrease the interactive mode voice speed by adding the -r or --rate command

python Text-To-Speech.py -i -v au-male -r -10%

# File Reading Mode
To convert the text from a text file into audio first put the text file you would like to be read out in the Audio folder. and proceed to type the following in your terminal:

python Text-To-Speech.py -f TXT.txt

## To change the file reading voice.

python Text-To-Speech.py -f TXT.txt -v gb-male

## To change the rate.

python Text-To-Speech.py -f TXT.txt -v gb-male -r +30%

# IMPORTANT DEPENDENCIES!!
These are the dependencies required for this program to even run at all, DO NOT FORGET.

## PIP PACKAGES
GTTS (Google Text To Speech Libraries)

Edge-TTS 

Pyttsx3

## Linux System Dependencies

xdg-utils

espeak







