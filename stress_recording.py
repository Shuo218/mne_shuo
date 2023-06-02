#! /usr/bin/python3

import random
import time
import pygame

# Initialize pygame
pygame.mixer.init()
pygame.init()

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
print("Please take a moment to relax while listening to 1 minute of soothing music.")
print("Afterward, you will be given 1 minute to answer 10 arithmetic questions.")
print("Please answer each question one by one.")

# Play the music for 1 minute
start_key = input("If you're ready, press ENTER and enjoy a 1-minute piece of music.")
play_music("relaxing_music.wav", 60)

# Set a timer
question_duration = 60

#start the timer
start_time = time.time()

# test starts
test_start = input("The music playback is over, please press ENTER to start answering the question.")
answers = []
for question in questions:
    answer = input(question)
    ##answers.append(answer)

    if time.time() - start_time >= question_duration:
        print("Time is up.")
        break

print("Arithmetic test completed!")
print("Please take a moment to relax while listening to 1 minute of soothing music...")
play_music("relaxing_music.wav", 60)

##print(answers)

print("Recording completed!")

pygame.quit()
