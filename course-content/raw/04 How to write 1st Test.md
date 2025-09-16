Chapter 1: Intro
0:00
hello and welcome i am raghav and today we are going to start to write our first test in playwright this is going to be
0:08
8 seconds
very easy and very interesting and i will show you step by step how to write the first test and we will also see the
0:15
15 seconds
syntax the keywords and the commands we use to run the test and there will be a quiz i will have the link for the quiz in the description of
0:23
23 seconds
this video and you can take the quiz and check your knowledge do let me know the score your score in the comment section below and if you have any questions you
0:32
32 seconds
can let me know in the comments or the q a session below this video and if you find this video slow you can increase the pace of the video from the video
0:39
39 seconds
settings so with that let's get started and let us see how to write our first test in playwright now step number one
Chapter 2: Step 1 - Create a new file under test folder
0:47
47 seconds
is we will create a new file under the test folder so i will go to my playwright project here and we have
0:55
55 seconds
already created this folder and started the playwright project here and here we have got a
1:03
1 minute, 3 seconds
test folder created and under the test folder we have all our test files so we already have some
1:11
1 minute, 11 seconds
sample tests here so you can see this sample test here this is how we start uh let me show you
1:20
1 minute, 20 seconds
this is how we start this is how we write the tests and this is how we write the steps now do not worry i am going to start and show you from scratch so i am
1:28
1 minute, 28 seconds
going to create a new file under the test folder now you can select the test folder and then you can
1:36
1 minute, 36 seconds
do a right click and then here select new file so you can do a right click and select new file or the other way is you
1:44
1 minute, 44 seconds
can select the test folder and here is the icon to create a new file so you can also click here so when you click here
1:52
1 minute, 52 seconds
a new file will get created under that folder that you have selected and here you can give some name so i will say uh my first
2:01
2 minutes, 1 second
test and then we say dot spec dot js and hit enter and the new file is
2:10
2 minutes, 10 seconds
created and now here we can start writing our playwright test now the first thing is we have to include the
Chapter 3: Step 2 - Add module ‘playwright/test’
2:17
2 minutes, 17 seconds
playwright test module into our script now if i show you if i go to the node modules folder of my project
2:26
2 minutes, 26 seconds
and you will see there is a playwright test module or playwright test package this is what we need
2:33
2 minutes, 33 seconds
and from this we need some specific modules or specific scripts so i will show you how to do that so here i will
2:41
2 minutes, 41 seconds
say require so require is a function it's a node.js function that is used to
2:49
2 minutes, 49 seconds
include modules which are present in external or separate files and that is the case here we want to include uh some
2:56
2 minutes, 56 seconds
modules which are present in separate files so i will use require and then i can i will
3:05
3 minutes, 5 seconds
give these codes and then you can see i'm getting this auto suggestion here playwright test so even if you're not getting you
3:12
3 minutes, 12 seconds
can start typing or press ctrl space on your keyboard to get the auto suggestion box and then select this playwright test and this will now
3:21
3 minutes, 21 seconds
include this playwright test module and all its scripts inside this script that is my first test and now i can use any
3:30
3 minutes, 30 seconds
of the scripts any of the modules under the playwright test package so this is good however out of all these all the
3:38
3 minutes, 38 seconds
packages and scripts under the playwright test package i just need the test and the expect modules so again if
3:46
3 minutes, 46 seconds
i show you if i go to the node modules and go to playwright test and here if i show you
3:54
3 minutes, 54 seconds
if i expand and show you under the test we have all these
4:02
4 minutes, 2 seconds
modules and scripts out of this i just need the test script this is test.js and i need the expect so test script will be
4:11
4 minutes, 11 seconds
used to create the test the structure of the test and expect is used to uh run the assertions or add any checks
4:19
4 minutes, 19 seconds
these are the two things i know that need as of now so for this what i will do is instead of importing or including everything i just need these two so i
4:28
4 minutes, 28 seconds
will say i can say where or const this is a keyword in javascript to declare a variable or a
4:36
4 minutes, 36 seconds
constant so it's good that you declare that constant because we don't want to change these variables or whatever we
4:45
4 minutes, 45 seconds
write here we don't want to change it or we don't want anybody or any script to change these values so i will say const and i will say test
4:53
4 minutes, 53 seconds
and expect and then i will say equals this so this is how we
5:01
5 minutes, 1 second
include the modules in a different script or a different module so this is what you will do and this is
5:09
5 minutes, 9 seconds
what is mentioned here as well in the notes i will have all the notes in the description of this video so you can always refer the description if you have
5:16
5 minutes, 16 seconds
any questions or any doubts so require is a node.js built-in function so make sure it is not a javascript function it
5:23
5 minutes, 23 seconds
is a node.js built-in function which is used to load modules present in separate files and here we are loading
5:31
5 minutes, 31 seconds
test and expect modules from the playwright package so this is important and if you allow me some more time i can show you what exactly this is now this
Chapter 4: Example how to add and import modules
5:39
5 minutes, 39 seconds
is not what i'm going to tell you may not be very important from the automation point of view but it will be very good if you understand how these
5:48
5 minutes, 48 seconds
importing and adding the module works so let's say i will go to my test folder and i'm going to create one
5:56
5 minutes, 56 seconds
more folder here so i will click on this i can do a right click new folder or click on this icon which will create a new folder and i will
6:04
6 minutes, 4 seconds
keep the folder name as demo so i have created a new folder under the tests folder and under the demo folder
6:11
6 minutes, 11 seconds
i'm going to create a file uh let's say i will call it as hello.js so i have created a
6:18
6 minutes, 18 seconds
javascript file hello.js under the demo folder now here i am going to create some functions so
6:25
6 minutes, 25 seconds
in javascript we say function now uh do not worry uh do not worry if you don't do not know javascript what i am going to show is
6:33
6 minutes, 33 seconds
very very easy and you will get exactly what i am doing just in case you want to know more about javascript and the
6:39
6 minutes, 39 seconds
basics of javascript you can always go to my website that is automation step by step
6:49
6 minutes, 49 seconds
dot com let me show you very quickly this is just if you want to you know study more javascript later on
6:56
6 minutes, 56 seconds
uh let me load this and see okay here
7:04
7 minutes, 4 seconds
you can just search for javascript and or you can just go to the programming section
7:13
7 minutes, 13 seconds
and here under the programming you will see a javascript you can directly go on my youtube channel as well and you will see
7:20
7 minutes, 20 seconds
the javascript playlist so this will again take you to the youtube javascript playlist and here you will see all the beginner
7:28
7 minutes, 28 seconds
tutorials on javascript but for now you can do this later if you want but for now coming back here i am creating a function i will say function
7:38
7 minutes, 38 seconds
f1 you can give any name and then you give these brackets and the curly brackets start and stop this is how we
7:45
7 minutes, 45 seconds
declare a function this is how we create a function and here i am just returning a string called
7:53
7 minutes, 53 seconds
hello i can create one more function here i will say function and i will give it a name f2
8:00
8 minutes
and here i am just returning a string called hello world so in this module in this
8:07
8 minutes, 7 seconds
script hello.js i have these two functions now if i want these functions to be exposed and if i want these
8:14
8 minutes, 14 seconds
functions to be included or imported in any other script or module i will have to say exports
8:22
8 minutes, 22 seconds
i will say exports and i will give some name let us say hello
8:30
8 minutes, 30 seconds
and i will make it equals to this function similarly for this i will say exports dot hello world now this name can be
8:38
8 minutes, 38 seconds
anything it's not necessary that you give the name same as the function name or same as whatever i am printing here it can be anything so now i am exporting
8:46
8 minutes, 46 seconds
these two functions using hello and hello world and if i have to import it if i have to add this in any other script so i'm going back to my
8:55
8 minutes, 55 seconds
first test and here i will say require
9:02
9 minutes, 2 seconds
and i will give the location of the script or module first so i will say dot
9:10
9 minutes, 10 seconds
and forward slash and you can see i am able to see the demo folder and it will give you auto suggestion if if the demo
9:17
9 minutes, 17 seconds
folder is uh even above the test folder then i may have to use double dot and then it will go one step up and i can
9:25
9 minutes, 25 seconds
here see node modules and other tests folder but it is within the test folder so i will just give a single dot forward
9:32
9 minutes, 32 seconds
slash and select demo and then from here i will select the script or file hello dot js
9:42
9 minutes, 42 seconds
and then because from here i just need the functions are
9:51
9 minutes, 51 seconds
the properties hello and hello world so i will use const hello
9:59
9 minutes, 59 seconds
and hello world equals require from here and as i told you instead of const i can use where as well but where means
10:07
10 minutes, 7 seconds
variable or i can say let let also is used to declare variable in javascript but in that case these will be these can be changed later
10:16
10 minutes, 16 seconds
on but i don't want this to be changed anywhere in the script so i am using const and now i can say
10:25
10 minutes, 25 seconds
i can now say hello and i can call this function
10:34
10 minutes, 34 seconds
when i call hello it should call this f1 function and if i say hello world it should call this f2 function let us see
10:42
10 minutes, 42 seconds
i will run this and because this is now a test under playwright to run this i
10:49
10 minutes, 49 seconds
can say normally we can say node and give the location of the file so if
10:57
10 minutes, 57 seconds
i say node and let me try to say if it runs this
11:05
11 minutes, 5 seconds
node and the location of the file that yes this is running and the reason is not printing anything because we have not printed anything here so i will just
11:14
11 minutes, 14 seconds
say console.log and then i will call this hello and it should print whatever is returned from
11:21
11 minutes, 21 seconds
this hello function which is hello here so let me now save and run it
11:29
11 minutes, 29 seconds
and you can see it is printing hello similarly if i say if i call hello world i say console.log
11:38
11 minutes, 38 seconds
and if i say hello world and you can see i'm also getting auto suggestions now
11:46
11 minutes, 46 seconds
so this should print hello world so if i now again run this you can see it is printing
11:54
11 minutes, 54 seconds
hello and hello world here so this is how you you can include or add modules and i can actually import it as well instead of
12:02
12 minutes, 2 seconds
using this require statement i can say import
12:10
12 minutes, 10 seconds
and i can say hello and hello world from
12:17
12 minutes, 17 seconds
again i will give the location of the file or the package demo hello so if i do this this will also
12:25
12 minutes, 25 seconds
work so let me now remove all of this and come back to our test this was for
12:32
12 minutes, 32 seconds
your knowledge and understanding so we can do this or we can say import as i
12:39
12 minutes, 39 seconds
have shown you we can say import test or expect from uh at playwright test now the next step is
12:47
12 minutes, 47 seconds
we will create our test function now playwright library or playwright package provides a test function and the expect
Chapter 5: Playwright Test provides a test function to declare tests and expect function to write assertions
12:54
12 minutes, 54 seconds
function to write assertions and that is what we have already included or imported in our
13:03
13 minutes, 3 seconds
script so now let me show you
Chapter 6: Step 3 - Create a test block - test(title, testFunction)
13:11
13 minutes, 11 seconds
i will create a test block
13:20
13 minutes, 20 seconds
so i will go and say here i will create a test block and
13:30
13 minutes, 30 seconds
we are also getting this auto suggestion and the syntax is in the test block or the test function i
13:38
13 minutes, 38 seconds
will first give the title of the test and then i will call a function so here let me give a title within quotes i will
13:47
13 minutes, 47 seconds
say my first test
13:54
13 minutes, 54 seconds
and then i will give a comma here and then i will create a
14:02
14 minutes, 2 seconds
javascript anonymous function and for that we just give these brackets start and close and then
14:10
14 minutes, 10 seconds
we create an arrow symbol by using equals sign and greater than symbol so this creates a arrow symbol and then a curly bracket
14:20
14 minutes, 20 seconds
start and stop and you can press enter to move these stop brackets to the next line so that we get some space to write our
14:28
14 minutes, 28 seconds
test steps so this is how we can create a test in playwright
14:36
14 minutes, 36 seconds
okay and here is the
14:42
14 minutes, 42 seconds
screenshot of the same thing and you can see here this is how we create the test now here
14:51
14 minutes, 51 seconds
uh to create a browser test we have to here
14:58
14 minutes, 58 seconds
pass up the fixture or a fixture called page now do not worry i will uh tell you more about this in detail
15:06
15 minutes, 6 seconds
uh in the coming sessions but for now just you have to go here and give a curly bracket start and stop
15:14
15 minutes, 14 seconds
and say page this is a page fixture and you can also see it is a coming from playwright and you can see it says
15:23
15 minutes, 23 seconds
isolated page instance created for each test each test pages are isolated between test due to fixture content so
15:31
15 minutes, 31 seconds
don't worry about all this as of now just create a fixture or just pass this page here within curly brackets
15:38
15 minutes, 38 seconds
and then using this page object i can now use the functions so for
15:46
15 minutes, 46 seconds
example i can say go to go back go forward so go to is the command we used to visit a url and
15:55
15 minutes, 55 seconds
within the course i will give the url so you can give any url of your application for now i will just go to google.com so i will say
16:04
16 minutes, 4 seconds
https.google.com and now if i try to run this so if i
16:13
16 minutes, 13 seconds
run this using the command npx i hope you remember the command that we used to run the playwright test it is
16:20
16 minutes, 20 seconds
npx playwright test and because i want to run this specific file i will
16:27
16 minutes, 27 seconds
give the file location or name so i will say my first
16:34
16 minutes, 34 seconds
test dot spec dot gs and if i hit enter let us see i will also expand this
16:44
16 minutes, 44 seconds
so that you can see and you can see there is a error here and here
16:51
16 minutes, 51 seconds
it is saying here you can see it is showing this error here
16:59
16 minutes, 59 seconds
page dot go to and it has aborted now for this what we'll have to do is
17:07
17 minutes, 7 seconds
i will have to use async keyword here and
17:15
17 minutes, 15 seconds
here i will use await okay so i'm using async and await now here
17:26
17 minutes, 26 seconds
the async keyword before any function makes the function to return a promise now promise is something so let's say
17:35
17 minutes, 35 seconds
the function returns something so we are actually waiting and we are making sure that this function returns something returns a
17:43
17 minutes, 43 seconds
promise and the await keyword before any function makes the function to wait for a promise now do
17:51
17 minutes, 51 seconds
not get confused here uh in very very simple words javascript is a asynchronous programming
17:59
17 minutes, 59 seconds
language and in very simple words asynchronous means not happening at the same time now if we
18:06
18 minutes, 6 seconds
do not use this javascript by nature is asynchronous that it will it will not uh wait for one thing to complete before
18:14
18 minutes, 14 seconds
starting the next thing it will not wait for the first step to complete before uh starting the next step but in our case
18:21
18 minutes, 21 seconds
in automation testing we want the uh execution to go sequentially in the sense that the first
18:29
18 minutes, 29 seconds
step should complete and then only the next step should get executed now here for example if i do not use async and await
18:38
18 minutes, 38 seconds
it will not wait for this page to get loaded completely and then move forward to the
18:45
18 minutes, 45 seconds
second step it will just run this step will not wait for the page to load completely and go to the next step and it may happen that the page is not
18:52
18 minutes, 52 seconds
loaded completely and our next step will fail and therefore we use a weight here and async so that all these functions
19:02
19 minutes, 2 seconds
will return some promise now if you want if you just go to this go to function you can press ctrl or command on your keyboard control key and
19:11
19 minutes, 11 seconds
then this will turn into a link and if you click here you can see this is the function and if you go down you will see
19:20
19 minutes, 20 seconds
it should be returning some promise so you can see it is returning a promise here
19:27
19 minutes, 27 seconds
and therefore we are using this async and wait here away it means this
19:34
19 minutes, 34 seconds
will now wait for the promise to be returned and then only it will go to the next step
19:40
19 minutes, 40 seconds
so next i can again say i can use expect for any assertion and i can now here say
19:48
19 minutes, 48 seconds
expect this page to have some title and i can check it has the title so i will say
19:56
19 minutes, 56 seconds
expect page dot to
20:03
20 minutes, 3 seconds
have and you can see so many things here to have length property to have title and i will say the title should be
20:11
20 minutes, 11 seconds
google so in general also if you go to google here the title of the page is
20:18
20 minutes, 18 seconds
google so this is what i will check and now
20:25
20 minutes, 25 seconds
again i will use await so that it waits for this to complete and then only moves to the
20:33
20 minutes, 33 seconds
next step so i will now run and check again i will save this save the file
20:41
20 minutes, 41 seconds
go to the terminal and clear the terminal
20:49
20 minutes, 49 seconds
and i will press the up arrow on my keyboard to go to the last command and run the command and let's
20:56
20 minutes, 56 seconds
see now and yes it is now running and you can see it is
21:04
21 minutes, 4 seconds
running three tests that means it is running on three browsers using one worker and let me see uh looks like
21:12
21 minutes, 12 seconds
some issue let me check the report
21:22
21 minutes, 22 seconds
i'll also expand this make it full screen so i can see all the logs here so here it says
21:31
21 minutes, 31 seconds
there is some issue in the assertion okay i think this is fine uh we had made a mistake i had made this mistake here
21:39
21 minutes, 39 seconds
so expected was this which i which was a typo from my end and received this google so actually this is good that we
21:48
21 minutes, 48 seconds
are able to also check that it is all running fine and let us see the report as well so report
21:55
21 minutes, 55 seconds
it is running here and here also you can see it is saying expected was this but actual was this so i can go and change
22:04
22 minutes, 4 seconds
this and make it pass so i will change this to google it is it was a typo here
22:12
22 minutes, 12 seconds
it should be google here and now if i run it should work fine and uh i can also
22:20
22 minutes, 20 seconds
run in a edit mode so that you can see here so i will say hyphen hyphen edit
22:28
22 minutes, 28 seconds
and let us run and check now so it should now run on a physical
22:36
22 minutes, 36 seconds
browser and yes it is going to google and checking the title it is done on chrome it is now running on firefox
22:44
22 minutes, 44 seconds
and then it will run on webkit and yes it is running and everything is fine it looks like everything is passed
22:52
22 minutes, 52 seconds
and now you can check the report by running this command or directly go to the report folder which is playwright report and
23:01
23 minutes, 1 second
check the report from here and you can see this to have title is coming from the expect a script or module again i
23:10
23 minutes, 10 seconds
can click on this i can press control on my keyboard and click here and you can see it is go it has gone here and this must also be
23:18
23 minutes, 18 seconds
returning a promise you can see it is returning a promise and similarly you will find
23:24
23 minutes, 24 seconds
a lot of assertions here so if i show you let me go here
23:32
23 minutes, 32 seconds
let me go to this expect here i'm going to display write a test
23:40
23 minutes, 40 seconds
library and here i will go to the lib and go to the expect.js this is what we have included
23:48
23 minutes, 48 seconds
and you can see here all these different assertions that we can use
23:55
23 minutes, 55 seconds
so you will find all the sessions here so we have to be checked to be disabled to be visible
24:02
24 minutes, 2 seconds
to have title to have count to have text to have id so all this we can use in our test in playwright tests so this is how
24:11
24 minutes, 11 seconds
we create test if you want you can take a screenshot of this screen and keep it handy with you
Chapter 7: Screenshot moment
24:20
24 minutes, 20 seconds
and watch it multiple times so that it will always be it will be very clear to you how to create tests in playwright
24:28
24 minutes, 28 seconds
and then you will be good with creating tests in playwright in the coming sessions we will see more options more
24:35
24 minutes, 35 seconds
ways and more things to do with test hooks and all the other things that we can do with test i hope this was very useful for you
24:43
24 minutes, 43 seconds
thank you for watching and never stop learning
