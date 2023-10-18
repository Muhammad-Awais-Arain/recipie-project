# LUBackendAutomation

Step 1:
#Clone this Repo

#####For Running Cypress Project
Step 2: 
Cd LU_Backend_Automation_Cypress

Step 3:
npm init

Step 4:
npm install cypress --save-dev

Step 5:
npx cypress open

Note:
If you want to change the backend then simply follow these steps,
1) Go to command.js file in Cypress folder.
2) Search websiteLink() function
3) Give the backend link in which you want the script to be run.

Make sure to use your own backend E-mail and password, You can change it by going to the Command.js
2) Search Login() funtion.
3)Change the e-mail and password.



##### To Run Python Scripts

Step 1)
Go to Chrome > Setting > About Chrome > Update Chrome to the latest Version
Like Version 112.0.5615.138 (Official Build) (64-bit) and restart chrome browser

Step 2)
After this, go to "https://chromedriver.chromium.org/downloads" and download the version nearest to 
your chrome version LIKE ChromeDriver 112.0.5615.49 and replace it with the Chromedriver in LU AUTOMATION SCRIPTS folder

Step 3)
After this, open the folder and change your directory to LU AUTOMATION SCRIPTS and run this command

pip install -r requirements.txt 

Step 4)
To run any specific pytest file i.e, any file starting with the name test_etc.py, do this in that files folder:
pytest test_filename.py and hit enter

Step 5)
To simply run all files, do this:
python Start_Automation.py ; it'll show a UI where you can click on any file you want to run.

 

