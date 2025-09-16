# Chapter 1: Introduction

0:00 hello and welcome i am raghav and welcome to this session and this series of playwright in this session and in this series we are going to learn

0:09 playwright step by step from scratch so do not worry if you are a complete beginner do not worry if you have no

0:16 background in automation or testing or programming or coding i'm going to start from scratch and we we are going to go

0:23 up step by step so in this session we will start with understanding what is playwright and we will look at the

0:30 features of playwright and i will show you all the features we will discuss uh what is playwright what are the applications supported what are the

0:38 browsers supported what are the operating systems supported and everything about playwright so this is going to be a very much theoretical introduction session and from the next

0:47 session onwards we will do hands-on we will see the prerequisites and then we will install and use playwright now if

0:54 you have any questions during this session you can always let me know in the comment section below or the q a section below this video and if you have

1:02 any general question which is not related to playwright or this video still you can ask me i read all my messages and i reply to everyone so you

1:11 can ask me your general questions as well if it is a general question then you can add the hashtag ask raghav if you want you can also go on my website

1:20 automationstepbystep.com and you will find all these tutorials here as well and you can see the ask raghav playlist

1:27 as well here so you can ask your general questions here and if you find the pace of this video slow you can go to the player settings the

1:36 video player settings and you can increase the speed from there so with that let's get started and let us first see what is playwright now playwright is a


# Chapter 2: What is Playwright

1:44 free and open source framework it is created by microsoft and it can be used for doing test automation on

1:53 web browser applications and when i say web browser it can be desktop browsers or it can also be mobile browsers so if


# Chapter 3: Applications supported

2:01 i talk about the applications supported by playwright all the web browser apps all the mobile web apps as well as we

2:08 can also do api testing with a playwright if i talk about the languages supported now playwright as of now is implemented


# Chapter 4: Languages supported

2:17 in four languages or four uh libraries the first one is the node.js library and if you use the node.js library or

2:26 node.js implementation of playwright then the options for programming language there is javascript or typescript so we can use

2:34 javascript.typescript then there is a java implementation or java api if we use the java library of playwright then we can create our test

2:42 cases we can create our framework in java then there is a python implementation we can use python there and then there is a dotnet

2:49 implementation where we can use dotnet languages like c sharp so we have all these languages support you can create your framework and write your test cases

2:58 in any of these languages if i talk about the browsers supported by playwright then all the modern browsers


# Chapter 5: Browsers supported

3:05 are supported by payride and uh we talk about the browser engines here so we have support for all the chromium based

3:13 browsers all the webkit browsers and all the firefox browsers when i say chromium it is a web browser engine and under

3:20 chromium we have google chrome we have microsoft edge we have opera we have brave browsers and many others under

3:27 webkit we have all the mac os and ios browsers like safari and all the ios browsers then if i talk about firefox

3:36 then all the versions all the flavors of firefox whether it is desktop firefox browsers or mobile firefox browsers

3:43 everything is supported by playwright and you can also use these browsers in a headless mode or a headphone mode headless means no gui

3:52 so when you run your tests in a headless mode you will not see anything coming up on the screen you will not see the physical browsers everything will be running at the back end and it will save

4:01 time it will save memory but if you want to run in a physical mode in a headed mode even that is possible where you can see the physical browsers on your screen

4:09 so if you just search for if you see some chromium browsers or you can just search for

4:17 chromium browser list and you can find all these browsers like we have opera microsoft

4:24 edge uh brave browsers google chrome so you can see all the list here so here is a list you can check uh this is the link

4:32 where you can see all the list of browsers under chromium similarly under webkit you can see all the

4:39 webkit browsers like safari and then firefox browsers so all these are supported then if i talk about the operating system


# Chapter 6: OS supported

4:46 supported by playwright then you can create your playwright framework on a windows operating system on a mac operating system or a linux operating

4:54 system and it also supports ci runs so if you want to use any ci cd tool docker all that is supported now this is the

5:02 official website of playwright so if i go and search for playwright

5:10 you can see here this is the official website playwright.dev and here you can see the details about playwright the

5:18 documentation all the features cross browser class cross platform cross language mobile web and all these features auto

5:27 weight assertions all this you can see here and here you can see the implementations so if you go

5:35 to this drop down you can see all these implementations we have node.js python java and dotnet so when you select any

5:43 of these implementations or libraries and then if you click on this github link it will take you to the github page for that particular

5:52 api of playwright or that particular implementation of payride so here i had selected node.js from here and then i clicked on this github link so it has

6:01 taken me to the github page for the playwright node.js implementation and you can see all the details here as well

6:08 similarly if i go here and select java and then i click on this github link it will take me to the

6:16 github page for the playwright java implementation and this is the link for playwright github and this is

6:24 also very important you will see all the comments everything here so that is why it is open source because

6:33 we can contribute to this playwright project and these two links are very important i have shown you these things so so that in future if there is any

6:41 changes if there are any changes you can always refer from here so this is what playwright is now if you want you can take a screenshot of this screen and


# Chapter 7: Screenshot moment

6:48 keep it handy with you you can keep it on your mobile or keep it on your desktop screen and look at it look at it multiple times so that it becomes very

6:57 clear for you that what is playwright and with that let us now go to the features of playwright so we have


# Chapter 8: Features of Playwright

7:05 already seen it is free and open source free means you can use it freely and open source means we can contribute to the playwright project then

7:14 it is multi-browser it has multi-browser support multi-language support multi-operating system support this we have already seen the setup and

7:21 installation is very easy in the coming session we will see how easy it is to set up and install and configure playwright

7:29 then we can do functional testing with playwright we can do api testing and we can also do accessibility testing so there is a third party plugin that we

7:37 can add into our playwright framework and then we can do accessibility testing as well playwright has built-in reporters so you

7:45 will not have to add separate reporters in your framework but if you want you can also use custom reporters and if you

7:53 want to use any reporters like leo reporting all that is supported so you can use custom reporters as well in playwright then we also have a ci cd

8:02 support and docker support so if you want to use any ci cd tools like jenkins or if you want to use any container platforms like docker that is also

8:10 possible with playwright then we have recording options so if you want to record your test and you want to get your test scripts generated that is

8:19 possible with playwright uh if you want to debug your test and if you want to do step by step debugging that is possible i will show you in the later sessions

8:27 how do we do recording and debugging and you can also capture the object locators from the screen so you do not have to

8:35 manually create the locators for your web objects playwright has options to explore and create locators for you and

8:42 then we can do parallel testing and with parallel testing we can make our testing very fast all the playwright in itself is very fast but with parallel testing

8:51 we can run playwright on multiple browsers at the same time then we have auto weight and auto


# Chapter 9: Some more features

8:58 timeouts so there are some auto weight inbuilt in playwright when we are loading a page or when we are finding some object or we are doing any action

9:07 on the object there is a timeout available and by default it is five seconds and we can change it as

9:14 well so auto wait is there then we have built-in assertions for example if you want to click on a button let us say we are on the login screen and we want to

9:22 click on the login button so we will just uh add the step to click on the login button but at the back end playwright will add will uh you know run

9:31 some assessions built in assessions like is the page already loaded if if the object is already loaded if the object is present if the object is clickable

9:39 all this will happen at the back end so there are built-in assertions and with auto wait timeouts and built-in assertions

9:46 our testing and our test cases are a very less flaky flaky test means when you run a test sometimes it passes and

9:54 sometimes it fails so so these kind of tests are flaky tests so with playeride they will be very less or no flaky test

10:03 then we have options for retry logic if you want to retry your field tests uh we have options to see the logs generate

10:11 the logs we have options for screenshot and videos of our test execution so all this is there then a very important

10:19 feature in playwright is we have support for multi-tab and multi window execution so a lot of times in

10:28 our applications in our scenarios we have a scenario like if i click on a link if i click on a button

10:36 it opens a page in a new window or a new tab and in a lot of automation tools this is not supported but in playwright

10:43 it is supported even if you want to do multi-window multi-tab testing you can do that with playwright then

10:50 playwright can handle iframes and shadow dom objects this is also very very important and very useful in automation

10:57 then if you want to emulate devices if you want to run your test by emulating some devices like a mobile device you can do

11:06 that if you want to set some viewport or the screen size or the resolution and then do the testing that is possible if you want to change the geo locations

11:14 even that is possible so for example uh if i just go to my uh let us say my chrome browser and i am pressing f12

11:22 on my keyboard so that i go to the chrome dev tools and here you can see here

11:30 we have option to select devices so if i click here on this devices

11:37 i will have option to select devices like galaxy iphone pixel samsung and i can set the

11:45 resolution from here so we can set the screen size and resolution and with playwright we can also do this we can also set the geo

11:54 locations so all this we can do with playwright then uh we can do parameterization we can add

12:01 variables we can do data driven testing or we can use some external files like a csv file to get our data and do testing

12:09 so that is possible and playwright is very fast when we run our test cases you will see how fast it is so play that is very very fast and of

12:17 course we have parallel testing as well so it will make it even more faster so these are all the features of playwright now if you want you can take a


# Chapter 10: All feature list *Screenshot moment

12:25 screenshot of this screen and keep it handy with you and look at it several times and you will never forget all the features of playwright and

12:34 with that we have completed this session from the next session we will do hands-on we will install playwright we will see the

12:42 prerequisites and then we will run create and run our test cases i hope this was very useful for you thank you

12:49 for watching and as i always say never stop learning
