# Space telegram

`PyastroAPI` is a set of console scripts to communicate with services like: NASA, SpaceX, EPIC. 

Main goal is to download beautiful photos of space launches, Earth and space in general to popularize astrophysics as a fundamental science. 

Main features are: 
+ download `NASA` picture of a day
+ download some number of random photos from `NASA` storage
+ download `SpaceX` launches photos
+ download beautiful photos of our home planet - `Earth`.
+ automatic photo publishing to the `@astro24channel` Telegram channel

## How to install

Python3 has to be already installed. 

In project folder create your own settings file - `.env`

It should include such fields:

+ IMAGE_FOLDER=
+ NASA_TOKEN=
+ TELEGRAM_TOKEN=
+ UPDATE_PERIOD=

`IMAGE_FOLDER` - photo storage folder name. It has to be in current scripts home directory.

`NASA_TOKEN` - access token for NASA services

`TELEGRAM_TOKEN` - access token for Telegram services

`UPDATE_PERIOD` - period of time between photo publishing in the channel


### Create virtual environment:
```
python3 -m venv venv
```

### Activate venv
```
source ./venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

---

## Scripts description

### `astronomy.py`

Main script, which combine all features - download photos from all available sources to the `IMAGE_FOLDER` and then, starts publishing it to Telegram channel with some particular delay - `UPDATE_PERIOD`.

To run script with default delay - `(4 hours)` run:
```
python3 astronomy.py
```

In order to override delay period you can run like this:
```
python3 astronomy.py --period 1
```

`--period <hours>` define hours number between photo publishings

By default, delay time is used from `.env` file environment

### `basic.py`

Includes common fuctions such as: 
+ download_image()
+ get_file_name()
+ get_file_extension() 

Main idea - put functions into separate file to re-use  them in our projects

### `fetch_nasa_images.py`
By default - script downloads only 1 NASA picture of a day. 

```
python3 fetch_nasa_images.py
```

In order to set number of photos to grab - we can run script like this:

```
python3 fetch_nasa_images.py --count XXX
```


### `fetch_spacex_images.py`
By default - script downloads fresh photos of SpaceX launch. 

```
python3 fetch_spacex_images.py
```

In order to grab particular launch photos, you can run script like this:

```
python3 fetch_spacex_images.py --launch_id=5eb87ce6ffd86e000604b33a
```

in this example `5eb87ce6ffd86e000604b33a` - is a launch identifier


### `fetch_epic_images.py`

This script download Earth photos from EPIC web-service

To run script enter command:
```
python fetch_epic_images.py
```

### `astro24bot.py`

This script implements the logic of communication with Telegram

`send_photo_to_channel(photo=None, text=None)`

Being run without parameters - it will publish 1 random space photo to the Telegram channel.

+ Parameter `photo` - define file name to send into channel.

+ Parameter `text`  - define text to send short message to the channel.