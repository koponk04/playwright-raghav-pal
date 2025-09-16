# Summary of 12 Annotation & Tags.md

This course on Playwright, presented by Raghav, focuses on understanding annotations and tags through step-by-step demonstrations. 

**Key Highlights:**
1. **Introduction to Annotations and Tags**: Definitions and usage of annotations like `only`, `skip`, `fail`, `fix me`, and `slow`, as well as tagging test cases with labels (e.g., `@regression`, `@smoke`).
   
2. **Using Annotations**: 
   - **Skip**: Use `test.skip` to skip certain tests.
   - **Fail**: Use `test.fail` to mark tests as failed if they pass.
   - **Fix me**: Marks tests for future fixes.
   - **Slow**: Indicates a test is slow, increasing its timeout.
   - **Only**: Runs only a specific test(s).

3. **Conditionally Skipping Tests**: Conditional skips based on certain parameters (e.g., browser type).

4. **Tagging Tests**: 
   - Tags can be attached to test cases to filter which ones to run.
   - Use `--grep` to run tests matching specific tags, and `--grep-invert` to skip them.

5. **Conclusion**: Annotations control test execution logic, which can be applied individually or to groups of tests. 

The session emphasizes practical implementation through coding examples and encourages participants to explore the official Playwright documentation for more details.