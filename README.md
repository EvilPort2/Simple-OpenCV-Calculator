# Simple-OpenCV-Calculator
A gesture controlled calculator.

## Outcome
Check it out here in this <a href ="https://youtu.be/6bE9veUsQf4">video</a>

## Problems being faced
1. Simple HSV masking is bad for skin segmentation. This is why I am using a dark room. [SOLVED using back projection]
2. Gesture for confirming a number (i.e making a fist) and for "one" needs improving. 

Really need help with these two. Please help me if you can.

## Requirements
1. OpenCV
2. Numpy

## Usage
1. Run the hand-calculator.py file using the command below

    python3 hand-calculator.py
2. A windows "Set hand histogram" will appear.
3. "Set hand histogram" will have 50 squares (5x10).
4. Put your hand in those squares.
5. Press 'c'. 2 other windows will appear. "res" and "Thresh".
6. On pressing 'c' only the parts of the image which has your skin color should appear on the "res" window. White patches corresponding to this should appear on the "Thresh" window. 
7. In case you are not successful then move your hand a little bit and press 'c' again. Repeat this until you get a good histogram.
8. After you get a good histogram press 's' to save the histogram. All the windows close.
9. A new window appears "Calculator".
10. Put your hand the rectangle. Making a fist means confirming a number. 
11. During operator selection, 1 means '+', 2 means '-', 3 means '\*', 4 means '/' and 5 means '%'.


## Got a question?
If you have any questions that are bothering you please contact me on my <a href = "http://www.facebook.com/dibakar.saha.750">facebook profile</a>. Just do not ask me questions like where do I live, who do I work for etc. Also no questions like what does this line do. If you think a line is redundant or can be removed to make the program better then you can obviously ask me or make a pull request.
