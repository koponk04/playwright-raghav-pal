# Chapter 1: Introduction

0:01 hello and welcome I am raghav from automationstepbystep.com and in this session we are going to go very basic

0:08 step by step and we are going to learn how do we create a page object model design project or framework with

0:16 playwright and this is going to be very easy and very interesting uh step number one is we will create a new folder and we will open that folder in our ID I am


# Chapter 2: Step 1 - Create a new folder and open in IDE or Editor (like VS Code)

0:25 going to use vs code so I'm I'm going to do a complete project from scratch and in this project first we will create a

0:33 normal test I will do a test I will create a test on this link this website

0:41 the internet login so here we will create a demo test I will add a username a password and click

0:49 on login button and this is the link I am using I will keep all these notes all the links everything in the description of this video so you can also refer from

0:58 there so this is the link I'm going to use and first I will create a very simple test and then we will convert it into a page object model design

1:07 Source first step is we will create a new folder and open it in the IDE so I am going to my system here and

1:16 you can create a new folder anywhere I'm going to my e Drive projects

1:22 I have a folder called play right here I have my older folders older projects

1:30 here so I'm just going to create a new folder here and I will call it as

1:39 playwright form demo you can name it anything

1:46 and then I will go to my vs code so I have opened my vs code here and I can either go to file and then open the

1:55 folder from here or open from here or I'll just drag and drop the folder

2:02 so I will drag and drop it on vs code and it is now opened here next step is


# Chapter 3: Step 2 - Initialize a new Node.js project by running npm init -y to create a package.json file

2:11 I will go to the terminal and to start a node project in this folder I will run the command npm init hyphen by

2:19 so I will first open the terminal and here I will say and I am using a

2:28 dark mode of vs code so if you go to the settings from here if you go to the settings you can see

2:35 set the color theme and I am using this default dock

2:41 okay so I will run the command npm init space hyphen y this will create

2:50 a package.json file and it will also initialize a node project on this folder so now we can add the node libraries and

2:59 packages and start any node project in this folder so you can see this package.json file is created now the next step is we will run the


# Chapter 4: Step 3 - Install & Setup Playwright by running npm init playwright@latest

3:07 command npm init playwright at the rate whatever version you want so if you want the latest version you can see latest or if you

3:15 want a specific question you can give the version number here so anyways we are going to go with the latest so I will say here

3:23 let me clear the terminal I will say npm in it playwrite

3:31 at the rate latest

3:38 so it is asking us do you want to use JavaScript or typescript as of now I will use

3:45 JavaScript so you can use the arrow keys to go to that option and select by enter

3:52 and it is asking where do you want to put the test so I'll just go with the tests folder and add a GitHub actions

4:00 workflow so here uh very recently I have created a video on what are GitHub actions so it is out of context not

4:08 required here but just in case you want to know what are GitHub actions you can watch my video and for now I'll just say why so that I can show you what it is

4:17 but it is not required for this particular session and then install predite browsers yes enter and now it will

4:25 start installing the libraries and it is done and if I if you now check your

4:32 package.json file you can see here we have playwright edit in the dependencies

4:39 so step number three is done now we will create a login test so here


# Chapter 5: Step 4 - Create a demo login test, can use Test Generator to record npx playwright codegen

4:46 I'm going to my tests folder and you can see one sample test is already created I will create a new file

4:54 I will call it as login Dot uh spec dot GS

5:04 and here we can create a new test so you can manually create or you can also record using the code gen

5:11 utility that is the test generator in playwright so to start recording we can run this command and PX playwright code

5:18 gen so I will go to the terminal and say npx

5:27 playwright code chain and hit enter

5:37 so it will start the browser and also the test generator of the right inspector

5:45 here so you can see two windows here this is the browser window and this is the playwright inspector uh if you want to if I can show you both the windows

5:53 side by side I will click on this browser window and press the Windows key and the left key

6:03 left Arrow key on my keyboard so that this window will be stacked docked on the left side and now I can select which

6:10 window I want on the right side so this is playwrite inspector and then I can also adjust the sizes so now you can see side

6:18 by side and here you can see recording is already on and whatever I will do on my browser it will get recorded here so let

6:27 us go to this link I will copy the link and paste it here and hit enter and you can see it is

6:36 getting recorded here I will then enter the username also you can see wherever I am taking my cursor it is showing me the locators of that

6:44 element so username is Tom Smith

6:51 password is this super secret password

7:00 and along with the exclamation mark and I will click on login and it is logged in and now I can

7:07 click on this record to stop the recording and then I can copy this and you can also

7:15 copy in for different platforms and languages like python Java etc for now we are using node.js just

7:23 use the node.js test and copy this and paste it in my test here

7:31 and our test is created okay I have shown this recorder in my separate session as well if you go to my website

7:40 automation step by step.com and go to the playwright section playwright playlist which will

7:48 take you to my YouTube playwright playlist so I think there is a session I recorded yes this is the one how to record test

7:57 so here you can see all the other options as well just in case you wanted to want to see all the options with the code gen utility so see the code gen the

8:05 recorder is still running to stop this you can either press Ctrl C here and then it will stop or you can just go

8:14 to the browser and close the browser and you can see it is stopped end it has come out here

8:21 okay so this is our test which is created it goes to the login page enters username enters password and then

8:31 clicks on the login button so let us run and check this so to run the test I will use the command


# Chapter 6: Step 5 - Run tests and check results - npx playwright test & npx playwright show-report

8:39 npx playwright test and when you use this command npx Player test it will run all the files all the tests which are

8:47 under the folder which is marked as the test directory in the playwright configuration file so let us check the

8:54 playwright configuration file and here the test directory is tests

9:01 okay so whatever tests are there under the tests folder will get executed if you say npx

9:09 paywrite test but I just want to run the login dot spec.js file so I will say npx

9:16 playwrite test and then I will say go to the tests folder and from here just run the

9:25 login.spec.js file okay so it says no tests found uh let us see

9:34 so what I'll do is I'll just under the tests folder I'm going to create one more folder called demo and I'm going to put my

9:43 login.spec.js under the demo folder so you can see I have moved my

9:51 login.spec.js under the demo folder which is under tests folder and here in the configuration file I will say the

9:59 test directory is tests forward slash demo folder so now if I say npx playwrite test

10:08 whatever is inside the demo folder will only get executed and here I only have my login dot spec file so let us go to

10:15 the terminal and I will say I'll now just say npx playwright test

10:22 and let us see if this works make sure that you have saved the configuration file

10:31 and every file okay so some have passed uh let me check

10:41 okay I think I did not save it before I started running so I will press Ctrl C to terminate the

10:49 report server and I will run it again so now I have saved all my files let me now run this

10:56 again in BX play right test and this time it should only run my login test yes it is running login test it is running three times because it is

11:05 running on three browsers Chrome Firefox and Safari webkit and if you only want to run a single

11:14 browser I will just show you how to do that so yes this time it is fine and you can also check the report by turning this

11:21 command npx rewrite show report so I want to run on a single browser

11:28 so I will say npx playwrite test and then I will say hyphen hyphen project

11:35 equals chromium so this will now only run on Chrome browser and if you want to see the execution on a physical browser

11:43 I can say hyphen hyphen headed headed means now our physical browser will come up and it will run there otherwise it

11:50 always runs in a headless mode that is no browser comes up it runs in the background so this is the command

11:58 and pxp write test hyphen hyphen project chromium hyphen hyphen headed okay so I'll run this and this time we

12:06 should be able to see the test execution so it goes to the browser it was very fast it has done the login and just to

12:15 check I can see the report using this command and PX playwright show report

12:21 this starts the server and shows us the HTML report and you can see this is our test and it ran on the Chrome browser

12:29 and everything is running fine okay and to stop the reporting server I can

12:36 press Ctrl C on my keyboard and say y to terminate the job and I will clear the terminal so this is

12:45 our test is running fine now let us start the process of converting our test into our page object model design so for


# Chapter 7: Step 6 - Create new folder "pages" in your project, this will contain all page objects

12:53 that we will create a folder called pages in our project and before I do that let me tell you why we are doing

13:01 this so here if you see this test all our objects all the object locators all the test data

13:09 all the test scripts actions everything is all is inside this single file this single test okay all our objects actions

13:19 data test scripts everything is at a single place now let's say in future if something changes on this page let's say

13:26 the locator of username changes or any other change in sequence or action then in case we are using that object let's

13:34 say some object locator changed and we are using that object in 50 test cases we will have to go manually to all the 50 places all the 50 test cases and then

13:43 change it there which will be a very time consuming manual process and it will not be very efficient so page object model design says that we should

13:52 have separate class for each page let's say this is a login page we will have a separate class or login

14:00 page and in that class we will keep all the object locators of that page along with all the actions we do on those

14:07 objects so for every page in our application we will have a separate class in our automation project and in

14:15 that class we will keep its objects and the actions so that tomorrow if anything changes on this page we will only have

14:22 to go to that Pages class and we will have to make the changes at a single location and it will be referred from there to everywhere wherever it is being

14:31 used okay so let's do that I will go to my project folder and create a new folder called

14:38 pages and it has gone inside my demo folder so I will drag and keep it outside so that

14:47 it is directly under my project folder so you can see now it is here under my project folder and then


# Chapter 8: Step 7 - Create a new file and class for each page e.g. login.js and LoginPage

14:56 I will create a class and in a login page which will be there in a file called login.js so for every page we

15:04 will create a separate class okay so I will inside the login inside the pages folder I will create a file

15:11 called login.js and it is created here and in this file I will create a class

15:20 login page so this is how we create a class in JavaScript I say class and the class name and then the curly bracket start and stop

15:30 okay so we have created a class and now in this class we will create the


# Chapter 9: Step 8 - In the class create element locators & action methods for login page

15:37 object locators and the action methods for the login page so here

15:45 on the login page we have we have to work with three objects that is username text box password text box and the login

15:53 button so I can make variables I can say username

16:01 and to make it me more meaningful I will say this is a text box so that anybody can understand this is a username text box then I will say

16:10 password text box and then login which is a button

16:19 and now I will say I will give it the value so I will add

16:27 the locators here and I can just copy the locators from here so this is the username

16:39 okay now see here

16:47 I cannot directly use it like this because we are using this page and this page has to be passed from wherever we

16:57 have started our test so you can see this page object is here and the same page object should be passed here to this class so for that I can create a

17:06 Constructor I will say Constructor and as a argument of the Constructor I will take this page object and then inside the Constructor I

17:15 will add all these locators and I will first say

17:24 this Dot Page equals page now what does this mean is I am creating a class

17:31 variable called page for this particular class and its value will be made equal to whatever comes in this Constructor

17:38 which is this one okay so now I can say I can use page here

17:48 and this also I'm using this keyboard to make them as a class variables okay

17:54 and I'm just going to copy all these

18:09 so this is the password and then this is for the

18:16 login button and I am just copying the locators not the actions as of now okay these are just the locators

18:25 okay you can also do a right click and say format document to correct all the formatting I can do this here as well

18:34 format document okay so I have created a Constructor and

18:41 inside the Constructor in the Constructor we are taking the page object and then we are also defining all our

18:49 locators for all the objects that we need for login page okay now after this I also have to

18:57 create methods which will do the action so here we have to do three actions that is enter username so I can create a

19:04 function I can say enter username I can say enter username and we can give any name here

19:13 and then I can create another function enter password

19:22 and then one more function click on login

19:30 so if we want we can create separate functions or Atomic functions Atomic function means one function is doing one

19:38 action so we can do that or we can create a single function called login and we can add all the three steps and the username and a password and click on

19:46 login there and it depends on our needs it depends on on the the complexity of the actions so if it is a very complex

19:54 action and you believe that you should have a separate functions for each action you can create separate functions or if you believe that anybody can understand if you are just create a

20:02 single function and add all the actions we can do that so I will now create a simple function called login and here

20:10 I will add all these actions to enter username password and click on login we have to use async here

20:21 and then here I will say a bit and I will call the username variable

20:29 that is username text box and you can see I am getting Auto suggestion I can just select from this order suggestion box and press enter and it has Auto

20:38 completed this dot username dot text box and then I will add the action which is dot fill and here I can give the

20:45 username similarly or password I will say a weight

20:55 this dot password text box dot fill and here I will keep the password value and

21:01 then the next thing is login button and here the BL will say dot

21:08 click okay now the next thing is I can give hard coded values here for username and

21:17 password however it will uh not make the function reusable I can only use this

21:24 function login with these hard-coded values of username and password and we don't want that we want that we can call this login function

21:33 from any test and we can pass multiple values so the same function can work for a valid login test for an invalid login

21:40 test or login with invalid credentials and it will work for all the values so for that instead of hard coding the values here I am going to take the

21:48 values as arguments to this function I will take a value called username and I will also get a variable called

21:56 password and whatever values comes in these variables will be passed here so I will pass username variable here

22:03 and password variable here okay

22:10 so let me show you and I will I can also uh hide this sidebar I am pressing Ctrl B on my keyboard

22:19 so to hide the sidebar you can press Ctrl plus b or if you're on Mac you can press command plus b

22:28 okay so this is our login page class now next step is so this is I have also put it here I will put all this in the

22:36 description of this video and now next step is we have to import this class in our test


# Chapter 10: Step 9 - In test file, import the page class, create instance of it, & use methods from LoginPage class

22:43 class or the test script or the wherever our test file is there and then create an instance of the login page class so that we can use its methods in our test

22:53 file so let us go to our test file which we which has our test that we created earlier and the

23:00 first thing is I have to import this class login page so I will say import and here in curly brackets I will give

23:08 the class name which is login page

23:15 and I will then give the location of the file so I will say from and I will say

23:21 double dot forward slash so when I say single dot forward slash

23:28 it is not finding any folder here and here it is finding the demo folder so I have to go one more step up I will say

23:35 double dot forward slash again and yes now it is able to see the pages folder I will select pages and then forward slash

23:44 login okay so now we have imported this and then I will also have to create a constant

23:53 and create a instance of the class so for that I will say create a constant called login you

24:01 can name it anything equals new login page so this is our class

24:09 okay and just to check if everything is fine uh when you hover over this login page

24:17 you press Ctrl on your keyboard and hover over this now it turns into a link and if I click this it should go to the

24:24 login page class but it is not going so see when I click this it is actually going to this login page that means it

24:31 is not yet exported or imported here and for that you will either have to export the module from here or I'll just I can

24:40 just say here just before the class declaration I can say exports Dot

24:49 login page equals so now it will be imported in the in this module when I say import login

24:58 page and now if you press Ctrl and click on this login page you can see it is now getting going back

25:05 to the login page class so this is a good way to find out that uh you have done the importing and object creation

25:14 instance creation properly and one more thing if I run this this will fail because whenever we create a instance of

25:21 a class like this new Under class name it will directly go to the class and call the Constructor and in the Constructor we are expecting the page

25:29 object so unless I pass the page object which is this one it will throw an error so let me just pass it here and now it

25:37 is done and now I can use this constant login this one and call all the methods of this class

25:46 so I will say login now see here we are also going to this login page first before heading username

25:55 password we first have to go here and if you want this also can be shifted to the login page class I can

26:02 create one more function I will say async go to login page

26:11 and here I will just paste this make sure that if you are using page it should be this Dot Page

26:19 because we have to refer this page here okay now I will say here

26:27 login Dot and you can see it is able to see all the functions I will say go to login page

26:33 and then I will say login Dot login this is the method and we know that this method takes two arguments

26:42 that is username and password values so the username value is Tom Smith

26:49 and the password value is super secret password

26:57 and that's it now this is our test this is our entire test if you want you can delete all this or for now I will comment this I am selecting everything

27:05 and pressing Ctrl and forward slash on my keyboard to comment comment all this once I will test and check everything is fine then I can delete all this

27:14 so you can now see the first thing is our test becomes very clean and clear anybody can look here and understand

27:21 what is what it's doing it is first going to the login page then it is doing login with these credentials and thus

27:28 major advantage here is now all our objects all the actions of login page all are here at a single location of

27:37 login page class tomorrow if anything changes on this page let's say the locator of username changes we will just have to come to this class and make the

27:45 changes and it will be referred from here to everywhere wherever it is used

27:52 so this is done and this is our test class where we have imported the login page class and this is how we have

28:01 added our functions and now finally we will run and check everything is working fine so let's go to our terminal


# Chapter 11: Step 10 - Run the test npx playwright test and check results

28:10 and I will press the up Arrow to go back to the last command and yes this is our Command to run the

28:19 login.spec file let us now see if it runs fine fine and everything is yeah okay I think some error let me check

28:29 it started the test but then it failed so here uh okay I think this is a problem here

28:37 it says what is the issue let me check

28:51 so here there is some problem on this go to login page

29:01 and let us just very quickly check so here we created the constant

29:08 and then we are going to this we can also control and click on this so that it goes back here

29:16 and here we are saying this Dot Page dot go to so this looks fine

29:25 okay I think uh we should have used a weight here because we have used async here so

29:33 along with async we use a weight let us try with that

29:41 and I will save and run again

29:52 and check so this has started the execution and yes this time it was passed we can also

30:01 confirm by looking at our reports so if I say npx playwright show report

30:10 and this is our report this is our test and here it went to the URL

30:17 then it entered username and password and then clicked on the login button and then finally it

30:25 closed the browser so this is all working fine and you can see this is our test now which is very clean and it is

30:34 now implemented with page object model design okay and I will also put this project on


# Chapter 12: Upload project on GitHub

30:41 GitHub and give you the link in the description or let me do it now I'll I will go to my GitHub account

30:50 and here I will create a new Repository I will call it as

30:58 layrite each object model and create the Repository

31:08 and this is our repository link I can copy it from here and here on vs code I will first create

31:17 a DOT get ignore file which is already created so in the dot get ignore file we put the location name and location of the folders or files that we do not want

31:26 to upload to the repository and by default you should not upload node modules and any results or reports folder because it will make the

31:33 repository very bulky and make the process uh very slow so this is already here in case you also want to do this

31:41 make sure that you create a DOT get ignore file and then I will go to the source code management Source control

31:50 section and I will say initialize Repository and you can see all this has come here there are nine changes which are

31:58 uncommitted so I will say this is my first commit and commit the changes

32:06 so the changes are committed and you can see everything has gone from here and here too there is nothing which is shown

32:13 as uncommitted so all these changes are committed but not yet pushed to the repository so for doing that first I will have to add the link of my

32:21 repository as remote here I am pressing Ctrl shift p and so I can also just go to

32:30 uh command palette from here or Ctrl shift p and I will say git add remote

32:39 so here it is get at remote I will add the URL sorry this is the URL I will copy it

32:51 and then I will give the name I will say this is playwright

32:59 underscore page object model and then

33:07 I can publish it so this is done

33:15 I can go and check on my Repository and yes it has come here so we have got

33:23 our tests folder and this is our demo folder and this is our test here

33:31 and then if I check the pages folder we have our login page class here so uh

33:39 this is the link to my project just in case you want to copy or clone my project you can do that I will give all

33:46 these links in the description of this video and all the notes will be there so please do Hands-On let me know if you face any issues you can write your

33:55 questions on messages in the comment section I read all my comments and I will reply to you and I hope this was very useful thank you for watching and

34:03 never stop learning
