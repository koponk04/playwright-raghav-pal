Chapter 1: Introduction
0:01
hello and welcome I am raghav from automationstepbystep.com and in this session we are going to go very basic
0:08
8 seconds
step by step and we are going to learn how do we create a page object model design project or framework with
0:16
16 seconds
playwright and this is going to be very easy and very interesting uh step number one is we will create a new folder and we will open that folder in our ID I am
Chapter 2: Step 1 - Create a new folder and open in IDE or Editor (like VS Code)
0:25
25 seconds
going to use vs code so I'm I'm going to do a complete project from scratch and in this project first we will create a
0:33
33 seconds
normal test I will do a test I will create a test on this link this website
0:41
41 seconds
the internet login so here we will create a demo test I will add a username a password and click
0:49
49 seconds
on login button and this is the link I am using I will keep all these notes all the links everything in the description of this video so you can also refer from
0:58
58 seconds
there so this is the link I'm going to use and first I will create a very simple test and then we will convert it into a page object model design
1:07
1 minute, 7 seconds
Source first step is we will create a new folder and open it in the IDE so I am going to my system here and
1:16
1 minute, 16 seconds
you can create a new folder anywhere I'm going to my e Drive projects
1:22
1 minute, 22 seconds
I have a folder called play right here I have my older folders older projects
1:30
1 minute, 30 seconds
here so I'm just going to create a new folder here and I will call it as
1:39
1 minute, 39 seconds
playwright form demo you can name it anything
1:46
1 minute, 46 seconds
and then I will go to my vs code so I have opened my vs code here and I can either go to file and then open the
1:55
1 minute, 55 seconds
folder from here or open from here or I'll just drag and drop the folder
2:02
2 minutes, 2 seconds
so I will drag and drop it on vs code and it is now opened here next step is
Chapter 3: Step 2 - Initialize a new Node.js project by running npm init -y to create a package.json file
2:11
2 minutes, 11 seconds
I will go to the terminal and to start a node project in this folder I will run the command npm init hyphen by
2:19
2 minutes, 19 seconds
so I will first open the terminal and here I will say and I am using a
2:28
2 minutes, 28 seconds
dark mode of vs code so if you go to the settings from here if you go to the settings you can see
2:35
2 minutes, 35 seconds
set the color theme and I am using this default dock
2:41
2 minutes, 41 seconds
okay so I will run the command npm init space hyphen y this will create
2:50
2 minutes, 50 seconds
a package.json file and it will also initialize a node project on this folder so now we can add the node libraries and
2:59
2 minutes, 59 seconds
packages and start any node project in this folder so you can see this package.json file is created now the next step is we will run the
Chapter 4: Step 3 - Install & Setup Playwright by running npm init playwright@latest
3:07
3 minutes, 7 seconds
command npm init playwright at the rate whatever version you want so if you want the latest version you can see latest or if you
3:15
3 minutes, 15 seconds
want a specific question you can give the version number here so anyways we are going to go with the latest so I will say here
3:23
3 minutes, 23 seconds
let me clear the terminal I will say npm in it playwrite
3:31
3 minutes, 31 seconds
at the rate latest
3:38
3 minutes, 38 seconds
so it is asking us do you want to use JavaScript or typescript as of now I will use
3:45
3 minutes, 45 seconds
JavaScript so you can use the arrow keys to go to that option and select by enter
3:52
3 minutes, 52 seconds
and it is asking where do you want to put the test so I'll just go with the tests folder and add a GitHub actions
4:00
4 minutes
workflow so here uh very recently I have created a video on what are GitHub actions so it is out of context not
4:08
4 minutes, 8 seconds
required here but just in case you want to know what are GitHub actions you can watch my video and for now I'll just say why so that I can show you what it is
4:17
4 minutes, 17 seconds
but it is not required for this particular session and then install predite browsers yes enter and now it will
4:25
4 minutes, 25 seconds
start installing the libraries and it is done and if I if you now check your
4:32
4 minutes, 32 seconds
package.json file you can see here we have playwright edit in the dependencies
4:39
4 minutes, 39 seconds
so step number three is done now we will create a login test so here
Chapter 5: Step 4 - Create a demo login test, can use Test Generator to record npx playwright codegen
4:46
4 minutes, 46 seconds
I'm going to my tests folder and you can see one sample test is already created I will create a new file
4:54
4 minutes, 54 seconds
I will call it as login Dot uh spec dot GS
5:04
5 minutes, 4 seconds
and here we can create a new test so you can manually create or you can also record using the code gen
5:11
5 minutes, 11 seconds
utility that is the test generator in playwright so to start recording we can run this command and PX playwright code
5:18
5 minutes, 18 seconds
gen so I will go to the terminal and say npx
5:27
5 minutes, 27 seconds
playwright code chain and hit enter
5:37
5 minutes, 37 seconds
so it will start the browser and also the test generator of the right inspector
5:45
5 minutes, 45 seconds
here so you can see two windows here this is the browser window and this is the playwright inspector uh if you want to if I can show you both the windows
5:53
5 minutes, 53 seconds
side by side I will click on this browser window and press the Windows key and the left key
6:03
6 minutes, 3 seconds
left Arrow key on my keyboard so that this window will be stacked docked on the left side and now I can select which
6:10
6 minutes, 10 seconds
window I want on the right side so this is playwrite inspector and then I can also adjust the sizes so now you can see side
6:18
6 minutes, 18 seconds
by side and here you can see recording is already on and whatever I will do on my browser it will get recorded here so let
6:27
6 minutes, 27 seconds
us go to this link I will copy the link and paste it here and hit enter and you can see it is
6:36
6 minutes, 36 seconds
getting recorded here I will then enter the username also you can see wherever I am taking my cursor it is showing me the locators of that
6:44
6 minutes, 44 seconds
element so username is Tom Smith
6:51
6 minutes, 51 seconds
password is this super secret password
7:00
7 minutes
and along with the exclamation mark and I will click on login and it is logged in and now I can
7:07
7 minutes, 7 seconds
click on this record to stop the recording and then I can copy this and you can also
7:15
7 minutes, 15 seconds
copy in for different platforms and languages like python Java etc for now we are using node.js just
7:23
7 minutes, 23 seconds
use the node.js test and copy this and paste it in my test here
7:31
7 minutes, 31 seconds
and our test is created okay I have shown this recorder in my separate session as well if you go to my website
7:40
7 minutes, 40 seconds
automation step by step.com and go to the playwright section playwright playlist which will
7:48
7 minutes, 48 seconds
take you to my YouTube playwright playlist so I think there is a session I recorded yes this is the one how to record test
7:57
7 minutes, 57 seconds
so here you can see all the other options as well just in case you wanted to want to see all the options with the code gen utility so see the code gen the
8:05
8 minutes, 5 seconds
recorder is still running to stop this you can either press Ctrl C here and then it will stop or you can just go
8:14
8 minutes, 14 seconds
to the browser and close the browser and you can see it is stopped end it has come out here
8:21
8 minutes, 21 seconds
okay so this is our test which is created it goes to the login page enters username enters password and then
8:31
8 minutes, 31 seconds
clicks on the login button so let us run and check this so to run the test I will use the command
Chapter 6: Step 5 - Run tests and check results - npx playwright test & npx playwright show-report
8:39
8 minutes, 39 seconds
npx playwright test and when you use this command npx Player test it will run all the files all the tests which are
8:47
8 minutes, 47 seconds
under the folder which is marked as the test directory in the playwright configuration file so let us check the
8:54
8 minutes, 54 seconds
playwright configuration file and here the test directory is tests
9:01
9 minutes, 1 second
okay so whatever tests are there under the tests folder will get executed if you say npx
9:09
9 minutes, 9 seconds
paywrite test but I just want to run the login dot spec.js file so I will say npx
9:16
9 minutes, 16 seconds
playwrite test and then I will say go to the tests folder and from here just run the
9:25
9 minutes, 25 seconds
login.spec.js file okay so it says no tests found uh let us see
9:34
9 minutes, 34 seconds
so what I'll do is I'll just under the tests folder I'm going to create one more folder called demo and I'm going to put my
9:43
9 minutes, 43 seconds
login.spec.js under the demo folder so you can see I have moved my
9:51
9 minutes, 51 seconds
login.spec.js under the demo folder which is under tests folder and here in the configuration file I will say the
9:59
9 minutes, 59 seconds
test directory is tests forward slash demo folder so now if I say npx playwrite test
10:08
10 minutes, 8 seconds
whatever is inside the demo folder will only get executed and here I only have my login dot spec file so let us go to
10:15
10 minutes, 15 seconds
the terminal and I will say I'll now just say npx playwright test
10:22
10 minutes, 22 seconds
and let us see if this works make sure that you have saved the configuration file
10:31
10 minutes, 31 seconds
and every file okay so some have passed uh let me check
10:41
10 minutes, 41 seconds
okay I think I did not save it before I started running so I will press Ctrl C to terminate the
10:49
10 minutes, 49 seconds
report server and I will run it again so now I have saved all my files let me now run this
10:56
10 minutes, 56 seconds
again in BX play right test and this time it should only run my login test yes it is running login test it is running three times because it is
11:05
11 minutes, 5 seconds
running on three browsers Chrome Firefox and Safari webkit and if you only want to run a single
11:14
11 minutes, 14 seconds
browser I will just show you how to do that so yes this time it is fine and you can also check the report by turning this
11:21
11 minutes, 21 seconds
command npx rewrite show report so I want to run on a single browser
11:28
11 minutes, 28 seconds
so I will say npx playwrite test and then I will say hyphen hyphen project
11:35
11 minutes, 35 seconds
equals chromium so this will now only run on Chrome browser and if you want to see the execution on a physical browser
11:43
11 minutes, 43 seconds
I can say hyphen hyphen headed headed means now our physical browser will come up and it will run there otherwise it
11:50
11 minutes, 50 seconds
always runs in a headless mode that is no browser comes up it runs in the background so this is the command
11:58
11 minutes, 58 seconds
and pxp write test hyphen hyphen project chromium hyphen hyphen headed okay so I'll run this and this time we
12:06
12 minutes, 6 seconds
should be able to see the test execution so it goes to the browser it was very fast it has done the login and just to
12:15
12 minutes, 15 seconds
check I can see the report using this command and PX playwright show report
12:21
12 minutes, 21 seconds
this starts the server and shows us the HTML report and you can see this is our test and it ran on the Chrome browser
12:29
12 minutes, 29 seconds
and everything is running fine okay and to stop the reporting server I can
12:36
12 minutes, 36 seconds
press Ctrl C on my keyboard and say y to terminate the job and I will clear the terminal so this is
12:45
12 minutes, 45 seconds
our test is running fine now let us start the process of converting our test into our page object model design so for
Chapter 7: Step 6 - Create new folder "pages" in your project, this will contain all page objects
12:53
12 minutes, 53 seconds
that we will create a folder called pages in our project and before I do that let me tell you why we are doing
13:01
13 minutes, 1 second
this so here if you see this test all our objects all the object locators all the test data
13:09
13 minutes, 9 seconds
all the test scripts actions everything is all is inside this single file this single test okay all our objects actions
13:19
13 minutes, 19 seconds
data test scripts everything is at a single place now let's say in future if something changes on this page let's say
13:26
13 minutes, 26 seconds
the locator of username changes or any other change in sequence or action then in case we are using that object let's
13:34
13 minutes, 34 seconds
say some object locator changed and we are using that object in 50 test cases we will have to go manually to all the 50 places all the 50 test cases and then
13:43
13 minutes, 43 seconds
change it there which will be a very time consuming manual process and it will not be very efficient so page object model design says that we should
13:52
13 minutes, 52 seconds
have separate class for each page let's say this is a login page we will have a separate class or login
14:00
14 minutes
page and in that class we will keep all the object locators of that page along with all the actions we do on those
14:07
14 minutes, 7 seconds
objects so for every page in our application we will have a separate class in our automation project and in
14:15
14 minutes, 15 seconds
that class we will keep its objects and the actions so that tomorrow if anything changes on this page we will only have
14:22
14 minutes, 22 seconds
to go to that Pages class and we will have to make the changes at a single location and it will be referred from there to everywhere wherever it is being
14:31
14 minutes, 31 seconds
used okay so let's do that I will go to my project folder and create a new folder called
14:38
14 minutes, 38 seconds
pages and it has gone inside my demo folder so I will drag and keep it outside so that
14:47
14 minutes, 47 seconds
it is directly under my project folder so you can see now it is here under my project folder and then
Chapter 8: Step 7 - Create a new file and class for each page e.g. login.js and LoginPage
14:56
14 minutes, 56 seconds
I will create a class and in a login page which will be there in a file called login.js so for every page we
15:04
15 minutes, 4 seconds
will create a separate class okay so I will inside the login inside the pages folder I will create a file
15:11
15 minutes, 11 seconds
called login.js and it is created here and in this file I will create a class
15:20
15 minutes, 20 seconds
login page so this is how we create a class in JavaScript I say class and the class name and then the curly bracket start and stop
15:30
15 minutes, 30 seconds
okay so we have created a class and now in this class we will create the
Chapter 9: Step 8 - In the class create element locators & action methods for login page
15:37
15 minutes, 37 seconds
object locators and the action methods for the login page so here
15:45
15 minutes, 45 seconds
on the login page we have we have to work with three objects that is username text box password text box and the login
15:53
15 minutes, 53 seconds
button so I can make variables I can say username
16:01
16 minutes, 1 second
and to make it me more meaningful I will say this is a text box so that anybody can understand this is a username text box then I will say
16:10
16 minutes, 10 seconds
password text box and then login which is a button
16:19
16 minutes, 19 seconds
and now I will say I will give it the value so I will add
16:27
16 minutes, 27 seconds
the locators here and I can just copy the locators from here so this is the username
16:39
16 minutes, 39 seconds
okay now see here
16:47
16 minutes, 47 seconds
I cannot directly use it like this because we are using this page and this page has to be passed from wherever we
16:57
16 minutes, 57 seconds
have started our test so you can see this page object is here and the same page object should be passed here to this class so for that I can create a
17:06
17 minutes, 6 seconds
Constructor I will say Constructor and as a argument of the Constructor I will take this page object and then inside the Constructor I
17:15
17 minutes, 15 seconds
will add all these locators and I will first say
17:24
17 minutes, 24 seconds
this Dot Page equals page now what does this mean is I am creating a class
17:31
17 minutes, 31 seconds
variable called page for this particular class and its value will be made equal to whatever comes in this Constructor
17:38
17 minutes, 38 seconds
which is this one okay so now I can say I can use page here
17:48
17 minutes, 48 seconds
and this also I'm using this keyboard to make them as a class variables okay
17:54
17 minutes, 54 seconds
and I'm just going to copy all these
18:09
18 minutes, 9 seconds
so this is the password and then this is for the
18:16
18 minutes, 16 seconds
login button and I am just copying the locators not the actions as of now okay these are just the locators
18:25
18 minutes, 25 seconds
okay you can also do a right click and say format document to correct all the formatting I can do this here as well
18:34
18 minutes, 34 seconds
format document okay so I have created a Constructor and
18:41
18 minutes, 41 seconds
inside the Constructor in the Constructor we are taking the page object and then we are also defining all our
18:49
18 minutes, 49 seconds
locators for all the objects that we need for login page okay now after this I also have to
18:57
18 minutes, 57 seconds
create methods which will do the action so here we have to do three actions that is enter username so I can create a
19:04
19 minutes, 4 seconds
function I can say enter username I can say enter username and we can give any name here
19:13
19 minutes, 13 seconds
and then I can create another function enter password
19:22
19 minutes, 22 seconds
and then one more function click on login
19:30
19 minutes, 30 seconds
so if we want we can create separate functions or Atomic functions Atomic function means one function is doing one
19:38
19 minutes, 38 seconds
action so we can do that or we can create a single function called login and we can add all the three steps and the username and a password and click on
19:46
19 minutes, 46 seconds
login there and it depends on our needs it depends on on the the complexity of the actions so if it is a very complex
19:54
19 minutes, 54 seconds
action and you believe that you should have a separate functions for each action you can create separate functions or if you believe that anybody can understand if you are just create a
20:02
20 minutes, 2 seconds
single function and add all the actions we can do that so I will now create a simple function called login and here
20:10
20 minutes, 10 seconds
I will add all these actions to enter username password and click on login we have to use async here
20:21
20 minutes, 21 seconds
and then here I will say a bit and I will call the username variable
20:29
20 minutes, 29 seconds
that is username text box and you can see I am getting Auto suggestion I can just select from this order suggestion box and press enter and it has Auto
20:38
20 minutes, 38 seconds
completed this dot username dot text box and then I will add the action which is dot fill and here I can give the
20:45
20 minutes, 45 seconds
username similarly or password I will say a weight
20:55
20 minutes, 55 seconds
this dot password text box dot fill and here I will keep the password value and
21:01
21 minutes, 1 second
then the next thing is login button and here the BL will say dot
21:08
21 minutes, 8 seconds
click okay now the next thing is I can give hard coded values here for username and
21:17
21 minutes, 17 seconds
password however it will uh not make the function reusable I can only use this
21:24
21 minutes, 24 seconds
function login with these hard-coded values of username and password and we don't want that we want that we can call this login function
21:33
21 minutes, 33 seconds
from any test and we can pass multiple values so the same function can work for a valid login test for an invalid login
21:40
21 minutes, 40 seconds
test or login with invalid credentials and it will work for all the values so for that instead of hard coding the values here I am going to take the
21:48
21 minutes, 48 seconds
values as arguments to this function I will take a value called username and I will also get a variable called
21:56
21 minutes, 56 seconds
password and whatever values comes in these variables will be passed here so I will pass username variable here
22:03
22 minutes, 3 seconds
and password variable here okay
22:10
22 minutes, 10 seconds
so let me show you and I will I can also uh hide this sidebar I am pressing Ctrl B on my keyboard
22:19
22 minutes, 19 seconds
so to hide the sidebar you can press Ctrl plus b or if you're on Mac you can press command plus b
22:28
22 minutes, 28 seconds
okay so this is our login page class now next step is so this is I have also put it here I will put all this in the
22:36
22 minutes, 36 seconds
description of this video and now next step is we have to import this class in our test
Chapter 10: Step 9 - In test file, import the page class, create instance of it, & use methods from LoginPage class
22:43
22 minutes, 43 seconds
class or the test script or the wherever our test file is there and then create an instance of the login page class so that we can use its methods in our test
22:53
22 minutes, 53 seconds
file so let us go to our test file which we which has our test that we created earlier and the
23:00
23 minutes
first thing is I have to import this class login page so I will say import and here in curly brackets I will give
23:08
23 minutes, 8 seconds
the class name which is login page
23:15
23 minutes, 15 seconds
and I will then give the location of the file so I will say from and I will say
23:21
23 minutes, 21 seconds
double dot forward slash so when I say single dot forward slash
23:28
23 minutes, 28 seconds
it is not finding any folder here and here it is finding the demo folder so I have to go one more step up I will say
23:35
23 minutes, 35 seconds
double dot forward slash again and yes now it is able to see the pages folder I will select pages and then forward slash
23:44
23 minutes, 44 seconds
login okay so now we have imported this and then I will also have to create a constant
23:53
23 minutes, 53 seconds
and create a instance of the class so for that I will say create a constant called login you
24:01
24 minutes, 1 second
can name it anything equals new login page so this is our class
24:09
24 minutes, 9 seconds
okay and just to check if everything is fine uh when you hover over this login page
24:17
24 minutes, 17 seconds
you press Ctrl on your keyboard and hover over this now it turns into a link and if I click this it should go to the
24:24
24 minutes, 24 seconds
login page class but it is not going so see when I click this it is actually going to this login page that means it
24:31
24 minutes, 31 seconds
is not yet exported or imported here and for that you will either have to export the module from here or I'll just I can
24:40
24 minutes, 40 seconds
just say here just before the class declaration I can say exports Dot
24:49
24 minutes, 49 seconds
login page equals so now it will be imported in the in this module when I say import login
24:58
24 minutes, 58 seconds
page and now if you press Ctrl and click on this login page you can see it is now getting going back
25:05
25 minutes, 5 seconds
to the login page class so this is a good way to find out that uh you have done the importing and object creation
25:14
25 minutes, 14 seconds
instance creation properly and one more thing if I run this this will fail because whenever we create a instance of
25:21
25 minutes, 21 seconds
a class like this new Under class name it will directly go to the class and call the Constructor and in the Constructor we are expecting the page
25:29
25 minutes, 29 seconds
object so unless I pass the page object which is this one it will throw an error so let me just pass it here and now it
25:37
25 minutes, 37 seconds
is done and now I can use this constant login this one and call all the methods of this class
25:46
25 minutes, 46 seconds
so I will say login now see here we are also going to this login page first before heading username
25:55
25 minutes, 55 seconds
password we first have to go here and if you want this also can be shifted to the login page class I can
26:02
26 minutes, 2 seconds
create one more function I will say async go to login page
26:11
26 minutes, 11 seconds
and here I will just paste this make sure that if you are using page it should be this Dot Page
26:19
26 minutes, 19 seconds
because we have to refer this page here okay now I will say here
26:27
26 minutes, 27 seconds
login Dot and you can see it is able to see all the functions I will say go to login page
26:33
26 minutes, 33 seconds
and then I will say login Dot login this is the method and we know that this method takes two arguments
26:42
26 minutes, 42 seconds
that is username and password values so the username value is Tom Smith
26:49
26 minutes, 49 seconds
and the password value is super secret password
26:57
26 minutes, 57 seconds
and that's it now this is our test this is our entire test if you want you can delete all this or for now I will comment this I am selecting everything
27:05
27 minutes, 5 seconds
and pressing Ctrl and forward slash on my keyboard to comment comment all this once I will test and check everything is fine then I can delete all this
27:14
27 minutes, 14 seconds
so you can now see the first thing is our test becomes very clean and clear anybody can look here and understand
27:21
27 minutes, 21 seconds
what is what it's doing it is first going to the login page then it is doing login with these credentials and thus
27:28
27 minutes, 28 seconds
major advantage here is now all our objects all the actions of login page all are here at a single location of
27:37
27 minutes, 37 seconds
login page class tomorrow if anything changes on this page let's say the locator of username changes we will just have to come to this class and make the
27:45
27 minutes, 45 seconds
changes and it will be referred from here to everywhere wherever it is used
27:52
27 minutes, 52 seconds
so this is done and this is our test class where we have imported the login page class and this is how we have
28:01
28 minutes, 1 second
added our functions and now finally we will run and check everything is working fine so let's go to our terminal
Chapter 11: Step 10 - Run the test npx playwright test and check results
28:10
28 minutes, 10 seconds
and I will press the up Arrow to go back to the last command and yes this is our Command to run the
28:19
28 minutes, 19 seconds
login.spec file let us now see if it runs fine fine and everything is yeah okay I think some error let me check
28:29
28 minutes, 29 seconds
it started the test but then it failed so here uh okay I think this is a problem here
28:37
28 minutes, 37 seconds
it says what is the issue let me check
28:51
28 minutes, 51 seconds
so here there is some problem on this go to login page
29:01
29 minutes, 1 second
and let us just very quickly check so here we created the constant
29:08
29 minutes, 8 seconds
and then we are going to this we can also control and click on this so that it goes back here
29:16
29 minutes, 16 seconds
and here we are saying this Dot Page dot go to so this looks fine
29:25
29 minutes, 25 seconds
okay I think uh we should have used a weight here because we have used async here so
29:33
29 minutes, 33 seconds
along with async we use a weight let us try with that
29:41
29 minutes, 41 seconds
and I will save and run again
29:52
29 minutes, 52 seconds
and check so this has started the execution and yes this time it was passed we can also
30:01
30 minutes, 1 second
confirm by looking at our reports so if I say npx playwright show report
30:10
30 minutes, 10 seconds
and this is our report this is our test and here it went to the URL
30:17
30 minutes, 17 seconds
then it entered username and password and then clicked on the login button and then finally it
30:25
30 minutes, 25 seconds
closed the browser so this is all working fine and you can see this is our test now which is very clean and it is
30:34
30 minutes, 34 seconds
now implemented with page object model design okay and I will also put this project on
Chapter 12: Upload project on GitHub
30:41
30 minutes, 41 seconds
GitHub and give you the link in the description or let me do it now I'll I will go to my GitHub account
30:50
30 minutes, 50 seconds
and here I will create a new Repository I will call it as
30:58
30 minutes, 58 seconds
layrite each object model and create the Repository
31:08
31 minutes, 8 seconds
and this is our repository link I can copy it from here and here on vs code I will first create
31:17
31 minutes, 17 seconds
a DOT get ignore file which is already created so in the dot get ignore file we put the location name and location of the folders or files that we do not want
31:26
31 minutes, 26 seconds
to upload to the repository and by default you should not upload node modules and any results or reports folder because it will make the
31:33
31 minutes, 33 seconds
repository very bulky and make the process uh very slow so this is already here in case you also want to do this
31:41
31 minutes, 41 seconds
make sure that you create a DOT get ignore file and then I will go to the source code management Source control
31:50
31 minutes, 50 seconds
section and I will say initialize Repository and you can see all this has come here there are nine changes which are
31:58
31 minutes, 58 seconds
uncommitted so I will say this is my first commit and commit the changes
32:06
32 minutes, 6 seconds
so the changes are committed and you can see everything has gone from here and here too there is nothing which is shown
32:13
32 minutes, 13 seconds
as uncommitted so all these changes are committed but not yet pushed to the repository so for doing that first I will have to add the link of my
32:21
32 minutes, 21 seconds
repository as remote here I am pressing Ctrl shift p and so I can also just go to
32:30
32 minutes, 30 seconds
uh command palette from here or Ctrl shift p and I will say git add remote
32:39
32 minutes, 39 seconds
so here it is get at remote I will add the URL sorry this is the URL I will copy it
32:51
32 minutes, 51 seconds
and then I will give the name I will say this is playwright
32:59
32 minutes, 59 seconds
underscore page object model and then
33:07
33 minutes, 7 seconds
I can publish it so this is done
33:15
33 minutes, 15 seconds
I can go and check on my Repository and yes it has come here so we have got
33:23
33 minutes, 23 seconds
our tests folder and this is our demo folder and this is our test here
33:31
33 minutes, 31 seconds
and then if I check the pages folder we have our login page class here so uh
33:39
33 minutes, 39 seconds
this is the link to my project just in case you want to copy or clone my project you can do that I will give all
33:46
33 minutes, 46 seconds
these links in the description of this video and all the notes will be there so please do Hands-On let me know if you face any issues you can write your
33:55
33 minutes, 55 seconds
questions on messages in the comment section I read all my comments and I will reply to you and I hope this was very useful thank you for watching and
34:03
34 minutes, 3 seconds
never stop learning
