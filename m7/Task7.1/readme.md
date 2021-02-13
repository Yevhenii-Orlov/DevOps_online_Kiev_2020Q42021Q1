### Module 7 Linux administration with bash
#### TASK 7.1 

A. Create a script that uses the following keys:

1. When starting without parameters, it will display a list of possible keys and their description.

2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet

3. The --target key displays a list of open system TCP ports.
 
 ![](Screenshots/1.png) 
 
 ```bash
 #!/bin/bash

if [ $# -eq 0 ]

then

echo "--all - key displays the IP addresses and symbolic names of all hosts in the current subnet"
echo "--target - key displays a list of open system TCP ports on this device" 

else

while [ -n "$1" ]

do

case "$1" in

--all) nmap -sn 192.168.88.* | awk '/scan report for/ {$1=$2=$3=$4=""; print $0}' ;;

--target) nmap -sT 192.168.88.135 | sed '1,5d' ;;

*) echo "Please enter parametr!"
echo "--all - key displays the IP addresses and symbolic names of all hosts in the current subnet"
echo "--target - key displays a list of open system TCP ports on this device" ;;

esac

shift

done
fi
```

B. Using Apache log example create a script to answer the following questions:

1. From which ip were the most requests?

```bash
#!/bin/bash

file='elog.log';

let max=0;

for (( i=1; i <= 1000; i++ ))

do 

ip=`cat $file | awk '{print $1}' | head -n$i | tail -n1`

count=`grep $ip $file | wc -l`


if [ $count -gt $max ];

then

let max=$count;
fip=`cat $file | awk '{print $1}' | head -n$i | tail -n1`

fi

done 

echo "IP - $fip sum - $max"
```

2. What is the most requested page?

![](Screenshots/2.png) 

```bash
#!/bin/bash

file='elog.log';

let max=0;

for (( i=1; i <= 1000; i++ ))

do 

site=`cat elog.log | grep "http" | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1`

count=`grep $site $file | wc -l`


if [ $count -gt $max ];

then

let max=$count;

fsite=`cat elog.log | grep "http" | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1`

fi

done 

echo "Site - $fsite sum - $max"
```

3. How many requests were there from each ip?

![](Screenshots/3.png) 

```bash
#!/bin/bash

file='elog.log';

let max=0;

for (( i=1; i <= 1000; i++ ))

do 

ip=`cat $file | awk '{print $1}' | head -n$i | tail -n1`

count=`grep $ip $file | wc -l`

echo "IP - $ip sum - $count"

done 
```

4. What non-existent pages were clients referred to?

![](Screenshots/4.png) 

```bash
#!/bin/bash

file='elog.log';

let max=0;

for (( i=1; i <= 1000; i++ ))

do 

site=`cat $file | grep "http" | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1 | awk -F[/:] '{print $4}'`

error=`cat $file | awk '{print $9}' | head -n$i | tail -n1 `

if [ $error = "404" ];

then

echo "Site with error - $site"

fi

done 
```

5. What time did site get the most requests?

![](Screenshots/5.png) 

```bash
#!/bin/bash

file='elog.log';

let max=0;

for (( i=1; i <= 1000; i++ ))

do 

site=`cat $file | grep "http" | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1 | awk -F[/:] '{print $4}'`

rm temp;

gsite=`grep $site $file >> temp`

rm temp1

timesort=`cat temp | awk '{print $4}' | awk -F[::] '{print $2}' | sort >> temp1`

count08=`grep 08 temp1 | wc -l` 

count09=`grep 09 temp1 | wc -l` 

count10=`grep 10 temp1 | wc -l` 

count11=`grep 11 temp1 | wc -l` 

count12=`grep 12 temp1 | wc -l` 

count13=`grep 13 temp1 | wc -l` 

count=$count08
rt='more requests at 8 am'

if [ $count09 -gt $count ];

then

count=$count09
rt='more requests at 9 am'

elif  [ $count10 -gt $count ];

then

count=$count10
rt='more requests at 10 am'

elif  [ $count11 -gt $count ];

then

count=$count11
rt='more requests at 11 am'

elif  [ $count12 -gt $count ];

then

count=$count12
rt='more requests at 12 am'

elif  [ $count13 -gt $count ];

then

count=$count13
rt='more requests at 13 am'


fi

echo "$site - $rt"

done 

#cat 123.log | awk '{print $4}' | sed -e 's/^..............//;s/......$//'
#grep https://www.google.co.uz 123.log | awk '{print $4}' | sed -e 's/^..............//;s/......$//' | wc -l
```

6. What search bots have accessed the site? (UA + IP)

![](Screenshots/6.png) 

```bash
#!/bin/bash

file='elog.log';

let max=0;

m=Mail.RU_Bot;
g=Googlebot;
mm=MJ12bot;
s=SentiBot;
a=AhrefsBot;

for (( i=1; i <= 100; i++ ))

do 

ipbotm=`grep -i $m $file | awk '{print $1}' | head -n$i | tail -n1`

imailbotm=`grep -i $m elog.log | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1 | awk -F[/:] '{print $4}'`

echo "$m - $ipbotm - $imailbotm"

ipbotg=`grep -i $g $file | awk '{print $1}' | head -n$i | tail -n1`

imailbotg=`grep -i $g elog.log | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1 | awk -F[/:] '{print $4}'`

echo "$g - $ipbotg - $imailbotg"

ipbotmm=`grep -i $mm $file | awk '{print $1}' | head -n$i | tail -n1`

imailbotmm=`grep -i $mm elog.log | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1 | awk -F[/:] '{print $4}'`

echo "$mm - $ipbomm - $imailbotmm"

ipbots=`grep -i $s $file | awk '{print $1}' | head -n$i | tail -n1`

imailbots=`grep -i $s elog.log | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1 | awk -F[/:] '{print $4}'`

echo "$s - $ipbots - $imailbots"

ipbota=`grep -i $a $file | awk '{print $1}' | head -n$i | tail -n1`

imailbota=`grep -i $a elog.log | sed 's/.*\(.*http\)/\1/g' | sed 's/".*//' | head -n$i | tail -n1 | awk -F[/:] '{print $4}'`

echo "$a - $ipbota - $imailbota"

done 
```

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

```bash
#!/bin/bash

#keys

if [ $# -eq 0 ]

then

echo "Please enter parametr!"
echo "First parametr is the path to the syncing directory"
echo "Second parametr is the path to the directory where the copies" 

else

	for file in *;
	
	do 
	
	cp $file $2$file;
	
	done

inotifywait -m $1 -e create -e delete |
    
	while read dir action file; do
        
		echo "`date` - - the file '$file' was '$action'" >> logbook.log
				
			if [ $action = "CREATE" ];
			
			then
			
			cp $file $2$file;
			
			fi
			
	done

fi
```
