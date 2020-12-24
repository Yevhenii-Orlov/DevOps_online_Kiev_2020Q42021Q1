### Module 3 Database Administration
#### PART 1

1. Installing MySQL Server.

```bash
ubuntu@ip-172-31-5-131:~$ sudo apt install mysql-server
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libaio1 libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-6 li
  libhtml-parser-perl libhtml-tagset-perl libhtml-template-perl libhttp-date-perl libh
  libio-html-perl liblwp-mediatypes-perl libtimedate-perl liburi-perl mysql-client-5.7
  mysql-client-core-5.7 mysql-common mysql-server-5.7 mysql-server-core-5.7
Suggested packages:
  libdata-dump-perl libipc-sharedcache-perl libwww-perl mailx tinyca
The following NEW packages will be installed:
  libaio1 libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-6 li
  libhtml-parser-perl libhtml-tagset-perl libhtml-template-perl libhttp-date-perl libh
  libio-html-perl liblwp-mediatypes-perl libtimedate-perl liburi-perl mysql-client-5.7
  mysql-client-core-5.7 mysql-common mysql-server mysql-server-5.7 mysql-server-core-5
0 upgraded, 21 newly installed, 0 to remove and 50 not upgraded.
Need to get 19.7 MB of archives.
After this operation, 157 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 mysql-common al
Get:2 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libaio1.1 [6476 B]
Get:3 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 mysql-c7.32-0ubuntu0.18.04.1 [6660 kB]
Get:4 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 mysql-c0ubuntu0.18.04.1 [1943 kB]
Get:5 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 mysql-s7.32-0ubuntu0.18.04.1 [7455 kB]
Get:6 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libevent-core-2-4build1 [85.9 kB]
Get:7 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 mysql-s0ubuntu0.18.04.1 [2935 kB]
Get:8 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libhtml-tagset-B]
Get:9 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 liburi-perl all
Get:10 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libhtml-parser1 [85.9 kB]
Get:11 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libcgi-pm-perl
Get:12 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libfcgi-perl a kB]
Get:13 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libcgi-fast-pe]
Get:14 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libencode-loca3 kB]
Get:15 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libhtml-templa0 kB]
Get:16 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libtimedate-peB]
Get:17 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libhttp-date-p]
Get:18 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libio-html-per
Get:19 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 liblwp-mediaty.7 kB]
Get:20 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libhttp-messag kB]
Get:21 http://us-west-2.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 mysql-tu0.18.04.1 [9944 B]
Fetched 19.7 MB in 1s (34.5 MB/s)
Preconfiguring packages ...
Selecting previously unselected package mysql-common.
(Reading database ... 57090 files and directories currently installed.)
Preparing to unpack .../0-mysql-common_5.8+1.0.4_all.deb ...
Unpacking mysql-common (5.8+1.0.4) ...
Selecting previously unselected package libaio1:amd64.
Preparing to unpack .../1-libaio1_0.3.110-5ubuntu0.1_amd64.deb ...
Unpacking libaio1:amd64 (0.3.110-5ubuntu0.1) ...
Selecting previously unselected package mysql-client-core-5.7.
Preparing to unpack .../2-mysql-client-core-5.7_5.7.32-0ubuntu0.18.04.1_amd64.deb ...
Unpacking mysql-client-core-5.7 (5.7.32-0ubuntu0.18.04.1) ...
Selecting previously unselected package mysql-client-5.7.
Preparing to unpack .../3-mysql-client-5.7_5.7.32-0ubuntu0.18.04.1_amd64.deb ...
Unpacking mysql-client-5.7 (5.7.32-0ubuntu0.18.04.1) ...
Selecting previously unselected package mysql-server-core-5.7.
Preparing to unpack .../4-mysql-server-core-5.7_5.7.32-0ubuntu0.18.04.1_amd64.deb ...
Unpacking mysql-server-core-5.7 (5.7.32-0ubuntu0.18.04.1) ...
Selecting previously unselected package libevent-core-2.1-6:amd64.
Preparing to unpack .../5-libevent-core-2.1-6_2.1.8-stable-4build1_amd64.deb ...
Unpacking libevent-core-2.1-6:amd64 (2.1.8-stable-4build1) ...
Setting up mysql-common (5.8+1.0.4) ...
update-alternatives: using /etc/mysql/my.cnf.fallback to provide /etc/mysql/my.cnf (my
Selecting previously unselected package mysql-server-5.7.
(Reading database ... 57258 files and directories currently installed.)
Preparing to unpack .../00-mysql-server-5.7_5.7.32-0ubuntu0.18.04.1_amd64.deb ...
Unpacking mysql-server-5.7 (5.7.32-0ubuntu0.18.04.1) ...
Selecting previously unselected package libhtml-tagset-perl.
Preparing to unpack .../01-libhtml-tagset-perl_3.20-3_all.deb ...
Unpacking libhtml-tagset-perl (3.20-3) ...
Selecting previously unselected package liburi-perl.
Preparing to unpack .../02-liburi-perl_1.73-1_all.deb ...
Unpacking liburi-perl (1.73-1) ...
Selecting previously unselected package libhtml-parser-perl.
Preparing to unpack .../03-libhtml-parser-perl_3.72-3build1_amd64.deb ...
Unpacking libhtml-parser-perl (3.72-3build1) ...
Selecting previously unselected package libcgi-pm-perl.
Preparing to unpack .../04-libcgi-pm-perl_4.38-1_all.deb ...
Unpacking libcgi-pm-perl (4.38-1) ...
Selecting previously unselected package libfcgi-perl.
Preparing to unpack .../05-libfcgi-perl_0.78-2build1_amd64.deb ...
Unpacking libfcgi-perl (0.78-2build1) ...
Selecting previously unselected package libcgi-fast-perl.
Preparing to unpack .../06-libcgi-fast-perl_1%3a2.13-1_all.deb ...
Unpacking libcgi-fast-perl (1:2.13-1) ...
Selecting previously unselected package libencode-locale-perl.
Preparing to unpack .../07-libencode-locale-perl_1.05-1_all.deb ...
Unpacking libencode-locale-perl (1.05-1) ...
Selecting previously unselected package libhtml-template-perl.
Preparing to unpack .../08-libhtml-template-perl_2.97-1_all.deb ...
Unpacking libhtml-template-perl (2.97-1) ...
Selecting previously unselected package libtimedate-perl.
Preparing to unpack .../09-libtimedate-perl_2.3000-2_all.deb ...
Unpacking libtimedate-perl (2.3000-2) ...
Selecting previously unselected package libhttp-date-perl.
Preparing to unpack .../10-libhttp-date-perl_6.02-1_all.deb ...
Unpacking libhttp-date-perl (6.02-1) ...
Selecting previously unselected package libio-html-perl.
Preparing to unpack .../11-libio-html-perl_1.001-1_all.deb ...
Unpacking libio-html-perl (1.001-1) ...
Selecting previously unselected package liblwp-mediatypes-perl.
Preparing to unpack .../12-liblwp-mediatypes-perl_6.02-1_all.deb ...
Unpacking liblwp-mediatypes-perl (6.02-1) ...
Selecting previously unselected package libhttp-message-perl.
Preparing to unpack .../13-libhttp-message-perl_6.14-1_all.deb ...
Unpacking libhttp-message-perl (6.14-1) ...
Selecting previously unselected package mysql-server.
Preparing to unpack .../14-mysql-server_5.7.32-0ubuntu0.18.04.1_all.deb ...
Unpacking mysql-server (5.7.32-0ubuntu0.18.04.1) ...
Setting up libhtml-tagset-perl (3.20-3) ...
Setting up libevent-core-2.1-6:amd64 (2.1.8-stable-4build1) ...
Setting up libencode-locale-perl (1.05-1) ...
Setting up libtimedate-perl (2.3000-2) ...
Setting up libio-html-perl (1.001-1) ...
Setting up liblwp-mediatypes-perl (6.02-1) ...
Setting up libaio1:amd64 (0.3.110-5ubuntu0.1) ...
Setting up liburi-perl (1.73-1) ...
Setting up libhtml-parser-perl (3.72-3build1) ...
Setting up libcgi-pm-perl (4.38-1) ...
Setting up mysql-client-core-5.7 (5.7.32-0ubuntu0.18.04.1) ...
Setting up libfcgi-perl (0.78-2build1) ...
Setting up libhttp-date-perl (6.02-1) ...
Setting up libhtml-template-perl (2.97-1) ...
Setting up mysql-server-core-5.7 (5.7.32-0ubuntu0.18.04.1) ...
Setting up libcgi-fast-perl (1:2.13-1) ...
Setting up libhttp-message-perl (6.14-1) ...
Setting up mysql-client-5.7 (5.7.32-0ubuntu0.18.04.1) ...
Setting up mysql-server-5.7 (5.7.32-0ubuntu0.18.04.1) ...
update-alternatives: using /etc/mysql/mysql.cnf to provide /etc/mysql/my.cnf (my.cnf)
Renaming removed key_buffer and myisam-recover options (if present)
Created symlink /etc/systemd/system/multi-user.target.wants/mysql.service > /lib/syste.
Setting up mysql-server (5.7.32-0ubuntu0.18.04.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...
Processing triggers for systemd (237-3ubuntu10.42) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...

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
