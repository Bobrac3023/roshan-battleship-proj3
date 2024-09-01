
## Battleship Game - Guess the Ship Location

## Introduction
The battelship game is one of the most popular game used to demonstrate the use of "python" language, its versality and ease of use.
The choice of this game for this project is to present the ***user*** with a game of logic, where their skills are tested against a machine, in this case a computer. It is a ***single player*** game, wherein the computer generates a random number to mark the ships location. A ***3x3*** grid presents a visual representation for hits, misses, and the ships location. The user is presented with relevant messages for guidance throughout the game. 

## Features
-The project code is written in python 3 inside the code institute IDE.   
-Github is used to host the repository.  
-Heroku the dynamic websites platform is used to host backend language python.  
-PEP8 style guide was referenced to style the code   
-The logic for the entire code is broken up in multiple parts- ***functions, while-if-else loops*** and ***try except*** methods.  
-A mindmanger map explains the logic below

![mindmanager_mindmap_logic_explaination](readme.doc/mindmanager_mindmap_logic_explaination.png)

-Install pytz package.  
-Import ***datetime*** and ***timezone*** module to display the ***date,month,year,time and day*** for **Asia/Dubai** timezone.  
-Import of  ***random*** module to generate random numbers for the game.  

-A **3x3** grid displays numbers from 1 to 9 . Used for visual representation of the ship location, hits and misses during the game.  
-A ***match*** function **checks and matches** the  ***user_input*** with input from the ***random module***.  

-A ***Main*** function **first** checks for input value and data type validation  with a ***while--if-else*** loop .  
- The input solicited from the users is an ***integer*** between 1 to 9. ***Floats and strings*** are not allowed.  
- ***try except*** method is used to handle exceptions.  
- Relevant ***print*** messages warn the user about what input is expected.  

-The **second** part of the ***Main*** function has a ***while--if-elif-else*** loop to solicit user response to continue or exit.  
- The input solicited from the user is a ***yes*** or ***no***. ***Floats and integers*** are not allowed.  
- ***strip*** function used to remove leading and trailing whitespaces.  
- ***lower*** function used to return string in lower case.   
- If the user input is"yes", a ***new random number*** is generated and game continues.  
- If the user input is "no", the games exits and user is displayed a **Goodbye** message.   

-The ***Grid*** displays **"H"** for hits, **"X"** for misses and **"L** for the correct ship position.  
-The game is designed to allow the user to play as long as they wish.  

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

![timezone_compiler_validation](readme.doc/timezone_compiler_validation_.png)

### Heroku app output for datetime and timezone ###

![heroku_app_datetime_zone_display](readme.doc/heroku_app_datetime_zone_display.png)

## Testing and code validation
-Code and functions were tested and validated using the three tools listed below:-  
- **programmiz.com** - an online python compiler  (https://www.programiz.com/online-compiler/7oVd1BFsuE3Bd).  
- **pythontutor** - Visualize code execution  (https://pythontutor.com/cp/composingprograms.html#mode=edit).  
- **gitpod IDE environment**  (https://bobrac3023-roshanbattle-cv53bgpnc73.ws-us115.gitpod.io/).  


### Test,validate and visualize "print_grid" function

- **Online Compiler output** 

![print_gird_function_compiler_output](readme.doc/print_grid_function_compiler_output.png)

- **pythontutor visualization output** 

![print_grid_function_pythontutor](readme.doc/print_grid_function_pythontutor.png)

### Test,validate and visualize "random no" generation inside the Main function

- **Online compiler output** 

![random_no_function_compiler_output](readme.doc/random_no_function_compiler_output.png)

- **Code insititute IDE output**

![random_no_gitio_test](readme.doc/random_no_gitio_test.png)

- **pythontutor visualization output** 

![random_no_function_pythontutor](readme.doc/random_no_pythontutor_visualizaton.png)

### Test,validate and visualize "Main" function", for "input validation" and "user choice" validation

- **Online compiler output** 

![main_function_compiler_output](readme.doc/main_function_compiler_output.png)


- **Code insititute IDE output**

![main_function_gitio_test](readme.doc/main_function_gitpio_test.png)

- **pythontutor visualization output**

![main_function_pythontutor](readme.doc/main_function_pythontutor.png)


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