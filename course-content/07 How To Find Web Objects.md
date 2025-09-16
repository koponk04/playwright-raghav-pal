# Chapter 1: Intro
0:00 hello and welcome i am raghav and today we are going to learn something very interesting and that is how can we find
0:08 objects on the web page how can we find elements on the web page using playwright and then we will do action on
0:15 those objects or elements now this is very important in automation whenever we have to use automation we first have to find these objects or elements this can
0:24 be anything like a text box a button a radio button a drop down box a title a image anything on the webpage that you
0:31 see is an element or an object and to do any action on on these objects or elements we first have to
0:39 find or locate these objects and for that we use selectors and locators and that is what we are going to learn today so today we are going to see what are
0:47 selectors and locators how to find these objects with playwright we will see different selectors like xpath css text
0:55 id how to use these and create locators and then we will also see how you can automatically generate these locators
1:03 using the playwright inspector so this is going to be very easy and very interesting and i will show you all the demos step by step from scratch so let's

# Chapter 2: What are Selectors and Locators
1:11 get started and let us first see what are selectors and locators and before we go into the definition and theoretical part let me go and show you some
1:19 practical i'm on this google home page so if you just go to google.com you will see this google home page now here
1:27 anything that you see like this search box this is an object or an element we call it object or elements in automation
1:34 and in general as well this is uh this button is an object this button is an object all these links are objects now
1:42 let us say i have to give something or i have to add something add a text here on this text

# Chapter 3: Google object locator example
1:51 box so first i have to find a locator or find a selector and create a locator for this box so what i'll do is i'll do a
2:00 right click and say inspect this will open the dom or the back end
2:07 of this page and you can see here it has opened this document object model of this page and here this area is
2:15 highlighted this corresponds to this search box now if you see here you will find there are
2:23 a lot of properties this is of type input it has a class property it has a name property name equals q type equals
2:32 text so it has lot of properties and using these properties we can create a locator for this object so i will go
2:40 here and i will press ctrl f or command f if you are on mac and you will get this
2:46 find box here i can create a selector or i can give a x path i can give a selector or create a xpath and i can try
2:54 to find this box this uh search box so here let us say i want to create a x path so i will
3:01 give forward slash forward slash and say input that means i am creating a relative xpath and i want to find
3:08 objects on this page that are of type input now if you see here as i say input you can see it says here one
3:18 of nine that means it has found nine objects on this page having the tag input or data for our of type input and
3:26 if you can see here if you will keep on if you click here it will show you all these objects some of these are hidden
3:34 and it will show all these objects and highlight them but we want this search box so i will go further and give
3:43 these brackets square brackets and i will say i want to find the input object that has the name property equals
3:51 q because we know there is a name property and its value is q for our search box and now you can see it is saying found one of one that is it has
4:00 found a unique object or a unique element using this x path and now you can see it is if i
4:07 see it is highlighting the search box and it is also highlighting the area of the search box on this dom so this is how we
4:15 use automation to find to create locators and find objects now today we have so many tools so many
4:23 automated tools and applications that can create these expats for us and in playwright as well we have options but before we go to the automated options
4:32 let me show you some of the ways so selectors in very basic words simple words
4:39 selectors are strings or properties of these web objects and using these selectors we can create locators so for
4:47 example the id the css property all these are selectors and using these we can create locators to
4:55 find these objects and all these css class name id text xpath all these are selectors and using this we can create
5:02 locators now locators in playwright if i talk about playwright locator is a class and here the syntax
5:11 is we say page dot locator and give any of these selectors and create a complete string do not worry i will show you uh in a
5:19 demo how exactly we use this so just for information locator is a class in playwright library now let us see how

# Chapter 4: How to find web objects with Playwright
5:26 can we create locators how can we find objects with playwright so i will go to my project the playwright project here
5:34 and here i will say uh i will go to the tests and i'll create a new file first
5:43 and i will call this as selectors you can just select us demo i'll just say selectors.spec
5:51 dot js and at the top i will import test and expect
6:00 from playwright and we have already seen this we know how to create a test so i'll create a
6:08 test first here i will say test and give the title i'll say selectors demo
6:16 and then create a async function and
6:25 then i will pass the page fixture in this function so within curly brackets i will say page
6:32 and that's it and now uh let me see what is the issue here
6:41 okay it should be async a typo all right so i have created our test block and now we can write our code here
6:50 so what i'm going to do here is let me show you the application i'm going to use i will go to this source demo.com and
6:57 here we have a login page where we have a username we have a password and then we have a login button so here
7:04 i will try to find out uh the properties and create locators for all these objects and then we will see how we can
7:12 do actions on these objects so the first thing is i have to go to this application so i will say
7:20 page dot go to and i will give the url of the application
7:29 and i will add this keyword await we have already learned about async
7:36 await in the earlier sessions when we learned how to create test cases so now after this uh let me just run this and
7:45 check if it is running fine so i will open the terminal you can open terminal from here or just press ctrl j on your
7:52 keyboard it will open the terminal here so we have got our terminal here and here i will say
8:02 npx playwright test
8:10 and then i want to run a specific test file so i will say
8:18 tests and selectors.spec
8:26 i'm pressing tab here to autocomplete and uh let us say i just want to run on a single browser so that it is we don't
8:33 waste time in running on multiple browsers so i will say hyphen hyphen project chromium it will only run on chrome browser and also i want to see the
8:41 execution so i will say hyphen hyphen headed and that's it uh if i press ctrl b it will
8:49 hide the explorer so this is the command and now i will run this and check
8:58 so this should run this test on a chrome browser in a headed mode and it was very fast
9:05 so that is fine now what i can do is i can say await
9:14 page dot pause now when i use pause here it will stop it will pause there and it will open the
9:22 playwright inspector window and with that we can do step by step execution we can also see all our steps we can see
9:28 the application so that will be very handy here so let me just run it again and check so i am running the same command i press
9:37 the up arrow on my keyboard to bring up the earlier command on the terminal and now i am running and you can now see it has
9:44 opened the application and open the browser and the application because we are using edit mode and now it has
9:51 gone to the playwright inspector it has opened the playwright inspector window here and here we can see our test and i can use this
10:00 step over to go to the next step or just click on this resume to resume to a resume button to uh resume to the
10:08 next steps and actually complete the entire test so for now this is the this is working fine i just wanted to check everything is working
10:16 fine so i'll just click this one and end the test now let us see the locators and selectors
10:24 so the first one is we can use any property of the object that is available that is present in the

# Chapter 5: using any object property
10:32 dom and then we can say page dot whatever action we want and give that property for example
10:40 let us say i want to click on this username box here so i will do a right click here and say inspect
10:48 and let me see the properties available here so you can see here we have all this we have class property we have text
10:56 property and then a data test property and the id property so let us say i want to use this id so i will copy this id
11:04 id equals user hyphen name and then i will say await page dot
11:13 click and then in the brackets within quotes i will give this id equals user hyphen
11:22 name and i can if i want i can remove this double quotes and just say id equals
11:31 user hyphen name that is the value of id and all this within single quotes let me also add this comment
11:40 using any object property okay
11:48 let us see now i will run the test again and we will see in the playwright inspector
11:57 so it opens the browser and the application and here is our playwright inspector so i will go to the next step
12:05 and you can see as i am going to the next step it is highlighting the step that will get executed when i again press this step over button and before
12:14 even executing the step it has found that this is the object that is id equals user hyphen
12:22 name which corresponds to this object this element and we have to click here so i will again say step over and you can
12:31 see it has clicked here and i will stop this so this is working fine now
12:38 generally in playwright we use the locator class so we say
12:45 await page dot locator and you can see here is a option locator in case you do not get this auto
12:53 suggestion box you can press control plus space on your keyboard and then here again i can say
13:02 i can give this id and then say dot click so i can i can give the same property that is id of the
13:10 object and say dot click
13:16 or here i can also say dot because i want to add something here so i will say dot fill and
13:25 i will add something here let us say edison and save and i will run again let us see now
13:34 so this opens the browser opens the application goes to the url and here we have got the playwright inspector
13:43 and it has paused here i will go next next and here again you can see this is the
13:50 step it will execute next and if i run it it has added edition on the username box so this is
13:58 working fine and this is how we can use any property so whatever property you find available for the object for example
14:06 even if i say data test equals username this will also work id equals username will work name equals username whatever is available
14:14 for the property for the object it will work here so this can be a direct way you can see whatever is a stable property and can directly use it in
14:22 playwright using directly like this or the preferred way is using the locator like this all right
14:31 so you can also directly say like this you can give this all this in square brackets or can directly say like this
14:40 okay so let me also show you if i say i'll let me copy this
14:48 and i'm just going to copy this complete thing and if you do that you should put a
14:56 square bracket like this and then just copy this entire thing
15:03 like this and here i will say
15:10 einstein and let us run and check again so this opens the browser goes to the
15:21 url and here is our playwright inspector it has paused and opened the playwright inspector so i will go next next and
15:30 here it has added edition and next it has added einstein here so this is working fine
15:38 i'll clear this terminal all right so this is how we can use any property we can use all this and we can
15:46 uh do actions on the object now we can also use css selector so let's say

# Chapter 6: using CSS selector
15:55 the next thing is using css selector
16:03 so here i will try to get the css selector of this login button and try to click on
16:11 this login button so i will do a right click and first say inspect it will go to the backend and open the dom
16:19 and it has highlighted this area this area which is for this login button and now
16:27 if i do a right click here let me again say inspect and now on this highlighted section that is for
16:35 login button i will do a right click and say copy and say copy selector this will copy the css selector
16:42 and if i just paste it here so here this is the css selector of this
16:50 login button and here i can say await page dot locator
16:58 and i can directly give the css selector within course here
17:04 and then i will do the action dot click so you can see here this is how i can
17:12 use the css selector and i will save and run the test again
17:23 so here it opens the browser goes to the application and here is our playwright inspector
17:32 and i will say next next and next
17:39 now you can also see one more thing here in the playwright inspector that even before doing the action it is
17:48 highlighting the object because it has resolved this selector this locator and this is working fine and before even
17:57 running that step it runs some inbuilt assertions and this is all the playwright features it runs inbuilt assertions and checks that the object is
18:06 there it is visible it is clickable if it is a click action and you can also check here if you see this explore section it has highlighted the selector
18:14 we are using also if you scroll down and see these logs so this is the action locator dot click
18:23 this button and even before running this action even before doing the action it has executed all these things it has
18:30 waited for the selector then it has resolved and it is it has checked that this is visible and
18:38 it will attempt a click action and waiting for the element to be visible enabled and stable before doing the click action and then it has checked
18:47 element is visible enabled and stable then scrolling into view if needed and then done scrolling so now our action is
18:54 ready to be done and this is what playwright does at the back end uh normally when we run our test we cannot see all this happening but in this
19:02 playwright inspector we can see all these things which are happening at the back end that playwright is making sure that the object is there if you are
19:09 doing a click action it is clickable it is visible it has crawled to the position all that it has resolved so now i will go next
19:18 and it will click on the button and of course because we have not given the password it is saying that password is required so this is working fine
19:26 and one more thing with playwright inspector is uh if you click on this explore button this explores here
19:34 you can now highlight go to your page and scroll and go anywhere take your cursor or pointer
19:41 anywhere it will highlight the objects and also show you the locators the best possible locators and
19:49 if i let's say i go to this login button and if i click and if i again go and check the playwright inspector window you can see
19:58 it has given this locator this is the best possible locator it has found so if you want to automatically get the locators you can
20:06 use playwright inspector like this so with that this is working fine i will run the entire test and it will stop
20:15 let me clear the terminal and next we can also use xpath in the initial example of google homepage i

# Chapter 7: using XPath
20:23 created a xpath and the same way we can create xpath here as well so for example again if i uh say
20:31 i'll say this is using xpath and here
20:39 let us say i want to type some something here on the password box
20:47 i will inspect and it is of type input
20:54 and it has class and it has a type it has name so let me say i will say i am pressing
21:04 ctrl f on my keyboard or command f on mac and then i have got this
21:11 here i will say find the element of type input where name property equals
21:21 password and yes it is able to find a unique match and this is what i will use so i can say here await
21:31 page dot locator now for xpath i can use it two ways
21:38 i can use this x python two ways i can either just say x path equals to the
21:44 x path i can say x path equals to this is what i'm using and then i will do the action i will say dot fill
21:53 and whatever i want let us say faraday
22:01 or i can also use it in a way await
22:08 page dot locator and i can directly give the x path i can just give the x path within the
22:17 codes so this is also another way i can use the x path and then i can again say dot fill
22:29 i will say ramanujan and let us save and run and check again
22:36 i believe if we are doing pause it will anyways open the playlight inspector so let me try it without headed
22:44 uh option let me see so whenever we debug or whenever we record or whenever we pause
22:52 we get to see the playwright inspector so no it did not open the playwright inspector here because we were not in
23:01 the headed mode so i'll have to add the headed option let me add it and run again
23:09 let us see now okay we have got our playright inspector
23:17 and this is all working fine and yes you can see using xpath it is
23:25 adding this password of course we cannot uh see the password but it is adding all this so this is all working fine
23:34 let me put this in the username let me see what is the properties for username so i'll create a xpath for username and
23:43 here we have id user hyphen name we have name also let me use this here i will say instead of password i will say id
23:52 user hyphen name so that we can see this text on the screen here also i will say id instead of name and say user hyphen
24:00 name so this time we should see this faraday and ramanujan added on the screen also this pause i will remove
24:07 from here because i don't want to see all this i will just add the pause here
24:15 just before using the xpath selectors and locators so i will again run
24:24 and let us see now so it opens the browser goes to the application and yes it has con
24:32 already executed all these steps and now it has paused here so now i will go to the next step and you can see it has uh
24:41 added this it has added faraday here and then next i will go next again and it has added
24:49 ramanujan here so this is all working fine and this is how we can use expats as well now you can also use the

# Chapter 8: using Text
24:56 text property of the objects so here i can say page dot locator and i can give the text whatever text is visible and
25:04 then i can do the actions so for example i will say here using
25:12 text so i will say await page dot locator and i will say here
25:21 text equals so here you can see the text for this login button here this is login
25:29 i will say text equals login and i will say dot
25:36 click now you can use text like this text equals login or we can also say hash
25:44 text so let me first run this and show you i will clear
25:52 and run the test so this opens the browser and
25:59 opens the playwright inspector window and here all this is fine and
26:07 you can see here next it has already found that this button is already present this object is present and clickable and then it has
26:16 done the click action so you can do like this or i can also say sometimes uh you have the text but it
26:24 can be a very complex text or dynamic in that case we can say has text i can say page dot
26:32 locator and then i will say has
26:40 text and i can use this column here like this so i will say has text and then i will give the text
26:48 here in brackets so i will say login
26:57 and then i will do the click action here so
27:05 let's run and check i will save the file and run it again
27:15 and let us see this is our playwright inspector
27:23 so here this is the step using text and this is working fine now here is the step
27:31 which is using hash text login and if you see here in the logs in the details here it is not able to
27:40 find or if i just go next it is not able to find it it is still
27:48 retrying it is detangled because in the conflict file we have uh retry equals one this is
27:55 what we did in the last session so let me just stop this and it has also shown us that this has
28:04 failed and let us see the reason i will go back
28:14 i will stop this i will press ctrl c and terminate clear
28:26 let us have one more step after this so i will again run this and check what exactly has happened here
28:35 so we have set here has text login

# Chapter 9: Screenshot moment
28:42 so i will again run it next step next step and this is where it fails
28:53 okay there is some unexpected text it is saying unexpected token i think
29:00 we have here we have said has text
29:09 this looks fine we have set hex text equals login here
29:18 okay we have not given the close double quotes and i will show you what
29:24 happens if we do not say input here if we just say hash text login so it will search for everything that has login
29:32 on the page so let us run this again and check make sure that you save the file the
29:41 test file and i will run it again and let us see now so we have got our playwright inspector
29:50 and yes so now you can see on coming to this step even before
29:57 executing it is saying here if you go to this section it is saying
30:07 so you can see has text login has resolved to 10 elements because it has found 10 elements on this page which have this
30:15 text login and it has also listed out all these 10 elements so therefore we cannot work on this object
30:23 it should always find a unique match and therefore we can also add the type of the object that we are trying to find which
30:31 has this text login so therefore i can say here i will say input has text
30:38 so i will say here find a type of object that that is input
30:45 which has this text login so this is what i will try now i will save and let me
30:52 stop this and i will clear and run the test again
31:07 and let us see this time and
31:15 we will go to the next step and yes so you can see now it is able to
31:24 resolve it and it is waiting for the element to be visible enable stable and it is it has checked everything and now
31:32 we can do action on this element and now it is all fine so this is how you can use the text property
31:40 now we have seen how to find web objects and these are some very basic locators uh you can uh we have already seen how you

# Chapter 10: How to find and record object locators using Playwright Inspector
31:48 can use playwright inspector to automatically create the locators so as i have shown you whenever you open playwright inspector now you can open
31:56 playwright inspector by adding this page dot pause so wherever you will have this pause and you run in a edit mode it
32:03 will pause here open the playwright window and from there you can do step by step execution using playwright inspector window or if you
32:11 run your test in a debug mode by using hyphen hyphen debug so if i say if i say here hyphen hyphen debug in
32:20 that case you will also not need to add this headed option the debug mode by default will open in a headed mode this will also open the
32:28 playwright inspector or if you are recording your test using the code gen tool that we have learnt how to in the session how to record your test even
32:37 then the playwright window will get opened so there are three ways you can open the playwright window when you are recording the test using code gen when you are debugging using hyphen hyphen
32:45 debug option in your command or whenever you add the page dot pause option page dot pause uh command in your test so we
32:53 have already added this so let me add this let me cut it from here and i will add
33:01 it just after going to the application i will say
33:09 page dot pause and
33:16 if i run the test now so
33:25 it will open the playwright inspector window okay i think uh it should i should have used
33:32 a weight here and now i will run it again
33:40 so this should open the application as we have we are doing in a headed mode and also open the play that inspector and the playback inspector
33:49 here it shows it has paused here and now i can do step by step execution now here you will whenever you open the playwright window you will see this
33:57 explore if you click here it will highlight and now you can find locators for the objects you can take your pointer to anywhere and you
34:05 will see it is showing you the locators the best possible locators and you can click and it will copy the locator here
34:14 in this explore section here in this field and from here you can just copy it and then use it in
34:22 your scripts and anyways when you record using code gen utility all the object locators will also get recorded if i show you the script that we created
34:30 using a recording option using code gen i am pressing ctrl b on my keyboard to show this
34:37 explorer window and now if i go to the this test that we created using recording using code gen you can see you will
34:45 always get this locators created by default so this is how you can also create the playwright locators by
34:52 recording now what we have seen here in this session are very basic locators and this is what you will be using most of the times but just in case you have a
35:01 very complex application or complex objects you don't have very straight away uh properties or locators or selectors
35:09 available then you can do a combination of multiple locators or selectors you can add css value along
35:16 with text value or you can say hash text you can also use the the position the relative position the location of the
35:24 objects based on that also you can find the object so there are so many other options you can use and for that you can go to the selectors page or the locator
35:32 class of playwright so let me show you if you go and check playwright selectors
35:40 and it will take you to the documentation selectors of playwright and here you can see
35:50 so you can see all these options there are so many things you can use with selectors you can do a combination you can
35:58 find based on the location or position of the element you can combine multiple selectors you can do union you can also
36:06 find shadow dom objects and this is how you can you know find these shadow dom elements on the web page
36:13 and you can see the text you can also find by position so all this you can check here and the other page that i
36:20 will refer to you is the locators class of playwright
36:28 and here it is i will have all these links everything in the description of this video so you can check so this is the locator class
36:35 and you can see all the functions all the options which are there in this class so you can always check this if
36:42 you have some complex objects and you want to see what's the best possible options you can do for finding that objects so i hope this was very useful

# Chapter 11: Outro
36:51 if you have any questions you can let me know i will see you in the next session of playwright thank you for watching and
36:58 never stop learning