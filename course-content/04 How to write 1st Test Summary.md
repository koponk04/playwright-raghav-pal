# Summary of 04 How to write 1st Test.md

**Summary of Playwright Course Video Content**

**Chapter 1: Introduction**  
The tutorial begins with Raghav introducing the Playwright testing framework and outlining the steps for writing the first test. Viewers are encouraged to take a quiz linked in the video description to assess their knowledge and to comment with their scores or questions.

**Chapter 2: Step 1 - Create a New Test File**  
Raghav demonstrates how to create a new file in the test folder of a Playwright project. He guides users to name their test file as `myFirstTest.spec.js`, setting the stage for writing a new test.

**Chapter 3: Step 2 - Import Playwright Test Module**  
He explains importing the Playwright test module into the script using Node.js's `require` function. Specifically, he highlights importing only the necessary modules (`test` and `expect`) to streamline the test process.

**Chapter 4: Example of Adding and Importing Modules**  
Raghav illustrates creating additional modules (e.g., `hello.js`) that contain functions to be exported and utilized in the main test file. This includes an overview of functions, their declaration, and exporting them for reuse.

**Chapter 5: Utilizing Playwright’s Test and Expect Functions**  
He introduces the functionality of the `test` and `expect` methods provided by Playwright for structuring tests and writing assertions, respectively.

**Chapter 6: Step 3 - Creating a Test Block**  
The tutorial progresses to creating a test block using the `test` function, where Raghav establishes a basic test titled "my first test." He explains the need to utilize a fixture called `page` for performing actions like navigating to a URL.

**Chapter 7: Running Tests and Assertions**  
He demonstrates using asynchronous programming (with `async` and `await`) to ensure that the test executes smoothly by waiting for page loads. Raghav also provides examples of making assertions using the `expect` function to confirm the title of the page being tested.

Throughout the session, Raghav encourages viewers to experiment with the Playwright framework, learn through practical examples, and check the report generated post-test execution. He concludes by thanking viewers and urging them to keep learning as they continue with the course.