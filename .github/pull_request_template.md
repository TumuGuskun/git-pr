<!-- Please start your PR title with one of [regression-fix] / [fix] / [migration] / [feat] / [refactor] / [build] / [docs] / [chore] -->

### Regression Fix <!-- required -->

<!--
If this is a regression fix, please:
1. Add a test that would have caught the regression (if applicable)
2. Check the following box, and add a link to the PR that introduced the regression

This allows us to make sure that the regression fix will get cherry-picked into the stable release.
-->

- [ ] This fixes a regression introduced by: [Regression PR Link] [FAQ](https://retoolconfluence.atlassian.net/wiki/spaces/EPD/pages/91586631/Fixing+Regressions+at+Retool)
- [ ] This is not a regression fix.

### Description <!-- required -->

### Screenshots <!-- required for visual changes -->

### Changelog <!-- required -->

<!--Choose one by changing [ ] to [x] -->

- [ ] [Describe customer-facing change] <!-- start with Added, Fixed, Improved, etc. -->
- [ ] Feature flagged: `[exampleFlag]` (Please add tests for both flag ON & OFF scenarios) <!-- write a changelog update in the tear down PR for small features; work with your PM on large features -->
- [ ] No customer-facing change

<!--
Questions: Ping in #changelog
Changelog: https://updates.retool.com/en
-->

### Tests <!-- required -->

<!--We are focusing on stability and quality right now at Retool, please fill this out and confirm test coverage-->

<!--Choose by changing [ ] to [x] -->

- [ ] ✅ [Describe the added or updated test coverage] <!-- e.g. Storybook, unit, integration, Cypress, screenshot. -->
- [ ] ❓ I don't know how to test this change <!-- Ping #eng-help for any help on writing tests! -->
- [ ] 🟡 I'm choosing not to write tests for this change because: [your reason here] <!-- This should be the exception (e.g. copy changes) -->
- [ ] 🔧 This fixes flaky/bad tests as described here: [cause of flaky or bad test] <!-- If the PR fixes tests, you can also put in a linear ticket with the cause -->

<!--
Frontend testing guide: https://retoolconfluence.atlassian.net/wiki/spaces/EPD/pages/246677950/Retool+Frontend+Testing+Guide
-->

### Test Instance

<!-- Start test instance -->

<!-- Choose by changing [ ] to [x] -->

- [ ] Create an On-Prem preview instance <!-- Run garden command to spin up a teset instance -->

<!-- Put environment variables below -->

Please put custom env vars in format: ABC=xyz (equal sign; no quotes/spaces)

-- environment variables starts --
EXAMPLE_ENVVAR=example
-- environment variables ends --

### Analytics Instrumentation

<!--
If this PR contains any new analytics events or updates to existing events, please:
1. Confirm you are following best practices from the instrumentation guide: https://retoolconfluence.atlassian.net/wiki/spaces/DATA/pages/80774026/How+to+instrument+Retool+adding+events+and+user+properties
2.  Request a review from the data team (use the Reviewers option on PR and select data team).
-->

<!--Choose one by changing [ ] to [x] -->

- [ ] This adds a new analytics event
- [ ] This edits an existing analytics event
- [ ] This does not touch analytics events
