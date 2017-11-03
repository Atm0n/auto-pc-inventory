# Auto-pc-inventory
A usefull utility to make the work of somebody htat have to make an inventory of a big number of computers, using a docker container of a mysql server (###STILL WORKS VERY BAD###using a google spreadsheet as data base at the branch:https://github.com/Atm0n/auto-pc-inventory/tree/automatic-computer-inventory(google-spreadshet).
I've tried to use an existing platform but that was too dificult and was not what i needed, so i decided to do it in my way.
Nothing more to add. I will update this as soon i do a big change i geuss.

### ONLY LINUX!!!

# HOW TO INSTALL
## CLIENT-SIDE
At the moment you only need to download the install.sh script and it would do the work for you, **BUT you also need to change the permissions of the script and run it as root**
So i will explain it step by step.

1-Open terminal make you root
  with ubuntu
  ```
  sudo su
  ```
  with debian
  ```
  su root
  ```
2-Use cd to go where is my script downloaded
```
cd /path/to/the/downloaded/file
```
3-now we are going to change the permissions
  ```
  chmod 2744 install.sh
  ```
4-Finally you can execute the script
  ```
    ./install.sh
  ```
5-Now you would be asked to enter the configuration data (ENTER IT PLS)
## SERVER-SIDE
#### SERVER MUST HAVE A STATIC IP
1-Create a mysql server, if you don't know how, here you have a [link](http://lmgtfy.com/?q=how+to+make+a+mysql+server)

2-after having configurated the mysql server and beeing able to connect from the lan, we have to create the database and here you have a [link](https://github.com/Atm0n/auto-pc-inventory/edit/master/mysql_config)

3-Finally you have it!
