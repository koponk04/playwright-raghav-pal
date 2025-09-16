Chapter 1: Intro
0:00
hello and welcome I am raghav and today we are going to learn annotations and tags in playwright this is going to be
0:09
9 seconds
very easy and very interesting and I will go very basic step by step so we are going to see what are tags and annotations in playwright how do we use
0:17
17 seconds
the annotations and tags and we will see a step-by-step Hands-On demo now in the last session we have already seen the
0:24
24 seconds
hooks and groups how do we use different hooks in playwright in the tests and how can we group our test cases and today we
Chapter 2: What are Annotations & Tags
0:32
32 seconds
will see annotations we have different annotations like only skip fix me slow Etc and then we can also tag our test
0:41
41 seconds
cases with tags like at regression at smoke at sanity at fast etc etc and then we can run the tests with specific tags
0:50
50 seconds
or we can also have an option where we can skip the tests having a certain tag we will see this in a moment so let's
0:57
57 seconds
get started and see some annotations and before that I will will go to my project I will open my vs code and this is my
1:05
1 minute, 5 seconds
project and I will first uh create a new file now some of you have
1:13
1 minute, 13 seconds
given me a feedback in the comments section to use the Dark theme in Visual Studio code so today I will try the Dark theme and you can let me know if that is
1:21
1 minute, 21 seconds
fine I will continue with that so to do that I can go to settings or I will just go to command palette I'm pressing Ctrl
1:28
1 minute, 28 seconds
shift and P key on my keyboard to bring up the command palette
1:35
1 minute, 35 seconds
and this is Ctrl shift p and then I will say color theme uh
1:42
1 minute, 42 seconds
yeah I have got this here and I will use the Dark theme here uh so
1:51
1 minute, 51 seconds
I think this is fine okay now I will go to the tests folder here this is my tests folder and then I will
1:59
1 minute, 59 seconds
create a new file I will name it as annotations
2:06
2 minutes, 6 seconds
and tax dot spec dot Js okay so I have created this file
2:13
2 minutes, 13 seconds
annotations and tags.spec.js and here I will start typing so I will first import
2:20
2 minutes, 20 seconds
I will import uh test and expect or I I will just need test here
2:29
2 minutes, 29 seconds
and I will import from playwright if you want you can also
2:39
2 minutes, 39 seconds
right click and say format documentation and now I will start creating some tests
2:45
2 minutes, 45 seconds
so I will say test and I will give some name test one
2:54
2 minutes, 54 seconds
and then I can give the async function here and
3:03
3 minutes, 3 seconds
this is my test now let us see the annotations one by one so the first one
Chapter 3: will skip the test
3:09
3 minutes, 9 seconds
is Skip I can say test dot Skip and this will skip the test so let us say
3:16
3 minutes, 16 seconds
I will also just pass the page fixture if I have to use it I will say test dot skip
3:24
3 minutes, 24 seconds
you can see it is also giving me this Auto suggestion and this should when I run this test file this particular test
3:32
3 minutes, 32 seconds
should be skipped so here I can run the test I will first open the
3:39
3 minutes, 39 seconds
terminal I will go to terminal and new terminal and now here I will say
3:49
3 minutes, 49 seconds
I will have to say here npx playwright test make sure that you save
3:57
3 minutes, 57 seconds
your test and now I will say tests folder press Tab Key to auto complete and then go to the file annotations and
4:07
4 minutes, 7 seconds
tags I will press tab to auto complete all this and then I just want to run on a single browser so I will say hyphen
4:14
4 minutes, 14 seconds
hyphen project chromium so this is my command and let us now run
4:24
4 minutes, 24 seconds
and check uh some issue let me very quickly see what is the issue here
4:37
4 minutes, 37 seconds
okay uh let me see this okay I believe uh I used this there was a typo in this
4:45
4 minutes, 45 seconds
word chromium I will run this again so I am pressing the up arrow on my keyboard
4:53
4 minutes, 53 seconds
this is chromium and now let us check and as you can see it says one skipped
5:01
5 minutes, 1 second
if I see the report in the report as well you will see that the test is skipped so I will say npx playwrite show
5:08
5 minutes, 8 seconds
report and here you can see this is skipped so this test is skipped so this is how
5:18
5 minutes, 18 seconds
we can use this annotation then we can also use the sale annotation and this will Mark the test as failure and in
Chapter 4: will mark test as failure
5:26
5 minutes, 26 seconds
case the test passes it will show some error so uh let me show you and I also have some of these uh tests already
5:34
5 minutes, 34 seconds
written so that I can save some time I'm just going to save this or all these tests will be there in the description of this video so in case you want you
5:41
5 minutes, 41 seconds
can copy it from the description or you will also get all this in the official documentation of playwright so let me
5:50
5 minutes, 50 seconds
run this test I am saying test and here inside the test I am saying test dot sale so if I now
5:59
5 minutes, 59 seconds
run this I will go to terminal first I will stop this uh report by pressing Ctrl C and Y
6:07
6 minutes, 7 seconds
and clear the console clear the terminal and I will use the top Arrow to go to the last
6:15
6 minutes, 15 seconds
command and yes I will run it again and let us see this time you this time this is running two tests
6:23
6 minutes, 23 seconds
and you can see here it is showing one escaped and one has failed so if I go to the field one this one is marked as
6:32
6 minutes, 32 seconds
field and the earlier test is marked as skipped so this is how we can also Mark the test as failure then if you have
Chapter 5: test will be aborted
6:41
6 minutes, 41 seconds
some test which you do not want to run and you want to mark it as uh you want to market for fixing you can use the fix
6:49
6 minutes, 49 seconds
me annotation so here you can use this let me again copy this
6:54
6 minutes, 54 seconds
test from here and add it to my script so you can see this will be
7:03
7 minutes, 3 seconds
about it and if I now save and
7:10
7 minutes, 10 seconds
run my command and let us see the report this time
7:19
7 minutes, 19 seconds
you can see here it is about it or skipped so this one is now marked for fixing so this is how we
7:27
7 minutes, 27 seconds
can Mark a test for fixing as well then
7:35
7 minutes, 35 seconds
I can use The annotation slow this uh marks that this particular test is slow
Chapter 6: marks the test as slow and triples the test timeout
7:43
7 minutes, 43 seconds
therefore it will triple the time out so whatever timeout you have set in the configuration file it will triple that
7:50
7 minutes, 50 seconds
time because this test runs slow so here I will copy this
8:00
8 minutes
and paste so this particular test will be will have the timeout with triple the count whatever you have given in the
8:08
8 minutes, 8 seconds
configuration file now I am not using any uh example of a browser but if you want you can run it and check you will
8:16
8 minutes, 16 seconds
have the triple time out so wherever you have any test which is slow you can use this annotation then the next we have
Chapter 7: runs specific tests
8:22
8 minutes, 22 seconds
only and this will run a particular test whenever you want to run some specific test or some specific uh tests inside
8:31
8 minutes, 31 seconds
the file you can mark it by dot only annotation so for example if I say
8:39
8 minutes, 39 seconds
dot only here it will run only this particular test from this file and we can mark multiple tests with this annotation only so let
8:47
8 minutes, 47 seconds
me run and check let us see this time you can see it has executed only one test and this test has
8:57
8 minutes, 57 seconds
passed if I check the report you will see the report that only this
9:03
9 minutes, 3 seconds
particular test which is slow test is executed here okay I will stop
9:12
9 minutes, 12 seconds
the report here and clear the terminal
9:21
9 minutes, 21 seconds
then there is also a annotation to skip conditionally sometimes you want to skip a particular test but based on some
9:29
9 minutes, 29 seconds
condition this you can also try and in fact if you go to uh
9:35
9 minutes, 35 seconds
playwright annotations it will take you to the official documentation of playwright and the annotations page annotations
9:44
9 minutes, 44 seconds
documentation and here you can see all these annotations so you can see uh skip with condition will be here conditionally Skipper test so you can
9:54
9 minutes, 54 seconds
see this test so here it is saying test dot skip if browser name equals Firefox so in case the browser is set to Firefox
10:02
10 minutes, 2 seconds
this will be skipped because maybe this particular test is not working on Firefox or whatever condition you want to use you can use it like this
10:10
10 minutes, 10 seconds
so we have we can use all these annotations and uh if you want
10:17
10 minutes, 17 seconds
you can take a screenshot of this screen and keep it handy with you so that you can go through it multiple times and
10:25
10 minutes, 25 seconds
then you will always remember all these annotations now coming to tags so here we can tag our test cases with tags like
Chapter 8: Tags
10:33
10 minutes, 33 seconds
at smoke at sanity at regression at slow at fast Etc whatever tax we want to use and then we can make the tests with
10:40
10 minutes, 40 seconds
specific tests run only when we run the test file so for that we uh we can do something like this
10:49
10 minutes, 49 seconds
I will use this particular test so let me show you
10:59
10 minutes, 59 seconds
in the test script I will say these are tags
11:06
11 minutes, 6 seconds
and you can see this test we give that we give the tag within the title of the
11:13
11 minutes, 13 seconds
test so basically that also means that it is not necessary that you use some symbol like add or anything you can give
11:22
11 minutes, 22 seconds
anything and then while running the command we will use the grep keyword to
11:28
11 minutes, 28 seconds
give these tags and whenever any test that matches that title or any test that has that word in the title of the test
11:37
11 minutes, 37 seconds
that will get executed but just to keep it more meaningful meaningful we use these at the rate symbol and then we can
11:44
11 minutes, 44 seconds
say at fast at slow at smoke at sanity so let us say I will say this is at smoke
11:51
11 minutes, 51 seconds
and then to run it we will say the normal command and then we will add this option hyphen hyphen grab and then
11:59
11 minutes, 59 seconds
give the tag here so I will save this and then I will go to my command so this was our earlier
12:07
12 minutes, 7 seconds
command here I will add hyphen hyphen grab so this is hyphen hyphen let me uh
12:14
12 minutes, 14 seconds
expand this and show you so this is hyphen hyphen grab and then I
12:21
12 minutes, 21 seconds
will within codes I will say at the rate smoke and Save
12:28
12 minutes, 28 seconds
and I will run this and you can see uh
12:35
12 minutes, 35 seconds
let me check again it says no tests found I will save this again
12:43
12 minutes, 43 seconds
okay I will have to remove this only because it is only running this test and here it did not find the tag
12:49
12 minutes, 49 seconds
at smoke so I will now remove the only tests or the tag tests tag tagged with
12:56
12 minutes, 56 seconds
only keyword and now I will run my command again and let us see this time
13:03
13 minutes, 3 seconds
and you can see it is running only one test because only one test was found having this tag at smoke and if I check
13:12
13 minutes, 12 seconds
the report you will see this only this test is getting executed that is test login
13:20
13 minutes, 20 seconds
page at the rate smoke is executed here and then I will stop the report
13:27
13 minutes, 27 seconds
control C and Y and clear the terminal then sometimes you may also want to uh
13:35
13 minutes, 35 seconds
skip the tests having a certain tag in that case you can use hyphen have hyphen grab inward in the command so here we
13:43
13 minutes, 43 seconds
used grab if you say graph in word and then whatever tag you give all the tests having this tag will be skipped so this
13:51
13 minutes, 51 seconds
also will be very useful and very handy so we have learned about annotations and we can Now understand annotations are
Chapter 9: What are Annotations
13:58
13 minutes, 58 seconds
keywords that contain some logical or conditional functionalities and you can use it within test blocks control execution of the tests as you require
14:07
14 minutes, 7 seconds
and we can apply annotations to single tests or also to a set of tests and also in a group I hope this was useful if you
14:15
14 minutes, 15 seconds
have any questions you can let me know in the comment section I will see you in the next session thank you for watching
14:21
14 minutes, 21 seconds
and never stop learning
