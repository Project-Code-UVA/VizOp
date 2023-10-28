# Project README

## Git Strategy

**Always do work and run the development server in your virtual environment**

### 1. Checkout `main` and pull the latest changes:

    git checkout main
    git pull


### 2. Create feature branch off `main` for the feature you are working on and push to set up remote feature branch:

    git checkout -b feature/branch-name main
    git push -u origin feature/branch-name

**OR create a new branch from an existing remote feature branch:**

    git checkout -b feature/branch-name origin/remote-branch-name


### 3. Within your virtual environment, install any packages that may have been added:
    pip install -r requirements.txt


### 4. Make changes to implement the feature, add files and commit changes:

    git add .
    git commit -m “your commit message”


### 5. Push changes to the remote feature branch:

    git push


### 6. When the feature is complete, make a pull request into the test branch. If the feature works in the test environment and does not cause any breaking changes or bugs, make a pull request into `main`.



## Virtual Environments + Package Management

**Virtual envs do NOT get committed/pushed to the remote repository. Make sure the virtual env (`env/`) on your local machine is included in the `.gitignore` file.**

### 1. Create a virtual env on your local machine in the project root folder (`/VizOp`) with:

-    Windows: `py -m venv env` 
-    Linux/Mac: `python -m venv env`


### 2. Activate the virtual env:

-   Windows: `.\env\Scripts\Activate.ps1`
-   Linux/Mac: `source ./env/bin/activate`


### 3. Install necessary dependencies:

`pip install -r requirements.txt`


### 4. Update requirements.txt dependency list:
-   If you install any additional packages while implementing a feature, install (if you have not already) and run the `pipreqs` command in the project root folder to generate a `requirements.txt` file that lists all of the projects dependencies

    pip install pipreqs
    pipreqs /path/to/project/root



## Getting Started with Node.js/npm and React


### 1. Install Node.js and npm

-   If you don't already have Node.js and npm installed, you can download and install them from the official website. npm (node package manager) is included with Node.js, so there's no need to install it separately. 
-   https://nodejs.org/en


### 2. Create a new React app

-   You can create a new React app using the `create-react-app` command-line tool, which sets up a new React project with all the necessary files and configurations. Open your terminal and run the following command to create a new React app:

    `npx create-react-app my-react-app-name`


### 3. Navigate to Your Project Directory

-   Change your working directory to the newly created project folder:

    `cd my-react-app-name`


### 4. Start Your React Development Server

-   To see your React application in action, run the development server with the following command:

    `npm start`

-   This will start a development server, and your React app will be accessible in your web browser at http://localhost:3000.


### 5. Updating .gitignore

-   Make sure to include the `node_modules` folder and `package-lock.json` in the `.gitignore` file. 

-   `package.json` does NOT go in `.gitignore`. This should be committed and pushed as it lists all of the project's dependencies and their versions, along with other configuration data needed for the project to run properly.


### 6. Managing Dependencies with npm

-   Running `npm install` will install all of the necessary dependencies listed in `package.json`. This will generate the `package-lock.json` file, and now your project should be able to run.

-   You can use `npm` to manage your project's dependencies. To add a new package to your project, use the `npm install` command. For example, to install a popular state management library like Redux. This will add the "redux" package to your project's `node_modules` directory.-

    `npm install redux`


