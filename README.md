# Intro To Java

Classroom link: https://classroom.github.com/classrooms/8591132-team-1339-intro-to-java-23-24

This repo is the public entry point for Angelbotics' "Intro To Java" course. We will use it for things such as common git and GitHub information, grading scripts, and pretty much any other common source of information that is okay to release or needs to be publicly accessible. More information will be published as time goes on.

# Directories
## images
Updating a GitHub wiki does not allow you to upload images directly. Instead, they have to be uploaded to an accessible location and then references via URL. While it is normally discouraged to upload binary content to a git repo, we accept the tradeoffs here to be able to use images in our Wiki. Please make sure to try and give good descriptive names to any images here.

## input and output
Most of our projects will get input from the user or output something. These currently are specified in the GitHub classroom autograding test itself and that's what's being graded against, but it seemed prudent to have a location to store all of those input and output files. The autograding test case will be named similarly to the text file so if you're not getting one correct, you can see the input used to test against and the output the autograder will see. If there is only one input, it will be in a file called `in.txt` for that assignment. Similarly if there is only one output, it will be called `out.txt`.

Note that your console will print back any characters you type, but that doesn't happen in the autograded tests. That means the output in the GitHub action may look strange compared to the output in your console because it won't contain your input. For example, if you ask for 5 things from the user, the test output will not include any newlines since the newlines will have come from user input. It would all appear on the same line. However, this is really confusing for learning from these output files. In these output files, we will also include the user input, making it match your console more than it does the autograded tests.

## scripts
Currently unused. Figured it would be helpful to have a common place for scripts as well.