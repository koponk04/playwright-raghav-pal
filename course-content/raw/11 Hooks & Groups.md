Chapter 1: Intro
0:01
hello and welcome to this session I am raghav and today we are going to learn Hooks and groups in playwright this is
0:08
8 seconds
going to be very easy and very interesting and I will go very basic step by step we will see what are Hooks and how do we use hooks in playwright
0:16
16 seconds
tests we will see what are groups how do we group our tests in playwright and we will see a Hands-On demo step by step
0:23
23 seconds
Hands-On demo so let's get started and uh in playwright or in general as well we have hoax where we can make some
Chapter 2: What are Hooks
0:32
32 seconds
tests or some steps done before all our tests before each of our tests after all our tests or after each of our tests so
Chapter 3: How to use Group and Hooks in Playwright
0:42
42 seconds
let me show you a demo I'm going to my playwright project here and here I'm going to create a new test
0:50
50 seconds
a new test file so in this tests folder so I have my test folder here and I will
0:58
58 seconds
create a new file I'll right click and say new file and I will name it as
1:04
1 minute, 4 seconds
Hooks and groups dot spec dot Js
1:11
1 minute, 11 seconds
you can name anything and here I will say import at the top I will import test and
1:19
1 minute, 19 seconds
expect from playwright
1:27
1 minute, 27 seconds
and now I will very quickly create a test I will say test and I'll give some title let us say I want to create a a
1:35
1 minute, 35 seconds
login test so I'll go to some demo website I'm going to this source demo.com and here is a login page
1:44
1 minute, 44 seconds
and I can use these usernames and password so I'm just going to this I will say
1:52
1 minute, 52 seconds
test this is the login test and I will use the async function and in the async
2:01
2 minutes, 1 second
function I will pass the page fixture and I will complete the test block
2:10
2 minutes, 10 seconds
and here I will say await page dot go to
2:18
2 minutes, 18 seconds
and I will use the URL of the application which is sourcedemo.com now I can manually add
2:28
2 minutes, 28 seconds
all the steps I can manually find the locators and then add all the steps as we have learned in the earlier sessions but now because we already know that I
2:36
2 minutes, 36 seconds
can use playwright inspector we have seen that in the earlier session where we learned how do we record so we can use a playwright inspector and then
2:44
2 minutes, 44 seconds
record rest of my steps and for that I will have to use a pause here I will say page dot pause I can record it
2:51
2 minutes, 51 seconds
separately as well but I will just save some time I will pause the test which will open the playwright inspector and then I will record the rest of the steps
2:59
2 minutes, 59 seconds
here so I will save this and now to run I will open a terminal and I will say here
3:08
3 minutes, 8 seconds
npx playwright test and then I will give the test file
3:17
3 minutes, 17 seconds
location which is under the tests folder I am typing tests and I will press tab on my keyboard so it will auto complete
3:24
3 minutes, 24 seconds
and here I will say Hooks and again I will press Tab Key so it should auto complete the file name
3:31
3 minutes, 31 seconds
and now this will run this particular test file which I have created here but this will run on all the browsers I just want to run on a single browser for now
3:40
3 minutes, 40 seconds
so I will say hyphen hyphen project and I will say chromium
3:48
3 minutes, 48 seconds
and then I will say I also want to run in a headed mode so that I can see the
3:56
3 minutes, 56 seconds
rewrite inspector and then I can record so I will say hyphen hyphen headed so this is hyphen hyphen it is coming in
4:03
4 minutes, 3 seconds
the next line I hope you can see this I hope you can see it now it is hyphen hyphen headed so the command I have used
4:11
4 minutes, 11 seconds
is this npx playwright test then the file location hyphen hyphen project chromium space hyphen hyphen headed I
4:19
4 minutes, 19 seconds
will run this and let us see so this should open the Chrome browser and go to the application and yes you
4:28
4 minutes, 28 seconds
can see as it encountered the pause statement it has paused and opened the predite inspector and now I can click on
4:35
4 minutes, 35 seconds
the record and record my rest of the steps so I'll click on record and I will add the username I am using this username that is
4:43
4 minutes, 43 seconds
standard underscore user and then the password the password is mentioned here Secret Sauce so I will
4:51
4 minutes, 51 seconds
say secret underscore let's say u c e source and I'll click on login and that's it if I go back to the
5:00
5 minutes
playwright inspector all these are recorded I will stop the recording and now I will copy the steps I can use this copy button which will copy everything
5:08
5 minutes, 8 seconds
but I just want these steps so I'll just manually select and copy from here yes this is what I need I will copy and
5:17
5 minutes, 17 seconds
add to my test script here so I'll go here
5:24
5 minutes, 24 seconds
and after this first step I will just paste it here I can do a right click and
5:30
5 minutes, 30 seconds
say format document to correct the formatting and for now I will also remove all these comment statements or
5:39
5 minutes, 39 seconds
comment steps I am clicking inside the comment and pressing Ctrl X on my keyboard if you're on Mac you can press command and X key
5:48
5 minutes, 48 seconds
so this will remove the entire line and that's it so this is my test now and it is going to this URL and then clicking
5:56
5 minutes, 56 seconds
on the username adding the username I don't want to click I just want to add so I can remove these click on username and password box as well so I have now
6:05
6 minutes, 5 seconds
my test here it enters username and password clicks on the login button and then checks that the application is
6:13
6 minutes, 13 seconds
navigated to this page and after that I will also close the page so I will say page Dot close I no longer need the pause so I will say play page Dot close
6:21
6 minutes, 21 seconds
and now let me run again I will press I'll go to the terminal and to stop this process I will press Ctrl C on my
6:29
6 minutes, 29 seconds
keyboard I will say bye so that it terminates the job and now I have my
6:40
6 minutes, 40 seconds
terminal ready I am pressing the top arrow on my keyboard to bring up the last command and now I will run this command let us
6:47
6 minutes, 47 seconds
see now it should now run the complete test the login test so yes it is it was very fast but it has completed and you
6:54
6 minutes, 54 seconds
can see here it says one passed now let us say I want to run one more test I want to create one more test which is I
7:02
7 minutes, 2 seconds
want to go to my home page and we want to do some actions on the home page and that I will do only after login so I'm creating one more test here
7:10
7 minutes, 10 seconds
I am saying test and I am giving the title as home page and again I will use the async function
7:19
7 minutes, 19 seconds
inside the async function I will pass the page fixture and then complete this test block
7:28
7 minutes, 28 seconds
and now here I will first have to do all the login steps so I will say
7:38
7 minutes, 38 seconds
I'll copy all these steps again and then at the end I will
7:47
7 minutes, 47 seconds
say page dot pause I will remove the close and say page dot pause so it will pause here and then I will record the
7:54
7 minutes, 54 seconds
steps on my home page also this time I just want to run this home page test so I will say test dot only this is The annotation we will learn more about
8:02
8 minutes, 2 seconds
different annotations in the next session but just for now I just want to run this particular test in this file so
8:09
8 minutes, 9 seconds
I'm saying dot only here so it will only run this particular test I will run the test again I will run the
8:17
8 minutes, 17 seconds
command again to run this test file which will run the home page test and yes I'm on the home page and now it
8:27
8 minutes, 27 seconds
has opened the playwrite inspector I will click on record and I will do some recording here
8:33
8 minutes, 33 seconds
so let us say I'll click on add to cart add to cart I'll go to this
8:40
8 minutes, 40 seconds
item and again say add to cart and that's it I'll go back to my playwright inspector
8:48
8 minutes, 48 seconds
and I will just stop the cutting and then copy all these steps so I'll just
8:55
8 minutes, 55 seconds
copy these steps from here and go back to my test script
9:02
9 minutes, 2 seconds
and after logging in I am pasting all these steps I am removing all these comments by pressing Ctrl X on my
9:12
9 minutes, 12 seconds
keyboard and I will do a right click and say format document to correct the formatting
9:20
9 minutes, 20 seconds
and here it is clicking on all these uh items on the home page and then it is
9:28
9 minutes, 28 seconds
waiting for this URL and then all this is fine I will also say page Dot
9:35
9 minutes, 35 seconds
close at the end and that's it now this is home page let me create one
9:43
9 minutes, 43 seconds
more test for logout so I'm creating one more test here I will say test and the title is
9:50
9 minutes, 50 seconds
log out and the async function
9:57
9 minutes, 57 seconds
and I will pass the page fixture and I will complete the test block now I
10:04
10 minutes, 4 seconds
have to just log out after uh wherever I am on the on any page so let us say I will first have to login again
10:12
10 minutes, 12 seconds
so that I can go inside the application and then I can log out
10:18
10 minutes, 18 seconds
so I'll copy the login steps again and then I will again say here
10:29
10 minutes, 29 seconds
of it page dot pause so it will pause and I
10:36
10 minutes, 36 seconds
can then record the login steps and I will say dot only and I will remove the only annotation from the earlier test
10:45
10 minutes, 45 seconds
so that it does not run this one and only runs my logout test and I will go to my
10:52
10 minutes, 52 seconds
terminal this process is already running so I will press Ctrl C and I will terminate the job and then I
11:01
11 minutes, 1 second
will say clear and I will run the command to run the tests
11:08
11 minutes, 8 seconds
and let's see now so yes it is running and it will pause here after login so I will record the
11:17
11 minutes, 17 seconds
steps so I have to click here on this menu and then click on log out and that's it I will go back to the
11:25
11 minutes, 25 seconds
playwrite inspector stop recording and copy these steps
11:35
11 minutes, 35 seconds
go back to my test and paste these steps here
11:42
11 minutes, 42 seconds
so you can see these are the steps and then it is also checking that it is navigated
11:49
11 minutes, 49 seconds
after logout to this particular URL which is fine and I will say page Dot close
11:56
11 minutes, 56 seconds
so I have created three tests here and everything is fine let me remove the only annotation so that now it should
12:05
12 minutes, 5 seconds
run all the three tests so these are the three tests login home page and log out I will go to my terminal
12:19
12 minutes, 19 seconds
and run the command to run this test file and let us see now it should run three tests login home page and log out
12:28
12 minutes, 28 seconds
so it is running the three tests that was login this is home page test and now the log out test uh
12:36
12 minutes, 36 seconds
I think the logout test fails let me see what is the issue here if I expand this okay uh I have to remove this as well
12:45
12 minutes, 45 seconds
this is not required here the browser context it got copied from the playwrite inspector but I don't need that
12:54
12 minutes, 54 seconds
so I'll remove this step and let me now run the
13:02
13 minutes, 2 seconds
tests again and check so this is running the tests the first
13:10
13 minutes, 10 seconds
test login the second test home page and now this is the log out test and now everything is running fine and you can see we have got all the three tests have
13:19
13 minutes, 19 seconds
passed and this is all running fine now now uh here
13:26
13 minutes, 26 seconds
you can now see we are repeating the login steps in all the tests so in the login test we
13:34
13 minutes, 34 seconds
anyways need to login but when we go to home page we again have to repeat the login steps when we go to logout as we again have to repeat the login steps
13:43
13 minutes, 43 seconds
there as well so what I can do is I can go to my login test and here I can give
13:49
13 minutes, 49 seconds
the hook I can say dot before and we have before all and before each I want
13:57
13 minutes, 57 seconds
to run this test before each test so that it can log into the application and then do the rest of the test so I will say before each
14:04
14 minutes, 4 seconds
and when I say before each I do not have to give the Title Here I just have to say the use
14:12
14 minutes, 12 seconds
the async function with the page fixture and I will also remove the close I can comment I am pressing Ctrl forward
14:21
14 minutes, 21 seconds
slash or I can just press Ctrl X and remove the close steps the close page step so this is my before
14:29
14 minutes, 29 seconds
each hook now which is having the login steps and this means this this
14:36
14 minutes, 36 seconds
particular function will run before each test of this file so that it will run before home page and it will also run
14:43
14 minutes, 43 seconds
before the log out so now I can remove the login steps from the home page test so I'm removing all this from here and I
14:52
14 minutes, 52 seconds
will also remove the login Steps From the log out page test so you can see this is my logout test only having the
15:00
15 minutes
log out steps this is my home page test only having the home page steps and then if you see after the test we are also
15:08
15 minutes, 8 seconds
closing the page in each of the test I am saying page dot flow so this also I can put into a hook
15:15
15 minutes, 15 seconds
I can create one more function I will say test dot after now we have after all and after each I want
15:24
15 minutes, 24 seconds
after all the tests are done I want to close the page so I will say after all and again I will use the async function
15:32
15 minutes, 32 seconds
having the page fixture and I will put this
15:41
15 minutes, 41 seconds
after page Dot close inside this function which is the after all
15:50
15 minutes, 50 seconds
hook and now I can remove it from here and also remove it from here so basically this file now has two tests that is
15:58
15 minutes, 58 seconds
home page and lockout and these are the hooks which are being used here let us first run and check if everything is
16:05
16 minutes, 5 seconds
working fine so I will now go and run the tests and let us see this time
16:14
16 minutes, 14 seconds
we will also see the report after running and see if these hooks are shown there so you can see everything is working fine this was home page and this
16:23
16 minutes, 23 seconds
is now the log out everything is running fine let me see the report by running the command show report
16:34
16 minutes, 34 seconds
and yes you can see here now we have home page and logout if I go to home page test here we have the before hook
16:42
16 minutes, 42 seconds
and you can see this before hook here and we can see all the details here and all the steps here and then at the end
16:51
16 minutes, 51 seconds
you will see the after hooks so we I have the after hooks here we have the
16:58
16 minutes, 58 seconds
here all these closing the page here and similarly if you want you can see
17:07
17 minutes, 7 seconds
the other test and you will see the before and after hooks here as well so this is the after all hook and here
17:15
17 minutes, 15 seconds
you can see all the details of this hook so this is how we can use these hooks now as of now we have not grouped our
17:24
17 minutes, 24 seconds
test if you see here we have directly added our tests inside the file but it may happen a lot of times that you want
17:31
17 minutes, 31 seconds
to run a particular group with some different types of hook for example your test file can have uh many tests let us
17:38
17 minutes, 38 seconds
say for example your test file has 10 tests after out of these 10 tests you want to group five tests and you want to
17:45
17 minutes, 45 seconds
have a separate or before each before all after each or after all hooks for those set of five tests in that case you
17:53
17 minutes, 53 seconds
can group these tests using the describe block and for that you can say I will create a describe block I will
18:00
18 minutes
just say describe let me say test Dot describe
18:12
18 minutes, 12 seconds
and then I will give some title I will say all my tests you can give any Title Here
18:21
18 minutes, 21 seconds
and then just give a function declaration here we are not using uh you know any async function or not passing any fixture just a function declaration
18:30
18 minutes, 30 seconds
and that's it so this is a describe block and all the tests you want to group under this block you can put inside this describe block so for now I
18:38
18 minutes, 38 seconds
will just uh remove these end brackets of the describe group or the describe block and put it at the end so that all
18:47
18 minutes, 47 seconds
these tests become a part of this describe group I'm putting it here and I will also do a
18:54
18 minutes, 54 seconds
right click and say format document and now you can see all these tests are inside this describe group if I expand
19:04
19 minutes, 4 seconds
this all these tests are inside the inside this described group and now this before each after all all these hooks
19:12
19 minutes, 12 seconds
will work only for the tests inside this describe group if I have more tests here after the described group it will not
19:20
19 minutes, 20 seconds
work for them so let us see I will run my tests again I'll run the
19:27
19 minutes, 27 seconds
file again and let us see now in the report as well it will show that all these tests are under the under a
19:34
19 minutes, 34 seconds
group so it is all running fine and you can see all the hooks are running properly and if I now see the report I
19:42
19 minutes, 42 seconds
will say show report and here in the reports you can see all my tests this is a group so here you can
19:50
19 minutes, 50 seconds
see all my tests home page all my tests log out if I go inside you can see all these hooks as well here everything is here
19:59
19 minutes, 59 seconds
and all these eyes working fine so this is the log out
20:06
20 minutes, 6 seconds
and here also you can see before after hooks as well so this is all this is all working fine and this is how we can use
20:13
20 minutes, 13 seconds
uh Hooks and groups now uh a little more about these uh hooks so these are the hooks we have seen
20:22
20 minutes, 22 seconds
before all uh before each after all after each these are the good these are the hooks we can use when we use the
Chapter 4: Organising & Grouping Tests
20:28
20 minutes, 28 seconds
before all hook it will execute before all the tests in the file and if you use this grow this particular hook inside a
20:37
20 minutes, 37 seconds
describe block then it will run before all the tests of that particular describe block or describe group and if
20:44
20 minutes, 44 seconds
you use multiple before all uh blocks or multiple before all sections they will run in order of their registration as
20:51
20 minutes, 51 seconds
you have created them they will run in that order as only in the file similarly before it runs before each test if it is
20:59
20 minutes, 59 seconds
uh created at a file level it will run before each test of that file if it is inside a described group it will run
21:06
21 minutes, 6 seconds
before each test of this group and again it will run in order of registration if more than one before each uh blocks are there or before each hooks are there the
21:15
21 minutes, 15 seconds
same goes for after all and after each hooks so this runs before after all the
21:22
21 minutes, 22 seconds
tests or after all the tests in a group after uh each will run after each of the test in a file or after each test in the
21:31
21 minutes, 31 seconds
group if it is inside a group and it will run in order of registration if there are more than one hooks used so
21:38
21 minutes, 38 seconds
this was about Hooks and uh organizing test using describe group I will tell you more about annotations and tags in
21:47
21 minutes, 47 seconds
the coming session I hope this was useful I will see you in the next session thank you for watching and never stop learning
