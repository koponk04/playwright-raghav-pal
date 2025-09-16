Chapter 1: Introduction
0:00
hello and welcome i'm raghav and today we are going to start with the installation process of playwright and this is going to be very easy and very
0:09
9 seconds
interesting and i will go very basic step by step and we'll start from scratch so we are going to see what are the prerequisites what all we need
0:17
17 seconds
before installing playwright and then we will see how to install playwright step by step and i will have a link for a
0:25
25 seconds
quiz in the description of this video so you can test your knowledge you can take the quiz and do let me know your score in the comment section and if you have
0:33
33 seconds
any questions any doubts any technical or general question you can always let me know in the comments section below i read all my messages and i will reply to
0:42
42 seconds
you and if you find the pace of this video slow you can always go to the player setting and increase the speed from there so with this let's get
Chapter 2: Prerequisites
0:51
51 seconds
started and let us see what are the prerequisites so uh we know that we can install playwright we can use playwright
0:59
59 seconds
with different languages and platforms and in the last video i have shown you all the four implementations or
1:06
1 minute, 6 seconds
libraries of playwright so again if i take you to the playwright website you can see we have node.js
1:14
1 minute, 14 seconds
pythonjava.net and if we get node.js we can use javascript or typescript so in this session i'm going to use the
1:22
1 minute, 22 seconds
node.js implementation so for that we should have node.js on our system and for that you can just go and check so if
1:30
1 minute, 30 seconds
you go to your command prompt on windows and if you are on mac or linux you can go to the terminal and run
1:38
1 minute, 38 seconds
the command npm space hyphen v or hyphen hyphen version it will show you if node is installed it
1:47
1 minute, 47 seconds
will show you the package of node or you should say node space hyphen hyphen version first
1:55
1 minute, 55 seconds
so you can see the version of node.js and npm is the node package manager which gets installed along with node so
2:03
2 minutes, 3 seconds
you should run both of these command and check if you are getting the version number and in case you are getting something like command not found or you're not getting the version that
2:11
2 minutes, 11 seconds
means node.js is not installed or not set up on your system and if you guess see that you can go to your browser
2:18
2 minutes, 18 seconds
and just say uh node.js download and this will take you to the node.js
2:26
2 minutes, 26 seconds
download website and node.js website and here you can get the installer for your operating system whether you are on
2:33
2 minutes, 33 seconds
windows mac or any other operating system you can get linux as well as here and then you can run the installer and
2:41
2 minutes, 41 seconds
node.js will be installed on your system and after installing open a new command prompt don't choose the same session of
2:48
2 minutes, 48 seconds
your command or terminal open a new command prompt on new terminal and then again run the commands node space hyphen v and npm space hyphen v or npm space
2:57
2 minutes, 57 seconds
hyphen iphone version and check if node is installed so this was the first prerequisite the second prerequisite is
3:04
3 minutes, 4 seconds
the ide that is integrated development environment now you can use any ide where you can create a node project and
3:12
3 minutes, 12 seconds
you can use javascript or typescript languages but i will prefer that you go with vs code and vs code it will be very
3:20
3 minutes, 20 seconds
easy there is also an extension for a playwright in vs code but you are free to use any ide where you can create a node project and you can use javascript
3:28
3 minutes, 28 seconds
or typescript now if you have no preference and even if you are a complete beginner with a vs code i will
3:35
3 minutes, 35 seconds
suggest that you use vs code and for that you can go on my website that is automation step by step dot com
3:44
3 minutes, 44 seconds
and here let me show you here this is my website automation step by step dot com and here
3:52
3 minutes, 52 seconds
uh you can go to editors or ides and here you will see
3:59
3 minutes, 59 seconds
there is a playlist for visual studio code and this will take you to my youtube playlist of vs code and here you can watch the first two videos what is
4:08
4 minutes, 8 seconds
vs code and learn vs code in seven steps both on windows and mac and this will be enough for you to get started with vs code so
4:16
4 minutes, 16 seconds
if you are completely new you can watch these two videos i will also have the links in the description of this video and then you are you will be good with
4:25
4 minutes, 25 seconds
the prerequisites so these are the two prerequisites we need for a playwright and once you have both of these we will go to the installation
Chapter 3: How to install Playwright
4:34
4 minutes, 34 seconds
steps now there are two ways we can install vs code or we can install playwright on vs code or
4:42
4 minutes, 42 seconds
you know any ide that you are using the first one is from the command line we can install playwright
4:51
4 minutes, 51 seconds
as npm package using commands and the second option is using vs code extension and this will be applicable only if you are using vs code
5:00
5 minutes
or visual studio code so let us see the first option first that is installing playwright as npm package
Chapter 4: Option 1 - using node commands
5:09
5 minutes, 9 seconds
using commands and here step number one is we will create a new folder and then open the folder in vs code so let's do
5:17
5 minutes, 17 seconds
that i will go to any folder or any location and create a new folder now in my case
5:25
5 minutes, 25 seconds
i'll go i'm on windows you can follow the same steps on mac as well or any operating system you are using so in my
5:32
5 minutes, 32 seconds
case i keep all my projects in the e drive under projects folder so i will go here and i will create a new folder
5:39
5 minutes, 39 seconds
first you can press ctrl shift n or command shift n for mac to create a new folder i'll just
5:46
5 minutes, 46 seconds
do it manually and here you can give the name so let's say i will say i'll give the name
5:54
5 minutes, 54 seconds
i'll say this is playwright underscore
6:03
6 minutes, 3 seconds
automation you can give any name to the folder and now the next step is we have to open this
6:11
6 minutes, 11 seconds
folder in vs code so open your bs code so i will just open my vs code visual studio code
6:19
6 minutes, 19 seconds
and here so this is the get started window if you don't get this you can
6:28
6 minutes, 28 seconds
always go to help and you will see this get started option here and from here we have an option to open
6:36
6 minutes, 36 seconds
folder so you can use this option or you can go to the file menu and here as well we have a option to open folder
6:45
6 minutes, 45 seconds
you can go from here or the third way is you can directly drag and drop the folder on vs code so let me do that i
6:53
6 minutes, 53 seconds
will just drag and drop my playwright automation folder on vs code
7:01
7 minutes, 1 second
so you can see it has opened it will ask you do you trust the folder and the authors i'll just say yes and the folder is now
7:09
7 minutes, 9 seconds
available here and as of now it's just a simple folder an empty folder let me open this folder and show you there's nothing inside this folder it's an empty
7:16
7 minutes, 16 seconds
folder as of now so we have done step number one now step number two is we will go to the terminal
7:24
7 minutes, 24 seconds
and then we will run the command npm init playwright at the red at the rate latest now i will show you what does this mean so uh you can go to the
7:33
7 minutes, 33 seconds
terminal within vs code or you can also do this from outside vs code if you go to your command line or terminal from outside bs code then you will first have
7:41
7 minutes, 41 seconds
to navigate to this folder your project folder but the easier way is you can directly go to vs code and go to this
7:49
7 minutes, 49 seconds
menu terminal and select new terminal you can also press ctrl plus shift plus back to key
7:56
7 minutes, 56 seconds
back to key is the key on the top or left of your keyboard just below the escape key or i think the other shortcut
8:04
8 minutes, 4 seconds
is if you press control plus j on your keyboard control plus j it will also open terminals you can see
8:11
8 minutes, 11 seconds
it opens a terminal window now you can increase the size of the window you can drag and increase or decrease
8:18
8 minutes, 18 seconds
the size or you can press this top arrow key to make it full screen so it will maximize
8:26
8 minutes, 26 seconds
the terminal panel and now i can write my commands also if you see here it opens the terminal on the
8:34
8 minutes, 34 seconds
same folder on the project folder that you have opened on vs code so that's what i said if you are running the command from outside vs code
8:43
8 minutes, 43 seconds
terminal then you will have to first navigate to this folder whatever is your project folder and then you can run the commands so it's better that we use the
8:51
8 minutes, 51 seconds
inbuilt terminal of vs code now the command is npm init npm init
8:58
8 minutes, 58 seconds
playwright at the rate latest now you can give a specific version here you can say at the rate and
9:06
9 minutes, 6 seconds
use some specific version like you know uh 9.0.0 or any version that you want but if you want the latest version you can
9:14
9 minutes, 14 seconds
just say npm init play right at the right at the right latest here the other way is to create a node project we can just run
9:23
9 minutes, 23 seconds
the command npm init or we can say npm init hyphen y to say yes to all the optional questions and then it will create a node
9:32
9 minutes, 32 seconds
project which will have package.json file and then we can install the library separately in that project like if you want to
9:40
9 minutes, 40 seconds
install playwright we will say npm install playwright and similarly we can install other libraries but to start a node project along with playwright
9:48
9 minutes, 48 seconds
already installed we can use npm in it and say playwright at the rate the version number or to get
9:57
9 minutes, 57 seconds
the latest version i will say latest now you can also just go to the playwright official website that is payride.dev and select
10:06
10 minutes, 6 seconds
node.js from here and then click on this github icon this will also take you to the github
10:13
10 minutes, 13 seconds
page and here also you can see all these commands so you can see the command i have used
10:20
10 minutes, 20 seconds
you can see this is the command i have used npm init playwright at the red latest so
10:28
10 minutes, 28 seconds
you can also get it from here so this is what we will do i will press enter and it will
10:35
10 minutes, 35 seconds
create a node project install playwright you can see we are getting some option do you want to use typescript or javascript you can use the arrow keys on your keyboard to select the option and
10:44
10 minutes, 44 seconds
press enter i am using javascript for now now it is asking where do you want to put your end to end tests if you want to
10:51
10 minutes, 51 seconds
uh you know name the folder something different you can name it whatever you want you can press your uh the keys and give the name or if you just want to go
10:59
10 minutes, 59 seconds
with tests you can just use tests here and press enter
11:07
11 minutes, 7 seconds
then it is asking do you want to add github action workflows so this will basically create a ml file which will
11:14
11 minutes, 14 seconds
have some uh steps to run when you are running in a ci cd environment using github workflows uh let us say true or
11:21
11 minutes, 21 seconds
let us say yes when you press y it is a it changes it to true and then it will now do the installation
11:30
11 minutes, 30 seconds
so it is now installing you can see it will also install all the browsers and now it is done let us see some of
11:38
11 minutes, 38 seconds
these logs and information here so it is installing playwright and then it is adding all these packages
11:46
11 minutes, 46 seconds
and you can see it is also adding all the browsers we need and then you can see it has created a tests folder that is
11:55
11 minutes, 55 seconds
what we mentioned and all our tests will go inside this folder and you can see some commands you can use npx playwright test to run all
12:04
12 minutes, 4 seconds
the tests you can say npm npx playwright test and give some particular browser to run on
12:11
12 minutes, 11 seconds
that browser we can run a specific test file by giving the name of the file or the location of the file
12:18
12 minutes, 18 seconds
then if you want to run a debug mode we can add hyphen hyphen debug if you want to record your test we can use the code
12:25
12 minutes, 25 seconds
gen tool and we can run this command and these are all the options so you can see some example or
12:33
12 minutes, 33 seconds
sample tests are also created and you can now see your project structure here so this is what it has created
Chapter 5: Playwright project structure
12:42
12 minutes, 42 seconds
so let us see all these you should have all these files and folders now first one will be package.json this is the this is a very
12:50
12 minutes, 50 seconds
important file that manages the node project so you can see this is our package.json file
12:58
12 minutes, 58 seconds
and here here it shows all the libraries added in the project so as of now we have playwright added
13:06
13 minutes, 6 seconds
and you can see some more options now just in case you want to know more about package.json what is package.json what is packagelock.json
13:15
13 minutes, 15 seconds
and all the details you can always go and check my video if you say package dot json and use my name
13:25
13 minutes, 25 seconds
and you will see this video what is package.json and you will get all the details here then
13:32
13 minutes, 32 seconds
you will see a configuration file playwright.config.js and if you have used typescript it will be playwright.config.ts
13:40
13 minutes, 40 seconds
and this is the configuration file and it is a very important file we will make all the settings configurations here and you can
13:48
13 minutes, 48 seconds
see some of the configurations so you can see which is your test directory so tests folder is your test directory that will mean that whenever
13:56
13 minutes, 56 seconds
you run the command npx playwright test it will run all the tests which is inside the test folder
14:04
14 minutes, 4 seconds
this is the timeout so the timeout is 30 into 1000 that is 30 000 milliseconds or 30 seconds this is the page load time
14:12
14 minutes, 12 seconds
out or this is the time out whenever you are using the expect assertions i will show you this later how do we add a
14:20
14 minutes, 20 seconds
sessions but whenever we are using expect the default timeout is five seconds but if you want you can change it from here
14:27
14 minutes, 27 seconds
then you can see some more options uh parallel runs workers retries reporters all this is
14:34
14 minutes, 34 seconds
here so we will learn more about this so you can see the mobile browsers which is as of now
14:43
14 minutes, 43 seconds
commented out all the mobile browsers these are the desktop browsers so you can do all these configurations here
14:51
14 minutes, 51 seconds
then we have the test folder and the test examples folder here some sample tests are created that you can uh you
14:59
14 minutes, 59 seconds
know see and you can see how these tests are created so if i go to the tests folder here is the
15:07
15 minutes, 7 seconds
example.spec.js file and here is a very basic test so you can see this is how we create a test this is how we declare a test and then we say page dot go to and
15:16
15 minutes, 16 seconds
give the url and then it is using the expect assertion and checking if the page have this title
15:24
15 minutes, 24 seconds
then you can see some more options uh it is getting some particular object using this locator
15:31
15 minutes, 31 seconds
and then doing some more action so this is a very basic sample test here if you go to the tests examples folder
15:39
15 minutes, 39 seconds
here you can you will find some detailed tests so you can see all these detailed tests here
15:46
15 minutes, 46 seconds
so this will be good for learning and execution then there is a dot get ignore file so
15:54
15 minutes, 54 seconds
here you will see there is a dot get ignore file now this will be used when we commit and push our projects to a git
16:01
16 minutes, 1 second
repository basically this file uh here we can put all the folders or file and locations that we don't want to commit
16:09
16 minutes, 9 seconds
and push to the repository so we will use this later as of now you don't have to do anything with this file then we will have a
16:17
16 minutes, 17 seconds
gml file if you go to this github folder you will see a playwright.ml file and this will be used
16:25
16 minutes, 25 seconds
when we are doing ci cd using github workflow so basically it will have all the steps to run like you can see it is
16:32
16 minutes, 32 seconds
uh you know installing the browsers installing all the dependencies and then running the test by using npx playwright test so
16:41
16 minutes, 41 seconds
this will be used in ci cd in github workflows as of now we don't need this so i'll just close this so this is what we have got this is the project
16:50
16 minutes, 50 seconds
structure okay so this is what we have got here now next step is
16:58
16 minutes, 58 seconds
we can also check the playwright version by running the command let me
17:06
17 minutes, 6 seconds
expand the terminal window and i will say here i'll clear
17:14
17 minutes, 14 seconds
and say npm playwright hyphen v this will check and show us the version
17:21
17 minutes, 21 seconds
of playwright so as of now as of the time of recording this video this is the latest version 8.5.0 and then
17:29
17 minutes, 29 seconds
i can also run the command npx playwright hyphen h so npx is used to execute the npm libraries on a local
17:38
17 minutes, 38 seconds
folder so if you have to execute anything we will use npx i will say npx playwright and hyphen
17:47
17 minutes, 47 seconds
hyphen help or hyphen h so it will show us all the options that we can use with the playwright command
17:55
17 minutes, 55 seconds
and you can see all these options uh the first one we will use is test which will run all the tests so you can see this here
18:05
18 minutes, 5 seconds
this is the test command we can say npx playwright test it will run all the tests here we have the show report all
18:12
18 minutes, 12 seconds
these options here so we will see this in more details in the coming sessions so this is how
18:19
18 minutes, 19 seconds
you can install playwright using the commands as a npm package if you want you can take a
18:27
18 minutes, 27 seconds
screenshot of this page and keep it handy with you and watch it several times so that it will become very clear to you now
Chapter 6: Option 1 - using vs code extension
18:35
18 minutes, 35 seconds
we will go to the next option of installing playwright that is using the vs code extension and here
18:43
18 minutes, 43 seconds
we will again create a new folder and open in vs code that is step number one so let me close this folder or if you want you can also
18:51
18 minutes, 51 seconds
go to a new window and then do the open the new folder there so let me just you can close this folder or close this
18:59
18 minutes, 59 seconds
window close folder and then open a new folder or just go to a new window so that i will have both of these open
19:07
19 minutes, 7 seconds
now here again i will create a new folder and open it here so let me create one more folder
19:17
19 minutes, 17 seconds
i will say this is playwright automation and underscore vs
19:25
19 minutes, 25 seconds
code extension you can give any name i'm just giving this name so that i will know that this has the vs code extension and
19:34
19 minutes, 34 seconds
i will open it in vs code so you can drag and drop or go to file open folder
19:41
19 minutes, 41 seconds
i'll just drag and drop it here and i will say yes i trust the authors
19:49
19 minutes, 49 seconds
and that's it so we have got our folder opened in vs code now we will go to the
19:57
19 minutes, 57 seconds
extensions section and install the playwright extension from microsoft so you can see here is the
20:04
20 minutes, 4 seconds
extensions section go here and just search for playwright
20:12
20 minutes, 12 seconds
and when you go here the first option when you search for playwright the first option you will get is playwright test for vs code and it is created by
20:20
20 minutes, 20 seconds
microsoft the same team who has created playwright and you can see all the details here and then you can click on the install button in my case
20:28
20 minutes, 28 seconds
it is saying uninstall because it is already installed so let me just uninstall and install it again so it is now installed now
20:37
20 minutes, 37 seconds
you can go back to your explorer and then step number three is we will go
20:45
20 minutes, 45 seconds
to the command palette and then type playwright and then from there we will select from the options we will select install playwright so if you go to view
20:54
20 minutes, 54 seconds
on your vs code go to view menu and you will find this option command palette you can also press ctrl
21:01
21 minutes, 1 second
plus shift plus p key on your keyboard or command plus shift plus b in case of mac and it will open command palette
21:10
21 minutes, 10 seconds
and here just start typing playwright
21:18
21 minutes, 18 seconds
so you can see here playwright and you will see all the options will get filtered out so here
21:27
21 minutes, 27 seconds
you will see an option called install playwright so click on this install playwright option and you will see all these options do
21:36
21 minutes, 36 seconds
you want to install all these browsers chromium firefox webkit and also want to add github action workflow so again
21:44
21 minutes, 44 seconds
these are the same options that we got from the command line so you can check or uncheck whatever options you want as of now i want all these all the browsers
21:52
21 minutes, 52 seconds
and also the github gml file and i will say ok or press enter and you will see now if you go to the terminal you will
22:00
22 minutes
see it is running similar commands so it is saying npm init playwright at the red at the rate latest that we already used
22:07
22 minutes, 7 seconds
and it is also adding all the browsers as well here so you can see the same thing here
22:15
22 minutes, 15 seconds
this is what we got when we used the command line so the same things we have got here and if you see the project structure as well you will see
22:24
22 minutes, 24 seconds
the similar structure as well here so we have test and test examples folder we have a configuration file in this case it is a dot ts file but if you see the
22:32
22 minutes, 32 seconds
same there are the same configurations here then you can see the package.json file is here and all these dependencies and
22:41
22 minutes, 41 seconds
everything is added dot get ignore file uh playwright.ml file everything is here
22:49
22 minutes, 49 seconds
so the same things the same structure we have got and now
22:56
22 minutes, 56 seconds
we have done all this we have also it will install all the libraries and create the project structure and the project folders and we have done that
23:04
23 minutes, 4 seconds
now the advantage or the benefit of using the vs code extension for playwright is now if you want
23:13
23 minutes, 13 seconds
you can get options to directly run your test you will get you know options to run select and run your test and some other options
23:22
23 minutes, 22 seconds
debugging options so basically the options that we can do from command line it will have a ui for doing all those
23:30
23 minutes, 30 seconds
actions so let me show you if i you again go to command palette you can press ctrl shift and p or go to view and
23:37
23 minutes, 37 seconds
again say playwright and you will see this option let me say playwright
23:47
23 minutes, 47 seconds
so we have this option testing focus on playwright view so i will go to the playwright view select this and you can
23:55
23 minutes, 55 seconds
see the playwright view here and here you can see some options you can use this run button debug button refresh button so i'll say refresh it will show
24:03
24 minutes, 3 seconds
you all the tests so basically all the tests in your test directory will be shown here so you can see this is the tests we have
24:13
24 minutes, 13 seconds
got and then you have a run button here we also have a drop down so you can run on a specific browser so let us say i
24:20
24 minutes, 20 seconds
will click chrome and it will start running and it will also highlight the steps that have that have got executed
24:29
24 minutes, 29 seconds
so you can see let me show you again just uh focus here it will highlight the steps which are getting executed and
24:37
24 minutes, 37 seconds
after execution it will it will also show you the time taken by each step so you can see it is showing the time taken by each step let me again run it
24:47
24 minutes, 47 seconds
i'll just run on one browser and just focus here so you can see it is highlighting the
24:54
24 minutes, 54 seconds
steps as it is running and it is also showing us the time taken by each step and if i see the
25:02
25 minutes, 2 seconds
terminal as of now there is nothing coming on the terminal but you can see it is highlighting it here we can also debug and some other things we can do with
25:11
25 minutes, 11 seconds
this vs code extension okay so these are the two ways you can install uh playwright and then you can start
25:19
25 minutes, 19 seconds
working with playwright i hope this was very useful in the coming sessions we will learn how to run our tests how to create our tests all the different
Chapter 7: Outro
25:27
25 minutes, 27 seconds
options that we can use all the different commands that we can use so this will be very interesting and very easy i hope all of this was useful thank
25:36
25 minutes, 36 seconds
you for watching and never stop learning
25:45
25 minutes, 45 seconds
you
