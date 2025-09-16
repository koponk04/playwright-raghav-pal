# Chapter 1: Intro

0:00 hello and welcome i'm raghav and today we are going to learn how we can record our test in playwright and this is going

0:09 to be very easy and very interesting in the last session we have learned how do we write our tests and i have shown you

0:16 step by step from scratch how do we create our test in playwright we have a tool called code gen also called as test

0:23 generator and we can use it to record our test and we can get our playwright test scripts created automatically so

0:32 today we are going to see what is code gen the test generator tool we will learn how to record test we will see

0:39 while recording test how can we set the screen resolution or the screen size we are going to learn how we can record on

0:46 a specific browser how we can emulate devices like iphone or samsung or nexus how can we emulate emulate these devices

0:55 while recording we are also going to see how can we emulate the color scheme like or the dark mode or the light mode or

1:01 the browser and i will send you a link you will find a link in the description below this video for the quiz you can take the quiz and do let me know your

1:09 score after the session and if you have any questions any doubts you can let me know your questions in the comments section below this video so with that


# Chapter 2: What is Codegen

1:18 let's get started and let us first see what is code gen and how do we use the test generator so playwright by default

1:27 comes with a tool called code gen and it is also called as the test generator tool and using this code

1:35 gen test generator tool we can record our test and when we start this code gen we have a command that i will show you in a moment when we start code gen it

1:44 will open two windows and the first window will be the browser window where we can go to our web application and we can interact with our

1:52 website and the second window will be the playwright inspector window this is the window that gets opened when we try

1:59 to debug our tests as well and that i will show you in a later session how to debug but for now it will open the

2:06 playwright inspector window where we can see the recorded scripts and then we can also start or stop recording from there


# Chapter 3: Step 1 - Open terminal and run codegen *npx playwright codegen

2:14 so with this let us start step number one that is we will open the terminal and we will run the code gen command and the

2:23 syntax is npx playwright and we say code gen now we can also add a url after this but for now let us

2:31 use this simple syntax first npx playwright code gen so i will go to my vs code and i have my project open here

2:39 and you can create you can open a new terminal or in my case the terminal is already open so i will go to the terminal here

2:48 and here i will say npx playwright

2:56 and i will say code gen and hit enter and let's see what happens so this


# Chapter 4: Step 2 - Check 2 windows open - Browser and Playwright Inspector

3:04 should open two windows the browser window and the playwright inspector window and you can see our browser window is open here and by default it

3:12 will open the chrome browser the chromium browser but we can also change the browser that i will show you in a moment so here is our browser window and if you

3:21 see here we also have our playwright inspector so this is our playwright inspector window

3:28 now i will split my screen so that i can show you both the windows i'm on windows operating system as of now and to split the screen on windows

3:36 operating system you can select one window and then press the windows key or the command key on your keyboard and the left or the right arrow i press the

3:44 windows and the left arrow so therefore this window is now stacked the browser window is now stacked on the left side

3:52 of my screen and then i will select the window to be stacked at the right side which is this playwright inspector so i

3:59 hope now you can see both these windows the browser window here and the playwright inspector window here and i can also

4:08 change the size like this now if you are on a mac you can do the same thing on mac as well for example you have two

4:15 windows open on mac uh let me say i have this two windows open on mac here

4:22 the way to stack or split the screen split the windows on mac is you press this green icon which is to maximize and you just

4:30 hover over it or keep it pressed and you will get the option to enter to set the window to the left or right

4:38 of the screen or make it full screen i will say do this on the left stack this on the left and this window i will select and it will get stacked on the

4:47 right so you can do this on mac as well and this is what i have done on windows so let me close this here

4:56 so now here i have my browser window and the playwright window and you will see this record option this record button is already enabled that means recording is


# Chapter 5: Step 3 - Record your test steps and check the test scripts getting created

5:05 in progress so i can start recording i will go to some website you can go to any demo website

5:13 and let us say i go to some website like uh sourcedemo.com you can go to any website here is a

5:21 website there is a demo website and here you can see you can give any of these usernames and

5:29 this is the password secret sauce and here now you can see wherever i am taking my cursor wherever i am taking my

5:36 mouse pointer it is highlighting the objects on the screen it is finding and highlighting the objects and

5:44 you can see it is also showing us the selector that it is going to use so in this case it is going to use this data

5:52 test equals username here if i go to the login button you can see this is what it is going to use as a selector so you can

5:58 see uh beforehand what is the selector it is going to use now let me enter the username i can select any of these usernames so i will say standard user

6:07 here i will click in the username box and you can see the scripts getting recorded in the playwright inspector i will say standard underscore

6:16 user and then i will click on the password box and the password is

6:23 secret underscore source and then i will click on the login

6:30 button so you can see it has logged in and all these actions are getting recorded in scripts here so i will just click on this

6:38 and say log out and that's it i will stop the recording so i will click on this record button and it will stop the


# Chapter 6: Step 4 - Save the recorded script in a test file | Run and check

6:47 recording now you can see some more options here is a copy button to copy the script then here is a resume button

6:54 a pause button and a step over button now these three buttons resume pause and step over will be useful when we do debugging but as of now we don't need

7:02 this so i have stopped the recording and here if you see this drop down here we have options to

7:10 export this recorded script in any of these platforms or languages so we can uh

7:17 export or copy this in playwright test java javascript python python async pi test c sharp etcetera but for now i just

7:26 want the same playwright so i can copy from here click on the copy button or you can manually also copy the steps

7:34 by selecting and then i will go back to my vs code to my project and under the

7:43 test folder i will create a new file and i will say

7:53 rec or record one underscore demo dot spec dot js you

8:01 can give any name to the file and i'm just going to paste the recorded script here so let me

8:08 show you i will expand and show you this i'm pressing control plus b on my keyboard

8:15 so that i will the sidebar is hidden and i can show you full screen so

8:23 you can see this is the recorded script it has everything it has also imported the test and expect scripts from the playwright package and

8:31 here is our starting of the test the name is test if you want you can give any name to this test

8:38 i will say record demo test and here you can see all the

8:47 scripts along with that it has also added the comments so it says go to this link then click on click here and here

8:55 it is filling the username then adding the password then you can see all these things

9:02 that we have recorded and everything is recorded here so i will press ctrl b again on my keyboard and now to run this

9:10 test i can just say i'll go to the terminal and now you can see the code gen is still

9:18 running to stop code gen you can either press ctrl c on the terminal and then say y so i can say control c and it will say

9:26 terminate job i will say y and it will stop code 10 or you can just go to the browser where you have recorded and

9:34 close the browser it will stop code gen so now to run this i will say

9:40 the command is npx playwright

9:49 uh it is npx playwright test and because i want to run the specific file

9:55 i will give the location with that is in the test folder record1 demo.spec.js

10:02 now if i run this it will run in a headless mode i want to run in a headed mode so i will say hyphen hyphen headed

10:09 or let me also say hyphen iphone project and i will say chromium so that it only runs on a single browser

10:16 we don't want to spend a lot of time in running in all the browsers and i will say hyphen hyphen headed all these commands we have learned in the earlier

10:24 sessions so let us now see it is running our test and opens the chromium browser and locks

10:32 in and locks out so it was quite fast so it is running fine so this is the command and uh we can also


# Chapter 7: Can also add the url *npx playwright codegen google.com

10:41 add the url of our application right in the command so that it will start the browser along with that application open so

10:48 this is the syntax you can just say npx playwright codegen or npx playwright codegen along with your application url

10:56 so if i say here on the terminal if i say here

11:03 npa okay so if i go to this terminal and say

11:12 npx playwright code chain and then i will say i'll give the

11:23 url so now it should open the browser along with this url open that is google.com

11:30 so you can see it has opened the browser and here is the playwright inspector and it has already gone to that

11:37 website that is google.com so you can see if i close this browser it will stop the code gen utility so it has stopped it here

11:46 so this is how you use it also if you want to see all the options all the commands we can use all the options we


# Chapter 8: See all options *npx playwright codegen --help

11:54 can use with code gen you can say npx playwright code gen

12:04 and say hyphen h or hyphen hyphen help and this will show you all the options we can use with

12:12 the code gen tool or the code gen command so you can see all these options so here i will show you some of these

12:19 some very common options so you can actually uh send the recorded script to our output file as of uh now as of the

12:26 earlier example we manually copied and added it to a file but you can use this i will show you this in a moment uh you

12:34 can use the browser by saying hyphen b or hyphen hyphen browser and select what browser you want to record on you can

12:40 select the channel color scheme the device emulate the device emulate the geo location coordinates

12:48 you can also do authentication and proxy then you can set the time zone you can

12:55 set the user agent you can set the resolution or screen size so all this we can do with this code gen utility so let

13:03 me clear my screen clear the terminal and let us go to step number two and we have already seen step number two

13:11 when we ran the command npx playwright code gen it opened two windows browser and playwright inspector and we recorded our steps and we also

13:20 checked that the scripts were getting generated and then we saw

13:27 we saved and ran and checked the execution so everything was fine we have seen all these steps if you want you can


# Chapter 9: Screenshot moment

13:34 take a screenshot of this screen and keep it handy with you and watch it multiple times so you will never forget what is code jan and how to use it

13:43 and with that let us see some different options we can use with

13:50 this code gen utility or this code gen command so if you want to run code gen on a specific browser or if you want to record on a specific browser you can say


# Chapter 10: Record on a specific browser (default:chromium) *npx playwright codegen --browser firefox

13:59 hyphen b or hyphen hyphen browser and give the browser name so we have already seen this

14:06 so here i can say i will say here

14:20 just give me a moment i think this is hanged let me just give me one

14:28 moment okay so here i will say npx playwright

14:36 code gen and then hyphen b or hyphen hyphen browser

14:43 and i'll say firefox now if you do not give any browser then by default it opens chrome but here i'm saying to open

14:51 in firefox and the rest of the things if you want to give a url along with the along with the command all that you can do

14:58 so you can use multiple options together so we have our browser window and our playwright

15:05 inspector window here and now i can do the same thing i can just go to

15:11 the website let us say source demo.com and you can see all this is

15:18 getting recorded and i can now use it and you can see this is the this is now being recorded on a firefox browser so you can

15:26 do that uh then the other thing is you can also save to a file so let us


# Chapter 11: Record and save to a file *npx playwright codegen --target javascript -o record_example.js

15:35 say we have a file so i'll create a file i'll create a file under the

15:43 test folder i will say record to

15:52 underscore demo dot spec dot gs so this is our js file

15:58 and now i will say npx playwright and

16:05 codegen and now i will say hyphen hyphen target and i will give the

16:13 language so as of now we are using javascript so i will say target hyphen hyphen target and i will give javascript here i want

16:22 to export the recorded steps in javascript and then hyphen o this is to give the output file and then

16:31 the location of the file so which is test and here i will say

16:40 record so i can just say here test hyphen o

16:48 test and record to demo i will press tab so that it will auto complete and this is also useful so

16:55 that uh i do not make any typos here so this is what i am doing so now whatever i will record should directly go here so

17:04 let me start the command and let us see so we have got our browser here browser

17:13 window and this is the playwright window and i have already shown you how i am splitting my screen

17:20 and opening both of these windows side by side so i'll just go to the

17:27 website sourcedemo.com i'll enter the username standard

17:36 underscore user and the password secret underscore source

17:45 and click on login and then click here and log out and i will stop the recording by clicking on this

17:53 record button now if you go and check if i go and check my record to demo you can see this is

18:01 recorded here everything is recorded here i can just stop my browser window i can close my browser window it will stop the code gen

18:09 tool as well and you can see everything is recorded here now here if you export like this if you record and save

18:18 to a file in this case you may have to add the test block so it directly starts with

18:25 async so let me add the test block here before async i have to give the

18:32 test and the name of the test

18:44 and that's it i think rest of the things looks fine

18:53 i don't need these extra brackets here this should be fine i can run and check this

19:00 so i will say npx playwright and

19:11 test and i will run this specific file record2.demo.spec.js

19:20 and let me run in a edit mode and let us see if it runs fine so yeah some issue it says const

19:28 chromium require playwright i think this again we have to change

19:39 if i say here require and then here if i start typing playwright or i

19:48 think i should say at the rate playwright you can actually copy this

19:56 from any earlier uh script so normally we say const and we say

20:04 get test and expect modules from

20:12 the playwright

20:22 package uh just copy this from any earlier script yeah this is what we need i can either say like this

20:30 i can import or say require this we have seen in very details in the last session so i hope you know about this

20:37 and here also let me just use this at playwright

20:44 test let me see if this works out i'll clear the terminal and run the command again

20:52 and let us see if this runs fine yes this is running fine and it is running in a headed mode so it

20:59 will run on all the three browsers chromium firefox and webkit it is done on chrome it is running on

21:06 firefox now and now it is running on webkit and everything is fine and

21:14 on webkit i think it is not able to find the icon where we have log out which is fine so let it fail that is okay

21:22 but yes this is how we can record and save to a file now you can also set the viewport or the screen resolution by saying hyphen hyphen


# Chapter 12: Set viewport - screen resolution (size) *npx playwright codegen --viewport-size=800,600

21:31 viewport hyphen size and give the size so i can say here let me close this

21:43 this is the report and here it has failed on webkit we will see this later for now

21:53 i will say i'll go here

22:02 stop the report and clear the terminal and i will say npx

22:10 playwright code gen and here

22:18 i will say hyphen hyphen viewport so this is viewport size so

22:25 hyphen hyphen viewport size equals 800 by 600

22:33 so this is the command and now if i run this it should open the browser in this size in this viewport size so

22:42 you can see it has opened the playwright inspector and it has opened the browser in that particular screen size so you

22:49 can also use this viewport size then we can emulate the devices so if you if


# Chapter 13: Emulate devices *npx playwright codegen --device="iPhone 11"

22:56 you go to your chrome and if you go to these three dots and go to more tools and go to developer tools or you can

23:04 just press f12 on your keyboard so it will go back go to this developer tools and here you can see these are the

23:11 device here is a device icon i can go here and then i can select the device from here iphone

23:20 etc i can select from all this list of devices any device and then i can do testing on

23:27 that particular screen which will emulate that device the same thing we can do with playwright and with codegen tool as well

23:37 so here i can say hyphen hyphen device and give the device name so here i will say npx

23:44 playwright code hyphen hyphen device

23:52 and then i will say equals the device name let us say equals and i am saying iphone 11 here

23:59 and hit enter and now you will see the browser window will emulate here iphone 11 i think uh

24:07 we have used a different name it is asking us it is showing us a list of devices i can use so

24:16 uh let me say i'll go with i can go with this one galaxy note 2.

24:32 uh i think the issue may be maybe it needs uh

24:40 let me see it is iphone space 11 yeah i think that

24:49 may be the mistake and i'll just put this in double quotes and let us now see

24:56 so this should start browser in that emulated yes you can see the browser is started

25:04 and it is emulating iphone 11 and this is our playlight inspector and now we can do our recording on this emulated

25:13 device so you can do like that and you can also emulate the color scheme you can say npx playwright code gen color


# Chapter 14: Emulate color scheme (if available) *npx playwright codegen --color-scheme=dark

25:20 scheme equals dark or light now this will uh happen only if the website supports the color scheme dark and light

25:27 if it is available on the website so let me say uh here if i see some website let me just go to the playwright

25:36 official website which is playwright.dev

25:43 and here i can set the color scheme dark or light and let me also directly do it from here

25:52 npx playwright code chain and then i will say hyphen hyphen color hyphen scheme

26:05 equals dark so i can hear say dark or light and i will also give the website url that is

26:13 playwright hyphen dev so you can see here on this i can set

26:21 dark or light mode this is dark and this is light mode so this is what i am trying to do here let us now see it

26:28 should open playtime.dev website in a dark mode or dark color scheme

26:35 and yes some error here let me see it says

26:43 navigating to dev waiting till load and it says name error so it is okay it is dot dev not hyphen dev

26:51 that was my mistake it is playwright.dev and let us now check

26:59 it should open the browser yes you can see it has opened playwright.dev in a dark mode and here

27:07 is the dark mode if you want you can change it to a light mode as well so you can set the color scheme

27:14 and then i have already shown you you can check all the options using the help command it will show you all the options that

27:22 that you can use with the playwright code gen command so you can take a screenshot of this screen and keep it handy with you watch it multiple


# Chapter 15: Screenshot moment

27:30 times and you will always remember all these commands and you can also take the quiz now i will have the link for the quiz in the description of this video

27:39 under this video and if you have any questions you can let me know i hope this was very useful i will see you in the next session thank you for watching

27:48 and as i always say never stop learning
