# :wave: The Basics of GitHub 


## 🤓 Course overview and learning outcomes 

The goal of this course is to give you a brief introduction to GitHub. We’ll also provide you with materials for further learning and a few ideas to get you started on our platform. 🚀
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be)

## What is Git?

Git is a distributed version control system (VCS) used to track changes to files over time. It lets you create snapshots (commits) of your project, switch between different lines of work (branches), and collaborate with others by merging changes. Git runs locally on your computer and stores the full history of your project so you can inspect, compare, and revert changes as needed.

## Installing Git and Setting Up Your Identity

Before you begin, Git must be installed on your computer and configured with your name and email.  
These values are used to identify you as the author of your commits.

---

### Step 1: Install Git

If Git is already installed, you can skip this step.

1. Open **Visual Studio**.
2. Go to **Git → Settings**.
3. If Git is not installed, Visual Studio will prompt you to install it.
   - Follow the on-screen instructions.
4. Restart Visual Studio after installation is complete.

> 💡 Visual Studio uses Git behind the scenes. You do not need to install Git separately unless Visual Studio prompts you to.

---

### Step 2: Set Your Git Username and Email

Your Git username and email are attached to every commit you make.

1. In **Visual Studio**, open the **Git** menu.
2. Select **Settings**.
3. Under **Git → Global Settings**, locate:
   - **User Name**
   - **Email Address**
4. Enter:
   - Your **full name** (first and last)
   - Your **WSU email address**
5. Close the Settings window — changes are saved automatically.

> ⚠️ Use your real name and school email. This is how your instructor identifies your work.

---

### Step 3: Verify Your Settings

1. Open the **Git Changes** window.
2. Make a small test change (or wait until you commit `STUDENT.md`).
3. After committing, check the commit details.
4. Confirm your name and email appear correctly.

If your name or email is incorrect, return to **Git → Settings** and update them before continuing.

---

### Why This Matters

- Every commit records **who** made the change.
- Incorrect or missing information makes grading and feedback difficult.
- Using consistent information helps you build a professional commit history.

You only need to set this up **once** on your computer.


## :octocat: Git and GitHub

GitHub is a way to use the same power of Git all online with an easy-to-use interface. It’s used across the software world and beyond to collaborate and maintain the history of projects.

GitHub is home to some of the most advanced technologies in the world. Whether you're visualizing data or building a new game, there's a whole community and set of tools on GitHub that can get you to the next step. This course starts with the basics of GitHub, but we'll dig into the rest later.

### Creating a GitHub account

1. Visit https://github.com and click **Sign up**.
2. Choose a username, enter your email, and set a strong password.
3. Verify your email address by clicking the link GitHub sends to your inbox.
4. (Optional but recommended) Enable two-factor authentication in **Settings → Security**.
5. Add a profile name and avatar in **Settings → Profile** so others can recognize you.
6. Create your first repository: click **New repository**, give it a name (e.g., `my-first-repo`), choose visibility (public/private), and click **Create repository**.


## :octocat: Understanding the GitHub flow 

The GitHub flow is a lightweight, branch-based workflow that helps you collaborate safely and deploy often. Below are the basic steps and a simple visual to make the process easier to follow.

## 💻 GitHub terms to know  

### Repositories

### What is a repository?
- A repository is your project folder on GitHub. It stores files, the full commit history, issues, pull requests, and other project metadata.
- Add a `README` to explain what your project does, how to run it, and how others can contribute.

### Who uses repositories?
- You can work alone or invite collaborators. Classroom assignments and forks are common for students; teams usually use shared org repos.

### How to access a repository
- Use the GitHub website to browse files and history, or `git clone <repo-url>` to work locally. Your [GitHub dashboard](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/about-your-personal-dashboard) helps you find your repos.

### What belongs in a repository?
- Source code, documentation, tests, configuration, and a `README` that explains the project.

### Cloning a Repository

- When a repository is created on GitHub, it is stored **online (remote)**.
- **Cloning** creates a **local copy** of that repository on your computer.
- The local copy stays linked to the GitHub version so changes can be synced.
- Cloning allows you to:
  - Edit files using tools like **Visual Studio** instead of the GitHub website.
  - Fix issues and add or remove files more easily.
  - Make and push **larger or multiple commits**.
- When you clone a repository, Git downloads:
  - All files and folders in the project.
  - The **entire version history** of the repository.
- Having the full history lets you:
  - Experiment safely.
  - Revert back to an older version if something breaks.
- read ["Cloning a Repository"](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 

### Committing and Pushing

- **Committing** and **pushing** are how you move changes from your computer to GitHub.
- A **commit**:
  - Saves a snapshot of your changes.
  - Acts like a **checkpoint** you can return to later.
- Each commit should include a clear **commit message** that describes what you changed.
  - Example: `Added README with project information`
- **Pushing**:
  - Uploads your commits to the remote repository on GitHub.
  - Allows your instructor and teammates to see your work.
- You can make multiple commits as you work and push them when you are ready to share.

💡 *Tip:* Small, frequent commits with clear messages make it easier to track your progress and troubleshoot issues.

- Learn more: [Creating, Cloning, and Archiving Repositories](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories) • [About READMEs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes)

### README guidance (what to include)
- Short overview: What the project is and why it exists.
- Getting started: How to clone, install, and run the project (example commands).
- Usage: Brief examples or screenshots.
- Contributing (optional): How others can help or submit changes.
- License and contact info.

### Quick tips
- Choose a clear repository name.
- Keep the `README` up to date with basic setup steps.
- Add small examples or commands so others can run the project quickly.

To learn more about repositories and READMEs, read [Creating, Cloning, and Archiving Repositories](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories) and [About READMEs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes). 

### Branches

- What are branches?
  - Independent lines of development that let you work without changing the `main` branch.
- Why use branches?
  - Develop features, fix bugs, or experiment safely in isolation.
- Create a branch (local)
  - `git checkout -b my-branch` or `git switch -c my-branch`
- Share and merge
  - Push: `git push -u origin my-branch`
  - Open a pull request to merge into `main` after review.
- Tips
  - Use descriptive names (e.g. `feature/login`, `fix/typo`) and keep branches focused and short-lived.
- Learn more: [About Branches](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches).

### Forks

- What is a fork?
  - A fork is a personal copy of someone else's repository on your GitHub account.
- Why fork?
  - Experiment, fix bugs, or add features without changing the original project.
- Typical workflow
  - Click "Fork" on the upstream repository (GitHub website).
  - Clone your fork: `git clone <your-fork-url>`
  - Make changes, commit, and push to your fork.
  - Open a pull request from your fork to the original repository to propose changes.
- Tips
  - Keep your fork up to date with the upstream repo (`git remote add upstream <url>` then `git fetch upstream` / `git merge` or `git rebase`).
  - Use branches in your fork for each change to keep work organized.
- Learn more: [Fork a repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

### Pull requests

- What is a pull request (PR)?
  - A PR is a request to merge changes from one branch (or fork) into another and starts a discussion and review process on GitHub.
- Why use PRs?
  - Get feedback, run automated checks (CI), and review changes before they become part of `main`.
- How to open a PR
  - Push your branch or fork to GitHub, then click "Compare & pull request" (or open a new PR) and add a description and reviewers.
- Review and iterate
  - Reviewers can comment or request changes. Push follow-up commits to the same branch to address feedback.
- Merge and close
  - After approval and passing checks, merge the PR into the target branch and delete the feature branch if desired.
- Tips
  - Write a clear PR title and description, link related issues, and keep changes focused to make review easier.
- Learn more: [About Pull Requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).

  [![What is a pull request? (short intro)](https://img.youtube.com/vi/nCKdihvneS0/hqdefault.jpg)](https://www.youtube.com/watch?v=nCKdihvneS0&list=PL0lo9MOBetEGWDtUgEsQoW0lgwytsZDvu&index=3)


### Using markdown on GitHub 

You might have noticed already, but you can add some fun styling to your issues, pull requests, and files. ["Markdown"](https://guides.github.com/features/mastering-markdown/) is an easy way to style your issues, pull requests, and files with some simple syntax. This can be helpful to organize your information and make it easier for others to read. You can also drop in gifs and images to help convey your point!
To learn more about using GitHub’s flavor of markdown, read ["Basic Writing and Formatting Syntax"](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).  


## 📝 Assignment

### Creating and Submitting `STUDENT.md`

Follow the steps below carefully. This file is your submission for this assignment.

1. **Step 1: Create a New Branch**
   - You must complete your work on a new branch.
   - Open your repository in Visual Studio.
   - Open the Git menu → Select **New Branch**.
   - Name your branch using this format: `firstname-lastname` (example: `scott-hadzik`).
   - Make sure the new branch is checked out (active).

2. **Step 2: Create the `STUDENT.md` File**
   - In Solution Explorer, right-click the project folder → **Add → New Item**.
   - Choose **Text File** and name the file exactly: `STUDENT.md`.
   - ⚠️ The file name must be spelled and capitalized exactly as shown.
   - Click **Add**.

3. **Step 3: Add the Required Content**
   - Open `STUDENT.md` and paste the following content:

     ```markdown
     # Student Information
     
     - Name:
     - WSU Email:
     
     ## Reflection
     
     - One thing I learned about Git or GitHub:
     - One thing that is still confusing:
     ```
   - Replace the placeholders with your own information. Do not leave any blank fields.
   - Write complete sentences for the reflection items.

4. **Step 4: Save and Stage the File**
   - Save `STUDENT.md`.
   - Open the Git Changes window in Visual Studio.
   - You should see `STUDENT.md` listed as a new file. Make sure it is staged (checked).

5. **Step 5: Commit Your Changes**
   - In the Git Changes window, enter a commit message such as:

     ```
     Add STUDENT.md with student information
     ```
   - Click **Commit All**.

6. **Step 6: Push Your Branch to GitHub**
   - After committing, click **Push** in the Git Changes window.
   - Confirm that your branch appears on GitHub.

7. **Step 7: Open a Pull Request (This Is Your Submission)**
   - Go to your repository on GitHub in a web browser.
   - You should see a banner offering to create a Pull Request. Click **Compare & pull request**.
   - Set:
     - Base branch: `main`
     - Compare branch: `firstname-lastname`
   - Title your Pull Request using this format:

     ```
     Firstname Lastname – GitHub Introduction
     ```
   - Review the checklist and click **Create Pull Request**.

8. **Step 8: Verify Your Submission**
   - Verify that `STUDENT.md` appears in the **Files changed** tab of your Pull Request.
   - Verify your Pull Request shows green checkmarks for all automated checks.
   - Ensure the Pull Request is open (do not close it yourself).

Important Notes

- Do **not** edit `README.md`.
- Do **not** merge your own Pull Request.
- If an automated check fails:
  - Fix the issue in Visual Studio
  - Commit and push again — the checks will rerun automatically

What to Submit in Canvas

- Submit the URL of your Pull Request.

## 📚  Resources 

* [A long video explaining what Git and GitHub are](https://www.youtube.com/watch?v=NUELGzIHT-I)

  [![A long video explaining what Git and GitHub are](https://img.youtube.com/vi/NUELGzIHT-I/hqdefault.jpg)](https://www.youtube.com/watch?v=NUELGzIHT-I)
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
* [How to use GitHub branches](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interactive Git training materials](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub's Learning Lab](https://lab.github.com/)
* [Education community forum](https://education.github.community/)
* [GitHub community forum](https://github.community/)
