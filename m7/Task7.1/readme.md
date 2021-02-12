### Module 7 Linux administration with bash
#### TASK 7.1 

A. Create a script that uses the following keys:

1. When starting without parameters, it will display a list of possible keys and their description.

2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet

3. The --target key displays a list of open system TCP ports.
 
 ![](Screenshots/1.png) 

B. Using Apache log example create a script to answer the following questions:

1. From which ip were the most requests?

2. What is the most requested page?

![](Screenshots/2.png) 

3. How many requests were there from each ip?

![](Screenshots/3.png) 

4. What non-existent pages were clients referred to?

![](Screenshots/4.png) 

5. What time did site get the most requests?

![](Screenshots/5.png) 

6. What search bots have accessed the site? (UA + IP)

![](Screenshots/6.png) 

C. Create a data backup script that takes the following data as parameters:

1. Path to the syncing directory.

2. The path to the directory where the copies of the files will be stored.

In case of adding new or deleting old files, the script must add a corresponding entry to the log file
indicating the time, type of operation and file name. [The command to run the script must be added to
crontab with a run frequency of one minute]

Initial view of the folder:

![](Screenshots/7.png)

Executing a script:

![](Screenshots/8.png)

Creating and deleting files:

![](Screenshots/9.png) 

Resault:

![](Screenshots/10.png) 

Logbook.log file:

![](Screenshots/11.png) 
