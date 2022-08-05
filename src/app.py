import sys
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (FileResponse, PlainTextResponse)
from src.bot import create_lyric, tweet_lyric

sys.path.append(os.path.abspath(os.path.join("..", "config")))

app = FastAPI(
    title="DrakeLyricsBot API",
    description="""A twitter bot that tweets drake lyrics every 30 minutess""",
    version="0.0.1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

favicon_path = "./images/favicon.ico"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
    DrakeLyricsBot API 
    A twitter bot that tweets drake lyrics every 30 minutes
    Note: add "/redoc" to get the complete documentation.
    """
    return note


@app.post('bot', tags=["bot"])
def home():
    tweet_lyric()
    return "Tweeting weather and a quote..."
