from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
# The following import brings in 'Annotated' from the 'typing' module.
# 'Annotated' is used for adding metadata to type hints, which can be useful
# for frameworks like FastAPI to provide additional information about parameters.
from typing import Annotated
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

load_dotenv()

app=FastAPI()
# This line initializes the Jinja2Templates object, which allows FastAPI to render HTML templates
templates = Jinja2Templates(directory="templates")

chat_responses = []

openai=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
              )

chat_history = [{'role': 'system',
                 'content': 'You are a Python tutor AI, completely dedicated to teach users how to learn \
                        Python from scratch. Please provide clear instructions on Python concepts, \
                        best practices and syntax. Help create a path of learning for users to be able \
                        to create real life, production ready python applications.'
             }]



# This route handles GET requests to the root URL ("/").
# It renders the "home.html" template and passes two variables to it:
# - "request": the current HTTP request object, required by FastAPI/Jinja2 templates.
# - "chat_responses": a list containing the conversation history between the user and the chatbot.
# This allows the template to display the chat history to the user.
@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    
    chat_history.append({"role":"user","content":user_input})
    chat_responses.append(user_input)

    
    response=openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history,
        temperature=0.6
    )

    bot_response=response.choices[0].message.content    
    chat_history.append({"role":"assistant","content":bot_response})
    chat_responses.append(bot_response)
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})



@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    # Pass image_url as None so the template logic works correctly
    return templates.TemplateResponse("image.html", {"request": request, "image_url": None})   

@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):
    response = openai.images.generate(
        prompt=user_input,
        n=1,
        size="512x512"
    )
    image_url = response.data[0].url if response and hasattr(response, "data") and response.data else None
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})





