# AWS-TaskList

The goal of this project was to deploy a fully functioning web app, accessible by anyone, on AWS Lambda. The application itself is a simple task or todo list with a users table and a tasks table. There is a one-to-many relationship between users and tasks. The application allows user and task creation, retrieval, and deletion. 

## Tools, Libraries, Languages, and Services Used

Backend Language: Python

Application Framework: Flask

Database: MySQL

Database Driver: MySQLdb

Database Hosting: AWS RDS

API Hosting: AWS Lambda + API Gateway

API Code Storage: S3 Bucket

Deployment Tool: Zappa


## Routes

Get all users: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/

Get specified user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/3/

Create user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/

Delete user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/users/3/

Get specified user's tasks: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/tasks/1/

Create task for specified user: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/tasks/1/

Delete task: https://nbnfbhc4t4.execute-api.us-east-2.amazonaws.com/dev/tasks/1/



## Notes

I allocated around 90% of my time on this project to researching tools that I was unfamiliar with. While I had used S3 buckets in a previous project, I was unfamiliar with the rest of the AWS services that I used. Even though I was able to speed up the process by using Zappa to deploy my application, I had to understand how everything worked in order to deploy the application correctly. For example, without understanding the "serverless" aspect of AWS Lambda, I would not have had the architectural understanding required to run this application on the cloud, which would have prevented me from writing any code in the first place. In addition to architecture, I did a lot of research on databases, because I had only previously worked with SQLite which was much simpler to use as it doesn't require external database hosting. 

## Roadmap

Although the application works in its current form, it is very bare in its current form and would not be adequate in a production environment. I plan on adding bits and pieces to the application until it feels complete, however, this specific application will never be used for anything other than my own research and curiosity. My first step would be to create user authorization with access and update tokens. Although I have already done this manually in another project, I would like to utilize AWS Cognito in this specific project as I had never used the service before and would be interested in understanding how it works. I would also like to hash my passwords for the sake of completeness, however, this wouldn't be anything new. After creating security infrastructure, I would like to modify my current domain using AWS Route 53. I'm trying to use as many Amazon services as possible as the purpose of this project is to get me more familiar with AWS. Next, I would like to implement a basic frontend with React. I am currently more focused on backend development but I would also like to learn some frontend just to have the skillset. At this point, my application would feel fairly complete. Any further development would be at least a couple months in the future.


