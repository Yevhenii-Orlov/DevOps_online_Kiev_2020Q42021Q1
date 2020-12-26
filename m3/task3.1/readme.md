### Module 3 Database Administration
#### PART 1

1. Installing MySQL Server.

```bash
ubuntu@ip-172-31-5-131:~$ sudo apt install mysql-server

...

ubuntu@ip-172-31-5-131:~$ sudo mysql_secure_installation

Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD PLUGIN can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD plugin?

Press y|Y for Yes, any other key for No: y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 2
Please set the password for root here.

New password:

Re-enter new password:

Estimated strength of the password: 50
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
Success.

By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : no

 ... skipping.
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
Success.

All done!
```
2. Database schema.

![](Screenshots/Untitled%20Diagram.png)

3. First start. Creation \ Removal of the base. Creation of tables and their filling. Executing SELECT operator with WHERE, GROUP BY and ORDER BY and other different SQL queries DDL, DML, DCL.

```bash
ubuntu@ip-172-31-5-131:~$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.7.32-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> Status
--------------
mysql  Ver 14.14 Distrib 5.7.32, for Linux (x86_64) using  EditLine wrapper

Connection id:          6
Current database:       Students
Current user:           root@localhost
SSL:                    Not in use
Current pager:          stdout
Using outfile:          ''
Using delimiter:        ;
Server version:         5.7.32-0ubuntu0.18.04.1 (Ubuntu)
Protocol version:       10
Connection:             Localhost via UNIX socket
Server characterset:    latin1
Db     characterset:    latin1
Client characterset:    utf8
Conn.  characterset:    utf8
UNIX socket:            /var/run/mysqld/mysqld.sock
Uptime:                 1 hour 26 min 1 sec

Threads: 1  Questions: 42  Slow queries: 0  Opens: 120  Flush tables: 1  Open tables: 113  Queries per second avg: 0.008
--------------

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> CREATE DATABASE KievDevOps;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| KievDevOps         |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> drop database KievDevOps;
Query OK, 0 rows affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> create databases WEB_Movies;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'databases WEB_Movies' at line 1

mysql> create database WEB_Movies;
Query OK, 1 row affected (0.00 sec)

mysql> use WEB_Movies;
Database changed

mysql> Create table Movies(Id INTEGER PRIMARY KEY, MovieName VARCHAR(252), Country VARCHAR(63), Genre VARCHAR(255), Movielehgth INTEGER, Budget DECIMAL, Rating DECIMAL);
Query OK, 0 rows affected (0.06 sec)

mysql> CREATE TABLE Cinemas (Id INTEGER PRIMARY KEY, CinemaAddress VARCHAR(255));
Query OK, 0 rows affected (0.10 sec)

mysql> CREATE TABLE CinemaHalls (Id INTEGER PRIMARY KEY, HallName VARCHAR(127), Technology VARCHAR(127));
Query OK, 0 rows affected (0.02 sec)

mysql> CREATE TABLE MovieSessions (Id INTEGER PRIMARY KEY, DATE INTEGER, Category VARCHAR(127), Cost DECIMAL);
Query OK, 0 rows affected (0.02 sec)

mysql> INSERT Movies(Id, MovieName, Country, Genre, Movielehgth, Budget, Rating) VALUES ('1', 'Inseption', 'USA', 'Adventure', '5', '10000', '10');
Query OK, 1 row affected (0.01 sec)
```

![](Screenshots/Screenshot%20(88).png)

![](Screenshots/Screenshot%20(90).png)

![](Screenshots/Screenshot%20(89).png)

![](Screenshots/Screenshot%20(91).png)

![](Screenshots/Screenshot%20(92).png)

4. Create new users for the database.

![](Screenshots/Screenshot%20(93).png)

![](Screenshots/Screenshot%20(94).png)

5. Checking the availability of content to users.

![](Screenshots/Screenshot%20(95).png)

6. Selecting and viewing the embedded MySQL database table "mysql".

![](Screenshots/Screenshot%20(96).png)

![](Screenshots/Screenshot%20(97).png)

#### PART 2

7. Backup of my database and dropping a table.

```bash
ubuntu@ip-172-31-5-131:~$ mysqldump -u orlovevg -p WEB_Movies > Movies.sql
Enter password:

ubuntu@ip-172-31-5-131:~$ ls
Movies.sql

ubuntu@ip-172-31-5-131:~$ mysql -u orlovevg -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 5.7.32-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> USE WEB_Movies
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+----------------------+
| Tables_in_WEB_Movies |
+----------------------+
| CinemaHalls          |
| Cinemas              |
| MovieSessions        |
| Movies               |
+----------------------+
4 rows in set (0.00 sec)

mysql> DROP TABLES Cinemas;
Query OK, 0 rows affected (0.01 sec)

mysql> SHOW TABLES;
+----------------------+
| Tables_in_WEB_Movies |
+----------------------+
| CinemaHalls          |
| MovieSessions        |
| Movies               |
+----------------------+
3 rows in set (0.00 sec)
```

8. Restore my database.

![](Screenshots/Screenshot%20(99).png)

9. Transfer my local database to RDS AWS and connecting to it.

![](Screenshots/Screenshot%20(100).png)

![](Screenshots/Screenshot%20(104).png)

```bash
ubuntu@ip-172-31-5-131:~$ mysql -h webmovies1.cbtsf8bftxdz.us-west-2.rds.amazonaws.com -P 3306 -u orlovevg -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 25
Server version: 5.7.31-log Source distribution

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database WEB_Movies;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| WEB_Movies         |
| innodb             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql> exit;
Bye

ubuntu@ip-172-31-5-131:~$ mysql -h webmovies1.cbtsf8bftxdz.us-west-2.rds.amazonaws.com -P 3306 -u orlovevg -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 27
Server version: 5.7.31-log Source distribution

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use WEB_Movies
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

mysql> show tables;
+----------------------+
| Tables_in_WEB_Movies |
+----------------------+
| CinemaHalls          |
| Cinemas              |
| MovieSessions        |
| Movies               |
+----------------------+
4 rows in set (0.01 sec)
```

10. Dumping my database.

![](Screenshots/Screenshot%20(106).png)

```bash
ubuntu@ip-172-31-5-131:~$ mysqldump -u orlovevg -h webmovies1.cbtsf8bftxdz.us-west-2.rds.amazonaws.com -P 3306 -p WEB_Movies > MoviesRDS.sql

Enter password:

'Warning: A partial dump from a server that has GTIDs will by default include the GTIDs of all transactions, even those that changed suppressed parts of the database. If you don`t want to restore GTIDs, pass --set-gtid-purged=OFF. To make a complete dump, pass --all-databases --triggers --routines --events'

ubuntu@ip-172-31-5-131:~$ mysqldump -u orlovevg -h webmovies1.cbtsf8bftxdz.us-west-2.rds.amazonaws.com -P 3306 -p WEB_Movies > MoviesRDS.sql --all-databases --triggers -                                     -routines --events

ubuntu@ip-172-31-5-131:~$ ls
Movies.sql  MoviesRDS.sql
```

#### PART 3

11. Creating an Amazon DynamoDB table and entering data into an Amazon DynamoDB table.

![](Screenshots/Screenshot%20(108).png)

![](Screenshots/Screenshot%20(109).png)

12. Query an Amazon DynamoDB table using Scan option.

![](Screenshots/Screenshot%20(111).png)

![](Screenshots/Screenshot%20(112).png)

![](Screenshots/Screenshot%20(113).png)

![](Screenshots/Screenshot%20(114).png)

![](Screenshots/Screenshot%20(115).png)

13. Query an Amazon DynamoDB table using Query option.

![](Screenshots/Screenshot%20(116).png)

![](Screenshots/Screenshot%20(117).png)

![](Screenshots/Screenshot%20(118).png)
