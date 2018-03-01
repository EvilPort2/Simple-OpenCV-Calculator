# Simple-OpenCV-Calculator
A gesture controlled calculator.

## Note
If you are looking for a program that can <b>recognize the 26 alphabets of the American Sign Language</b> then visit <a href="http://github.com/evilport2/sign-language">here</a>.

## Outcome
Check it out here in this <a href ="https://youtu.be/Q5oeA-ebL7c">video</a>

## Requirements
1. OpenCV
2. Numpy
3. Keras with Tesorflow as backend

### Creating a gesture
  1. First set your hand histogram. You do not need to do it again if you have already done it. But you do need to do it if the lighting conditions change. To do so type the command given below and follow the instructions below.
    
    python set_hand_hist.py

  * A windows "Set hand histogram" will appear.
  * "Set hand histogram" will have 50 squares (5x10).
  * Put your hand in those squares.
  * Press 'c'. 2 other windows will appear. "res" and "Thresh".
  * On pressing 'c' only the parts of the image which has your skin color should appear on the "res" window. White patches corresponding to this should appear on the "Thresh" window. 
  * In case you are not successful then move your hand a little bit and press 'c' again. Repeat this until you get a good histogram.
  * After you get a good histogram press 's' to save the histogram. All the windows close.

  2. The next thing you need to do is create your gestures. That is done by the command given below. On starting executing this program, you will have to enter the gesture number and gesture name/text. Then an OpenCV window called "Capturing gestures" which will appear. In the webcam feed you will see a green window (inside which you will have to do your gesture) and a counter that counts the number of pictures stored.

    python create_gestures.py    
3. Press 'c' when you are ready with your gesture. Capturing gesture will begin after a few seconds. Move your hand a little bit here and there. You can pause capturing by pressing 'c' and resume it by pressing 'c'. Capturing resumes after a few secondAfter the counter reaches 1200 the window will close automatically.
  4. When you are done adding new gestures run the load_images.py file once. You do not need to run this file again until and unless you add a new gesture.
    
    python load_images.py

### Displaying all gestures
  1. To see all the gestures that are stored in 'gestures/' folder run this command
    
    python display_all_gestures.py

### Training a model
  1. So training can be done with Keras. To train using Keras then use the cnn_keras.py file.
  
    python cnn_keras.py
2. If you use Keras you will have the model in the root directory by the name cnn_keras2.h5.

You do not need to retrain your model every time. In case you added or removed a gesture then you need to retrain it.

### Running the calculator
0. Make sure you have already run the set_hand_hist.py file to set the histogram.
  1. Run the hand-calculator.py file using the command below

    python3 hand-calculator.py
    
2. This version uses numbers in American Sign Language.
3. To confirm a digit make sure you keep the same gesture for 20 frames. On successful confirmation, the number will appear in the vertical center of the black part of the window.
4. To confirm a number make a fist and keep in the green box for 25 frames. You will get used to the timing :P.
5. You can have any number of digits for both first number and second number.
6. Currently there are 10 operators.
7. During operator selection, 1 means '+', 2 means '-', 3 means '\*', 4 means '/', 5 means '%', 6 means '\*\*', 7 means '>>' or right shift operator, 8 means '<<' or left shift operator, 9 means '&' or bitwise AND and 0 means '|' or bitwise OR.


## Got a question?
If you have any questions that are bothering you please contact me on my <a href = "http://www.facebook.com/dibakar.saha.750">facebook profile</a>. Just do not ask me questions like where do I live, who do I work for etc. Also no questions like what does this line do. If you think a line is redundant or can be removed to make the program better then you can obviously ask me or make a pull request.
