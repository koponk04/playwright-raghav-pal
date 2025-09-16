# Chapter 1: Intro
0:00 hello and welcome i'm raghav and today we are going to learn something very easy and very interesting and that is
0:08 assertions in playwright so in this session we will see what are assertions we will see what are the assessions in playwright and then we will see how to
0:16 add assertions in our test in playwright so this is going to be very interesting let's get started with what are

# Chapter 2: What are Assertions
0:23 assertions now in very very simple words assertions are like checks or verifications that we do in our test for
0:31 example if i want to check if an element is present or not present if a text is present or not present or if the element has some particular value or not all
0:39 these will be assertions so we actually check uh these things and whenever we add a session it checks
0:47 whatever we have given in the session is it equal to the actual and if actual and expected are equal it will pass
0:54 otherwise it will fail the test so in assertions uh in playwright we use the expect keyword this comes from the jest

# Chapter 3: Assertions in Playwright
1:02 testing test runner and this is what we use and it comes inbuilt in the playwright library so we can directly say expect and then we can write our
1:11 assertions in a moment i will show you how to add a sessions so in this session we are going to see how to check if an element is present or not present

# Chapter 4: How to add Assertions
1:19 visible or hidden whether an element is enabled or disabled whether the text matches some particular value or does
1:26 not match a particular value we can check the element attribute as well like the class id or any attribute that you want to check we can check the page url
1:35 we can check the page title and then we will also see how we can
1:42 match or how we can assert our web page against a screenshot and in this case we are doing visual validation
1:50 and it means that we are going to check how does the page looks in terms of the colors the location of the objects the size of the objects the the font the
1:59 pixel and anything that you want to check based on the visual validation or the appearance of the web page we can do
2:06 that as well and then i will talk about soft assertions what are softer sessions so generally when we add these assertions whenever
2:15 there is a failure whenever an assertion fails it will stop the execution and come out of the execution but in case we want that our
2:23 execution the test execution should not stop if a session fails we can use soft assertions so we will look at that so
2:30 first let's start with uh present not present and i will go to my vs code and here is the project

# Chapter 5: Create a new Test
2:39 and i will go to my test folder and i am going to create a new file so i will say this is
2:47 assertions dot spec dot js so i have created this file
2:55 assertions.spec.js and here at the top i will say import i want to import page and expect
3:04 libraries or scripts from the playwright test library
3:12 and after this i can start writing my test so i will say test and i will first give the title i will say
3:20 assertions demo and then i will create a
3:26 async function so let me add this async function here
3:36 and i will give this arrow symbol and curly bracket start and stop and in this function i am going to pass a page
3:43 fixture so this is how we declare our test and then i will just say await
3:51 page dot go to to visit our web page i will say page dot go to all this we have already learned and here i will give the url of the
4:00 application now for this demo uh let us go to uh this

# Chapter 6: Demo App
4:08 demo application kitchen.applytools.com and here you can see here we have this web page we have all these buttons
4:17 here so we will use this and in case at your time this application is not up or not available you can use any other
4:24 application or you can use your own application as well so i will just go to this link i will have all these links all the
4:32 notes in the description of this video so you can always check from there i will also add the code there and now
4:39 i'm going to say await page dot pause now i'm adding this pause statement here
4:47 so that as soon as it comes to the power statement it will pause the execution and open the playwright inspector window
4:54 so we can then uh run our execution step by step and we can also see the execution the statements where exactly
5:01 it has gone and we can see everything on the screen so now i will try to run this and
5:08 here i will first open a terminal window so i can go from here and say new terminal or press control plus j key on your keyboard to bring up the terminal

# Chapter 7: Command to Run the test
5:17 window and here i will now say npx
5:25 playwright test and i want to run a specific file so i will say tests i am pressing tab so
5:33 it will auto complete and assertion i am again pressing tab on my keyboard it will auto complete now it will run on all the
5:41 browsers which are configured in the config file but i just want to run on one browser so that we can save some time so i will
5:49 say hyphen hyphen project chromium so it will only run on chrome browser and also i want to see the execution so i will say hyphen hyphen headed so it will run
5:58 in a headed mode and it will bring up the physical browser on the screen so i have started the execution and you can see it has gone to the chrome browser
6:06 and gone to the application and now here it has as soon as it encountered the pause statement it has opened the playwright
6:14 inspector and now i can do step by step execution by using this button so before going here
6:22 we want to check all these assertions first element present not present visible or
6:29 hidden enabled or disabled text matches value or not and the element attribute so here

# Chapter 8: Check element Present/Not present
6:38 let us say i first want to get some element so i will click on this explore button on the playwright
6:45 inspector and now i will go to the web page and wherever i am taking my pointer it is highlighting let me just go to this the kitchen
6:54 element and if i again check my playwright inspector this is the selector
7:01 i can create a locator using this so i will just go to my project and in the test i will say
7:11 await page dot locator and i will use this locator
7:18 and now i can do my assertions so let me also add the comments so it will be easier for you
7:25 i will say assertions and the first session we are going to check is uh check if the element is present
7:34 so check i will say check element
7:41 present or not okay now here we can say expect and we can give the locator and
7:48 then say to have count or we can also give the element handle let me show you so here i will say
7:56 await and i will say expect and this page dot locator i will put in this
8:04 brackets like this and then i will say to have count and i will say count one so this
8:12 means we are checking or we are asserting that there should be a unique element a single element with this
8:19 locator so we can run this i will save and on the terminal i will press ctrl c
8:26 to stop this process and clear the terminal and i am pressing the up arrow on my keyboard to go to the last command
8:34 and i will now run this again so let us see this time it should run this assertion as well
8:42 so it has come here it has paused i will go next and you can see this is the it has also highlighted this element and if
8:50 there is a single instance of this element present on this page or with this locator it should pass and
8:57 if i now resume you can see it has passed so this is working fine now
9:03 i can also say here i can say page dot dollar this is an element handle i can say await
9:12 page dot dollar and you can see here you can see the use of element handle is discouraged so when
9:20 you want to check whether it is present or not you should always use the expect keyword and add the assertions but i will show you where exactly it will be
9:29 helpful so i can just give the locator of the element which is this
9:37 and now if i run this this will pass but if i have to add a condition that if this element is present then i want to
9:44 do something based on that condition so if i create a if loop or the if condition sorry this is the condition if condition and in the
9:53 bracket i will just pass this and then i will say inside the if block i will
10:02 say i'll just use this i will say
10:10 await and page dot locator and this locator and i will say dot click so i'm just saying that if
10:18 this is present if this element is present then i should go inside this if block
10:25 and click on the element now let me save and run it again so i am running the command again and
10:35 let us see the execution this time so if you want you can do hands-on along with me and if you face any issues you
10:43 can let me know i will click on next next and you can see it has now come to this if block and this condition
10:51 was true and therefore it has come inside the block and now it should click on the element and it has clicked and now i will resume the execution and
10:59 everything has passed so it can be helpful this way of using the element handle can be helpful if you want to add
11:07 this in a condition that whether this element is present or not based on that condition you want to do some action now if you try to add this in a condition it
11:15 will not work so if you want you can try to add this in the if block in the condition of the if block here and you can try this will not work because it is
11:24 not returning true or false but this statement is returning true or false so therefore this will work now you can also check whether an

# Chapter 9: Check element Visible/Hidden
11:32 element is hidden or not so i can use the same statement and i can say so i will say
11:41 check element hidden or visible
11:50 and here i can use the same statement expect and the locator and then i can say to be visible
11:59 or i can say dot to be hidden
12:06 and this will check whether the element is hidden or visible now i am not re-executing it now i will execute after
12:13 adding some more assertions so we can save some time in the same way we can check enabled or disabled so i will say

# Chapter 10: Check element Enabled/Disabled
12:22 check element enabled or disabled and i will say
12:30 to be enabled and you can see as i'm typing to be we are getting so many options to be
12:38 checked to be close to be disabled to be editable to be empty to be focused so you can try all these successions and
12:45 you can use them so i will say to be i will say to be enabled
12:55 and then i will say dot to be disabled
13:04 so this will checked enabled or disabled okay now let me save
13:12 and run it once so i will clear the terminal and run the command again and let us see what
13:20 happens this time so here some assertions will fail let us see what happens when we have failed accessions so
13:28 we have got the update inspector i will go next next next and all this is passing and now we
13:35 have come to this assession that is this element should be hidden but this should fail so if i go next you can see it will
13:44 check and it will go until the timeout that we have in our configuration file and then it has
13:51 failed it and therefore you can see it is shown here as a failure i will again go next and you can see it stopped the
13:58 execution as it encountered the failure and it will also open the report
14:06 so let me just resume it and if i want to check the report
14:14 it is opening the report and here you can see it says that this was failed this was the issue
14:23 this is failed here to be hidden has failed and then if you check after this step it has stopped but if
14:31 you want that this should continue even after this step then we can make it as a soft assertion now also you can see it has after failing it has retried for one
14:40 more time therefore we are getting this retry result as well but we just want this to run once so for that
14:49 i will go to my configuration file and here you can see the timeout we have already
14:57 decreased the timeout in the earlier session so it is waiting just for three seconds let me make it even
15:03 less two seconds so that we don't waste time in demo and here is the retries i will comment this out
15:12 so it was uncommented i am pressing control and forward slash on my keyboard to comment this and i will save so this will now not retry after failure and
15:21 then coming here back to the assertions now in case you want that in case a session fails it should not stop the

# Chapter 11: How to add Soft Assertions
15:28 execution in that case you can make it as a soft session and to make it as a softer session after this expect i will
15:36 just say dot soft so this will make it a softer session this also i will make a soft accession
15:43 so that it should not stop the execution let us try i will press ctrl c on the terminal to stop this process and
15:52 run my command again and this time it should not stop the execution when these accessions fails that we have
16:00 made as software sessions so it has come here i will go next next next next and now this should fail and
16:09 let us see what happens so you can see it failed but it still went to the next step so i will say next
16:17 this one has passed and again this one should fail and it has failed and i will resume
16:24 and now if i see the report you can see here the first thing is it has not retried
16:32 now if i check the execution you can see here it has executed all the steps so this one was failed it went ahead this
16:39 one was passed and then this one was again failed so we have got our complete test execution and we can see what all has failed
16:47 so this was how you can check enabled or disabled if you want to check whether the element has some text you can say

# Chapter 12: Check element Text matches value or not
16:54 dot to have text and give the value or you can say not to have text and this will check that
17:01 element does not have this text so it is also a negative assertion that you can check or you can say the
17:08 assertion to check if it does not have something so i can say check
17:16 text and here i will give the same thing
17:23 and i will say dot to have text and here you can use regular expressions as well if you want to give
17:31 some partial text i can say the kitchen and then
17:39 i can copy the same assession and paste it again
17:50 and here just before to have i will say dot not so this will check it does not have this
17:57 text i am pressing control plus b on my keyboard so that the sidebar is hidden and now we can see all this
18:07 okay okay so next we can also check the

# Chapter 13: Assert Element attribute
18:16 value of the elements attribute so the elements may have multiple attributes like the type the class the id or any other
18:25 attribute can be a custom attribute if you want to check you can use this to have attribute function and give the attribute name and
18:32 the value and the value you can give the complete value or if you want to give a partial value or give some regular expressions you can also do that and if
18:40 you want to select or if you want to check a particular attribute like class id we have separate
18:48 functions for that as well like to have class so i can say here i will say
18:55 check attribute value and here i'll just copy this
19:04 and say dot to have attribute and here if i check this uh this element which says the kitchen here
19:13 if i do a right click and say inspect and check what all properties it has so here you can see
19:22 this has a class property and this is the name or the value of the class property so let me try this i will say
19:31 class and then give the value which is this
19:39 i'll copy this value and paste it here so this will check that this a particular element
19:46 has a class property and it has this value now this will work fine because we have given the complete value but just in case you want to use a regular
19:54 expression and let us say i just want to check that there can be anything before this and then i will check this so in that
20:02 case i will remove these quotes and i will say
20:10 i will give a forward slash and say dot star this means anything can be here and then i will end with a forward slash so this means they can be
20:19 anything before this so if you have any dynamic value you can use regular expressions like this and then you can
20:25 check this or i can also say i can say here
20:35 await page dot locator and i will say to have you can see
20:42 you can check css class count id etc so i can say to have class and then again i can
20:49 give this regular expression or i can give the complete value here so let us try
20:57 i will run it again i'll clear the terminal
21:05 and run the command so let us see now so it opens the browser and now we have
21:14 our playwright inspector window open now also you can see it is pausing here and if i press this resume button it
21:23 will complete the test but if i want to pause at one more location i can add that pause statement once again here so
21:30 i'll just copy this pause statement and we have already tested all these assertions so we don't want to test them again and i will just pause it
21:39 here as well also let me just comment out the assertions which are failing so that we can save some time so to be
21:47 hidden to be disabled all this will fail so i'll just save i'll comment this out
21:55 and let us go back to our execution so i will go next next next
22:02 and this will fail so from next time onwards these field sessions will not get executed and we will save some time
22:10 and all this is running fine and now we have come to the uh attribute
22:18 so let me check again this one has also failed okay yeah this one was also failed and
22:26 we did not made it as a softer session that is why it has stopped the execution so let me run the execution
22:34 once again so this time all these failed sessions should not get executed
22:42 and also because i have already added pause i will click on this resume button and it will again
22:50 execute everything and pause again here and now i will click on next and you can see it is running these two assertions and here we are using regular
22:58 expressions so it is running fine and let us see the result and this time everything is pass
23:06 so this is how we can use and check the attributes and use these assertions now we also have assessions for checking the

# Chapter 14: Screenshot Moment

# Chapter 15: Check Url of the page
23:15 url of the page title of the page and also doing visual validation using the screenshot and software sessions we have already seen that
23:23 if you do not want to stop the execution when an assertion fails you can make them as a soft assertion and for that
23:30 you can just use the soft keyword after the expect keyword so this we have already seen let us see the url so you
23:38 can say expect page to have url so i will say
23:48 here check page url and title and here i will say await and i will put
23:57 page in this bracket and then i will say dot i should first say expect
24:05 and then i am saying page to have url so i will say dot to have url and
24:13 i can check this complete url like this i can give the complete url like this or here as well i can use the uh regular
24:22 expressions by giving these forward slashes and i can check a partial url as well and then we have the other

# Chapter 16: Check Title of the page
24:30 uh assertion for title here as well i can say the same thing await and expect
24:38 page dot to have title and the title is
24:44 so this is the url but if you see here on the top the kitchen is the title so i can say i can give the complete value within
24:53 course or if i have to use this regular expressions i can say dot star and i will just say
25:00 kitchen and i will save and
25:08 run the test again so let us see what happens this time
25:17 so it has started and we have got the periodic inspector i will say resume to go to the next pause and all this is passing and here it is
25:26 checking the url and here it is checking the title and all this has passed and you can see we have got everything as
25:35 passing now i can say uh await expect page dot to have screenshot so this function will take a screenshot and will

# Chapter 17: Check Page matches screenshot* Visual Validation
25:44 compare so i will say this is visual validation with screenshot
25:51 so i will say await and i will say expect and say page
25:58 dot to have screenshot now see this time we do not already have a screenshot of the application or we do
26:07 not have any screenshot against which we can compare our page so for the first time it will take a screenshot and from the next time onwards it will compare
26:16 against that screenshot and you can also see there are so many options with this function to have screenshot we have
26:22 animations enabled disabled allowed we have clips we have all these x y axis width height you can also give
26:30 the resolution of the page all this we can do so for now let me just use this simple to have screenshot function and
26:38 let me also put this pause i'll remove from here and i will put the pause here
26:48 let me see i will
26:54 put this here and remove from here so let us run this again
27:04 i have saved my test and i am running the test again and it has come here
27:12 i will click on resume so it will go to the next pause and now i will run this and let us see what
27:20 happens so it has executed if i complete the test and check here so here
27:28 you can see it says here it says this screenshot is missing
27:37 so if you see here this screenshot it has taken the screenshot and it is saying is missing in snapshot so it is writing actual so
27:46 now if you see your folder in the project so i'm pressing ctrl b to see the sidebar and the project tree so you will see here under test it has created
27:54 this snapshot of the application and from for the next run it will actually
28:01 compare against this snapshot so let us see i will run this again i will
28:09 stop this process and you can also see in the report as well it will show this
28:16 statement that this snapshot is missing and it is writing actual and now from
28:24 the next step it will so you can see it has not failed it it is just saying that because it did not had a snapshot it has
28:31 taken a snapshot now and from the next time onwards it will check against this snapshot so let us go back and run it again
28:42 and let us see this time what happens so it opens the browser goes to the application and
28:50 it has opened the payday inspector and i will resume so it goes to the next pause and here let us see now i have
28:58 executed this and this time it should pass and you can see everything has passed it has checked the
29:06 webpage against this screenshot and everything is passing so this is how you can use the screenshot and you can do visual
29:14 validation with your application you can and this will check everything on the page the color the size of the objects pixels
29:22 location everything so this will be a good visual validation and we have already seen how to use the soft accessions we just add this soft keyword

# Chapter 18: Screenshot Moment | Outro
29:30 after expect so i hope this was very useful for you if you have any questions you can let me know and i will see you in the next session thank you for
29:39 watching and never stop learning