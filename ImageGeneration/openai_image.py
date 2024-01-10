from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO
load_dotenv()

client = OpenAI()

def create_variation_from_file():
    response = client.images.create_variation(
      model="dall-e-2",
      image = open("openai_image_test_1.jpg","rb"),
      size="1792x1024",
      n=1
    )
    return response

def get_img_with_prompt(prompt):
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1792",
      quality="standard",
      n=1,
    )
    return response

def show_img_response(response):
    image_url = response.data[0].url
    print(image_url)
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()


prompt = "minimalist professional background, very small algorand logo at the top,white background, professional certificate template, has empty space for text in the middle, \
no lines,make it look like a document"
# prompt = "white gold elegant modern certificate"
show_img_response(get_img_with_prompt(prompt))