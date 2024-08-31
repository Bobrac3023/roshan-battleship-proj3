![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

## Battleship Game - Guess the Ship Location


## Introduction


## Features
-The project code is written in python 3.  
-The logic for the entire coding is broken up in multiple parts.  
-Import of ***dateline*** module to display the date, month, year and time in UTC.  
-Import of  ***random*** module to generate random numbers for the game.  
-A 3x3 grid displays numbers from 1 to 9 . Used for visual representation of the ship location, hits and misses during the game.  
-A ***match***function **checks and matches** the  ***user_input*** with input from the random module.  
-A ***Main*** function with a ***while*** loop for input value and type validation.  
-   The input solicited from the users is an ***integer*** between 1 to 9. Floats and strings are not allowed.  
-   Relevant ***print*** messages warn the user about what input is expected.  
-The ***Main*** function also inlcudes a ***while*** loop to solicit user response after every input.  
-   The input solicited from the users is a ***yes*** or ***no***. Floats and integers are not allowed.  
-   if the user input is"yes", a new random number is generated and game continues.  
-   if the user input is "no", the games exits and user is displayed a **Goodbye** message
-The ***Grid*** displays **"H"** for hits, **"X"** for misses and **"L** for the correct ship position.  
-The game is designed to allow the user to play as long as they wish.  




## Existing Features


## Deployment
### Deployment from GitHub
-The site was deployed to GitHub pages as below.
-In the GitHub repository,navigate to the Settings tab,select pages, under **Branch** dropdown change to **Main** hub from **none**.

-select_branch_github_deployment

-From the **Actions** tab, select **Deployment** to check deployment status and capture external link.

### Github_page_deployment

-Once the main branch has been selected, the page will automatically refresh to indicate the successful deployment.

-The live link can be found here - https://bobrac3023.github.io/Project2-Quiz/

### Deployment from gitpod
-Site deployed from Gitpod using python http server

#### python3_http_server

-website viewed from Code Institute IDE Enviroment

#### website_code_ide_environment

-use gitpod commands to add, commit code to gitub repository

##### git_add_commit_command

-gitpod push command to push commited changes to github repository

##### git_push

## Credits
-Extra help to understand key Javascript scripts (https://www.youtube.com/watch?v=Hr5iLG7sUa0&list=PLu71SKxNbfoBuX3f4EOACle2y-tRC5Q37).
-Understand how to design the quiz (https://www.sitepoint.com/simple-javascript-quiz/).
-Understand var and const declarations (https://www.giraffeacademy.com/web-development/javascript/building-a-quiz/).

### Content
-How to design, structure and write code instructions taken from (https://www.youtube.com/watch?v=PBcqGxrr9g8).
-The icons in the footer and header were taken from Font Awesome.

### Media
-No media was used for this project.