# Logs Analysis Project

## Technologies used
This project create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Technologies used
1. PostgreSQL
2. Writing Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant

## Project Requirements
What are we reporting:
1. What are the most popular three articles of all time?

- Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time?

- when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors?

- The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser


Style Requirements:
* Project follows good SQL coding practices 
* The code is error free and conforms to the PEP8 style recommendations.
* The code presents its output in clearly formatted plain text.

## System setup
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

#### Installing the dependencies and setting up the files:
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install.
3. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.
4. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 

* Unzip the data to get the newsdata.sql file.
* Put the newsdata.sql file into the vagrant directory

5. Clone this repository to a directory of your choice.


#### Start the Virtual Machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` command to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/log_analysis ```

## Views used in this project
#### Error view:
to get the number of error by day
````sql
CREATE VIEW error as
SELECT date_trunc('day', time) "day", COUNT(*) AS errors
FROM log
WHERE status LIKE '404%'
GROUP BY day;
````
#### Total view:
to get the total number of requests by day

````sql
CREATE VIEW total as
SELECT date_trunc('day', time) "day", COUNT(*) AS total
FROM log
GROUP BY day;
````


## The output should be something like this: 
````
What are the most popular three articles of all time?

------------------------------------------------------------
Candidate is jerk, alleges rival - 338647
Bears love berries, alleges bear - 253801
Bad things gone, say good people - 170098


Who are the most popular article authors of all time? 
------------------------------------------------------------
Ursula La Multa - 507594
Rudolf von Treppenwitz - 423457
Anonymous Contributor - 170098
Markoff Chaney - 84557


days did more than 1% of requests lead to errors: 
------------------------------------------------------------
JUL 17, 2016 - 2.26 %
````
## Helpful Resources you can see

* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)