#! /usr/bin/python3

import random
import time
import pygame

# Initialize pygame
pygame.mixer.init()
pygame.init()
"""
def add_buffer():
    # Load the sound file
    sound_file = "relaxing_music.wav"
    sound = pygame.mixer.Sound(sound_file)

    # Set the sound buffer size
    buffer_size = 2048  # Adjust the buffer size as needed

    # Create a sound buffer
    sound.set_volume(0)  # Set initial volume to 0
    sound.play()  # Start playing the sound to create the sound buffer

    # Fill the sound buffer
    while sound.get_buffer().get_length() < buffer_size:
        pygame.time.wait(10)  # Wait for a short time to fill the buffer

    # Set the desired volume after the buffer is filled
    sound.set_volume(1)  # Set the volume to 1 (full volume)

    # Continue with your program logic

    # Clean up
    pygame.mixer.quit()

add_buffer()
"""
# create 10 questions
questions = []
for _ in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2} = "
    questions.append(question)

# Play music
def play_music(file_path, duration):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.time.wait(int(duration * 1000))
    pygame.mixer.music.stop()

# Music before recording
print("We will now begin the recording.")
print("Please take a moment to relax while listening to 2 minute of soothing music.")
print("Afterward, you will be given 1 minute to answer 10 arithmetic questions. Please answer as many as you can and press ENTER to go forward.")
print("Please answer each question one by one.")

# Play the music for 1 minute
start_key = input("If you're ready, press ENTER and enjoy a 2-minute piece of music.")
play_music("relaxing_music.wav", 60)

# Set a timer
question_duration = 60

#start the timer
start_time = time.time()


# test starts
test_start = input("The music playback is over, please press ENTER to start answering the question.")
answers = []
while time.time() - start_time < question_duration:
    for question in questions:
        answer = input(question)
        answers.append(answer)

        if time.time() - start_time >= question_duration:
            print("Time is up.")
            break

    if time.time() - start_time >= question_duration:
        break

print("Arithmetic test completed!")
print("Please take a moment to relax while listening to 2 minute of soothing music...")
play_music("relaxing_music.wav", 60)

# print(answers)

print("Recording completed!")

pygame.quit()
