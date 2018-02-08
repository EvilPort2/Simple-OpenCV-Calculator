# Simple-OpenCV-Calculator
A gesture controlled calculator.

## Outcome
Check it out here in this <a href ="">video</a>

## Problems being faced
1. Simple HSV masking is bad for skin segmentation. This is why I am using a dark room.
2. Gesture for confirming a number (i.e making a fist) and for "one" needs improving. 

Really need help with these two. Please help me if you can.

## Requirements
1. OpenCV
2. Numpy

## Usage
First run the range-detector.py to set the range for the mask for colour segmentation. The easiest way to use it is to put your hand in front of the camera and then slowly increasing the lower parameters(H_MIN, V_MIN, S_MIN) one by one and then slowly decreasing the upper parameters (H_MAX, V_MAX, S_MAX). When the adjusting has been done you will find that only the palm will have a corresponding white patch and rest of the image will be dark.Press 'q' to exit. Your configuration will be saved. Then run the hand-calculator.py file.

    python3 range-detector.py -f HSV -w
    python3 mouse.py

## Got a question?
If you have any questions that are bothering you please contact me on my <a href = "http://www.facebook.com/dibakar.saha.750">facebook profile</a>. Just do not ask me questions like where do I live, who do I work for etc. Also no questions like what does this line do. If you think a line is redundant or can be removed to make the program better then you can obviously ask me or make a pull request.
