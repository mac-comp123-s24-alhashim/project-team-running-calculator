# Creating a Detailed Running Pace Calculator 


## Team Members 
Tyler Edwards (tedward1@macalester.edu) and Noah Koch (nkoch1@macalester.edu)


## Team Running Calculator 


### Description 
This project will be an advanced running pace and split calculator which will output a variety of different statistics based on user inputs. Using a Python graphical user interface, a user will select the units of measurement (meters, kilometers, or miles) along with inputing an integer representing (in the chosen units) the distance they are racing. 


### Project Sketch
![1712285740253-61f7292c-d021-4c58-bb6a-2fc0c49796cd_1](https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156855239/8ff3602d-55f4-4cc5-af0d-1702e5dfe3de)

![1712285740253-61f7292c-d021-4c58-bb6a-2fc0c49796cd_2](https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156855239/d391520c-b815-44bd-9db9-e2cdbc6c4bd9)


### How to Use 
The user will  have the option of inputting either their desired pace per mile or overall time (or both!). There will also be a checkbox to specify whether the race is occuring on a 200m indoor track or a 400m outdoor one. Lastly, the user will select whether the distance they are inputting is present in track meets (such as the 1000m, 3200m, etc), so that the program can output per lap splits. Then, the user will click submit and a popup will appear with a variety of new calculated statistics. Firstly, the program will fill in per mile pace or total time if either were left blank in the intial input, then if the input value is one of the distances pre-designated as being common in track meets, there will also be an output of splits per lap, and other important statistics like halfway point times. If the distance entered is not in the list of pre-designated distances, then the program will still fill in per mile pace or total time if either were left blank in the intial input, but will not give per lap splits, just their splits per mile or km (depending on the selected units).


#### Package and Python Version Requirements 
Our project was coded on Python Version 3.12 and requires the following packages to be installed: PIL, ttkbootstrap, tkinter, and datetime.


#### How to Run the Software
Open our project link on github and navigate to the file labeled "Running_Calculator.py". Run this file and then a popup screen will appear with input boxes for time, pace, and distance, as well as units for distance and pace. In addition, you can also select a specific track type (indoor or outdoor) in order to have lap splits appear in the next popup. Once you have inputted 2 of the 3 main variables, selected units, and decided if you want lap splits to appear, click submit and a new window will open with your desired information. 


#### Limitations 
If you input values for all 3 of pace, distance, and time, the program will not run as there is nothing to be calculated. Additionally, if you do not select units for either distance or pace, the calculated values in the next window will be incorrect. Lastly, if you input a negative number for any of the inputs or put decimals in pace or time, the function will either not run or calculated obviously incorrect values given the nature of trying to input a negative value for distance, pace, or time. 


### Why We Chose This Project
We chose this project because, as two runners on the Cross Country and Track teams, we noticed there is a lack of a super detailed running pace calculator in the world as of now. Being able to calculate lap splits and pace per mile/km is very important for us as competitive runners, and thus the more data that we can have prior to a race the better. 


### Inspiration Behind This Project
We have used multiple online pace calculators in the past, but none of them have an effective way of getting splits per lap nor other data points which would be useful for running nerds like ourselves. 

### Recources Referenced
We look at ttkbootstraps website in order to improve our GUI. 


### Implementation / Responsibility Plan
This project will require a lot of different functions that will all interact with eachother dependent on the inputted values by the user. Therefore, the vast majority of our time will be spent creating said functions and testing them with different input values to ensure there is no buggy interaction nor inaccurate results. We will both be working on making these functions and holding each other accountable to making the workload be split evenly. Ultimately, since the functions will be so interactive, it will be difficult to split the work into multiple parts, rather we will both be working congruently on ensuring everything gets done on time. The primary aim of this project is to have a running calculator which will display not just pace per mile, total time, and distance run, but also things like splits per lap and halfway point times. 

### Screenshots of Example Scenarios

### Initial Window
<img width="494" alt="Screenshot 2024-05-02 at 7 44 25 PM" src="https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156964308/8d949882-4b2e-43e0-a3dc-1566da943a74">

### Initial Window With Example Inputs
<img width="503" alt="Screenshot 2024-05-02 at 7 44 45 PM" src="https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156964308/e2eeb916-7a1e-4202-bb64-4b42916acb04">

### Secondary Window Without Lap Splits
<img width="662" alt="Screenshot 2024-05-02 at 7 46 01 PM" src="https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156964308/aad50741-811b-4fd6-818d-eddde6615eea">

### Secondary Window With 200m Track Lap Splits
<img width="916" alt="Screenshot 2024-05-02 at 7 45 12 PM" src="https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156964308/d0da438a-0f43-4ad2-bf0b-b4a2d9685ecd">

### Secondary Window With 400m Track Lap Splits
<img width="528" alt="Screenshot 2024-05-02 at 7 45 27 PM" src="https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156964308/d9fed3da-51e4-4296-9575-8b60eef34797">

