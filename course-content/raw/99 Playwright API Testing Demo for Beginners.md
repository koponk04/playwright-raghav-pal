0:00
hello and welcome I am raghav and today we are going to learn step by step from
0:06
scratch how to do API testing with playwright this is going to be very easy and very interesting we will start with
0:12
the project setup how do we set up the API testing project we will learn how to
0:17
create a API test step by step we will create a get API request a post EPA
0:24
request put and delete API request and then we will see how do we validate the
0:30
API response how do we add the assertions and then we will see how we can use the playwright UI mode and we
0:37
can check our responses logs error console output and everything and then we will see how do we see the HTML
0:45
report for our tests this is going to be very easy and very interesting so let's get started and you will also find all
0:52
the nodes all the links in the description of this video so first let us start with project setup
0:59
now if you are already working with a playwright project you can use the existing project or if you want to do a
1:07
new project setup you can follow me so in case you want to continue with your existing project you can skip the
1:13
project setup and continue from the next slide however I will show you all the steps from scratch so step number one is
1:20
we will create a new folder for our API testing project so I will
1:27
go here you can keep the folder at any location on your system I keep all my
1:33
project folder under this projects folder and then playwrite so here I will
1:40
create a new folder and I will call this as
1:48
playwright API
1:53
testing okay so I have created this folder playwright API testing and now
2:02
next step is you have to open this folder in your IDE so you can use any ID that you are using or you can use vs
2:10
code that I am going to use so I will first open my vs code
2:18
and here I'm going to open the folder so you can open it from here we have open folder
2:24
you can also go to file and we have options for open folder here or you can
2:29
just drag and drop the folder onto vs code so I'm going to drag and drop this folder
2:36
here and here I will say yes trust the authors
2:44
and you can see we have got our
2:50
playwright EPA testing folder added on vs code
2:58
okay next step is we will open the terminal or the command line on the folder
3:04
location and then we will run the command npm init playwright at the rate latest so this will set up a node
3:12
project and will also add playwright in the project and we'll do the all the project setup so here
3:20
you can open a command line and then first go to the location of the folder
3:26
that is playwrite API test or whatever folder you have created or you can use the integrated terminal in vs code so
3:34
here if you see if you go to the top we have this terminal here and we can open a new terminal or you can press the Ctrl
3:41
shift and back take key back the key is the top left key on your keyboard just below the Escape key or you can also
3:49
press Ctrl plus back the key and this will open the terminal you can see it has opened the terminal and it has
3:56
opened the terminal at the same project folder location so this is the advantage of using Ides like
4:03
vs code we can use the integrated terminal and it opens on the same project folder we can directly start
4:09
typing our commands here so I will say npm init playwright at the rate latest
4:16
npm init playwright and if you want to use a
4:23
specific version you can give the version number or if you want to use the latest I will just say latest so this is
4:29
the command I have written here and I will hit enter
4:37
so this will do the setup so here it is asking do you want to use typescript or JavaScript you
4:44
can use the up or down arrows on your keyboard and select I am selecting
4:50
JavaScript and hit enter where you want to put your end-to-end tests it is giving the default folder
4:56
tests I will use the default I'll just press enter here then add a GitHub
5:02
action workflow I will go by the default false and press enter install playwrite browser I will go with
5:08
the default true and press enter and this will now initialize the node project
5:15
so you can see package.json file is created package log.json file is created in a node project this is a very
5:23
important file so here it has all the information about
5:28
the project it also has all the dependencies that we you have used in the project so you can see we have got
5:34
playwrite test I had created a video earlier on what is package.json package log.json if you
5:42
want you can check that so if you just search for what is package.json by my
5:48
name you should get that video or yes this is the one you can check this video
5:56
and we have got our project setup you can see we have got our tests folder
6:01
here it has some example tests already created we can
6:07
just run these tests and check if you want to increase the font you can go to the settings so here is the
6:15
settings icon go to settings and go to text editor
6:23
and font and here you can increase the
6:29
font so you can see it has increased the font
6:35
size also if you want you can increase the font size of the terminal text so
6:41
for that you have to open the command palette you can go to view and we have command palette here you can also use
6:47
the keyboard shortcut Ctrl shift p and if you say
6:52
open uh user settings Json
6:59
or first you can just go to open default settings Json this will open the Json
7:04
file and here you can check what is the terminal
7:10
font size so there is a terminal
7:15
font size setting
7:22
let me check what it is okay it is terminal dot integrated
7:32
dot font yes this is the setting however in this
7:40
particular file it may not be editable so I if I try to edit you can see it
7:45
says I cannot edit in read-only editor so you can just copy this setting
7:50
and then go to command palette I'm pressing Ctrl shift p and then say open
7:59
settings and you will see this open user settings Json open this file
8:06
and here you can give a comma at the end and add this setting let's say I want to make it
8:13
20 and say save it you can see the font
8:18
size increases for the terminal as well okay
8:27
okay so now we have I think you can see it properly
8:32
so we have done this step and we have got our package.json and the
8:40
test folder the project setup is done now if you want to run and check the
8:46
existing test you can see npx pre-write test this will be good to check if everything is working fine I will clear
8:52
the terminal you can also hit this
8:57
up Arrow to maximize the terminal window and here if I say npx
9:04
playwright test it will run the existing tests
9:10
and we can check if our project setup is done correctly
9:17
so it is running six tests using one worker so it is running on Chrome Firefox
9:23
webkit
9:31
and yes everything is working fine you can also run this command npx
9:36
playwright show report to check the HTML report
9:44
so it opens the browser and you can see all the details about your tests
9:49
and we have the filters as well here
9:56
all right so this is all working fine I can press Ctrl C on the terminal to stop
10:01
the report and I will say clear
10:07
okay so we can also then see our tests and see the UI mode of
10:15
playwright so if you say npx playwrite test I am pressing the top Arrow up arrow on
10:21
my keyboard to go to the last command so in PX play right test hyphen hyphen UI and hit enter
10:29
so this will open the playwright UI and here
10:34
we have a light mode and you can change the mode from here dark mode and you can see all our tests
10:42
come here we can run from here we can see all the details for example if I want to run
10:48
this particular test I can say run I will get all the details here I can
10:54
see each and every step the screenshot and I can also see the output from this
11:03
button toggle output and then I can see my tests
11:11
I can go to the source and I can see the test code source code we have logs Network
11:20
attachments everything is here all right you can also watch it and also
11:27
open it in vs code so if I say open in vs code
11:33
you can see it goes to vs code and it is asking for permission I will say yes and it opens that particular test here
11:43
all right so this is very handy very intuitive you can see all the screenshots before after
11:50
action you can see this before was this after watch this for this page dot go to
11:56
this was the action everything is here right this is very intuitive and in a moment we will see how we can use it for
12:03
API testing as well okay and we have already seen the report
12:10
now we are going to create a new file for our API tests so I will go to the
12:16
folder test folder you can do a right click and say new file or you can
12:22
click on this button that says new file here
12:28
and I will say API underscore tests dot spec dot JS you can
12:35
give it any name but it should follow the convention set in the playwrite config.js file so if you open this file
12:42
free write config.js if you see any particular naming convention to be followed you can use according to that
12:49
as of now I don't see any naming convention is here it just says that this particular folder that is tests
12:58
which is just under the main project folder will be considered for all the tests
13:03
all right so let me open back my file I have created this file
13:09
API underscore tests Dot spec.js and as of now it is empty so we are done
13:15
with the project setup here if you want you can take a screenshot of the screen
13:20
and keep it handy with you now we will continue with the steps to create a API request and
13:28
validate the response run it validate the response and see the results
13:33
so here the first step is we will import the test and expect packages from the
13:40
playwright Library okay so I will say here import
13:50
test and expect
13:59
from I am getting this Auto suggestion if you don't get the order suggestion box you
14:05
can try pressing Ctrl and spacebar on your keyboard so this is what
14:12
I have added I can save using Ctrl s on my keyboard
14:20
step number two is now we will create a test so let me first just create a simple test
14:27
I will say test and I will give the title
14:34
or I'll just say API get request
14:40
and I will say async and here
14:47
I will use the API request context so I will say
14:53
request and use this arrow symbol and a curly
15:01
bracket start and stop so I have created this test you can see this is the
15:06
body of our test and this is the API request context and this is what we will
15:12
use to run our apis get the response and do all the validation so this is very very important and you can see it is
15:19
coming from this API request context okay
15:24
so here this is what if you want you can read more about this API request context on the official
15:31
documentation so this is what we use for our API testing
15:38
okay now next step is we will
15:43
use a API URL and use the get method to
15:49
run the API and then we will also store the response in a variable so for that
15:54
we need some demo apis so here I am going to this uh website req res
16:02
dot in it has some demo apis are requires.in this is the
16:08
website and here if you scroll down you can see some dummy apis that we can use for
16:15
testing so we have get requests Post Port patch delete Etc
16:22
so here I will say
16:27
this is what we use await request dot get and the URL or the endpoint and
16:33
whatever will be the output that is the response we are storing in a variable called response so I am saying here
16:42
const response you can use any variable name is called equals to
16:47
a weight request Dot and you can see all the
16:53
methods are here delete fetch get patch post put I will say get
16:59
and within the brackets Within codes I will give the URL or the end
17:05
point of the API so here let us see this is a list users get request this is get
17:13
a single user let us use this one and this is the URL you can click here open
17:18
in a new tab and you will get the complete URL that you can copy
17:25
and add it here
17:30
okay so this is now our this will run our API request and store the response in a
17:38
variable called response okay at this moment if you want you can
17:46
save I am pressing Ctrl s and you can go to the UI if you have closed the UI you
17:52
can open it again and even if you it is running it will take the live changes so
17:58
you can see it has taken this changes it has got our API get request the file and
18:04
the test here I can run from here and check if everything is fine until now
18:09
and yes looks like everything is fine I am getting this if I go to the network I can see this
18:16
I'm getting all the details here response request response body
18:21
everything is coming here so that means everything is working fine until now
18:28
okay so now next step will be I will check
18:34
the status code so here I can use the expect assertion and say response dot
18:39
status to be 200 so I will say here expect
18:47
and I will say
18:53
response Dot status
19:01
dot 2 b and I will give the status code 200.
19:08
okay so I am anyways going to keep all the notes in the description if you want you can refer from there as well let me
19:15
just go back I will save this and go back to the UI and run it again just to
19:20
check if it is able to run this assertion and yes looks like it is able
19:25
to I if I see this this is pass now so this is running fine then
19:34
I can also check if the response contains some particular text for that I have to extract the text from the
19:41
response and store it in a variable so I am saying I will use this variable
19:50
text you can use any variable name and here I will say a weight and I will say response dot text
20:02
and then I can check if text contains some
20:07
particular value I will say expect
20:17
Dot to contain
20:22
and here if you see this particular API request it gives us the details of a
20:29
particular user first name is Janet last name is Vivo and we have got some other details I am just going to check that in
20:36
the response we get the value Janet I will save this and run again and check
20:45
if everything is working fine and you can see
20:50
this all is working fine okay I can also check in case of Janet
20:57
if I say John they should fail I will see when now run again and let us see
21:03
what happens now so you can see it fails expect to contain and here it says this particular
21:11
thing has failed if I check the source I will also get the source here
21:17
I can see the errors here and this is the particular line which has field so you can see this is so easy
21:23
to find the errors the code which has thrown the error and what's the actual issue and the details here okay
21:32
and now if you want you can also write the response on console for that you can
21:38
say console.log and await response dot Json so if I say here
21:46
console Dot log
21:52
weight response Dot Json so this will now also write the
22:00
response on the console so save and I will run it again let me change this
22:06
back to Janet so it will not fail I will save and run again
22:14
and this time it has passed you can see everything is working fine and now if I go to the console you can see we also
22:22
get the response written on the console if I check the network
22:28
I can see the request response body everything is coming fine here
22:33
all right and we have already ran and checked the results so this is
22:40
how these are the steps to create a very simple get API request with playwright if you want you can take a screenshot of
22:46
the screen and keep it handy with you now let us go to a post API request now
22:53
get request was very simple we just have to give the URL or the end point and then we do do all these assertions
22:59
however in a post request we have the request body or the payload as well so
23:06
if I check this particular example you can see along with the URL we also have to pass the request body or payload so
23:14
let us take this example and the first steps are the same
23:21
we will add the Imports and we will create the test now because we are going
23:26
to continue in the same file I am not going to add the Imports again I will just say
23:35
I'll create a test I will say test and give the title API post
23:44
request I'll say async
23:49
give the request context
23:57
and I will create the test now if you say if you add this dot only
24:06
here if you run this entire file it will only run this particular test however as
24:11
we are using the UI we are running from the UI we don't need this we can just keep it as it is
24:20
okay now this remains same
24:26
I will use request dot post so I'm just copying it from
24:34
here the method will change instead of get I will say dot post
24:39
all right and I am storing it in a variable response however after giving this URL
24:47
so let me also give check the URL that we have to give so this is the URL so I'll change the
24:54
url here
25:01
so after the URL we have to give the request body so here you can see step
25:06
number three is send a post request along with request body and store the response in a variable and this is how
25:12
we give it so here after the URL I will give a comma
25:20
and then I'll start a curly bracket start and
25:25
stop and then here I will say data colon and give the
25:31
request body so I will say data
25:36
colon and here I am just going to copy this request body
25:43
and paste it here you can also correct the formatting by
25:50
doing a right click and say format document
25:55
and save it okay so this is how we give the request body
26:02
in a post request
26:07
then the rest of the things will remain as it is we can add the assertions here we can
26:15
check the Response Code we can check some particular value in the response so let's say
26:22
I will just copy this assertions
26:28
all these assertions checking the status code checking a value in the response and also writing the response on the
26:34
console I am copying this from the last test and pasting it here
26:46
okay the status code for a successful post request is 201 so I am adding 201
26:53
here and then in the response whatever name and job we give we get back the same
27:01
values here so let me check I am going to give my name here log herb and I will
27:07
say job is teacher and in the response I am going to check if I
27:14
get back the name here and that's it so this is our
27:21
test for a post request save this and I will run and check
27:28
it has come here API post request I will run this
27:36
and you can see everything is fine I also get the console output
27:43
I see the network I see the request response body
27:49
everything is fine here here also all the assertions are working
27:55
fine okay
28:01
so we are able to run our post request as well and we have already
28:06
ran and checked the results so if you want you can take a screenshot of the screen as well and keep it handy
28:13
with you next we will see a put request now put is very much similar to a post request
28:19
because it also has a payload or a request body so for a put request let us
28:26
see some example we have this put put is used for update and it is used to
28:33
replace the entire resource on the server and Patch is also for update but
28:38
it is for a partial update it does not replaces the entire resource it changes something but put is for a complete
28:45
replacement of the resource so let us take this example I will go to my vs code
28:52
and I'm just going to copy this entire post API request
28:59
and I will
29:05
copy and paste it again and I will call it API
29:12
put request and here instead of post method I will use a put method request
29:17
Dot put we will have to change the url
29:26
so let me just copy the URL
29:37
so you can see this is going to update a particular user with id2 here
29:43
right and here the body looks same we have name and job so this is fine the
29:50
status quo we should check is 200 a successful post a successful update or a put request sends the status quo to 200
29:58
and then we are checking the values in the response and writing the response
30:04
this is all fine so I will save this and check on the playwright UI it has
30:10
come here let us run this and check
30:15
and yes looks like everything is working fine we are able to run this if I get check
30:21
the console we are getting this output here if I check the network everything is fine we get status 200
30:30
method put this was a request content type duration size
30:36
I can check the request here this was a request that went to the server this is
30:41
the response from the server and this is the response body
30:48
okay so this is all working fine now we have got the delete API request
30:55
here we just give the URL and we can check the status code 204 so
31:01
if I check a delete request here this one is for delete so I'll take this URL let me first just
31:10
copy the get API request test
31:18
and I will paste it here
31:24
I will say this is API delete request and here I will say request
31:31
dot delete and this is a particular user
31:39
so this is the URL I think it should be the same yes it is the same it is deleting the
31:46
user with id2 here and here I'll just check the status quo should be 204 I don't need all these
31:55
here so this is my delete request
32:01
I will go to the I will save and go to the playwrite UI we have got the request
32:06
here let us run and check
32:13
so everything is working fine you can see if I check the network
32:18
this is delete 204 and request
32:24
in the response we get this response headers and here body will be empty because the
32:30
resource is now deleted all right so this is how we use a delete API
32:39
request this is how we run our API request on playwright now here are some
32:45
references if you go to the official documentation if you search for
32:50
playwright API testing you will see the official documentation and this will be
32:56
very useful and very handy you can see the latest changes here so here you can
33:01
see all the latest changes then if you check the API request context so this is the
33:07
context we have been using the request contest which is actually the API request context you can read more about
33:13
it you can see all the methods delete is here dispose fetch all these methods you can
33:21
check and then you can also see the
33:27
response methods or API response assertions so if you search for
33:33
pi response you can see the API response here
33:39
then API response assertions are here
33:44
you can see methods so here you can see if I say await expect response dot to be
33:51
okay that means it will check the response is in range 200 to 299 that means all the positive response status
33:58
codes similarly if I say not to be okay it will check it is not in that range so
34:04
you can check all these API response assessions as well
34:09
all right and this is the demo apis that we have
34:14
used and please do some Hands-On if you have any issues if you face any problems let me know and I will see you soon I
34:21
hope this was very useful thank you for watching and never stop learning
34:29
foreign