### Module 5 Linux Essentials
#### TASK 5.2

1.1 The structure of the /etc/passwd.

/etc/passwd file stores essential information, which required during login. In other words, it stores user account information. The /etc/passwd is a plain text file. It contains a list of the system’s accounts, giving for each account some useful information like user ID, group ID, home directory, shell, and more. The /etc/passwd file should have general read permission as many command utilities use it to map user IDs to user names. However, write access to the /etc/passwd must only limit for the superuser/root account.

 ![](Screenshots/1.png)

/etc/passwd Format

	- Username: It is used when user logs in. It should be between 1 and 32 characters in length.

	- Password: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to computes the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file.

	- User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.

	- Group ID (GID): The primary group ID (stored in /etc/group file)

	- User ID Info: The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.

	- Home directory: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /

	- Command/shell: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell. For example, sysadmin can use the nologin shell, which acts as a replacement shell for the user accounts. If shell set to /sbin/nologin and the user tries to log in to the Linux system directly, the /sbin/nologin shell closes the connection.

The list of users in the system:

![](Screenshots/3.png)

The users have ‘nologin’ at the end of their line. This means that these users cannot login to the system. These users are referred as pseudo-users.

Generally, a normal user has UID greater or equal to 1000. This means the user with UID >=1000 is a normal user and users with UID less than 1000 are system users.

1.2 The structure of the /etc/group.

/etc/group is a text file which defines the groups to which users belong under Linux and UNIX operating system. Under Unix / Linux multiple users can be categorized into groups. Unix file system permissions are organized into three classes, user, group, and others.

![](Screenshots/2.png)

/etc/group Format

	- Group: It is the name of group. If you run ls -l command, you will see this name printed in the group field.
	
	- Password: Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups.
	
	- Group ID (GID): Each user must be assigned a group ID. You can see this number in your / etc/ passwd file.
	
	- Group List: It is a list of user names of users who are members of the group. The user names, must be separated by commas.

2. What are the uid ranges? What is UID? How to define it?

A UID (user identifier) is a number assigned by Linux to each user on the system. This number is used to identify the user to the system and to determine which system resources the user can access.

This can be found by the UID stored in the / etc / passwd file. This is the same file that can be used to list all the users in a Linux system.

![](Screenshots/1.png)

Most Linux distributions reserve UIDs 1-500 for system users. On Ubuntu and Fedora, the UID for new users starts at 1000.

	- UID 0 (zero) is reserved for the root.
	
	- UIDs 1–99 are reserved for other predefined accounts.
	
	- UID 100–999 are reserved by system for administrative and   system accounts/groups.
	
	- UID 1000–10000 are occupied by applications account.
	
	- UID 10000+ are used for user accounts.

3. What is GID? How to define it?

A group identifier, often abbreviated to GID, is a numeric value used to represent a specific group. The range of values for a GID varies amongst different systems; at the very least, a GID can be between 0 and 32,767, with one restriction: the login group for the superuser must have GID 0. This numeric value is used to refer to groups in the /etc/passwd and /etc/group files or their equivalents. 

![](Screenshots/2.png)

Groups in Linux are defined by GIDs (group IDs).

	- GID 0 (zero) is reserved for the root group.
	- GID 1–99 are reserved for the system and application use.
	- GID 100+ allocated for the user’s group.

4. How to determine belonging of user to the specific group?

Use the "groups <username>" comand we can define which groups the user is in.

![](Screenshots/4.png)

5. What are the commands for adding a user to the system?

There are two commands for creating a user:

	adduser - this is not a standard Linux command. It’s essentially a Perl script that uses the useradd command in the background. This high-level utility is more efficient in properly creating new users on Linux. Default parameters for all new users can also be set through the adduser command.	
	
![](Screenshots/5.png)	
	
	useradd - This command adds an entry to / etc / passwd but does not create a home directory. Also, this user, according to the / etc / passwd, has a password that has not been set. User1's settings can be changed by editing /etc/login.defs.
	
![](Screenshots/6.png)	

![](Screenshots/7.png)	

The main parameters:

	 username is the login name of the user. This is the only required parameter in all commands.
	
	 uid comment is an additional comment about the user with the specified name.
	
	 dir - indicates to the user's home directory.

	 expire - indicates the exact date untill registration record are availble .

	 inactive - indicates a continuous number of days without registration in the system before this record is blocked.
	
	 gid - defines the id or name of the group to which the user belongs.
	
	 new_username - Replaces the old login name.

	 shell - defines the shell for the command interpreter for the given user.

	 skel_dir - contains files which must be copied to the new user's home directory.
	 uid - this is the unique user identifier associated with this name.

	 -m - indicates need to create a new home directory (useradd) or move the current one to a new location (usermod).
	
	 -o - Allows repeating the same user ID.

	-g - Select the main group for the login name.

	-G - selects additional groups.

	-r - Tells the user's home directory to be moved. If the home directory for the registration entry is out of date, existing files will be migrated to the new directory.
	
6. How do I change the name (account name) of an existing user?

The username on the system can be changed using the usermod command. To change the username, you must use the username command with the -l parameter.

![](Screenshots/8.png)	

7. 