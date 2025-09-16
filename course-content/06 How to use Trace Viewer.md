# Chapter 1: Intro
0:02 and today we are going to learn something very important and very very interesting in testing in automation
0:10 whenever we have any failure whenever our test fails one of the very important things is we need to find out and figure
0:17 out why exactly this failure happened what was the error or what exactly happened at the time of the failure or
0:25 what was the screenshot of our application what was the state of our application we want to see all the snapshots and the exact time the
0:33 timeline and all the details at that particular moment when when the failure happened so that is exactly what we are
0:40 going to solve today using Trace viewer in playwright so we are going to see what is Chase viewer we will see how to
0:47 use test viewer with all the options all the command line options uh different ways to view Trace in playwright we will
0:55 also learn how to set a tracing programmatically that is into our code and then after watching this session you
1:02 can take the quiz you will find the link in the description below this video so with that let's get started and let us see what is Trace viewer so Trace viewer

# Chapter 2: What is Trace Viewer
1:10 in playwright is a GUI tool that helps us to uh view our test after it has got
1:18 executed we can go back and see how the test got executed what was the snapshots the timelines all the screenshots all
1:26 the details all the environment details all the network details and everything about our test and that is why we call it as Trace that like we are tracing the
1:35 test that has been executed with all the details now uh here you can see this is a screenshot of the trace viewer and let
1:42 me show you the exact Trace here so you can see this is the trace viewer this is a GUI application and here you can see
1:50 uh this is one of the tests that I have bought I have executed and you can see at the top there is a timeline and as I go through the timeline you can see the
1:59 application screenshot the state of the application at every point you can see from here and then you can see all these
2:07 steps here so you can see here we went to the browser here we went to the application and then you can see the screenshot of the application the
2:15 snapshot you can also see action before and after state so let me show you on any click event this will be very interesting to see let us say this click
2:24 on logout button here you can see the action when you go to the action you can see exactly where did the action happened and you can see this red dot
2:33 here and then if I say before so it shows the state of the application before this action and then after you
2:42 can see this was the state after so it got logged out and we can see the screen here you can see all the call all the details console Network and the source
2:50 uh where exactly from where exactly uh this was executed so this is the line that got executed here so this is
2:59 something very very useful very very important end and in a moment you will be able to see this case viewer for your
3:06 test so let's get started let me stop this Trace viewer now and now

# Chapter 3: How to use Trace Viewer
3:14 let us see how to use Trace viewer and we will go step by step step number one is we can open our config file and set
3:22 the property and option for Trace now I will tell you exactly I will tell you the other options as well how you can do
3:30 it from the code itself or how you can do it from the command but let us start with the config file so I will go to my
3:37 vs code and I will go to my project
3:44 so this is my project and in your project you will find this config file that is playwright.config so I will go to this config file and
3:53 here let us see the trace option or configuration so here if I
4:00 scroll down you can see here is the trace configuration and it is set on first retry that means whenever a test
4:09 will be retried then it will uh have this Trace enabled and it will capture the trace of the test and there are
4:17 other options that I will show you there are options that you can keep it on permanently so it will keep tracing every execution you can only trace on
4:26 failure or you can trace on the first three try or you can keep it off permanently so let us go with this Trace
4:34 is on first retry and then uh if I have to get the trace only on the first retry
4:40 I should also have the retries set to at least one so I will just say retries
4:48 and I will say one here already there is retry for the CI environment let me
4:55 comment this out I am pressing control and forward slash on my keyboard to add a comment here so this is commented out
5:03 and now I have recharized one and the trace is set to on first retry so now we have already discussed this will
5:11 collect the trace only when retrying for the first time now let us run our test and let us run a test to fail so let me
5:20 go to any of my tests let us go to uh this was the test we recorded in the record demo when we learned how to
5:27 record so here we are going to this source demo.com application and we are clicking on the username adding the
5:35 username and then adding the password and then clicking on the login button so let us say I will uh change the selector
5:43 for the login button I will just add here something like one two three which will make it a invalid
5:50 locator invalid selector and now I will try to run this so this is the name of this file is
5:57 record one hyphen uh demo dot spec underscore demo.spec all right so let me
6:05 run this and we have already set the configuration make sure that you save the configuration file and now I will go to the terminal
6:13 you can go from here or just press Ctrl and J on your keyboard Control Plus J it will bring up the terminal and here I
6:21 will say npx playwright test and the test file I want to run is
6:30 our record okay it is I think it has gone to the
6:37 test results folder that is not what I want I want to go to the tests folder and then from here I want
6:46 to run this record one underscore demo Dot spec.js and if you want you can also run in a headed mode so that you can see
6:53 the execution on the browser so browser will be in a headed mode that is you will see the physical browser so it is
7:01 running and you can see here it has entered username and password and now it will try to click on the login button
7:09 but because the selector it will not find the login button we have already added our invalid selector
7:16 so it should fail now the other thing is uh let me just stop this for now what I want to do is
7:25 I'm pressing Ctrl C and I will stop this for now
7:37 okay so what I want to do is because you can see whenever there is a failure it is waiting for a long time I can decrease the time out again I will go to
7:45 the config file and this is optional I am doing this just for this demo so the timeout is 30 into 1000 here which I
7:54 will change to 10 into 1000 which will be like uh 10 000 milliseconds like 10 seconds and here also I can change this
8:02 timeout for expect to something like 3000 milliseconds that will be three seconds and now I will run
8:10 again so I will say here I am pressing the top arrow on my keyboard to go to the last command and I will just say hyphen
8:19 hyphen project if I want to run on a single browser I will say project
8:27 chromium so it will only run on Chrome so that we will save some time in the demo so let's see now
8:34 so it has started the test and it will only run on this browser so you can see it has added username and password and
8:41 now waiting for the login button or waiting for the object with the selector that we have which which will fail so
8:49 now you can see it is retrying one time because we have set retry count to one in our config file so now it is daytime
8:56 and now it should also uh get the traces so it has completed and now if you see the report
9:04 it has already opened the report you can see this is the initial run the for the primary run and this is the retry so we
9:11 have got the retry as well as the Run results and here you can see it has failed here and here
9:19 also in the retry it has failed now if you see in the retry if you go to the retry execution and you see here you can
9:28 see there is a traces here so there is a section for traces and you can click
9:35 here and it will open the trace uh GUI tool or you can download the trace zip file from here now before doing that let
9:44 me show you I will go to the next step which is after running you should check
9:51 that chase.zip file is created under the test results folder so you can go to your project and there should be a test results folder now and under the test
9:59 results folder you should find a trace dot zip file and if you physically go to
10:07 this folder on your system I will say reveal in file explorer you can see this is the test results and here because we
10:14 have executed for a single browser therefore we have a a trace only for Chrome otherwise if you had executed on
10:22 multiple browsers you will have multiple Trace files and you can see this is the trace dot zip now there are different ways to view this one of the ways is you
10:31 can directly go to your result and click on this traces and you can see this is our
10:37 Trace viewer tool the GUI tool and here as I have shown you at the top we have the timeline and you can also see the
10:45 steps here so you can see this is the browser contacts this is this says go to this page then here it says click
10:54 on this locator then here it says fill this username and you can see the username is added here now as you can go
11:03 in the timeline you can see this happening okay and then here you can see the metadata where you can see the start
11:11 time and time duration all the environment the browser the platform uh the screen size viewport all these
11:19 details you will get and in the actions you can see all these steps so here it went to the URL and you can see the
11:26 screenshot here then here you can see it clicked on this username box and here you can see the
11:35 before and after screenshots then here it fills the data username so you can see this was the action this was the
11:42 before screenshot and in the after screenshot we have this username added also if you come here to the right side
11:51 here you can see the call details here we have all this duration parameters all the logs this is the console if you have any
12:00 anything in the console you will get it here and this is the network details so if you have any details for the network you can see here in this case there were
12:09 so many requests that went to the server all these API requests you can see you can see all the details here you can
12:16 expand and see all the details and then in the source you can see the exact code of our test and it will highlight the
12:24 steps that got executed here Okay so
12:32 you can see here this will now become very easy to troubleshoot this was our step and here you can see the action
12:40 so the action is it will click on this login button and it it has a red dot but it is kind of
12:48 invisible because the background also is red otherwise you will see this red dot wherever it is clicking so you can see you see it like this and then you can
12:57 see the before and the after and then you can see all the details so this is how you can get the trace and now this
13:07 was how you can get it from the HTML report but if you do not have the HTML report or you don't want to get it from there you can also directly open the use
13:16 the trace.zip file and use the command npx playwright show hyphen trace and the location of the trace zip file so let me
13:25 show you this I'm going to close this now and I am also going to stop the stop serving the HTML report
13:34 and now I will say npx playwrite
13:42 and I will say show hyphen Trace and then the location of the trace file so our Trace file is under this test
13:51 results so I will say test hyphen results and then we have this uh this folder and then we have this
13:59 Trace dot zip file now see I'm I just type the first few characters and then I press Tab and it is auto completing the
14:07 name and you should also do this this is just for beginners so that you do not make any typo and you can be very fast in writing these commands so I will hit
14:16 enter and let us now see it should bring up the trace viewer application again and yes you can see the same Trace
14:23 viewer is again here and again you will see all these details so this is how you can view the trace

# Chapter 4: Screenshot moment
14:31 you can create and view the chase now the other options we have we have already seen this on first retry it will

# Chapter 5: Trace Viewer Options
14:39 record the trace only when retrying only for the first time then if you want to keep it off permanently you can keep it off you can say off in the config file
14:48 or or from the command you can keep it permanently on but make sure if you do this it will hamper the performance
14:55 because it will keep on tracing every test every step it will keep on taking all the snapshots screenshots so it can
15:02 be uh it can it will be heavy on performance then retain on failure this can be a very common option using uh for
15:10 using traces because this option will record a trace it will record for each test but it will remove from the
15:18 successful test run so let's say you have you have executed all your tests at the end when you will see you will only find traces for the failed tests and
15:27 that is what we want we want to see what exactly happened what was the issue only for the failed tests and you can also set Trace from the command if you do not

# Chapter 6: Screenshot moment
15:36 want to set it from the config file you can set it from the command line and this is the command this is our normal command that is npx
15:44 playwright test along with this we can add the option hyphen hyphen trace and then we can use any of these options on
15:51 off on first three try retain on failure we can use here okay so this was interesting now let us

# Chapter 7: Different ways to view trace
15:59 say we see different ways to view the test we have already seen the command line way we have already seen the HTML report way that is you can directly see
16:08 uh you can view the trace from HTML report and from the HTML report you can also download the trace zip file we have already seen these two options the third
16:17 option is using this utility Trace dot playwright.dev so you can directly go to this link on your browser
16:25 trace.playwright.dev so let me show you I will go to my browser and I will go to trace dot playwright uh
16:34 dot Dev uh Chase Dot playwright.dev
16:42 this is the link and here you can just drag and drop your Trace zip file or you can also
16:51 browse from here so in my case let me go to the folder where I have my Trace dot zip file it is here I'm just going to
16:57 drag and drop it here I will drag and drop it here and you can
17:04 see we have got our Trace viewer so this is the third option so these are the different ways you can view the trace
17:11 now how to set trays in the code programmatically so this is very uh

# Chapter 8: How to set Tracing programmatically
17:18 important so I'll just go here I'll go to my project and
17:27 here let us say I will go to a different file let me go to this
17:35 example.spec.js this this is the file everyone will be having because this is the default example file that comes
17:43 along with playwright installation so here I can say I can add the step here so you can see
17:53 we normally add the page fixture we can also pass the context picture fixture here which is the browser context and
18:01 then using this context we can say context dot tracing dot start and we can give the options like snapshots through
18:09 screenshots true and then we can have our test code and wherever we want to stop we can say context dot tracing dot
18:17 stop and we can give the location and name of the trace zip file so wherever you want to start you can start the
18:25 tracing and wherever you want to stop you can stop the tracing so let us try this I am going to this
18:32 test file and I will say here at the start of the test
18:40 let me make this title of the test shorter so that you can see this
18:50 part as well so here where we are passing the page fixture I will say comma and I will also pass the context
18:57 fixture and this is the browser context if you hover over it you can see all the details for this context
19:05 and then let's say I want to start at the start before we start our steps
19:11 so I will say here await context dot tracing dot start await
19:19 context dot tracing you should also see all these order suggestions otherwise you can press control plus space on your keyboard to get the auto suggestion box
19:27 and I will say start and then I will give the options so I will say here so the options we can give
19:36 is snapshots screenshots so I will say snapshots you can see we are getting these options and I will say true
19:44 and then I will say screenshots and I will say true okay and if you want to see the
19:53 difference if you hover over the snapshots you can see this will capture the Dom snapshots on every action so if you have seen in the trace viewer we
20:02 could see the before after action all these what was exactly the snapshot before what was exactly the snapshot of the application after this action all
20:10 that is coming from snapshots and in the screenshots this will capture the screenshots during tracing now uh this
20:18 is the code and if you like you can put this in a in the next line for easy readability
20:26 so I can do like this I can put all this in different lines so that it is very easy to read and you can
20:34 also do a right click and say format document or press shift plus alt plus F to correct all the formatting and you
20:42 can save so this code this program this command will start the tracing and then wherever you
20:50 want to stop so I want to go to the end and then here I want to stop the chasing so again I will say
20:58 a weight context dot chasing dot stop
21:09 and here in the options I will pass the path that is where I want to
21:18 store the file so let's say I will say you can give any name so I will say
21:30 test one dot zip or I can say test one underscore
21:39 Trace dot zip and that's it all right
21:46 and that's it so I am uh getting I'm I want to get trace for this particular test let us now go to the terminal
21:55 and I will run it now so here
22:03 I will say npx make sure that you save the file and I will say npx
22:12 playwrite test and I want to go to a particular file so I will give the location of this
22:21 example.spec.js and this time I'm just running it in the Headless mode with all the browsers so because there are two tests so it is
22:28 running uh this that is fine because it will overwrite the earlier test file on Avenue execution that is why it is
22:37 showing me this okay so it is running
22:44 and let's just wait and check if we get the trace file
22:52 and this is done and now if I go and check
22:59 uh let me expand this terminal window and clear everything and I will say LS to list out
23:07 all the contents and you can see Trace one test one hyphen Trace dot zip is created and it is here you can see here
23:15 and to check it to view the trace I will say the command npx play right
23:23 and I will say show hyphen trace and then I will give the name of the or location of the file along with name
23:31 which is test one Trace dot zip and I will hit enter let us now see
23:39 so it opens the trace viewer and yes you can see and because here it had gone to the playwright.dev application so you
23:47 can see all the all these screenshots and all the snapshots and if I go to this step which is clicking on this get
23:57 started you can see it is highlighting this get started and if I see the before snapshot this was before the snapshot
24:04 before the section and the after snapshot you will see it will go to that particular link so let me see here
24:14 action before and after it has gone to this intro and you can see all the details here and here you can see all
24:23 these details so you can do like this and then uh this we have done within a test now if you like uh normally in
24:32 Practical uh in in real world scenario you may not want to add these these codes for starting the phrase and
24:41 stopping the trace with every test you may want to do it once at a global level uh at a file level mostly so you may
24:48 want that when you are at the top of your file you may start the trace and at the end of the file when all the tests are executed you can then stop the
24:57 tracing now we can use hooks here we can use before all and after all hooks now until this lecture in this series we
25:04 have not yet discussed about hooks I will have a separate session uh on hoax what are hooks how do we use them but
25:12 for now let us just see the before all and after all hook and that simply means if you want to run something if you want
25:20 to do something before running all the tests we can use before all hook and if you want to do something if you want to run something after all the tests are
25:28 completed we can use the after all hook so here I will say I will go back to my project
25:37 and I will say here in this file itself that is
25:46 example.spec.js I will create a hook I will say test Dot before all and here
25:57 I will just use this async function and I'll say async
26:07 and here I will pass the browser context or the browser fixture
26:14 because for this uh before all and after all hooks we don't have the page or the browser context directly that we can
26:22 pass in a test we cannot do that so therefore I am passing this browser and then
26:29 I will again use this declaration like this so we have created a before all function
26:37 like this and here I will say I will have to declare a context
26:45 a variable called context so I will say at the top let context and then
26:53 in this function I will say context is equal to browser.new context and then I
27:00 can use this context variable so I will say context is equals to browser Dot
27:09 new context and this we have to do because in a before all uh hook we cannot directly
27:17 pass context so if I try to pass this you will see there is some error and you
27:25 will not be able to use it directly so if I try to say here context Dot
27:33 you know start you will you will see we are not getting the start tracing here
27:39 or if even if I say context dot tracing let me see if we do it like
27:48 this you will see some issue let me let me show you if I directly say here
27:54 if I directly copy this here
28:05 let me try to do it this way and you will see the details here
28:11 and let me comment this out and then here
28:21 if I say test Dot after all and then again I say
28:29 async function and here if I try to pass a context
28:41 uh I think here I will have to say directly using the async I will
28:49 just say I will declare this function like this
28:58 and here I am going to stop chasing so I'm just going to copy this stop
29:06 tracing command and I will comment it out from here and I will add it in the after all
29:13 function and let me change the file name to test two dot Trace
29:20 now you can see here uh let me do formatting as well you can see here it is not getting the context here and that
29:28 is the reason here if we are using before all and we have to use the same context in after all I can just say here
29:37 let context and here I will pass the browser context or browser fixture
29:46 and then here I will say a weight
29:52 context equals browser Dot new context
30:02 okay and then here
30:09 yeah this should work now then here I am saying
30:19 I will say now here
30:28 okay uh I will have to foreign
30:42 now I will say context Dot chasing and I will say start
30:57 okay so this is now working fine and also you can see in the after all there is no error and we can use it now one
31:05 more thing that you will have to do here is uh here we have to use the same context to
31:12 create a new page so I will say here I'll declare one more variable called page
31:19 and then I will say here page equals
31:31 context Dot new page
31:42 and now from the test we can remove both of these fixtures because now the pages being used from
31:50 here this one where we we have already set this to a new page here so I can remove this from here in all the tests I can
31:59 remove the page fixture so in the second test as well I can remove the page picture and now tracing should work for
32:06 all the tests in this particular file and also if you see here uh the after all it is not necessary that you put
32:14 this after all hook at the end of the file you can put it anywhere it will anyways run after all the tests so this
32:21 should run and get the trace in this file test to hyphen Trace dot zip and let us see make sure that you save your
32:28 file and now I will say here
32:39 I have to stop this Trace and I will go and run the
32:48 this test and let us now see so I'm running the test file so it will run the two tests on all the
32:56 three browsers so that means six test now there is some issue it says uh page
33:03 dot go to is not a function and that is because I think we here
33:10 did some mistake we are saying here uh I think we should have a weight
33:20 and then here we should directly be able to say context
33:28 yes and yes it is it is same here I have added it here but forgot to edit here and this should be fine
33:37 and here also now I should be able to say context.new page and there is no error that means they
33:46 should be fine and then here now it should work so let us now try
33:56 I will say Ctrl C and Y and I will
34:02 run this or sorry this is for Trace let me go to the command to run the test
34:11 and this is the command and I will now run it and check so let's now see
34:18 it is running three uh it is running two tests on three browsers so there will be a total of six runs
34:27 it is done and still there is some issue and the same issue page dot go to is not a function
34:34 let me check again I will say
34:43 okay I believe uh did we add a weight here uh in the when we declared this page I
34:50 think this was the this may be the issue uh let me check now should work now
34:59 let me see here I will stop this and
35:08 run it again make sure that you save and this is the command now see I'm I'm
35:19 not editing out all these uh sections where I have made a mistake and I am troubleshooting and figuring out and uh collecting the mistakes so that you can
35:28 also see you will also be making such mistakes in the beginning and then you will learn from here so hopefully this
35:34 should work let me check it has gone to Firefox so hopefully it is working now
35:41 and now it has it is running the second test on Firefox and then it is now
35:50 still on Firefox okay it is retrying on Firefox because we also have if we have a failure it
35:58 will retry so that means there was some failure as well and now it is running on webkit
36:08 and I believe it is uh also creating the trace file as we can see here
36:19 and it is also reaching I think one of the test is failing that is the reason it is retrying that test because in the conflict we have set retry count to one
36:28 so that is why it is retrying which is fine and yes this should complete now
36:38 again on webkit because of the failure it is retrying once and then
36:46 let us just wait for this to complete okay so now it is done and it has also
36:56 started the uh report and you can see there are all these home has playwright this is passing demo test has passed on
37:05 chromium but has failed on Firefox and webkit and this home has playwright has failed on webkit that is all fine what
37:13 we are interested in is we want to check the you can see it has retried here and
37:20 you can see all these details uh it is missing the attachment Trace that is fine because we have programmatically
37:27 added it so let us see if we have got if we have got the Trace file and you can press Ctrl B to
37:36 hide the Explorer or to show the Explorer and you can see Test 2 underscore Chase dot zip is here so to
37:44 see this file I will say I will say here
37:51 npx playwright show trace
37:59 and I will go to this test to
38:06 Trace dot zip and let us now see if we get the all the details on the trace file
38:15 so yes it is opening the trace file and you can see we have got all these details along with all the screenshots
38:22 and everything is here so this is how you can create these are the different ways you can see what is the best way

# Chapter 9: Outro
38:29 for you and uh with that we have completed this session you can take the quiz and you will find the link in the description if you have any questions
38:37 you can let me know thank you for watching and never stop learning