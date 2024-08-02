# ssh_logger
Log of all ssh conections 

# Info 
it works by reading lines form /var/log/auth.log outputs it in a nice format,
and prints the date and the location of the ip adress.



install and run
----------
```
git clone https://github.com/mkn025/ssh_logger.git
cd ssh_logger
sudo pyhton3 main.py
```


install using and run using screen
----------
screen will make it run in the background 
```
git clone https://github.com/mkn025/ssh_logger.git
cd ssh_logger
sudo apt install screen
screen -S ssh_logger
sudo pyhton3 main.py
ctrl + a
ctrl + d 
```

Reattach to the screen
----------
```
screen -R ssh_logger
```
