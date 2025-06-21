This repo demonstrates how to setup and deploy a basic Python based function app. Function apps are a high versitiale technology that allow you to run code on demand leveraging a serverless architecture.

Before we get started there are a few pieces of software that we will need.
1. VS Code with the following extensions (Azure, Dev Containers)
2. Docker Desktop
3. Git

Before we begin, ensure that you have all three of these programs installed and docker desktop is running in the background.

# Step 1: Provision the dev container.

A dev container provides a containerized developed environment. This means that when you develop in a dev container, you are not actually using your computers operating systems and software. Instead, you are working in an isolated environment that is specifically configured for your specific use case. In this example, we will be using a dev container image that contains all the necessary software that we need to develop and run a python based function app.


# Step 2: Provision the function app project

Using the Azure Extension in VSCode, we will provision a function app with an HTTP trigger. This will give us the necessary file structure that we will need for our function app. 

# Step 3: Create a virtual Python environment inside of the dev container. 


# Step 4: Understanding the Azure function project structure


# Step 5: Debugging an Azure Function Project Locally


# Step 5: Provisioning an Azure Function resource in the Azure Portal


# Step 6: Deploying your Azure Function project to a Function App


# Step 7: Debugging and testing a deployed function app