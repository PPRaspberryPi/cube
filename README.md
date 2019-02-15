# (WIP) 8x8x8 LED cube - Pi³
> University project

8x8x8 LED cube with some apps running on a Raspberry Pi.

(Not the latest version)
![](https://lambda.sx/ZSn.jpg)

## Requirements

Linux (Raspberry Pi):

* (fresh) Raspbian installation
* Python 3.5 (comes pre-installed with Raspbian)
* Check if you have the latest pip3 version: ``python3 -m pip install --user --upgrade pip``
    * If you have any problems with pip3, use ``python3 -m pip install --user [package]`` instead.
* Libraries (you can install them all via ```pip3 install [package]```):
    * [Numpy](https://pypi.org/project/numpy/) (pip3 install --user numpy)
    * [Scipy](https://pypi.org/project/scipy/) (pip3 install --user scipy)
        * There might come an error on your Pi. You might need to install scipy via your packet manager 
            
            (f.ex. apt: ```sudo apt-get install python3-scipy```) 
        * Another solution is installing libatlas3-base: ```sudo apt install libatlas3-base```
        * There are several solutions lurking github and stackoverflow (f.ex. https://github.com/scipy/scipy/issues/5995)
        * You can also try installing scipy via piwheels (https://www.raspberrypi.org/blog/piwheels/)
        * If those solutions won't fix your problems, you can follow the official guide: https://www.scipy.org/install.html
    * [SimpleAudio](https://pypi.org/project/simpleaudio/) (pip3 install --user simpleaudio)
    * [Inputs](https://pypi.org/project/inputs/) (pip3 install --user inputs)
        * (you have to edit the get_gamepad method tho - more below)
    
    Optional:
    * [PyGame](https://pypi.org/project/Pygame/) for vCube (visualization)


## Usage example

You can play snake, pong (single and multiplayer). In addition you can display the current weather state. There is also an inbuilt music player which visualizes the spectrum (via DCT).

I mean, you can play 3D Snake, isn't that enough? 🤷

## Development setup

oof


## Release History (software)
* 1.0.0
    * Everything working as intended
* 0.6.0
    * Current state
* 0.5.0
    * I don't remember every fucking step
* 0.3.0
    * What shall we do now?
* 0.2.1
    * vCube fixed and optimized
* 0.2.0
    * vCube finished
* 0.1.1
    * Let's start with some visualization
* 0.1.0
    * How the fuck do we start?
* 0.0.1
    * "Look for another project" - Professor

## General information

This is just a university project of five guys who decided to have zero free time that semester. Congratulations, you did it. It's NOT meant to be reproduced.

First of all, you would need a 8x8x8 LED cube (which you probably don't have), secondly you would need to have the exact same setup as we have (which you also (probably) do not have).
To sum everything up: you cannot reproduce that (probably).

Why would we put that on GitHub then, you might ask?
> We don't know.

## Inputs library

The default inputs library only returns the game which was plugged in first when using get_gamepad(). Since we use two
gamepads, we had to edit the library a bit to make it working flawlessly.

You have to navigate to the library's location (depends if you have installed the libarary user/system wide) 
and edit the file ```inputs.py```. Go to the very bottom of the file (you can ignore everything else) and edit the 
method ```get_gamepad()``` to 
```python
def get_gamepad(num):
    """Get a single action from a gamepad."""
    try:
        gamepad = devices.gamepads[num]
    except IndexError:
        raise UnpluggedError("No gamepad found.")
    return gamepad.read()

```

If you've followed this guide, you've installed the library user-wide and the location is 
``/home/pi/.local/lib/python3.5/site-packages/inputs.py``

Otherwise the path is something like ``/usr/local/lib/dist-packages/inputs.py``

## Contributing

You (probably) can't.
