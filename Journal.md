---
title: BLOOM
author: Ayomide Abraham
description: 80% Mechanical Keyboard
created at: 07/20/2025
total time: 13 hours
---

Time: 5 hours

- I started by brainstorming what I wanted on my keyboard. I looked at layouts, features, and the number of keys I would need for daily use.
- I researched how to build an 80% keyboard from scratch. This was my first time making a keyboard, so I had to learn each step carefully.
- I began working on the schematic, mapping out how each key would connect to the microcontroller and how the rows and columns would be wired.

One of the biggest challenges was choosing the right microcontroller. Many options were either too expensive or didn’t have enough GPIO pins. After some research, I found the Raspberry Pi Pico. It was affordable, reliable, and had more than enough I/O for the 87-key layout. Once I chose the Pico, building the schematic became much more easier.

![schematic](https://github.com/Doubtfull/Bloom/blob/main/Assets/Schematic1.png)
![schematic](https://github.com/Doubtfull/Bloom/blob/main/Assets/Schematic2.png)

Day 2

time: 8 hours

- Started routing the PCB

Routing the PCB was fairly easy and after I finished, I got 0 errors from DRC first try! I also changed the PCB design a little by adding field zones. It makes the PCB looks so much better!

It wasn't until I finished wiring till I realized that my pico was too low. But instead I'll just make a longer hole so that the cable can reach the pico.

![PCB](https://github.com/Doubtfull/Bloom/blob/main/Assets/PCB.png)
![PCB Render](https://github.com/Doubtfull/Bloom/blob/main/Assets/PCB%203D.png)

- Then I got on Fusion and I started to work on the case
- I created the bottom and top case fairly quickly
- I then made a little opening to show off the silkscreen

The case that I made is very similar to the hackpad case that I made, this time I wanted to show off some of the PCB design.

![CAD Base](https://github.com/Doubtfull/Bloom/blob/main/Assets/Bottom%20Case.png)
![CAD Cover](https://github.com/Doubtfull/Bloom/blob/main/Assets/Top%20Case.png)
![case compatibility](https://github.com/Doubtfull/Bloom/blob/main/Assets/Compatibility.png)

Don't worry there's more than enough space for the cable to connect to the pico!

I also worked and finished my BOM, compiled and sorted all my file for submission.
