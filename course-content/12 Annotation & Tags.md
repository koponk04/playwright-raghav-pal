# Chapter 1: Intro

0:00 hello and welcome I am raghav and today we are going to learn annotations and tags in playwright this is going to be

0:09 very easy and very interesting and I will go very basic step by step so we are going to see what are tags and annotations in playwright how do we use

0:17 the annotations and tags and we will see a step-by-step Hands-On demo now in the last session we have already seen the

0:24 hooks and groups how do we use different hooks in playwright in the tests and how can we group our test cases and today we


# Chapter 2: What are Annotations & Tags

0:32 will see annotations we have different annotations like only skip fix me slow Etc and then we can also tag our test

0:41 cases with tags like at regression at smoke at sanity at fast etc etc and then we can run the tests with specific tags

0:50 or we can also have an option where we can skip the tests having a certain tag we will see this in a moment so let's

0:57 get started and see some annotations and before that I will will go to my project I will open my vs code and this is my

1:05 project and I will first uh create a new file now some of you have

1:13 given me a feedback in the comments section to use the Dark theme in Visual Studio code so today I will try the Dark theme and you can let me know if that is

1:21 fine I will continue with that so to do that I can go to settings or I will just go to command palette I'm pressing Ctrl

1:28 shift and P key on my keyboard to bring up the command palette

1:35 and this is Ctrl shift p and then I will say color theme uh

1:42 yeah I have got this here and I will use the Dark theme here uh so

1:51 I think this is fine okay now I will go to the tests folder here this is my tests folder and then I will

1:59 create a new file I will name it as annotations

2:06 and tax dot spec dot Js okay so I have created this file

2:13 annotations and tags.spec.js and here I will start typing so I will first import

2:20 I will import uh test and expect or I I will just need test here

2:29 and I will import from playwright if you want you can also

2:39 right click and say format documentation and now I will start creating some tests

2:45 so I will say test and I will give some name test one

2:54 and then I can give the async function here and

3:03 this is my test now let us see the annotations one by one so the first one


# Chapter 3: will skip the test

3:09 is Skip I can say test dot Skip and this will skip the test so let us say

3:16 I will also just pass the page fixture if I have to use it I will say test dot skip

3:24 you can see it is also giving me this Auto suggestion and this should when I run this test file this particular test

3:32 should be skipped so here I can run the test I will first open the

3:39 terminal I will go to terminal and new terminal and now here I will say

3:49 I will have to say here npx playwright test make sure that you save

3:57 your test and now I will say tests folder press Tab Key to auto complete and then go to the file annotations and

4:07 tags I will press tab to auto complete all this and then I just want to run on a single browser so I will say hyphen

4:14 hyphen project chromium so this is my command and let us now run

4:24 and check uh some issue let me very quickly see what is the issue here

4:37 okay uh let me see this okay I believe uh I used this there was a typo in this

4:45 word chromium I will run this again so I am pressing the up arrow on my keyboard

4:53 this is chromium and now let us check and as you can see it says one skipped

5:01 if I see the report in the report as well you will see that the test is skipped so I will say npx playwrite show

5:08 report and here you can see this is skipped so this test is skipped so this is how

5:18 we can use this annotation then we can also use the sale annotation and this will Mark the test as failure and in


# Chapter 4: will mark test as failure

5:26 case the test passes it will show some error so uh let me show you and I also have some of these uh tests already

5:34 written so that I can save some time I'm just going to save this or all these tests will be there in the description of this video so in case you want you

5:41 can copy it from the description or you will also get all this in the official documentation of playwright so let me

5:50 run this test I am saying test and here inside the test I am saying test dot sale so if I now

5:59 run this I will go to terminal first I will stop this uh report by pressing Ctrl C and Y

6:07 and clear the console clear the terminal and I will use the top Arrow to go to the last

6:15 command and yes I will run it again and let us see this time you this time this is running two tests

6:23 and you can see here it is showing one escaped and one has failed so if I go to the field one this one is marked as

6:32 field and the earlier test is marked as skipped so this is how we can also Mark the test as failure then if you have


# Chapter 5: test will be aborted

6:41 some test which you do not want to run and you want to mark it as uh you want to market for fixing you can use the fix

6:49 me annotation so here you can use this let me again copy this

6:54 test from here and add it to my script so you can see this will be

7:03 about it and if I now save and

7:10 run my command and let us see the report this time

7:19 you can see here it is about it or skipped so this one is now marked for fixing so this is how we

7:27 can Mark a test for fixing as well then

7:35 I can use The annotation slow this uh marks that this particular test is slow


# Chapter 6: marks the test as slow and triples the test timeout

7:43 therefore it will triple the time out so whatever timeout you have set in the configuration file it will triple that

7:50 time because this test runs slow so here I will copy this

8:00 and paste so this particular test will be will have the timeout with triple the count whatever you have given in the

8:08 configuration file now I am not using any uh example of a browser but if you want you can run it and check you will

8:16 have the triple time out so wherever you have any test which is slow you can use this annotation then the next we have


# Chapter 7: runs specific tests

8:22 only and this will run a particular test whenever you want to run some specific test or some specific uh tests inside

8:31 the file you can mark it by dot only annotation so for example if I say

8:39 dot only here it will run only this particular test from this file and we can mark multiple tests with this annotation only so let

8:47 me run and check let us see this time you can see it has executed only one test and this test has

8:57 passed if I check the report you will see the report that only this

9:03 particular test which is slow test is executed here okay I will stop

9:12 the report here and clear the terminal

9:21 then there is also a annotation to skip conditionally sometimes you want to skip a particular test but based on some

9:29 condition this you can also try and in fact if you go to uh

9:35 playwright annotations it will take you to the official documentation of playwright and the annotations page annotations

9:44 documentation and here you can see all these annotations so you can see uh skip with condition will be here conditionally Skipper test so you can

9:54 see this test so here it is saying test dot skip if browser name equals Firefox so in case the browser is set to Firefox

10:02 this will be skipped because maybe this particular test is not working on Firefox or whatever condition you want to use you can use it like this

10:10 so we have we can use all these annotations and uh if you want

10:17 you can take a screenshot of this screen and keep it handy with you so that you can go through it multiple times and

10:25 then you will always remember all these annotations now coming to tags so here we can tag our test cases with tags like


# Chapter 8: Tags

10:33 at smoke at sanity at regression at slow at fast Etc whatever tax we want to use and then we can make the tests with

10:40 specific tests run only when we run the test file so for that we uh we can do something like this

10:49 I will use this particular test so let me show you

10:59 in the test script I will say these are tags

11:06 and you can see this test we give that we give the tag within the title of the

11:13 test so basically that also means that it is not necessary that you use some symbol like add or anything you can give

11:22 anything and then while running the command we will use the grep keyword to

11:28 give these tags and whenever any test that matches that title or any test that has that word in the title of the test

11:37 that will get executed but just to keep it more meaningful meaningful we use these at the rate symbol and then we can

11:44 say at fast at slow at smoke at sanity so let us say I will say this is at smoke

11:51 and then to run it we will say the normal command and then we will add this option hyphen hyphen grab and then

11:59 give the tag here so I will save this and then I will go to my command so this was our earlier

12:07 command here I will add hyphen hyphen grab so this is hyphen hyphen let me uh

12:14 expand this and show you so this is hyphen hyphen grab and then I

12:21 will within codes I will say at the rate smoke and Save

12:28 and I will run this and you can see uh

12:35 let me check again it says no tests found I will save this again

12:43 okay I will have to remove this only because it is only running this test and here it did not find the tag

12:49 at smoke so I will now remove the only tests or the tag tests tag tagged with

12:56 only keyword and now I will run my command again and let us see this time

13:03 and you can see it is running only one test because only one test was found having this tag at smoke and if I check

13:12 the report you will see this only this test is getting executed that is test login

13:20 page at the rate smoke is executed here and then I will stop the report

13:27 control C and Y and clear the terminal then sometimes you may also want to uh

13:35 skip the tests having a certain tag in that case you can use hyphen have hyphen grab inward in the command so here we

13:43 used grab if you say graph in word and then whatever tag you give all the tests having this tag will be skipped so this

13:51 also will be very useful and very handy so we have learned about annotations and we can Now understand annotations are


# Chapter 9: What are Annotations

13:58 keywords that contain some logical or conditional functionalities and you can use it within test blocks control execution of the tests as you require

14:07 and we can apply annotations to single tests or also to a set of tests and also in a group I hope this was useful if you

14:15 have any questions you can let me know in the comment section I will see you in the next session thank you for watching

14:21 and never stop learning
