# LightBoard-Project
Hello! This is a center for my LED-enabled personal climbing wall. When the software is closer to done I'll have a separate section on that. For now, here's a section on construction

## Construction:
This board is an 8 foot by 8 foot wall set at 35 degrees from vertical. It has a 12 inch kickboard and with t-nuts placed 8 inches apart with 4 inches of padding to the edge of the face plywood. The frame is simple 2 by 4s with 2 by 6s as legs. The plywood is 3/4 inch thick. The t-nuts and bolts were purchased from [Escape Climbing](https://escapeclimbing.com/) who are, in my book, the best hardware company around. 
### Frame
The frame is 2 by 4s in a rough framing pattern. Here's an image of it, Here's another image of it. It's supported by plywood on the sides to give more rigidity to the kickboard. If these weren't here the bottom would flex considerably and possibly be unstable. <img src="/images/backFrame.jpg" width="216" height="384" /> <img src="/images/standingFrame.jpg" width="216" height="384" /> <img src="/images/frameWithLegs.jpg" width="384" height="216" />
### Face
The frame is the simplest part of the build. It's in two basic parts, the kickboard, and the main wall. The kickboard is 12 inches tall at the front and slightly taller at the back. It's cut at an angle that matches the 35 degree angle the wall is set at. The larger portion of the face is just two 4 by 8 sheets of 3/4 inch plywood. This is a typical thickness for climbing walls. The goal of the face was to make as few cuts in the plywood as possible. 
## Electronics
I used WS2811 LEDs for the lighting. Originally, I went with the WS2812b LEDs but these were sold as single LEDs that needed to be soldered together. After spending far too many hours soldering I went with the WS2811s which are sold as Christmas lights on AliExpress. These are IP68 rated and are fully programmable. To control them I am using an Arduino with the FastLED library. 
## Paint
I used 3 coats of latex floor paint with anti-skid additive to grip the holds so that they don't spin once installed. I also used a layer of water-based primer before the paint coats. The streaks indicating which LED corresponds to which hold were done using spray-paint and a stencil. 
## Software
The software portion of this is on its way slowly but surely. 
