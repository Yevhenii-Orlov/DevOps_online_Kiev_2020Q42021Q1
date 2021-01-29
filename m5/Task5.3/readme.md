### Module 5 Linux Essentials
#### TASK 5.3

1. How many states could has a process in Linux?

Depending on various circumstances, the state of the process during operation may change. In Linux, a process can be in the following states:

		Running: This is a state where a process is either in running or ready to run.
		
		Interruptible: This state is a blocked state of a process which awaits for an event or a signal from another process
		
		Uninterruptible: It is also a blocked state. The process is forced to halt for certain condition that a hardware status is waited and a signal could not be handled.

		Stopped: Once the process is completed, this state occurs. This process can be restarted

		Zombie: In this state, the process will be terminated and the information will still be available in the process table.
		
2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.

The pstree command is similar to ps , but instead of listing the running processes, it shows them in a tree. The tree-like format is a more convenient way to display the processes hierarchy and makes the output more visually appealing.

The general syntax for the pstree command:

		$ pstree [OPTIONS] [USER OR PID]

 ![](Screenshots/1.png)
 
 The top item in the tree is the parent process for all system processes. In this case, it is *systemd*, the first process to start at boot.
*pstree* concatenates identical branches by enclosing them in square brackets and preceding them with an integer representing the number of branches. 

The -t option show the full threads names. If we want to hide threads and show only processes use the -T option.

 ![](Screenshots/2.png)
 
 The -p option instructs pstree to show the PIDs:
 
 ![](Screenshots/3.png)
 
 The -n option tells pstree to use numeric sort, i.e. sort by PIDs:
 
 ![](Screenshots/4.png)
 
 The process group ID or PGIDs is the process ID of the first member of the process group. To view PGIDs use the -g option:
 
 ![](Screenshots/5.png) 
 
 To view how the process was started, use the command together with the -a option:
 
 ![](Screenshots/6.png) 
 
 *pstree* also allows you to highlight processes for better visual representation.
The -h option instructs pstree to highlight the current process and all its ancestors.

 ![](Screenshots/7.png) 
 
 For example, the Teams process, PID 3179:
 
 ![](Screenshots/8.png) 
 
 3. What is a proc file system?
 
 Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down.

It contains the useful information about the processes that are currently running, it is regarded as control and information centre for kernel.

The *proc* file system also provides communication medium between kernel space and user space.

To display information about processes using the *proc* command, enter the command:

		$ ls /proc
		
 ![](Screenshots/9.png) 
 
 When using the -l switch in the ls command, processes are highlighted in different colors.
 
  ![](Screenshots/12.png) 
 
		Blue – The blue part of the output represents sub-directories.
		
		White – The files that are uncolored are normal files containing data.
		
		Cyan – The cyan colored files are symbolic links.
		
Given the PID of a process, you can view its contents with the *ls /proc/PID* command.

![](Screenshots/13.png) 

View the status using the *cat /proc/PID/status* command.

![](Screenshots/14.png) 
 
 4. Print information about the processor (its type, supported technologies, etc.).
 
 The easiest way to do this is to display the contents of the virtual */proc/cpuinfo* file.
 
 		$ less /proc/cpuinfo
 
 ![](Screenshots/10.png) 
 
 Or use the *lscpu* command:
 
 ![](Screenshots/11.png) 
 
 5. Use the ps command to get information about the process.
 
 *ps -aux* command displays a detailed list of processes by user, PID, etc.
 
 ![](Screenshots/15.png) 
 
 Displaying process tree by user *yevhenii*:
 
  ![](Screenshots/16.png) 
  
  
 6. 