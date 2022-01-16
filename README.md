# AWS-TaskList

The goal of this project was to deploy a fully functioning web app, accessible by anyone, on AWS Lambda. The application itself is a simple task or todo list with a users table and a tasks table. There is a one-to-many relationship between users and tasks. The application allows user and task creation, retrieval, and deletion. 


Tools, libraries, languages, and services used:

Backend Language: Python

Application Framework: Flask

Database: MySQL

Database Driver: MySQLdb

Database Hosting: AWS RDS

API Hosting: AWS Lambda + API Gateway

API code storage: S3 Bucket

Route Testing: Postman

Deployment tool: Zappa


Routes:

Get all users: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/

Get specified user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/3/

Create user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/

Delete user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/3/

Get specified user's tasks: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/tasks/1/

Create task for specified user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/tasks/1/

Delete task: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/tasks/1/


I allocated around 90% of my time on this project to researching tools that I was unfamiliar with. While I had used S3 buckets in a previous project, I was unfamiliar with the rest of the AWS services that I used. Even though I was able to speed up the process by using Zappa to deploy my application, I had to understand how everything worked in order to deploy the application correctly. For example, without understanding the "serverless" aspect of AWS Lambda, I would not have had the architectural understanding required to run this application on the cloud, which would have prevented me from writing any code in the first place. In addition to architecture, I did a lot of research on databases, because I had only previously worked with SQLite which was much simpler to use as it doesn't require external database hosting. 


