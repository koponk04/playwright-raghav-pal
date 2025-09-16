Chapter 1: Intro
0:00
hello and welcome i'm raghav and today we are going to learn something very easy and very interesting and that is
0:08
8 seconds
assertions in playwright so in this session we will see what are assertions we will see what are the assessions in playwright and then we will see how to
0:16
16 seconds
add assertions in our test in playwright so this is going to be very interesting let's get started with what are
Chapter 2: What are Assertions
0:23
23 seconds
assertions now in very very simple words assertions are like checks or verifications that we do in our test for
0:31
31 seconds
example if i want to check if an element is present or not present if a text is present or not present or if the element has some particular value or not all
0:39
39 seconds
these will be assertions so we actually check uh these things and whenever we add a session it checks
0:47
47 seconds
whatever we have given in the session is it equal to the actual and if actual and expected are equal it will pass
0:54
54 seconds
otherwise it will fail the test so in assertions uh in playwright we use the expect keyword this comes from the jest
Chapter 3: Assertions in Playwright
1:02
1 minute, 2 seconds
testing test runner and this is what we use and it comes inbuilt in the playwright library so we can directly say expect and then we can write our
1:11
1 minute, 11 seconds
assertions in a moment i will show you how to add a sessions so in this session we are going to see how to check if an element is present or not present
Chapter 4: How to add Assertions
1:19
1 minute, 19 seconds
visible or hidden whether an element is enabled or disabled whether the text matches some particular value or does
1:26
1 minute, 26 seconds
not match a particular value we can check the element attribute as well like the class id or any attribute that you want to check we can check the page url
1:35
1 minute, 35 seconds
we can check the page title and then we will also see how we can
1:42
1 minute, 42 seconds
match or how we can assert our web page against a screenshot and in this case we are doing visual validation
1:50
1 minute, 50 seconds
and it means that we are going to check how does the page looks in terms of the colors the location of the objects the size of the objects the the font the
1:59
1 minute, 59 seconds
pixel and anything that you want to check based on the visual validation or the appearance of the web page we can do
2:06
2 minutes, 6 seconds
that as well and then i will talk about soft assertions what are softer sessions so generally when we add these assertions whenever
2:15
2 minutes, 15 seconds
there is a failure whenever an assertion fails it will stop the execution and come out of the execution but in case we want that our
2:23
2 minutes, 23 seconds
execution the test execution should not stop if a session fails we can use soft assertions so we will look at that so
2:30
2 minutes, 30 seconds
first let's start with uh present not present and i will go to my vs code and here is the project
Chapter 5: Create a new Test
2:39
2 minutes, 39 seconds
and i will go to my test folder and i am going to create a new file so i will say this is
2:47
2 minutes, 47 seconds
assertions dot spec dot js so i have created this file
2:55
2 minutes, 55 seconds
assertions.spec.js and here at the top i will say import i want to import page and expect
3:04
3 minutes, 4 seconds
libraries or scripts from the playwright test library
3:12
3 minutes, 12 seconds
and after this i can start writing my test so i will say test and i will first give the title i will say
3:20
3 minutes, 20 seconds
assertions demo and then i will create a
3:26
3 minutes, 26 seconds
async function so let me add this async function here
3:36
3 minutes, 36 seconds
and i will give this arrow symbol and curly bracket start and stop and in this function i am going to pass a page
3:43
3 minutes, 43 seconds
fixture so this is how we declare our test and then i will just say await
3:51
3 minutes, 51 seconds
page dot go to to visit our web page i will say page dot go to all this we have already learned and here i will give the url of the
4:00
4 minutes
application now for this demo uh let us go to uh this
Chapter 6: Demo App
4:08
4 minutes, 8 seconds
demo application kitchen.applytools.com and here you can see here we have this web page we have all these buttons
4:17
4 minutes, 17 seconds
here so we will use this and in case at your time this application is not up or not available you can use any other
4:24
4 minutes, 24 seconds
application or you can use your own application as well so i will just go to this link i will have all these links all the
4:32
4 minutes, 32 seconds
notes in the description of this video so you can always check from there i will also add the code there and now
4:39
4 minutes, 39 seconds
i'm going to say await page dot pause now i'm adding this pause statement here
4:47
4 minutes, 47 seconds
so that as soon as it comes to the power statement it will pause the execution and open the playwright inspector window
4:54
4 minutes, 54 seconds
so we can then uh run our execution step by step and we can also see the execution the statements where exactly
5:01
5 minutes, 1 second
it has gone and we can see everything on the screen so now i will try to run this and
5:08
5 minutes, 8 seconds
here i will first open a terminal window so i can go from here and say new terminal or press control plus j key on your keyboard to bring up the terminal
Chapter 7: Command to Run the test
5:17
5 minutes, 17 seconds
window and here i will now say npx
5:25
5 minutes, 25 seconds
playwright test and i want to run a specific file so i will say tests i am pressing tab so
5:33
5 minutes, 33 seconds
it will auto complete and assertion i am again pressing tab on my keyboard it will auto complete now it will run on all the
5:41
5 minutes, 41 seconds
browsers which are configured in the config file but i just want to run on one browser so that we can save some time so i will
5:49
5 minutes, 49 seconds
say hyphen hyphen project chromium so it will only run on chrome browser and also i want to see the execution so i will say hyphen hyphen headed so it will run
5:58
5 minutes, 58 seconds
in a headed mode and it will bring up the physical browser on the screen so i have started the execution and you can see it has gone to the chrome browser
6:06
6 minutes, 6 seconds
and gone to the application and now here it has as soon as it encountered the pause statement it has opened the playwright
6:14
6 minutes, 14 seconds
inspector and now i can do step by step execution by using this button so before going here
6:22
6 minutes, 22 seconds
we want to check all these assertions first element present not present visible or
6:29
6 minutes, 29 seconds
hidden enabled or disabled text matches value or not and the element attribute so here
Chapter 8: Check element Present/Not present
6:38
6 minutes, 38 seconds
let us say i first want to get some element so i will click on this explore button on the playwright
6:45
6 minutes, 45 seconds
inspector and now i will go to the web page and wherever i am taking my pointer it is highlighting let me just go to this the kitchen
6:54
6 minutes, 54 seconds
element and if i again check my playwright inspector this is the selector
7:01
7 minutes, 1 second
i can create a locator using this so i will just go to my project and in the test i will say
7:11
7 minutes, 11 seconds
await page dot locator and i will use this locator
7:18
7 minutes, 18 seconds
and now i can do my assertions so let me also add the comments so it will be easier for you
7:25
7 minutes, 25 seconds
i will say assertions and the first session we are going to check is uh check if the element is present
7:34
7 minutes, 34 seconds
so check i will say check element
7:41
7 minutes, 41 seconds
present or not okay now here we can say expect and we can give the locator and
7:48
7 minutes, 48 seconds
then say to have count or we can also give the element handle let me show you so here i will say
7:56
7 minutes, 56 seconds
await and i will say expect and this page dot locator i will put in this
8:04
8 minutes, 4 seconds
brackets like this and then i will say to have count and i will say count one so this
8:12
8 minutes, 12 seconds
means we are checking or we are asserting that there should be a unique element a single element with this
8:19
8 minutes, 19 seconds
locator so we can run this i will save and on the terminal i will press ctrl c
8:26
8 minutes, 26 seconds
to stop this process and clear the terminal and i am pressing the up arrow on my keyboard to go to the last command
8:34
8 minutes, 34 seconds
and i will now run this again so let us see this time it should run this assertion as well
8:42
8 minutes, 42 seconds
so it has come here it has paused i will go next and you can see this is the it has also highlighted this element and if
8:50
8 minutes, 50 seconds
there is a single instance of this element present on this page or with this locator it should pass and
8:57
8 minutes, 57 seconds
if i now resume you can see it has passed so this is working fine now
9:03
9 minutes, 3 seconds
i can also say here i can say page dot dollar this is an element handle i can say await
9:12
9 minutes, 12 seconds
page dot dollar and you can see here you can see the use of element handle is discouraged so when
9:20
9 minutes, 20 seconds
you want to check whether it is present or not you should always use the expect keyword and add the assertions but i will show you where exactly it will be
9:29
9 minutes, 29 seconds
helpful so i can just give the locator of the element which is this
9:37
9 minutes, 37 seconds
and now if i run this this will pass but if i have to add a condition that if this element is present then i want to
9:44
9 minutes, 44 seconds
do something based on that condition so if i create a if loop or the if condition sorry this is the condition if condition and in the
9:53
9 minutes, 53 seconds
bracket i will just pass this and then i will say inside the if block i will
10:02
10 minutes, 2 seconds
say i'll just use this i will say
10:10
10 minutes, 10 seconds
await and page dot locator and this locator and i will say dot click so i'm just saying that if
10:18
10 minutes, 18 seconds
this is present if this element is present then i should go inside this if block
10:25
10 minutes, 25 seconds
and click on the element now let me save and run it again so i am running the command again and
10:35
10 minutes, 35 seconds
let us see the execution this time so if you want you can do hands-on along with me and if you face any issues you
10:43
10 minutes, 43 seconds
can let me know i will click on next next and you can see it has now come to this if block and this condition
10:51
10 minutes, 51 seconds
was true and therefore it has come inside the block and now it should click on the element and it has clicked and now i will resume the execution and
10:59
10 minutes, 59 seconds
everything has passed so it can be helpful this way of using the element handle can be helpful if you want to add
11:07
11 minutes, 7 seconds
this in a condition that whether this element is present or not based on that condition you want to do some action now if you try to add this in a condition it
11:15
11 minutes, 15 seconds
will not work so if you want you can try to add this in the if block in the condition of the if block here and you can try this will not work because it is
11:24
11 minutes, 24 seconds
not returning true or false but this statement is returning true or false so therefore this will work now you can also check whether an
Chapter 9: Check element Visible/Hidden
11:32
11 minutes, 32 seconds
element is hidden or not so i can use the same statement and i can say so i will say
11:41
11 minutes, 41 seconds
check element hidden or visible
11:50
11 minutes, 50 seconds
and here i can use the same statement expect and the locator and then i can say to be visible
11:59
11 minutes, 59 seconds
or i can say dot to be hidden
12:06
12 minutes, 6 seconds
and this will check whether the element is hidden or visible now i am not re-executing it now i will execute after
12:13
12 minutes, 13 seconds
adding some more assertions so we can save some time in the same way we can check enabled or disabled so i will say
Chapter 10: Check element Enabled/Disabled
12:22
12 minutes, 22 seconds
check element enabled or disabled and i will say
12:30
12 minutes, 30 seconds
to be enabled and you can see as i'm typing to be we are getting so many options to be
12:38
12 minutes, 38 seconds
checked to be close to be disabled to be editable to be empty to be focused so you can try all these successions and
12:45
12 minutes, 45 seconds
you can use them so i will say to be i will say to be enabled
12:55
12 minutes, 55 seconds
and then i will say dot to be disabled
13:04
13 minutes, 4 seconds
so this will checked enabled or disabled okay now let me save
13:12
13 minutes, 12 seconds
and run it once so i will clear the terminal and run the command again and let us see what
13:20
13 minutes, 20 seconds
happens this time so here some assertions will fail let us see what happens when we have failed accessions so
13:28
13 minutes, 28 seconds
we have got the update inspector i will go next next next and all this is passing and now we
13:35
13 minutes, 35 seconds
have come to this assession that is this element should be hidden but this should fail so if i go next you can see it will
13:44
13 minutes, 44 seconds
check and it will go until the timeout that we have in our configuration file and then it has
13:51
13 minutes, 51 seconds
failed it and therefore you can see it is shown here as a failure i will again go next and you can see it stopped the
13:58
13 minutes, 58 seconds
execution as it encountered the failure and it will also open the report
14:06
14 minutes, 6 seconds
so let me just resume it and if i want to check the report
14:14
14 minutes, 14 seconds
it is opening the report and here you can see it says that this was failed this was the issue
14:23
14 minutes, 23 seconds
this is failed here to be hidden has failed and then if you check after this step it has stopped but if
14:31
14 minutes, 31 seconds
you want that this should continue even after this step then we can make it as a soft assertion now also you can see it has after failing it has retried for one
14:40
14 minutes, 40 seconds
more time therefore we are getting this retry result as well but we just want this to run once so for that
14:49
14 minutes, 49 seconds
i will go to my configuration file and here you can see the timeout we have already
14:57
14 minutes, 57 seconds
decreased the timeout in the earlier session so it is waiting just for three seconds let me make it even
15:03
15 minutes, 3 seconds
less two seconds so that we don't waste time in demo and here is the retries i will comment this out
15:12
15 minutes, 12 seconds
so it was uncommented i am pressing control and forward slash on my keyboard to comment this and i will save so this will now not retry after failure and
15:21
15 minutes, 21 seconds
then coming here back to the assertions now in case you want that in case a session fails it should not stop the
Chapter 11: How to add Soft Assertions
15:28
15 minutes, 28 seconds
execution in that case you can make it as a soft session and to make it as a softer session after this expect i will
15:36
15 minutes, 36 seconds
just say dot soft so this will make it a softer session this also i will make a soft accession
15:43
15 minutes, 43 seconds
so that it should not stop the execution let us try i will press ctrl c on the terminal to stop this process and
15:52
15 minutes, 52 seconds
run my command again and this time it should not stop the execution when these accessions fails that we have
16:00
16 minutes
made as software sessions so it has come here i will go next next next next and now this should fail and
16:09
16 minutes, 9 seconds
let us see what happens so you can see it failed but it still went to the next step so i will say next
16:17
16 minutes, 17 seconds
this one has passed and again this one should fail and it has failed and i will resume
16:24
16 minutes, 24 seconds
and now if i see the report you can see here the first thing is it has not retried
16:32
16 minutes, 32 seconds
now if i check the execution you can see here it has executed all the steps so this one was failed it went ahead this
16:39
16 minutes, 39 seconds
one was passed and then this one was again failed so we have got our complete test execution and we can see what all has failed
16:47
16 minutes, 47 seconds
so this was how you can check enabled or disabled if you want to check whether the element has some text you can say
Chapter 12: Check element Text matches value or not
16:54
16 minutes, 54 seconds
dot to have text and give the value or you can say not to have text and this will check that
17:01
17 minutes, 1 second
element does not have this text so it is also a negative assertion that you can check or you can say the
17:08
17 minutes, 8 seconds
assertion to check if it does not have something so i can say check
17:16
17 minutes, 16 seconds
text and here i will give the same thing
17:23
17 minutes, 23 seconds
and i will say dot to have text and here you can use regular expressions as well if you want to give
17:31
17 minutes, 31 seconds
some partial text i can say the kitchen and then
17:39
17 minutes, 39 seconds
i can copy the same assession and paste it again
17:50
17 minutes, 50 seconds
and here just before to have i will say dot not so this will check it does not have this
17:57
17 minutes, 57 seconds
text i am pressing control plus b on my keyboard so that the sidebar is hidden and now we can see all this
18:07
18 minutes, 7 seconds
okay okay so next we can also check the
Chapter 13: Assert Element attribute
18:16
18 minutes, 16 seconds
value of the elements attribute so the elements may have multiple attributes like the type the class the id or any other
18:25
18 minutes, 25 seconds
attribute can be a custom attribute if you want to check you can use this to have attribute function and give the attribute name and
18:32
18 minutes, 32 seconds
the value and the value you can give the complete value or if you want to give a partial value or give some regular expressions you can also do that and if
18:40
18 minutes, 40 seconds
you want to select or if you want to check a particular attribute like class id we have separate
18:48
18 minutes, 48 seconds
functions for that as well like to have class so i can say here i will say
18:55
18 minutes, 55 seconds
check attribute value and here i'll just copy this
19:04
19 minutes, 4 seconds
and say dot to have attribute and here if i check this uh this element which says the kitchen here
19:13
19 minutes, 13 seconds
if i do a right click and say inspect and check what all properties it has so here you can see
19:22
19 minutes, 22 seconds
this has a class property and this is the name or the value of the class property so let me try this i will say
19:31
19 minutes, 31 seconds
class and then give the value which is this
19:39
19 minutes, 39 seconds
i'll copy this value and paste it here so this will check that this a particular element
19:46
19 minutes, 46 seconds
has a class property and it has this value now this will work fine because we have given the complete value but just in case you want to use a regular
19:54
19 minutes, 54 seconds
expression and let us say i just want to check that there can be anything before this and then i will check this so in that
20:02
20 minutes, 2 seconds
case i will remove these quotes and i will say
20:10
20 minutes, 10 seconds
i will give a forward slash and say dot star this means anything can be here and then i will end with a forward slash so this means they can be
20:19
20 minutes, 19 seconds
anything before this so if you have any dynamic value you can use regular expressions like this and then you can
20:25
20 minutes, 25 seconds
check this or i can also say i can say here
20:35
20 minutes, 35 seconds
await page dot locator and i will say to have you can see
20:42
20 minutes, 42 seconds
you can check css class count id etc so i can say to have class and then again i can
20:49
20 minutes, 49 seconds
give this regular expression or i can give the complete value here so let us try
20:57
20 minutes, 57 seconds
i will run it again i'll clear the terminal
21:05
21 minutes, 5 seconds
and run the command so let us see now so it opens the browser and now we have
21:14
21 minutes, 14 seconds
our playwright inspector window open now also you can see it is pausing here and if i press this resume button it
21:23
21 minutes, 23 seconds
will complete the test but if i want to pause at one more location i can add that pause statement once again here so
21:30
21 minutes, 30 seconds
i'll just copy this pause statement and we have already tested all these assertions so we don't want to test them again and i will just pause it
21:39
21 minutes, 39 seconds
here as well also let me just comment out the assertions which are failing so that we can save some time so to be
21:47
21 minutes, 47 seconds
hidden to be disabled all this will fail so i'll just save i'll comment this out
21:55
21 minutes, 55 seconds
and let us go back to our execution so i will go next next next
22:02
22 minutes, 2 seconds
and this will fail so from next time onwards these field sessions will not get executed and we will save some time
22:10
22 minutes, 10 seconds
and all this is running fine and now we have come to the uh attribute
22:18
22 minutes, 18 seconds
so let me check again this one has also failed okay yeah this one was also failed and
22:26
22 minutes, 26 seconds
we did not made it as a softer session that is why it has stopped the execution so let me run the execution
22:34
22 minutes, 34 seconds
once again so this time all these failed sessions should not get executed
22:42
22 minutes, 42 seconds
and also because i have already added pause i will click on this resume button and it will again
22:50
22 minutes, 50 seconds
execute everything and pause again here and now i will click on next and you can see it is running these two assertions and here we are using regular
22:58
22 minutes, 58 seconds
expressions so it is running fine and let us see the result and this time everything is pass
23:06
23 minutes, 6 seconds
so this is how we can use and check the attributes and use these assertions now we also have assessions for checking the
Chapter 14: Screenshot Moment
Chapter 15: Check Url of the page
23:15
23 minutes, 15 seconds
url of the page title of the page and also doing visual validation using the screenshot and software sessions we have already seen that
23:23
23 minutes, 23 seconds
if you do not want to stop the execution when an assertion fails you can make them as a soft assertion and for that
23:30
23 minutes, 30 seconds
you can just use the soft keyword after the expect keyword so this we have already seen let us see the url so you
23:38
23 minutes, 38 seconds
can say expect page to have url so i will say
23:48
23 minutes, 48 seconds
here check page url and title and here i will say await and i will put
23:57
23 minutes, 57 seconds
page in this bracket and then i will say dot i should first say expect
24:05
24 minutes, 5 seconds
and then i am saying page to have url so i will say dot to have url and
24:13
24 minutes, 13 seconds
i can check this complete url like this i can give the complete url like this or here as well i can use the uh regular
24:22
24 minutes, 22 seconds
expressions by giving these forward slashes and i can check a partial url as well and then we have the other
Chapter 16: Check Title of the page
24:30
24 minutes, 30 seconds
uh assertion for title here as well i can say the same thing await and expect
24:38
24 minutes, 38 seconds
page dot to have title and the title is
24:44
24 minutes, 44 seconds
so this is the url but if you see here on the top the kitchen is the title so i can say i can give the complete value within
24:53
24 minutes, 53 seconds
course or if i have to use this regular expressions i can say dot star and i will just say
25:00
25 minutes
kitchen and i will save and
25:08
25 minutes, 8 seconds
run the test again so let us see what happens this time
25:17
25 minutes, 17 seconds
so it has started and we have got the periodic inspector i will say resume to go to the next pause and all this is passing and here it is
25:26
25 minutes, 26 seconds
checking the url and here it is checking the title and all this has passed and you can see we have got everything as
25:35
25 minutes, 35 seconds
passing now i can say uh await expect page dot to have screenshot so this function will take a screenshot and will
Chapter 17: Check Page matches screenshot* Visual Validation
25:44
25 minutes, 44 seconds
compare so i will say this is visual validation with screenshot
25:51
25 minutes, 51 seconds
so i will say await and i will say expect and say page
25:58
25 minutes, 58 seconds
dot to have screenshot now see this time we do not already have a screenshot of the application or we do
26:07
26 minutes, 7 seconds
not have any screenshot against which we can compare our page so for the first time it will take a screenshot and from the next time onwards it will compare
26:16
26 minutes, 16 seconds
against that screenshot and you can also see there are so many options with this function to have screenshot we have
26:22
26 minutes, 22 seconds
animations enabled disabled allowed we have clips we have all these x y axis width height you can also give
26:30
26 minutes, 30 seconds
the resolution of the page all this we can do so for now let me just use this simple to have screenshot function and
26:38
26 minutes, 38 seconds
let me also put this pause i'll remove from here and i will put the pause here
26:48
26 minutes, 48 seconds
let me see i will
26:54
26 minutes, 54 seconds
put this here and remove from here so let us run this again
27:04
27 minutes, 4 seconds
i have saved my test and i am running the test again and it has come here
27:12
27 minutes, 12 seconds
i will click on resume so it will go to the next pause and now i will run this and let us see what
27:20
27 minutes, 20 seconds
happens so it has executed if i complete the test and check here so here
27:28
27 minutes, 28 seconds
you can see it says here it says this screenshot is missing
27:37
27 minutes, 37 seconds
so if you see here this screenshot it has taken the screenshot and it is saying is missing in snapshot so it is writing actual so
27:46
27 minutes, 46 seconds
now if you see your folder in the project so i'm pressing ctrl b to see the sidebar and the project tree so you will see here under test it has created
27:54
27 minutes, 54 seconds
this snapshot of the application and from for the next run it will actually
28:01
28 minutes, 1 second
compare against this snapshot so let us see i will run this again i will
28:09
28 minutes, 9 seconds
stop this process and you can also see in the report as well it will show this
28:16
28 minutes, 16 seconds
statement that this snapshot is missing and it is writing actual and now from
28:24
28 minutes, 24 seconds
the next step it will so you can see it has not failed it it is just saying that because it did not had a snapshot it has
28:31
28 minutes, 31 seconds
taken a snapshot now and from the next time onwards it will check against this snapshot so let us go back and run it again
28:42
28 minutes, 42 seconds
and let us see this time what happens so it opens the browser goes to the application and
28:50
28 minutes, 50 seconds
it has opened the payday inspector and i will resume so it goes to the next pause and here let us see now i have
28:58
28 minutes, 58 seconds
executed this and this time it should pass and you can see everything has passed it has checked the
29:06
29 minutes, 6 seconds
webpage against this screenshot and everything is passing so this is how you can use the screenshot and you can do visual
29:14
29 minutes, 14 seconds
validation with your application you can and this will check everything on the page the color the size of the objects pixels
29:22
29 minutes, 22 seconds
location everything so this will be a good visual validation and we have already seen how to use the soft accessions we just add this soft keyword
Chapter 18: Screenshot Moment | Outro
29:30
29 minutes, 30 seconds
after expect so i hope this was very useful for you if you have any questions you can let me know and i will see you in the next session thank you for
29:39
29 minutes, 39 seconds
watching and never stop learning
