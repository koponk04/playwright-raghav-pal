Chapter 1: Introduction
0:00
hello and welcome i'm makhav and today we are going to see the different commands that we can use to run our tests and the different options we have
0:09
9 seconds
like how can we run all the tests how can we run specific tests how can we run in a headless mode or a headed mode how
0:17
17 seconds
do we run a specific test from us a test file uh how can we use multiple workers
0:24
24 seconds
how can we run in parallel how can we debug our tests so let's get started and we are going to see how to run the test
0:31
31 seconds
all the commands with options and then i will have a quiz i will share a link for quiz in the description of this video so you can take the quiz and check your
0:40
40 seconds
knowledge and do let me know your score in the comment section and if you have any questions you can let me know if you have any message you can write your message in
0:48
48 seconds
the comment section below and i will reply to you and in case you feel the speed of the video is slow you can go to the video player settings and increase
0:57
57 seconds
the speed from there so with that let's get started and let us see the commands and for this i have already opened my vs code and this is the project this is the
1:06
1 minute, 6 seconds
project uh this is the playwright project we created in the last session by using the npm commands so you can see
1:13
1 minute, 13 seconds
all the tests are here all this project structure is already created now uh here we have these tests already
1:22
1 minute, 22 seconds
added as sample test so if you go to the test folder here we have all these added
1:30
1 minute, 30 seconds
and now i will say i will use all these commands and let me
1:39
1 minute, 39 seconds
show you the first command is npx playwright test and this command will run all the tests
Chapter 2: npx playwright test runs all tests on all browsers in headless mode
1:46
1 minute, 46 seconds
in your test folder now the test folder is this one this is where we have all our tests so i will open the terminal
1:54
1 minute, 54 seconds
you can go to the terminal and say new terminal or press ctrl j on your keyboard and it opens the terminal
2:01
2 minutes, 1 second
and here i will say and you can see i am on the
2:09
2 minutes, 9 seconds
project folder by default it opens in the project folder so i will say npx playwright
2:18
2 minutes, 18 seconds
and i will say test and hit enter and this will run all the test files in that in the test folder
2:25
2 minutes, 25 seconds
and as of now we have a single test file so it is running there and you can see it is running three tests using one worker that means it is running that
2:33
2 minutes, 33 seconds
test with uh on all the browsers that is chromium webkit and firefox and it is using one worker so one worker means it
2:41
2 minutes, 41 seconds
will run sequentially one after the other and it is done it says all three passed and it took approximately 15
2:48
2 minutes, 48 seconds
seconds and we have got our report as well and if you want to see the report you can directly go to the playwright
2:56
2 minutes, 56 seconds
report folder here and it will be a html report and you can open it so i can do a right click and
3:03
3 minutes, 3 seconds
say reveal in file explorer it will open the folder with the report and then you can open the report from here or you can
3:10
3 minutes, 10 seconds
directly run this command and px playwright show report and this will run and show the report on the browser
3:19
3 minutes, 19 seconds
so if i run this command you can see the report is here it's an html report it will show all your tests here and you have the filters here if
3:27
3 minutes, 27 seconds
you want to see all passed failed etc then we can also filter by uh writing some name of our test and you can see
3:34
3 minutes, 34 seconds
this single test was executed on chromium firefox and webkit and this is the approximate time taken and you can
3:42
3 minutes, 42 seconds
go and check any of the tests and see all the details now as of now we have not yet started writing our test in this
3:49
3 minutes, 49 seconds
session i am showing you all the options all the ways you can run the test and then in the coming session we will learn step by step how to write the tests so
3:58
3 minutes, 58 seconds
you can see all these details are here every step with the time taken all the details are here so i will go back to my
4:05
4 minutes, 5 seconds
vs code and i will press ctrl c and y to quit this and
4:13
4 minutes, 13 seconds
i will say clear to clear all these locks so we have seen this command npx playwright test now if you want to use
Chapter 3: npx playwright test --workers 3 runs with 3 workers in parallel
4:22
4 minutes, 22 seconds
multiple workers and run in parallel you can say hyphen hyphen workers and give the worker count so i can say with this command i'm pressing the top arrow on my
4:31
4 minutes, 31 seconds
keyboard to bring up the earlier commands and here along with the command npx playwright test i will say workers
4:39
4 minutes, 39 seconds
and i will say three so that means now all the three browsers
4:47
4 minutes, 47 seconds
the test on all the three browser will run in parallel and you can see it is all running in parallel and it will save us some time now in this case the time
4:56
4 minutes, 56 seconds
difference may not be very much because it's a single test we are running but when you have like multiple tests you will see the time difference so you can see as of now there is not much
5:04
5 minutes, 4 seconds
difference it is 13 seconds but when we have a lot of tests you will see this time difference so you can increase the number of workers and run
5:13
5 minutes, 13 seconds
in parallel then if you want to run a specific file you can give the location or name of the file so i can say
Chapter 4: npx playwright test one.spec.js runs a specific test file
5:21
5 minutes, 21 seconds
let me clear the screen i will go back to the earlier command so here
5:29
5 minutes, 29 seconds
i will say npx playwright test and now i want to run a specific test file so i will go to that folder that is tests
5:35
5 minutes, 35 seconds
folder and the test file name is example spec.js this is the file so if i
5:43
5 minutes, 43 seconds
run like this it will run that particular test file only and you can see it is running that
5:50
5 minutes, 50 seconds
test file then if you want to run specific files from a folder you can
Chapter 5: npx playwright test one.spec.js two.spec.js runs the files specified
5:57
5 minutes, 57 seconds
give the names like this so like we had mentioned a single file you can mention multiple files as well
Chapter 6: npx playwright test one two runs files that have one or two in the file name
6:04
6 minutes, 4 seconds
then if you want to run the files having uh which has these words in the name
6:12
6 minutes, 12 seconds
having let's in this example i am saying one and two so it will run the files that have one or two in the file name so something like i can say
6:21
6 minutes, 21 seconds
i can just say npx playwright test and i will say example so it will pick up the file
6:29
6 minutes, 29 seconds
in which which has the name which has example in the name and it will start running the file and you can see it is executing our test file
6:37
6 minutes, 37 seconds
then we can also uh run a specific test by
Chapter 7: npx playwright test -g "check title" runs test with the title
6:44
6 minutes, 44 seconds
saying minus g and give the title of the test
6:50
6 minutes, 50 seconds
so let us say if i go if i go in my
6:57
6 minutes, 57 seconds
file the test file and here this is my test which has this title now
7:06
7 minutes, 6 seconds
don't worry about how these tests are created in the session when we where we learn how to create test how to write test i will show you all this all the
7:14
7 minutes, 14 seconds
syntax and everything but for now let us say this is the test and this is our title homepage has playwright in title i will copy this
7:22
7 minutes, 22 seconds
and then i will go to my terminal and here i will say npx playwright test and
7:32
7 minutes, 32 seconds
i will use the minus g option so i will say npx playwright test
7:42
7 minutes, 42 seconds
and minus g and then i will give the title so this is the title so it will pick up that particular test
7:50
7 minutes, 50 seconds
from the file and it will start executing so you can see it is now running the test so while it is running let us go and check the next command
7:59
7 minutes, 59 seconds
so here this is the next command so if you want to run on on a specific
Chapter 8: npx playwright test --project=chromium runs on specific browser
8:06
8 minutes, 6 seconds
browser you can say hyphen hyphen project and give the browser so i can say npx playwright
8:14
8 minutes, 14 seconds
playwright test and then i will use the option hyphen hyphen project
8:22
8 minutes, 22 seconds
and i will say chromium and hit enter and this time you will see it will execute on a single browser so
8:30
8 minutes, 30 seconds
you can see running one test using one worker and it is running on that particular browser only if i check the report now
8:38
8 minutes, 38 seconds
you will see that the execution has happened on a single browser so here you can see a single test card
8:45
8 minutes, 45 seconds
executed if i see and go inside you can see it's only it has executed on chromium only
8:52
8 minutes, 52 seconds
so you can select a browser like this then if you want to run in a headed mode headed means you will see the physical
Chapter 9: npx playwright test --headed runs tests in headed mode
8:59
8 minutes, 59 seconds
browser by default all execution is done in a headless mode that is no gui no physical browser comes up on the screen
9:07
9 minutes, 7 seconds
it happens at the back end and it is good for automation it saves a lot of time and memory but still if you want to see you can use the
9:15
9 minutes, 15 seconds
option headed so i can say here let me stop this control c and y clear
9:24
9 minutes, 24 seconds
i can say i want to use chrome and then i will say hyphen hyphen headed so i want to run in
9:31
9 minutes, 31 seconds
a edit mode and i will press enter and now you will see the physical browser on the screen so you can see it is now running it was very fast because in the
9:40
9 minutes, 40 seconds
test it just goes to the playwright website and checks the title so you can see the browser has come up
9:48
9 minutes, 48 seconds
browser was up and we could see the test running now the next is the debug option so whenever you want
Chapter 10: npx playwright test --debug debug tests
9:56
9 minutes, 56 seconds
to troubleshoot you want to debug you can use the hyphen hyphen debug option now i will have a separate video on how
10:04
10 minutes, 4 seconds
to troubleshoot and debug and we will see more options there but for now if i have to debug i can say
10:11
10 minutes, 11 seconds
npx playwright test and let us say i just want to use chrome only and i will say debug now
10:19
10 minutes, 19 seconds
in debug because we have to see and then we have to watch and then troubleshoot therefore by default when you run in a
10:26
10 minutes, 26 seconds
debug mode it will run in a headed mode that is the browser will come up so if i press enter you will see the browser
10:33
10 minutes, 33 seconds
will come up and it will run our test and now you will see it has actually paused
10:41
10 minutes, 41 seconds
it has not gone forward it has just opened the browser and you will see here a playwright inspector window has opened
10:48
10 minutes, 48 seconds
so this is a playwright inspector and you can see here it highlights the step where it has
10:56
10 minutes, 56 seconds
paused and then we have all these options so we can resume we can pause we can step over step over means going to the next step so we can do step by step
11:05
11 minutes, 5 seconds
debugging so i will click on this step over and you will see it goes to the next step and it has gone to playwright.dev the next step is it will
11:13
11 minutes, 13 seconds
uh check for the title i will again say step over and it has gone next step and then again next and then it will click
11:22
11 minutes, 22 seconds
on get started and then the last step and then it will stop so this is how you can do debugging
11:30
11 minutes, 30 seconds
and in debugging we can create breakpoints we can make breakpoints in our script and then do debugging all that i will show you in the debugging session
11:39
11 minutes, 39 seconds
and then we can debug a specific test file so all these options we can also use most of these options we can use
Chapter 11: npx playwright test example.spec.js --debug debug specific test file
11:47
11 minutes, 47 seconds
along with each other for example here this is the command to run a specific file and then we have used debug with it so this also we can do
11:56
11 minutes, 56 seconds
then uh here we have
12:03
12 minutes, 3 seconds
a option if you want to debug starting with a specific line or a specific test then we can use colon and the line
Chapter 12: npx playwright test example.spec.js:21 --debug debug starting from specific line where test(.. starts
12:12
12 minutes, 12 seconds
number and the line number should be the start of some specific test let me show you this is very interesting i will go
12:18
12 minutes, 18 seconds
to my test file and this is my test let me copy this test and paste it again in the same file so that you will
12:26
12 minutes, 26 seconds
come to know exactly what is happening so i have copied and pasted the test in
12:34
12 minutes, 34 seconds
the same file and in the this copy test i will change the title i will say this is
12:42
12 minutes, 42 seconds
demo test and i will save by pressing ctrl s or you can go to file and then save from here now
12:50
12 minutes, 50 seconds
in the and you can see this test starts from line number 23 so now i will go to
12:57
12 minutes, 57 seconds
the terminal and now i will say i will go to the earlier commands and here
13:05
13 minutes, 5 seconds
i will point to a specific test file
13:12
13 minutes, 12 seconds
so i will say i want to go to tests folder and then i want to run this example dot
13:19
13 minutes, 19 seconds
spec dot js file and then i will say colon 23 so i want to start debugging from the test which
13:27
13 minutes, 27 seconds
starts from line number 23 and i have already used the debug flag debug option here so let us start
13:35
13 minutes, 35 seconds
and let's now see so you can see it is running a single test not two tests because uh there were two tests in the file but it is not taking the earlier
13:43
13 minutes, 43 seconds
test it is running the single test and if you see the inspector the playwright inspector you can see it has skipped the
13:50
13 minutes, 50 seconds
earlier test and it is now starting with this test that is our demo test so this also you can do
13:57
13 minutes, 57 seconds
and i will press ctrl c to stop this and then we have commands to record our test that all we will run when we learn
14:06
14 minutes, 6 seconds
how to write the test and these are all the commands if you want you can take a screenshot of this screen keep it handy with you on your mobile or desktop
Chapter 13: All commands screenshot
14:15
14 minutes, 15 seconds
screens and go through it several times so that you will understand all these commands and as we go along this session you will remember all these commands i
14:24
14 minutes, 24 seconds
hope this was very useful for you if you have any questions you have any doubts you can let me know in the comment section do take the quiz the link will
14:31
14 minutes, 31 seconds
be in the description and i will see you in the next session thank you for watching and never stop learning
14:45
14 minutes, 45 seconds
you
