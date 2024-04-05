# Creating a Detailed Running Pace Calculator 


## Team Members 
Tyler Edwards (tedward1@macalester.edu) and Noah Koch (nkoch1@macalester.edu)


## Team Running Calculator 


### Description 
This project will be an advanced running pace, split, and race plan calculator which will output a variety of different statistics based on user inputs. Using a Python graphical user interface, a user will select the units of measurement (meters, kilometers, or miles) along with inputing an integer representing (in the chosen units) the distance they are racing. 


### Project Sketch
![1712285740253-61f7292c-d021-4c58-bb6a-2fc0c49796cd_1](https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156855239/8ff3602d-55f4-4cc5-af0d-1702e5dfe3de)

![1712285740253-61f7292c-d021-4c58-bb6a-2fc0c49796cd_2](https://github.com/mac-comp123-s24-alhashim/project-team-running-calculator/assets/156855239/d391520c-b815-44bd-9db9-e2cdbc6c4bd9)


### How To Use 
The user will  have the option of inputting either their desired pace per mile or overall time (or both!). There will also be a checkbox to specify whether the race is occuring on a 200m indoor track or a 400m outdoor one. Lastly, the user will select whether the distance they are inputting is present in track meets (such as the 1000m, 3200m, etc), so that the program can output per lap splits. Then, the user will click submit and a popup will appear with a variety of new calculated statistics. Firstly, the program will fill in per mile pace or total time if either were left blank in the intial input, then if the input value is one of the distances pre-designated as being common in track meets, there will also be an output of splits per lap, and other important statistics like halfway point times. If the distance entered is not in the list of pre-designated distances, then the program will still fill in per mile pace or total time if either were left blank in the intial input, but will not give per lap splits, just their splits per mile or km (depending on the selected units).


### Why We Chose This Project
We chose this project because, as two runners on the Cross Country and Track teams, we noticed there is a lack of a super detailed running pace calculator in the world as of now. Being able to calculate lap splits and pace per mile/km is very important for us as competitive runners, and thus the more data that we can have prior to a race the better. 


### Inspiration Behind This Project
We have used multiple online pace calculators in the past, but none of them have an effective way of getting splits per lap nor other data points which would be useful for running nerds like ourselves. 


### Implementation / Responsibility Plan
This project will require a lot of different functions that will all interact with eachother dependent on the inputted values by the user. Therefore, the vast majority of our time will be spent creating said functions and testing them with different input values to ensure there is no buggy interaction nor inaccurate results. We will both be working on making these functions and holding each other accountable to making the workload be split evenly. Ultimately, since the functions will be so interactive, it will be difficult to split the work into multiple parts, rather we will both be working congruently on ensuring everything gets done on time. The primary aim of this project is to have a running calculator which will display not just pace per mile, total time, and distance run, but also things like splits per lap and halfway point times. 

