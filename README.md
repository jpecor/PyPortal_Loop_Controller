# PyPortal_Loop_Controller
Simple PyPortal-based loop/sequencer controller for Apple GarageBand.

I'm currently working on the electronics for an art installation that will be happening this spring in my hometown. The project is a fusion of metalworking sculpture and technology for the purpose of creating an engaging discovery and play attraction for kids in a local park.

The PyPortal makes an excellent prototype for the touch sensors / human interface that the real project will have. For the sake of ease and expediency, I wanted to use GarageBand to create a simple multi-track song that I can loop.

GarageBand doesn't provide much in the way of external controls, but it *IS* possible to navigate up and down the tracks via arrow keys and mute/umute each track with the "M" key.  So, using that crude form of navigation and control, I am sending HID keycode commands from the PyPortal that jump to the desired track, toggle the mute status, then return to the top of the track list. 

There are a number of ways to improve this approach, but it's good enough to demonstrate proof of concept. 

Read about the art exhibit: 
[Trolling for Whimsey - Altoona’s River Prairie to get interactive sculptures of mythical monsters](https://volumeone.org/articles/2019/11/27/33319_trolling_for_whimsey)

[Click here to buy a PyPortal from Adafruit.](https://www.adafruit.com/product/4116)

[Click here to learn more about CircuitPython.](https://circuitpython.org/)

![loop_controller](https://live.staticflickr.com/65535/49454680858_a03c7a9890.jpg)
