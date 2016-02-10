# Silent-Night-API
An API into a stealth/discovery space combat game.

# Basic Idea
Multi-player stealth combat asteroids game. Game world is simulated on the server, in brief snapshots done by request. The player is given a small view into the world through the game API, that allows them to control their ship with a range of commands.

# Environment Setup
Linux - Ubuntu
```
$ sudo apt-get install postgresql       # PostgreSQL
$ sudo apt-get install libpq-dev        # postgresql dev library
$ sudo apt-get install python3-pip      # for installing libs for python3
$ sudo apt-get install git              # for version control
$ sudo pip3 install --upgrade virtualenv virtualenvwrapper


$ mkvirtualenv --no-site-packages snapi     # makes python virtual_env
$ mkproject silent-night-api                # creates project directory
$ workon snapi                              # will activate virtual_env
(snapi)$ git clone https://{{YOUR_USERNAME}}@github.org/Maaack/Silent-Night-API.git
(snapi)$ cd silent-night-api/
(snapi)$ pip install -r requirements.txt    # install all requirements
(snapi)$ vim local_settings.py              # ask me to make a sample of these, I haven't yet. I should.
```

# Structure
Django Based REST API

Game stuff is in the `game_api` folder! All models that are persistent have schema's so they are stored in the database between requests. Everything else is python objects. The objects will need to be serialized so that they can be stored in a snapshot model to save the current state of the game world. Snapshots might need to be saved every couple of seconds so that the physics simulator doesn't have to simulate for huge leaps of time on each request.
