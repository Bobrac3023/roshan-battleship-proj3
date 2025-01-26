
## Battleship Game - Guess the Ship Location

## Introduction
The battelship game is one of the most popular game used to demonstrate the use of "python" language, its versality and ease of use.
The choice of this game for this project is to present the ***user*** with a game of logic, where their skills are tested against a machine, in this case a computer. It is a ***single player*** game, wherein the computer generates a random number to mark the ships location. A ***3x3*** grid presents a visual representation for hits, misses, and the ships location. The user is presented with relevant messages for guidance throughout the game. 


## Features 
- The project code is written in python 3 inside the code institute IDE.
- Github is used to host the repository.
- Heroku the dynamic websites platform is used to host backend language python.
- **pep8ci** linter from code institute is used to check the code for PEP8 styling. https://pep8ci.herokuapp.com/# 
- The logic for the entire code is broken up in multiple parts- **functions, while-if-else loops** and **try except** block.
- Install **pytz package** that brings the Olson tz database into Python and thus supports almost all time zones
- Import **datetime** and **timezone** module to display the **date,month,year,time and day** for **Asia/Dubai** timezone.
- Import of  **random** module to generate random numbers for the game.
- A **print_grid** function to print the **3x3** grid and display numbers from 1 to 9.This grid is used for visual representation of the ship 
  location, hits and misses during the game.
- A **match** function **checks and matches** the  **user_input** with input from the **random module**.
- A **play_game** function used to play the game.This function checks if user_input matches the value of the **code_generator**.
    - Based on the outcome it marks the board with an **X** for a miss, **H** for a hit and **L** for the correct position,with relevant messages 
      displayed on the screen.
    - **Input validation** and **data type validation** is used when seeking user input for the ship's location.
    - A **try and catch block** is used to capture **valueError**exceptions for correct data type validation.
    - **strip** function used to remove leading and trailing whitespaces.
    - **lower** function used to return string in lower case.
    - The input solicited from the users is an **integer** between **1 to 9**.
    - **Floats and strings** are not allowed.
    - Relevant **print** messages warn the user about what input is expected.
- A **continue_game** function seeks user input to continue with the game or exit.
    - The input solicited from the user is a **yes*** or **no**. 
    - **strip** function used to remove leading and trailing whitespaces.
    - **lower** function used to return string in lower case.
    - The **while len** method is used to check if the **user_input** is **greater** than **2**.
    - However, if the user inputs an **integer greater than 2** then game exits
- A **main** function is used to initialise the game.
    - The main function inlcudes the **print_board** function
    - The code then moves on to generate the **random number** between **1 and 9**
    - The **play_game** function is then initialised to start the game
    - The **continue_game** fuction is called from within the **play_game** function  

- A mindmanger map explains the logic below.

![mindmanager_mindmap_logic_explaination](readme.doc/mindmanager_mindmap_logic_explaination.png)


## Links to Github, Gitpod and Heroku

- External Link  
  https://bobrac3023.github.io/roshan-battleship-proj3/

- Heroku app Program link  
  https://roshan-battleship-proj3-06066cd9a93e.herokuapp.com/

- Link to Github repository.  
  https://github.com/Bobrac3023/roshan-battleship-proj3

- Link to Gitpod workspace.  
  https://bobrac3023-roshanbattle-cv53bgpnc73.ws-us115.gitpod.io/

## Features to implement later

- Use color packages like **colorama** or **termcolor** to print bold text.  
- Display images using libraries like **openCV**, **matplotlib**, **pillow** or **tensorflow**.


## Install pytz package and configure timezone

### ptyz package
- The pytz package was installed to allow import of the timezone module. 

![pip_install_pytz](readme.doc/pip_install_pytz.png)

### pip3 freeze > requirements.txt output ### 
- The pip3 freeze > requirements.txt command was used to capture the pytz package dependency for the Heroku app. 

![requirements.txt_update](readme.doc/requirements_txt_update.png)

### datetime and timezone configuration details ###

- The time zone configured for this game is UTC+4 which is Asia/Dubai.  
- The time is displayed in 12 hour format with AM/PM.  
- The day of the week is also displayed. 

![date_time_programiz](readme.doc/date_time_programiz.png)

### Heroku app output - initialize screen - display datetime and timezone ###

![heroku_app_deployment_0125](readme.doc/heroku_app_deployment_0125.png)

## Code validation
-Code was validated using code institute PEP8 linter  
- **code validation** pep8 from Code Institute https://pep8ci.herokuapp.com/# 

### Code Institute PEP8 Linter test output
![pep8ci_linter_output_0](readme.doc/pep8ci_linter_output_0.png)
![pep8ci_linter_output](readme.doc/pep8ci_linter_output.png)

## Code Testing 

-Code functions were tested and validated using the below tools.:-  

- **programmiz.com** - an online python compiler  https://www.programiz.com/online-compiler/7oVd1BFsuE3Bd.  
- **pythontutor** - Visualize code execution  https://pythontutor.com/cp/composingprograms.html#mode=edit.  
- **gitpod IDE environment**  https://bobrac3023-roshanbattle-cv53bgpnc73.ws-us115.gitpod.io/.  


### Test,validate and visualize "play_game" function

**User is asked to guess a number** 

![user_input_guess_ship_1](readme.doc/user_input_guess_ship_1.png)

**user choose to continue- input from user to prompt is "YES"** 

![user_choose_continue](readme.doc/user_choose_continue.png)

**user input validation and data type validation**
![input_type_and_data_type_validation](readme.doc/input_type_and_data_type_validation.png)

### Test,validate and visualize "continue_game" function

**user inputs YES- game continues** 

![continue_game_yes](readme.doc/continue_game_yes.png)

**user inputs NO- game terminates**

![continue_game_no](readme.doc/continue_game_no.png)

**user input validation**

![]()

- **pythontutor visualization output** 

![]()

### Test,validate and visualize "Main" function", for "input validation" and "user choice" validation

- **Online compiler output** 

![]()


- **Code insititute IDE output**

![]()

- **pythontutor visualization output**

![]()


### Odd Quirk issue - "input statement"  

- In order to allow the input statement to work corectly in the Heroku mock terminal, code institute requires the additon of **/n** line character at the end of the text.  
- Without this extra character the text for the **input request** will not show in the terminal.

![odd_quirk_input_text](readme.doc/odd_quirk_input_text_issue.png)

## Deployment

### Deployment from GitHub
-The site was deployed to GitHub pages as below.  
-In the GitHub repository,
-   Navigate to the Settings tab,
-   Select pages
-   Under **Branch** dropdown, change to **Main** hub from **none**.

-select_branch_github_deployment

-From the **Actions** tab, select **Deployment** to check deployment status and capture external link.

![github_page_enable](github_page_enable.png)
![github_pagebuild_deployment](github_pagebuild_deployment.png)
![github_pagebuild_sucess](github_pagebuild_sucess.png)

### Github_page_deployment

-Once the main branch has been selected, the page will automatically refresh to indicate the successful deployment.

-The live link can be found here - https://bobrac3023.github.io/roshan-battleship-proj3/

### Gitpod after creation from Github Repository using Code-Institute-Org/python-essentials-template

![gitpodio_after_creation](readme.doc/gitpodio_after_creation.png)

### Code_ide_environment

![gitpod_code_ide_environment](readme.doc/gitpod_code_ide_environment.png)

### git_add_commit_push_command

-use gitpod commands to add, commit code to gitub repository.  
-gitpod push command to push commited changes to github repository 

![add,commit,push](readme.doc/add_commit_push_github.png)

## Heroku 


### Heroku Eco Dynos Plan config

![heroku_eco_dynos_plan](readme.doc/heroku_eco_dynos_plan.png)

### Heroku Buildpacks Config- Add python and Nodejs

![heroku_add_buildpacks](readme.doc/heroku_add_buildpacks.png)

### Heroku Github conectivitiy and deployment 

![heroku_authorise](readme.doc/heroku_authorise.png)
![heroku_auto_deploy_github](readme.doc/heroku_auto_deploy_github.png)
![heroku_app_github_connected](readme.doc/heroku_app_github_connected.png)
![heroku_manual_deply](readme.doc/heroku_manual_deploy.png)

### Heroku app deployed 

![heroku_app_deployed](readme.doc/heroku_app_deployed.png)

### Heroku app program link

https://roshan-battleship-proj3-06066cd9a93e.herokuapp.com/

## Credits

- **Extra help to understand key python concepts.**  
    https://www.youtube.com/watch?v=KzqSDvzOFNA.  
    https://www.youtube.com/watch?v=piJc18hcH0Y.  
    https://www.youtube.com/watch?v=CasqhmeopnU.  
    https://www.youtube.com/watch?v=8UCIvrs9LZw.  
    https://www.youtube.com/watch?v=Ej7I8BPw7Gk.  
    https://www.youtube.com/watch?v=PY9hvAFrxMI.  
    https://pythonbasics.org/try-except/  
    https://www.youtube.com/watch?v=TqPzwenhMj0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=6  
    https://www.youtube.com/watch?v=4OX49nLNPEE  
    https://www.youtube.com/watch?v=ON70wvKYops
    https://www.youtube.com/watch?v=kLI31o7mDsA  
    https://www.youtube.com/watch?v=zPFZy6wKhVA&list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn&index=34  
    https://www.youtube.com/watch?v=94UHCEmprCY.  
    https://www.w3schools.com/python/ref_string_lower.asp.  
    https://www.w3schools.com/python/ref_string_strip.asp  
    https://www.geeksforgeeks.org/python-comments/


- **Programmiz.com**- An online compiler to test functions and pieces of code   
    https://www.programiz.com/online-compiler/7oVd1BFsuE3Bd.  

- **Visualize Code execution** - pythontutor.  
    https://pythontutor.com/cp/composingprograms.html#mode=edit.  

- **PEP8 style guide**  
    https://pep8.org/  
    https://realpython.com/python-pep8/



### Content creation assistance- reference code

- **design the grid**  
    https://www.youtube.com/watch?v=PY9hvAFrxMI.  
- **input validation**  
    https://www.youtube.com/watch?v=ON70wvKYops.  
- **validate data type**  
    https://www.youtube.com/watch?v=kLI31o7mDsA.  
- **user input**  
    https://bobbyhadz.com/blog/python-input-boolean  
- **pytz install and configure timezone**  
    https://www.geeksforgeeks.org/python-pip/  
    https://strftime.org/  
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes  
    https://mljar.com/blog/list-pytz-timezones/




### Media
-All images used in this readme file are placed under the readme.doc file.

![readme_doc_images](readme.doc/readme_doc.png)