# Chapter 1: Intro
0:00 hello and welcome i'm raghav and today we are going to create a sample login test and you can follow along with me
0:08 and you can do hands-on so we are going to create a demo login test and the applications i am going to use is i will first go to this

# Chapter 2: Demo Apps
0:17 link demo.epitools.com and here we will do login on this page then i will show you a login test on this link that is
0:25 orange hrm live application and we will do login on this page and then i will also show you login on this demo
0:33 application that is uh no commerce dot com login page so we will see different login pages and how do we do login test
0:42 so let's get started i will go to my vs code and my project is already open here i will go to the tests folder here
0:51 and i will create a new file and i will call it as login
0:59 underscore demo dot spec dot gs you can name it anything and the first thing i have to do on this file is i
1:08 will first import the test and expect libraries
1:15 from playwright package and now i will create a test so i will say test

# Chapter 3: 1st Login test
1:23 and i will give the title of the test i will say demo login test 1
1:31 and then i will create a async function that will be a anonymous function so i will give this
1:38 arrow symbol and a curly bracket start and stop and i will take this stop brackets to the next line
1:46 and also we have to pass the page fixture here in the async function so i will pass the page fixture
1:54 and now using page i can say i will say await page dot
2:01 go to so this is the first statement the first command we have to go to the page so i will first go to this page
2:10 and i will have all the links of all these demo websites and all the notes in the description section of this video so
2:18 we are going to this page demo dot tools demo.aptitools.com now in the last session in the earlier session
2:25 we have seen how to find objects how to create locators so if i want i can uh go and do a right click here manually on
2:33 this username page username box and say inspect and it will take me to the document object model or the backend of
2:41 this page and here i can see all the options or all the properties so we have a id of this page so id is username then
2:51 we have class property then we have placeholder property that says enter your username then i have typed property so i have so many we have so many
3:00 properties here and we can create a locator as we have learnt in the earlier session but because we are using an automation tool we should use the
3:09 features we should use the option of the tool to create the locators for us or to give us the object selectors so for that
3:16 what i'm going to do is i will have i want to open the playwright inspector and from the playwright inspector window
3:24 i want to explore and find the object locators or the object selectors so for that i will just add the command to
3:32 pause so i will say await page dot pause and in playwright when i say page dot pause
3:39 the execution will pause here and it will open the playwright inspector window and from there we can either
3:45 record or we can uh explore and find the objects we have also learned earlier how to record a test and you can also use
3:53 that way but for now let us do this way and here to run this i will say i will go to the terminal
4:02 and i will say npx playwright test and i want to run this specific file so i will
4:09 go to this the tests folder and i just want to run this specific file that is
4:18 login underscore demo.spec.js and then i also want to run it in a headed mode
4:26 and only on a single browser so i will say hyphen hyphen project chromium now you can also set the browsers in the config file but as of
4:34 now we are just setting it on the from the command so it will only run on chrome browser and i am saying hyphen hyphen headed so that
4:44 we can see the execution on our physical browser and i am now running it so let's see it should start the execution yes it
4:52 is starting on chrome browser and you can see as it encountered the pause statement it has paused the execution
5:00 and it has opened the playwright instructor window for us and now in this playwright inspector window you can either record and then copy the
5:09 recorded script or i can just go here and click click on this explore button and now if i take my cursor if i if my i
5:18 take my pointer anywhere on the screen it is finding all these objects and you can see it is also giving us the locators so if i click on this object on
5:27 this username box it copies the locator or the selector here and i can copy it from here i can manually copy or
5:36 just click on this copy button here is the copy button and then i will go to my code and then here i will say
5:45 await page dot locator we have seen we have learned how to use locators in the earlier session so i will just copy and
5:53 paste this locator and then here i have to fill the username so i will say fill and this
6:02 is a demo website i can use any username so i will just say raghav and then again i have to add the
6:10 command to fill password so i will say page dot locator and i will get the password locator here and then again i will say dot fill
6:19 and i will use some dummy password here so i have to find the locator for
6:25 password box as well so let us go and again go to explore
6:32 and click on the password text box and then copy the password
6:40 selector or locator and set it here paste it here and then finally we have to
6:48 click on the login button so i will say page dot locator and
6:56 again i will add the locator here and then i will say dot click if you do not get this auto suggestion box you can always press
7:04 control plus space on your keyboard and here i will again go to the playwright inspector
7:12 and get the locator for the sign in button and i will copy this
7:20 and paste it here and that's it so this completes the
7:27 login steps so let us run and check and i will close this playwright inspector window
7:34 and then i will again run the command and i am keeping the page.pause as it is here so that we can
7:42 see the execution step by step and we can do it step by step so i will run the command again
7:48 and this should start our execution and yes it is running and it has come to the pause statement and
7:57 it has paused here so now i can use this button that says step over or i can also press
8:04 the keyboard shortcut f10 this is to resume this will go until the end of the text and end of the test so i will use this
8:13 and you can see it has gone to the username enters the username it went to the password enters the password and clicks on the
8:21 sign in button now again here if you want to explore more objects you can do that but for now we will just click here resume and it
8:30 should stop the execution so this is how we have created this login
8:36 test on this demo application now if you want you can also use these uh

# Chapter 4: Commands to wait for element
8:43 commands if you want to check if some particular object is available or not or if you want to wait for that
8:51 you can add these assertions however in playwright there are inbuilt assertions so even when you
8:57 just use the commands fill click etc at the back end it runs all these assertions like wait for the object to
9:05 be present and the default beta with time is timeout is five seconds you can change this in the configuration file so
9:12 if i show you if i take you to the playwright.config.js this is the configuration file and you can see here
9:20 the default timeout is it is five seconds i have changed it here just to make it uh
9:27 just to wait only for three seconds but by default it is five but you can change it here like i had done i have made it three seconds also that page load
9:35 timeout is by default 13 to 1000 that is 30 000 milliseconds or 30 seconds i have changed it to
9:43 10 seconds so you can change it here if you want to or for a specific object if you want to change or
9:50 overwrite the default or global timeout you can use it like this so you can say await page dot wait for selector and
9:57 give the selector and then say timeout is this so i can say something like in my test i can say something like before clicking
10:05 on this sign in link i will say await page dot
10:12 wait for and you can see we have so many options wait for function load state i will save it for selector and i will give this
10:21 selector here that is for our login or sign in button and then i will give a comma
10:29 and then i will give so until here until this statement this you do not need to add explicitly because it will
10:37 anyways playwright will anyways run this and check if the object is available it is visible it is ready for action before
10:44 actually doing the action but just in case you want to change the default timeout you can say here within curly brackets you can say
10:53 timeout and then whatever timeout you want to change so this is in milliseconds thousand milliseconds means five seconds
11:01 and similarly you can also use something like uh expect page dot locator to have count so if you want to count how many
11:10 objects are there with this particular selector you can use this as well and i will have all this in the description of this video you can also
11:18 copy from there so here now let me comment out the pause statement and i
11:26 will run this again to check everything is working fine so it has started execution and yes it
11:36 was very fast and you can see everything has passed so this is all working fine now let us take another application

# Chapter 5: 2nd Login test
11:44 this one orange hrm and i will create one more test i can just copy this
11:52 test block so that i do not have to write everything again and i will also copy these n brackets
11:59 and i will do a formatting right click format document and i just want to run this test so i will say
12:07 test dot only so this will only execute this test from this file so i will say this is demo login test 2
12:14 and the first thing i have to do is go to this link so i will say page dot go to
12:22 and give this url and i will say
12:30 await and then again i can say page dot pause
12:40 and this will pause the execution and i can check the objects find the object locators and then
12:48 complete my code so i will save and run and because i have used test dot only here it will only run this test
12:56 so yes it has started and we have also got our playwright inspector
13:04 now if you want as we have done earlier i can explore and find this
13:12 object and then copy the selector from here then add in my code and add the actions like fill user name fill password here
13:20 the username is admin and the password is admin123 or the other way is i can click on record so
13:28 here i will click on record and then you can see as i record
13:35 it will start recording so let me also split my screen so that you can see the playwright inspector window and the application window both
13:44 side by side so i will say admin admin 123
13:52 click on login and then i want to click here
14:00 and then click on log out and if i see here you can see all this is recorded
14:07 if you want you can just copy it from here all these statements all the commands you can copy
14:14 from here and then paste it in your test so let me say
14:21 you can just copy this and it should be from here
14:27 and then just paste it in your test so this will also work you can do like this

# Chapter 6: 3rd Login test
14:35 let me show you one more example and some more options
14:43 so i'm creating one more test i'll again copy this declaration of the test
14:52 and again i will say dot only and i will say this is demo login test 3
15:01 and i will add the n brackets now here i'm not adding any statement
15:08 here i will just i just want to record now to bring up the playwright inspector window where we can record there are
15:16 three ways either you can directly uh run the code gen utility so that it will directly start recording and we have
15:24 already seen in the earlier session how can you use code gen to record or you can uh run with debug there also we will get
15:33 the recording option or you can use pause as we have already seen here so let me just continue with the same way i will just say ph dot pause and i have
15:42 not added any statements for the test as of now i have just added page dot pause here and i will save and
15:50 run so let me stop this execution and run it again
16:01 and this time i will go to this application that is demoncommerce.com so it has started you
16:08 can see it has opened the browser and the playwright inspector and it has not gone to any link as of yet so let me
16:16 again split my screen i'm pressing the windows key and the left key to split the screen and add these two
16:26 applications and this is just to show you the demo side by side this is not mandatory to
16:33 split your screen and here what i'm going to do is now i will click on record button here
16:41 and then i will go here
16:51 go to this site i think i did not copy this properly the url
16:58 yes and then here you can see in this case the email and the password or the username and password are already filled
17:07 in so i will either have to clear this text whatever is there in this box or i
17:14 can just say i am clicking and pressing ctrl a and then i'm adding
17:21 the username admin your store.com and if you see in
17:28 the recorded actions it has also recorded the control a that is selecting everything
17:35 the same thing i will do here control a and the password is uh admin
17:43 and then click on login button and then here i will click on logout
17:51 and i will stop the recording and let me show you the recorded script so this is what it has recorded let me
17:59 just copy this all so it should start from going to the page that is this one
18:07 going to this page so i will just copy this from here and then paste it in my test
18:17 now here if you see it has also added some comments so it goes to this page let me just do formatting i will say
18:24 right click format document so it goes to this page then it clicks on this username
18:32 box and then you can see here it has pressed control plus a to select everything and then we fill our username
18:40 similarly for the password also it presses control a to select everything and then enters the password
18:46 and then here we click on login and then it waits for this then it clicks on logout and then waits for this url and
18:54 then here it has used context dot close and browser dot close we will just be saying because we have not used these i
19:02 will say page dot close and that's it and let us see i will
19:11 say control c on the terminal to stop this process and run this again
19:20 and let us see the execution so it has opened the browser and this is
19:28 our playwright inspector and we will go to the next step
19:36 and it goes to the application and it goes to the email box and it has selected everything
19:44 and then fills the email goes to the password box selects everything by pressing ctrl a and then
19:52 adds the password and then clicks on the login button and now here it will click on the logout button
20:01 and then it completes the test so this is how we can do login test and this is the example all these examples that we
20:09 have seen so i hope you can do some more hands-on now and try to do some more login tests on some demo
20:18 applications if you have any questions you can let me know i will see you in the next session thank you for watching
20:24 and never stop learning
20:34 you