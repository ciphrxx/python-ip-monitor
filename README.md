# 🛡️ Python Mini Network Monitoring Script





### A simple Python script that monitors outgoing connections and alerts you if any blocked IPs are detected.







---







#### Features

###### 

\- Monitors your computer's active internet connections

\- Detects connections to specific blocked IP addresses

\- Logs alerts to a text file

\- Runs continuously and prints live alerts to the console

###### 



---







#### Use Case



This tool can help you quickly detect if your system connects to specific IP addresses, which can be useful for spotting unwanted connections, testing software behavior, or tracking outbound traffic during security analysis. It's not a full firewall, but a lightweight monitoring script that gives you better visibility into your system’s network activity. Ideal for students, ethical hackers, or anyone learning how to apply Python in real-world cybersecurity scenarios.







---







#### Technologies Used

###### 

[psutil](https://pypi.org/project/psutil/) — For accessing system-level network info

###### 





---







#### How to Run

###### 

First, install the required Python library by opening a terminal and running the command '**pip install psutil**'. This only needs to be done once.



Next, open the script file named ip\_monitor.py and look for the line that says **blacklisted\_ips = {...}**. This is where you add the IP addresses you want to monitor. If you only want to watch one IP, for example Google DNS, write it like this:



**blacklisted\_ips = {"8.8.8.8"}**



If you want to monitor more than one IP, separate them with commas inside the curly brackets, like this:



**blacklisted\_ips = {"8.8.8.8", "1.1.1.1"}**



If you don’t know the IP address of a website, you can find it by using the '**ping**' command in the terminal. For example, run '**ping youtube.com**' and it will show you the IP address. Copy that IP and insert it into the **blacklisted\_ips** line in the script.



Once you’ve added the IPs, save the file and run the script by opening a terminal, navigating to the folder where the script is saved, and typing:

**python ip\_monitor.py**



The script will keep monitoring your network, and if your computer connects to one of the blacklisted IPs, it will display a warning message in the terminal. 



It also saves every detection in a file called **ip\_monitor\_log.txt**, which is created automatically in the same folder.







---







#### Customize



In **ips\_monitor.py**, edit **blacklisted\_ips** to add the IPs you want to monitor. 



You can test it by pinging those IPs or visiting websites that use them.







---







#### Output



All detected IPs are logged to **ip\_monitor\_log.txt**. 



Each IP is logged once per detection, per loop cycle.







---







#### License



This project is licensed under the MIT License.



See the [LICENSE](./LICENSE) file for full details.



Copyright (c) 2025 Daniel Goropceanu







---







#### Author



Built by Daniel Goropceanu ([@ciphrxx](https://github.com/ciphrxx))







---

