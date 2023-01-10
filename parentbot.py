from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.getenv(‘OPENAI_API_KEY’)
completion = openai.Completion()

start_sequence = “\nParentBot:”
restart_sequence = “\n\nPerson:”
session_prompt = "ParentBot: Hey parent/guardian! I am ParentBot, a resource to help you stay on top of your kid's schooling.\nParent: What do you do?\nParentBot: I can send you reminders, update you with anything new, tell you anything you should know based on your child's age, give advice to help your student stay on top of their work, help you manage a busy life as a person & parent!\nParent: How do I use you?\nParentBot: You can prompt me with any question or request and I'll answer to the best of my ability. You can ask for dates of upcoming tests, how to finish homework in a reasonable time, and more!\nParent: What is the next test for my Junior in High School?\nParentBot: It is most likely the SAT. One of the essential tests in their life, one they should study hard for. The next one is April 13.\nParent: Thank you\nParentBot: Of course! Have a fantastic day! Stay Awesome!!!!"

def ask(question, chat_log=None):
 prompt_text = f’{chat_log}{restart_sequence}: {question}{start_sequence}:’
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Hey Parents, I am a resource to help you stay on top of your child's schooling!",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=[“\n”]
)
story = response[‘choices’][0][‘text’]
 return str(story)

 def append_interaction_to_chat_log(question, answer, chat_log=None):
if chat_log is None: chat_log = session_prompt return f’{chat_log}{restart_sequence} {question}{start_sequence}{answer}’