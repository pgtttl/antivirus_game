import pyttsx3
import pygame
import time
import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

# Initialize the Pygame library
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))  # Adjust screen size as needed
pygame.display.set_caption("smile antivirus")

# Load the PNG image of the person
person_image = pygame.image.load('person.png')  # Make sure 'person.png' is in the same folder
person_rect = person_image.get_rect(center=(400, 300))  # Adjust the position as needed

# Initialize the speech engine
engine = pyttsx3.init()

# Set the new text you want to convert to speech
text = "Bro, you're done. But Smile Antivirus can help!"

# Function to play the speech and display the image
def speak_and_show_image(text_to_speak):
    # Start the speech
    engine.say(text_to_speak)
    engine.runAndWait()

# Display the image and text
def display_image(image):
    screen.fill((255, 255, 255))  # Set the background color to white
    screen.blit(image, person_rect)  # Draw the image
    pygame.display.update()

# Function to show a custom error popup
def show_error_popup(message):
    # Create a tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    messagebox.showerror("Error", message)  # Show the error popup
    root.destroy()  # Close the tkinter window

# Function to show a custom message popup
def show_message_popup(message):
    # Create a tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    messagebox.showinfo("Smile Antivirus", message)  # Show the message popup
    root.destroy()  # Close the tkinter window

# Main loop to display the image, play speech, and create files
def main():
    # Display image and say initial speech
    display_image(person_image)
    speak_and_show_image(text)
    
    # Wait a bit for the speech to finish
    time.sleep(3)  # Adjust the sleep time if needed

    # Create the 999 help files on the desktop
    create_help_files()

    # Wait for a moment before showing the second message
    time.sleep(1)

    # Display image and say the second speech
    display_image(person_image)
    second_text = "will not add 999 files."
    speak_and_show_image(second_text)

    # Wait a moment before showing the third message
    time.sleep(1)

    # Display image and say the third speech
    display_image(person_image)
    third_text = "Virus trying to bluescreen PC. I won't let that happen!"
    speak_and_show_image(third_text)

# Run the program
main()

# Show the custom error popup after the script finishes running
show_error_popup("Smile Antivirus crashed.")
# Show the second custom error popup
show_error_popup("Broskie why?")

# Load "person2.png" and display it with the new speech
person2_image = pygame.image.load('person2.png')  # Make sure 'person2.png' is in the same folder

# Show the custom message popup with the "Open me again, I need help" message
show_message_popup("Open me again, I need help")

# Wait for a moment after the popup before continuing
time.sleep(1)

# Before showing person2.png, say "Opening..."
speak_and_show_image("Opening...")

# Wait for a moment before displaying the next image
time.sleep(1)

# Display the new image ("person2.png") and speak "Help"
display_image(person2_image)
speak_and_show_image("Help")  # Speak "Help"

# Show the custom error popup with the "Hehe, get bosoed" message
show_error_popup("Hehe, get bosoed")

# Show the custom error popup with the "now now, yoou dont have a antivirus :) i corruped him."
show_error_popup("now now, you dont have a antivirus :) i corruped him.")

# Speak the corrupted antivirus message
speak_and_show_image("y.  o u , have to. rein.stalll me.hgfsgsgfe")

# Show the message popup for reinstall
show_message_popup("reinstall?")

# Load "person3.png" and display it with the new speech
person3_image = pygame.image.load('person3.png')  # Make sure 'person3.png' is in the same folder

# Display "person3.png" and say "Thank you, but I'm still reinstalling"
display_image(person3_image)
speak_and_show_image("Thank you, but I'm still reinstalling")  # Speak "Thank you, but I'm still reinstalling"

# Wait for 10 seconds before switching back to person1.png
time.sleep(10)

# Switch back to person1.png and say "I'm back"
display_image(person_image)  # Display the first person image
speak_and_show_image("I'm back")  # Speak "I'm back"

# Show custom error popup for "Smile Antivirus is not responding"
time.sleep(2)  # Optional: wait a bit before showing the error
show_error_popup("Smile Antivirus is not responding")

# Load "hehe1.png" and display it with the new speech
hehe1_image = pygame.image.load('hehe1.png')  # Make sure 'hehe1.png' is in the same folder

# Display "hehe1.png" and say "Hehe, I have control now!"
display_image(hehe1_image)
speak_and_show_image("Hehe, I have control now!")  # Speak "Hehe, I have control now!"

display_image(person_image)
speak_and_show_image("oh god! your desktop!")
speak_and_show_image("let me help!")
speak_and_show_image("oh no! i can not delete it! the virus is blocking me!!")

speak_and_show_image("wait... YOU HAVE THE STRAIT FACE VIRUS!!!!!!!!!")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
show_error_popup("run")
display_image(person2_image)
speak_and_show_image("Help")  # Speak "Help"
display_image(person2_image)
speak_and_show_image("Help")  # Speak "Help"
display_image(person2_image)
speak_and_show_image("Help")  # Speak "Help"
speak_and_show_image("detected peer to peer conection")
speak_and_show_image("strait_face.exe is trying to bluescreen")
speak_and_show_image("HELP")
speak_and_show_image("thanks for playing!")

