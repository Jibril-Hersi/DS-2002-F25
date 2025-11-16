# Lab 2: Git and GitHub
Follow all the steps below for practice using Git and GitHub.

<br>

## Part 0. Setup
1. **Create a single GitHub Gist to submit the URLs you create in these steps. The URL to this Gist will be what you submit on Canvas for grading.** Please use the following format in your Gist:
```
Part 1: <paste repo URL here>
Part 2: <paste repo URL here>
Part 3: <paste repo URL here>
Part 4: <paste repo URL here>
```
- Ensure you have already installed `git` for the environment you will be working in.
- Ensure you have set up your **SSH key authentication** with GitHub and your working environment. If you completed Activity 2, you should be all set!
- **Reference**: If you still need to set up and dislike the resources on Canvas, you can go to https://uvads.github.io/git-basics/ and work through pages 0, 1, and 2. When setting up `git` CLI authentication, I strongly suggest SSH key authentication.

<br>

## Part 1. Git/GitHub Basics (10 out of 30 points)
For this quick exercise, you will create a simple project to demonstrate your understanding of fundamental Git commands. Rather than cloning a repository, we will be making one in GitHub and one in out local Git, and then we will be connecting them!

1. Create a new repository on GitHub called `data-science-lab-2-yourcomputingid` (e.g., data-science-lab-2-atr8ec). Do not add a README or any other files during creation.
2. On your local machine, navigate to the directory where you store your projects (**I highly recommend setting up the following directory** `~/Documents/GitHub/DS_2002`) and initialize a new Git repository from the command line and name it something else, because we can!:
```
git init replace-with-fun-repo-name
```
3. Add a new file called `README.md` to this local directory.
4. Edit or append text to your README to tell me your current plans after graduation.
   - "Still figuring it out ¯\\_ (ツ)_/¯" is valid.
5. Run `git status` to see that you have edited the file. (You should see it say `Changes not staged for commit:` and `modified: README.md` in red)
6. Run `git diff` to see the changes you have made. (You should see it note the file(s) being modified and the lines of code added or subtracted)
7. Stage your changes. (You may get this warning that you can ignore: `warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it`)
8. Run `git status` to see that you have staged the file. (You should see it say `Changes to be committed:` and `modified: README.md` in green)
9. Make your first commit.
10. Run `git status` to see that you have committed the file. (You should see it say `nothing to commit, working tree clean`)
11. Run `git log` to see your list of commits. (You should see it say the following but with a different hash `commit a3ff5fb5e6f357482137747ebbd1bf38af6426cf (HEAD -> main)`)
12. Link your local repository to the GitHub repository you created in step 1:
```
git remote add origin git@github.com:your_username/data-science-lab-2-yourcomputingid.git
```
13. Push your changes to GitHub:
```
git push -u origin main 
```
14. Go back to GitHub and look at your repository, you should now see your README!
15. Put the URL of the repository you created into the Gist.

<br>

## Part 2. Practice With GitHub Skills (10 out of 30 points)

1. Go to **GitHub Skills** https://skills.github.com/
2. Find the first lesson, "Introduction to GitHub" and right-click on the link to open it in a new browser tab.
3. Read the page closely, paying attention to what you will do in this lesson.
4. Right-click on the "Start course" button (as instructed) to open it in a new brower tab.
5. Follow the instructions closely to copy their lesson into your own account.
6. Once that is complete, wait about 20 seconds and refresh the page in your copy of the lesson.
7. Follow the instructions to complete the lesson.
8. THERE ARE FOUR (4) STEPS TOTAL
9. Keep going until you see "Congratulations, you've completed this course and joined the world of developers!"
10. Add the URL to the new repository you created in this step to the GitHub Gist.

**OPTIONAL EXTRA FUN:** GitHub Skills has many other lessons you can complete. Give some more a try!

<br>

## Part 3. Set up your GitHub Profile README Page (5 out of 30 points)

You can use GitHub to showcase your own work, interests, and projects.

1. [Follow these instructions](https://docs.github.com/en/get-started/start-your-journey/setting-up-your-profile#adding-a-profile-readme) to set up yours.
2. Take a look. [Here](https://github.com/schacon/) is a good example from Scott Chacon. Remember that your code and projects are some of the most important evidence of your work, so highlighting that is a part of obtaining internships and interviews. Even if you don't feel you have much to showcase now, this will give you one place to display your technical work.
3. Add the URL to your GitHub Profile page to the GitHub Gist.

<br>

## Part 4. Fork a Repository and Submit a Pull Request (5 out of 30 points)

1. Go to https://github.com/austin-t-rivera/ds_2002-directory/ and fork the repository by clicking on the FORK button in the upper-right of the page. Create the fork in your own GitHub account.
2. Clone your fork to your local computer, or open it in a GitHub Codespace.
3. Within the `people` directory create a subdirectory named with your computing ID, i.e. `atr8ec` or `mst3k`, etc.
4. Inside of that subdirectory, create a `README.md` file.
5. Paste the code below into that file, and fill out the appropriate fields. If you'd like to include an image of yourself (jpg, png, gif, etc.) add it to your subdirectory as well. Introduce yourselves! If you need an example for reference, see [this page](https://github.com/austin-t-rivera/ds_2002-directory/blob/ecbac67d680d881c7a5b50d133998529e1d1e591/people/atr8ec/README.md). Here is a Markdown [reference](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) for formatting your page.

    Be sure the first line uses the `#` character followed by a space and your name.

    ```
    # Your Name
    
    ![Path to an image](myphoto.jpg)

    - Hometown: 
    - Hobbies: 
    - First Computer I Ever Touched: 
    - My GitHub Profile: <Insert the full URL to the README page you set up in Step 3>
    ```
    
7. `git add` your file(s), then commit them, and push them back to **your fork** in GitHub.
8. From your forked repo in the GitHub website, submit a Pull Request for your changes to be incorporated back upstream into the original repository. You can submit a PR by clicking on the "Contribute" drop-down and selecting "Open Pull Request". That will open up a form which you will submit to trigger the PR. Give your PR an informative title then submit.
9. Add the URL to your PR to the GitHub Gist.

You will get a notification email that your Pull Request has been accepted. Merged Pull Requests will display your name and a link to your profile on the home page of the main repository.

## BONUS: Create a GitHub Pages website

Follow [these instructions](https://pages.github.com/) and create a "user" site. A few examples:

- https://schacon.github.io/
- https://nmagee.github.io/
- https://mk.gg/

<br>

## Submission
Copy and paste the URL of your Gist into the Lab 2 submission page on Canvas.
