Chapter 1: Intro
0:00
hello and welcome i'm raghav and today we are going to learn something very interesting in playwright we are going
0:07
7 seconds
to see how we can slow down the speed of execution of our test so generally playwright is very fast and sometimes
0:15
15 seconds
you may want to see what is happening on the screen on the browser and in that case you may want to slow down the speed of execution so we will see how we can
0:22
22 seconds
run our tests in slow motion and then we will also see how we can record video of our test execution and both of these
0:30
30 seconds
features are inbuilt in playwright so we do not have to use any third-party tools or any third-party libraries all these
0:38
38 seconds
features are built in within playwright and we will see these options from the config file how to set these configurations from the config file at a
0:46
46 seconds
global level and we will also see how we can do this at a test level so let's get started and let us see the first step is
Chapter 2: How to run tests in Slow Motion | How to Record Video
0:55
55 seconds
we will go to our config file and we will add the configuration for slow motion and video recording so i will go
1:03
1 minute, 3 seconds
to my project so here is my project and i will go to the configuration file
1:10
1 minute, 10 seconds
so here i have my playwright.config file i will go here and here
1:17
1 minute, 17 seconds
you will see there is a configuration called cost config and here we can set all this config we
1:25
1 minute, 25 seconds
have test directory timeout etc and here within this option we will
1:34
1 minute, 34 seconds
add the option for video and slow motion so under cost config
1:41
1 minute, 41 seconds
you will see a section called use and here it is the use section where we can set all
1:48
1 minute, 48 seconds
these action timeout base url trace so we have already seen a video on how do can we do a tracing so here
1:57
1 minute, 57 seconds
i will say within this i will say video and you can see we are also getting this auto suggestion box in case
2:05
2 minutes, 5 seconds
you do not get this auto suggestion you can start typing and then press control space on your keyboard and if you still do not get then you must check whether
2:13
2 minutes, 13 seconds
you are adding this configuration at the right location so this i can i will say
2:20
2 minutes, 20 seconds
on and you can see we have all these options i can say on off on first retry retain on failure so as of
2:28
2 minutes, 28 seconds
now i will just say on i want to make it on and then i will give a comma at the end because there is there is more
2:35
2 minutes, 35 seconds
configurations after this and for slow motion we will add a launch option and then within the launch options we will
2:42
2 minutes, 42 seconds
add slow motion so i will say launch options and you can see i'm again getting this auto suggestion and
2:51
2 minutes, 51 seconds
this i will add within these curly brackets because we can add many launch options so i will say
2:59
2 minutes, 59 seconds
slow motion this is slo-mo and then i will give the milliseconds so the number that you give is milliseconds
3:07
3 minutes, 7 seconds
and 1000 milliseconds means one second and basically when we say slo-mo 1000 that means we are going to slow down all
3:15
3 minutes, 15 seconds
the playwright operations by one second and of course at the end of the curly bracket after the end you will give a comma because there is more
3:22
3 minutes, 22 seconds
configuration after this and this looks fine there are no errors so you can save the file and here
3:31
3 minutes, 31 seconds
as i said slow motion will slow down the playwright operations by the specified milliseconds and for the video recording we have all these options on means it
3:40
3 minutes, 40 seconds
will record for each test off means it will not record the video retain on failure it will record for each test but then remove for the successful test runs
3:48
3 minutes, 48 seconds
and you will get videos only for the field executions and then on first retry this can be a very common option that is
3:56
3 minutes, 56 seconds
do not record video for each execution because that can be uh that can hamper the performance so only record video on
4:04
4 minutes, 4 seconds
the first retry and we can set the retry count as well so we have seen this in one of the earlier session that we can set the reach i
4:12
4 minutes, 12 seconds
count so here if i show you uh the resize
4:20
4 minutes, 20 seconds
you can see this is i have commented out we had set this three tries to one so this can be a very common option and
4:26
4 minutes, 26 seconds
then you can save and run and here once you have added this video option as on you will see the video appear in the
4:35
4 minutes, 35 seconds
test results folder so let us see this i have made these configurations i have added these configurations here and now
4:44
4 minutes, 44 seconds
i will go to any of the tests so let us go to our login demo test that we created in one of the earlier sessions so here we are going to this uh
4:53
4 minutes, 53 seconds
application and then we are doing a login here so let us run this so here we have act we actually have
5:00
5 minutes
three tests you can take any of your earlier tests or any of your existing tests i am saying test dot only here so it will
5:09
5 minutes, 9 seconds
only run this one test out of this file so i will open my terminal you can press control plus j on
5:16
5 minutes, 16 seconds
your keyboard to open the terminal and here i will say npx playwright
5:25
5 minutes, 25 seconds
test and i want to run this specific test so i will say this file i am pressing tabs to auto complete all these
5:34
5 minutes, 34 seconds
names and files and i want to only run on a single browser so i will say project hyphen hyphen project and i will say chromium
5:43
5 minutes, 43 seconds
and then i want to run in a headed mode so that i can see the execution so i will say hyphen hyphen headed and i will
5:50
5 minutes, 50 seconds
run this command so let us see so it opens the browser and
5:58
5 minutes, 58 seconds
it has opened the playwright inspector because we had this pause option here so let me comment out this pause from here
6:05
6 minutes, 5 seconds
and let me see if there is any pause statements yeah this was the only statement and i will save and for now that is fine
6:14
6 minutes, 14 seconds
i will just resume this execution here and you will see this should go to this page and you can
6:22
6 minutes, 22 seconds
see it has slowed down the execution it is running very slowly otherwise it is very fast it
6:30
6 minutes, 30 seconds
is sometimes not easy to see exactly what is happening on the screen but now because we are using slow motion so you can see
6:37
6 minutes, 37 seconds
all these actions have slowed down and everything has passed and now we can check the report so you can see
6:45
6 minutes, 45 seconds
npx playwright show report and this will open the report
6:53
6 minutes, 53 seconds
and this is our test and here you can see all these tests and we can also see the video recording so we have
7:00
7 minutes
got this video recording here in the report file and you can see the video now the video will also be recorded in the slow motion as we have
7:09
7 minutes, 9 seconds
slowed down the execution so you can see it is recorded in the same pace
7:16
7 minutes, 16 seconds
and this can be handy because sometimes it is very fast and even in the video you may not be able to see exactly what
7:25
7 minutes, 25 seconds
is happening so you can slow down and if you see one second or 1000 milliseconds uh is something which has slowed down a lot you can use
7:33
7 minutes, 33 seconds
like 500 milliseconds or 100 milliseconds whatever you feel is good and then i will also check in my folder
7:41
7 minutes, 41 seconds
so i will go back and see in my test results folder you will see this video is recorded here this video file is here
7:48
7 minutes, 48 seconds
i can open it in a file explorer so i will say reveal in file explorer and in the test results folder
7:56
7 minutes, 56 seconds
i have got my chromium because we have executed only on one browser and you can see this is the video that got recorded
8:05
8 minutes, 5 seconds
and we can see this video recording here so we have got our
8:15
8 minutes, 15 seconds
video recorded and the execution is happening in a slow motion now uh this
Chapter 3: Screenshot moment
8:23
8 minutes, 23 seconds
slow motion is a field in the browser type launch options class and you can also see from this link
8:30
8 minutes, 30 seconds
so if i go to let me show you here if i go to
8:37
8 minutes, 37 seconds
playwright browser type launch options and you can
8:46
8 minutes, 46 seconds
see you can go to the docs here and here we can see this is the
8:54
8 minutes, 54 seconds
because you can check whatever is the latest version and here is the class browser type
9:03
9 minutes, 3 seconds
launch options let me reload it browser type launch options and you can see all these fields so we have all these fields here
9:12
9 minutes, 12 seconds
and if you see slow motion is also a field here so here slow motion slows down playwright operations by the specified
9:20
9 minutes, 20 seconds
amount of milliseconds and useful so that you can see what is going on and there are many other options here we can set the proxy we can set the headless
9:30
9 minutes, 30 seconds
mode all this we can set from these launch options now here this is how we do it from the
9:37
9 minutes, 37 seconds
config file now we can also set it at a test level by using the browser context now
Chapter 4: How to set video recording and slow motion from test (Browser Context)
9:45
9 minutes, 45 seconds
browser context in playwright we can create a new browser context which will be like a
9:52
9 minutes, 52 seconds
incognito isolated context of a browser and then we can create a context and page within that browser and this will be very handy when
10:01
10 minutes, 1 second
we do multi window or multi-tab application testing and even when we do not explicitly create a browser context
10:07
10 minutes, 7 seconds
playwright always creates a isolated incognito browser context so for this i will first
10:15
10 minutes, 15 seconds
remove these global configurations i will go to my config file and i will remove all this video and
10:23
10 minutes, 23 seconds
launch options slow motion and i will comment out i have selected everything and pressed control and forward slash on my keyboard to comment
10:31
10 minutes, 31 seconds
all this and now let me create a new test i will go to my tests folder and i will create a new file i will say
Chapter 5: Create a new test
10:41
10 minutes, 41 seconds
slow motion underscore video recording
10:47
10 minutes, 47 seconds
underscore demo dot spec dot yes you can name it anything i have named it this slow motion
10:54
10 minutes, 54 seconds
underscore video recording demo.spec.js and here i will say
11:01
11 minutes, 1 second
import so let me say here import
11:11
11 minutes, 11 seconds
and i will import a test and expect libraries from the
11:19
11 minutes, 19 seconds
playwright test package and then i can create a test block i will give the title i will say
11:28
11 minutes, 28 seconds
slow motion and video recording demo
11:36
11 minutes, 36 seconds
and then i will create a async function and give this arrow symbol
11:44
11 minutes, 44 seconds
and a curly bracket start and stop and now i'm not going to say send the page fixture here in the earlier examples we
11:51
11 minutes, 51 seconds
have sent a page picture and then we start saying page dot go to and create our test here i will now say uh
11:59
11 minutes, 59 seconds
i will launch the browser first so in playwright we can create isolated incognito browser sessions using the browser context so i will say
12:09
12 minutes, 9 seconds
here const browser equals and here i will say
12:16
12 minutes, 16 seconds
await chromium.launch or await firefox dot launch or await webkit don't launch whatever browser you want to use so i
12:23
12 minutes, 23 seconds
will say await chromium dot launch and you can see as i am typing i am getting all these auto suggestions
12:31
12 minutes, 31 seconds
and now within this bracket of chromium.launch we can give some configuration and i will show this in a
12:38
12 minutes, 38 seconds
moment but before that let me also say context and i will say await
12:49
12 minutes, 49 seconds
browser dot new context so i'm creating a new context here and again we can give a curly bracket here
12:57
12 minutes, 57 seconds
and then add some more configurations and i am creating a page and here i will say await
13:05
13 minutes, 5 seconds
context dot new page okay so this is how we create a browser
13:11
13 minutes, 11 seconds
context and now i can just say i can keep on adding my test i can now create my test
13:18
13 minutes, 18 seconds
as usual i can say page dot go to and i can give the url and everything will be as it is from now onwards so
13:28
13 minutes, 28 seconds
this is how we can create a browser context and make sure that you close the context at the end so after your test
13:35
13 minutes, 35 seconds
you should say await context dot close okay
13:43
13 minutes, 43 seconds
so this is how we create a browser context now for setting the configuration for slow
Chapter 6: Set configurations for slow motion and video recording at test level
13:51
13 minutes, 51 seconds
motion and video recording from within the test we will create the browser context that is step number one we have already done that and then we will add
13:59
13 minutes, 59 seconds
the options for slow motion in the browser and then the options for recording in the new context and then we will close
14:07
14 minutes, 7 seconds
the context so let me show you this is how we do that in the browser here
14:15
14 minutes, 15 seconds
in the options for the browser launch we will say slow motion so i will say here within the curly brackets i will say slow motion and you
14:24
14 minutes, 24 seconds
can see i am getting this auto suggestion and you can move it to a new line for easy readability so if i press ctrl spacebar i am getting
14:33
14 minutes, 33 seconds
this slow motion and i will say let us say 500 milliseconds and then you can also
14:41
14 minutes, 41 seconds
set other options as we have seen here all these fields you can set here so you can set
14:49
14 minutes, 49 seconds
slow motion here then we can set headless as well so i will say headless as well here
14:56
14 minutes, 56 seconds
and i will say headless is false that means i want to run in a headed mode so these two options you can set in the
15:04
15 minutes, 4 seconds
new browser launch and then for this video recording we can set in the new context so in the new context i will
15:12
15 minutes, 12 seconds
again give a curly bracket start and stop i will move to the next line for easy readability and i will say record video i am getting this auto suggestion
15:21
15 minutes, 21 seconds
and here i have more options first i will keep the directory where i want to
15:28
15 minutes, 28 seconds
save the video files so i will say i want to create a new folder called videos and here i want to store the video files and then i can also set the
15:37
15 minutes, 37 seconds
size in which i want to do the recording so here i can say i can set the height and width so i am
15:45
15 minutes, 45 seconds
saying width should be 800 and height i can set to let us say 600 so i can set the viewport size or the screen
15:54
15 minutes, 54 seconds
size for video recording like this okay and then i can create my rest of the test so let me just copy the test
16:02
16 minutes, 2 seconds
from my login demo so that we can save some time and here i will start from
16:09
16 minutes, 9 seconds
going to this link and until clicking on the login button so
16:17
16 minutes, 17 seconds
i'll just go until here i will copy these steps and paste it here
16:25
16 minutes, 25 seconds
and then at the end i will also close the context so let me show you this is my test now
16:41
16 minutes, 41 seconds
i will show you this this is my test now i have created all these browser context
Chapter 7: Screenshot moment for test
16:49
16 minutes, 49 seconds
and then this is my test which is going to this link and sending setting email and password so it first selects all that is written and then
16:58
16 minutes, 58 seconds
adds the username in the username field then goes to the password selects everything by pressing ctrl a and then as the new password and then clicks on
17:06
17 minutes, 6 seconds
login button and then we are closing our context so let us now save this
17:14
17 minutes, 14 seconds
and i will run so here
17:22
17 minutes, 22 seconds
on the terminal i will say
17:30
17 minutes, 30 seconds
npx playwright test and i will go to the tests folder and
17:37
17 minutes, 37 seconds
the name of my file is slow motion underscore video recording underscore demo.spec.js
17:45
17 minutes, 45 seconds
and here i will i only want to use the chromium browser so i will say hyphen hyphen project
17:53
17 minutes, 53 seconds
chromium so let me show you the complete command this is what i am saying hyphen iphone project chromium and i do not
18:02
18 minutes, 2 seconds
have to say had uh headed hyphen hyphen headed because we have already set this headless false here so this is what i am
18:10
18 minutes, 10 seconds
running now and i will run and check so i have started execution and let me see yeah it is running and
18:19
18 minutes, 19 seconds
you can see it is it has slowed down by half a seconds because we have set 500 milliseconds and everything is passed
18:26
18 minutes, 26 seconds
and now i want to check i will check the report first so i will say npx
18:33
18 minutes, 33 seconds
and npx playwright show report and you can see this is our report here
18:41
18 minutes, 41 seconds
and here is our report and now i also want to check if we have got the videos folder and yes we have got our videos
18:47
18 minutes, 47 seconds
folder and this is our video let me go in the file explorer and go to the videos folder and here we
18:56
18 minutes, 56 seconds
have got our video file so i can run this video file and you can see this is our video recorded with 500
19:03
19 minutes, 3 seconds
milliseconds of slow uh slowness in the execution and this is how we can set this configuration for uh
Chapter 8: Outro
19:12
19 minutes, 12 seconds
slowing down down our execution and also recording the video i hope this was very useful for you if you have any questions you can let me know you will find all
19:20
19 minutes, 20 seconds
the steps all the links in the description of this video and i will see you in the next session thank you for
19:26
19 minutes, 26 seconds
watching and never stop learning
