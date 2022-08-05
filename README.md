# DrakeLyricsBot :robot:




[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Flask-darkgreen.svg?style=flat&logo=flask&logoColor=white)](https://DrakeLyricsBot-api.herokuapp.com/docs)
![hosted](https://img.shields.io/badge/Railway-430098?style=flat&logo=railway&logoColor=white)
[![Twitter](https://img.shields.io/badge/Twitter-blue.svg?style=flat&logo=twitter&logoColor=white)](https://twitter.com/_DrakeLyricsBot)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
[![Gitpod](https://img.shields.io/badge/Gitpod-orange?style=flat&logo=gitpod&logoColor=white)](https://gitpod.io/#https://github.com/Nneji123/DrakeLyricsBot)
![reposize](https://img.shields.io/github/repo-size/Nneji123/drakelyricsbot.git)



## About
>A Twitter Bot that tweets Drake lyrics made with Python, Tweepy and Flask and deployed with RailWay.

Twitter: https://twitter.com/_DrakeLyricsBot




## Contents
  * [About](#about)
  * [Contents](#contents)
    + [Features](#features)
  * [Repository File Structure](#repository-file-structure)
  * [Pre-requisites](#pre-requisites)
  * [How to run the Application](#how-to-run-the-application)
  * [Tests](#tests)
  * [Deployment](#deployment)
- [Todo](#todo)
- [License](#license)


### Features
The bot works by reading and parsing a text file containing the lyrics. The text file can be found [here.](https://github.com/Nneji123/drakelyricsbot/data/drake_lyrics.txt) The code can be found in the [src] folder.



## Repository File Structure
```bash
├───.github # Github Workflows
│   └───workflows
├── app.json # For Deploying to Heroku
├── data
│   └── drake_lyrics.txt # lyrics file
├── docker-compose.yml # For Containerization with Docker
├── Dockerfile
├── LICENSE # For deploying to Heroku and Railway
├── README.md
├── requirements.txt
├── src
│   ├── bot.py # Tweet bot
│   ├── __init__.py
│   ├── server.py # flask server
├── tests # Tests folder
    ├── __init__.py
    └── test_bot.py

```

## Pre-requisites

To build and use the bot, you'll need to:
 
 1. Create a new Twitter account to act as the bot.
 2. Register for a [twitter developer account.](https://developer.twitter.com/en)  
 3. Create a [twitter app](https://developer.twitter.com/en/portal/projects-and-apps). Make sure to give it **Read and Write** permissions.
 4. Set up a [Railway](https://railway.app/) or [Heroku Account.](https://heroku.com)

 


## How to run the Application
<details>
    <summary><b>How to Run the application locally.<b></summary>


To make your own bot follow these steps:

1. Clone this repository on your local machine
2. Create a virtual environment in your project's root directory: `python3 -m venv environment && source environment/bin/activate`
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Create a file called `.env` in the root directory of your project. Put your twitter App keys there (and any other keys required for scraping data if needed). 
    * THIS IS JUST FOR TESTING. Once everything is tested and ready to deploy, you'll move these to environment variables.
    * ADD THIS FILE(`.env`) TO THE .gitignore so you're not putting your api keys publicly on github!
```
ACCESS_TOKEN=<YOUR_ACCESS_TOKEN_HERE>
ACCESS_TOKEN_SECRET=<YOUR_ACCESS_TOKEN_SECRET_HERE>
CONSUMER_KEY=<YOUR_CONSUMER_KEY_HERE>
CONSUMER_SECRET=<YOUR_CONSUMER_SECRET_HERE>
```
1. Make changes in the logic of the bot by modyifing `src/bot.py`
2. Test your changes locally by running `python src/bot.py` from the root directory of your project

</details>


<details> 
  <summary><b>Running on Local Machine with Docker Compose</b></summary>

**You can also run the application in a docker container using docker compose(if you have it installed)**

1. Clone the repository:
```bash
git clone https://github.com/Nneji123/DrakeLyricsBot.git
```

2. Change the directory:
```
cd DrakeLyricsBot
```

3. Run the docker compose command
```docker
docker compose up -d --build 
```
And then the lyrics should be tweeted.
</details>


<details> 
  <summary><b>Running in a Gitpod Cloud Environment</b></summary>


**Click the button below to start a new development environment:**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Nneji123/DrakeLyricsBot)
</details>

## Tests
<details> 
  <summary><b>Test Bot</b></summary>

To test the API functions do the following:
1. Clone the repository:
```
git clone https://github.com/Nneji123/DrakeLyricsBot.git
```
2. Change the working directory and install the requirements and pytest:
```
cd drakelyricsbot
pip install -r requirements.txt
```
3. Move to the tests folder and run the tests
```
cd .. && pytest tests
```
</details>

## Deployment

<details> 
  <summary><b>Deploying the Bot to Heroku</b></summary>

Click the button below to deploy the application.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)



</details>

<details>
    <summary><b>Deploy the Bot to Railway<b></summary>
Click the button below to deploy the bot to railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new?template=https%3A%2F%2Fgithub.com%2Fnneji123%2Fdrakelyricsbot)


</details>


# Todo
- [ ] Add more lyrics
- [x] Update Readme.
- [x] Update tests


# License
[MIT](https://github.com/Nneji123/DrakeLyricsBot/LICENSE.md)









