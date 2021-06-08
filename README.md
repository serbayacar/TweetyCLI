# TweetyCLI

Quickly scrolling through Twitter allows you to instantly view your messages and followers.  
Twitter on your computer and at your prompt!


## Installation 
---
###  with Virtual Environment(venv)

To set your virtual environment and activate it:

```text
$ python3 -m venv .env/
$ source .env/bin/activate
```

Install dependencies in virtual environment:

```text
$ pip install -r requirements.txt
```

### with Dockerfile

First, make sure that the Docker environment is installed on your computer.
After the Docker installation is complete, in the root folder of the project (in the directory where the Dockerfile file is located),

To build the Dockerfile,


```text
docker build -t <image_name> \
--build-arg CONKEY=<twitter_app_consumer_key> \
--build-arg CONSEC=<twitter_app_consumer_secret> \
--build-arg ACCTOK=<twitter_app_api_key> \
--build-arg ACCSEC=<twitter_app_api_secret> \
.
```

After build successfully, you must run this image into container,

```text
docker run -it <image_name>
```

---

## Usage

To use TweetyCLI:

```text
(.env)$ python3 twitcli <command>
```
