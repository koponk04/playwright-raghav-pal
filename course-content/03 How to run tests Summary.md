# Summary of 03 How to run tests.md

### Summary of the Course Content

**Chapter 1: Introduction**
- The instructor, Makha, introduces commands for running tests using Playwright, such as executing all tests, specific tests, headless vs. headed modes, parallel runs, and debugging.
- A quiz link is provided for knowledge assessment, and viewers are encouraged to engage in the comments.

**Chapter 2: Run All Tests**
- The command `npx playwright test` executes all tests in a project folder, running on all browsers in headless mode, producing an HTML report.

**Chapter 3: Parallel Test Execution**
- The `--workers` option allows running tests with multiple workers in parallel to save time, especially beneficial for larger test suites.

**Chapter 4: Running Specific Test Files**
- The command structure allows running specific test files, and multiple files can be specified simultaneously.

**Chapter 6-7: Test Selection by Name or Title**
- Tests can be executed based on file names or specific test titles using the `-g` flag.

**Chapter 8: Running on Specific Browsers**
- Use `--project` to run tests on specific browsers.

**Chapter 9: Headed Mode Execution**
- The `--headed` option runs tests visibly in a browser instead of in headless mode.

**Chapter 10: Debugging Tests**
- The `--debug` option enables step-by-step debugging, employing a Playwright inspector for detailed troubleshooting.

**Chapter 11-12: Debugging Specific Test Cases**
- Users can run and debug specific test files or from specified lines to focus on particular tests.

**Chapter 13: Summary of Commands**
- A recap of essential Playwright commands is provided, encouraging users to keep them handy for reference.

Overall, the course covers command usage for Playwright, including executing tests, running in different modes, debugging processes, and optimizing test execution.