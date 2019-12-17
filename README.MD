
# ESHH Plant Watering

Flask App and Webinterface for a plant watering system with a Raspberry Pi 3


## Setup and Installation:

### Raspberry Pi

1. Install Raspbian Buster with desktop and recommended software
https://www.raspberrypi.org/downloads/raspbian/

### Nginx and Flask

2. Clone this repository to Raspberry Pi to /home/pi/

2.5 Rename repo folder from "ESHHPlantWatering" to "flask"
(this is because I couldn't be bothered to change all the config file paths for wsgi nginx and so on)

3. sudo apt-get update && sudo apt-get install nginx

4. sudo pip3 install virtualenv

5. cd flask

6. virtualenv appenv
7. source appenv/bin/activate
8. pip3 install uwsgi flask rpi.gpio
9. deactivate

10. cp app.service /etc/systemd/system

11. sudo systemctl start app
12. sudo systemctl enable app
13. sudo systemctl status app (should be active)

14. sudo vim /etc/nginx/sites-available/default

-> add the following to the file below the line with "server_name _;"

location /app/ {
	include uwsgi_params;
	uwsgi_pass unix:/home/pi/flask/app.sock;
}


15. sudo reboot

16. sudo cp -r /home/pi/flask/dashboard/* /var/www/html

### MariaDB

(GUIDE: https://pimylifeup.com/raspberry-pi-mysql/)

17. sudo apt-get install mariadb-server

18. sudo mysql_secure_installation

19. sudo mysql -u root -p

20. (in mariadb cli) source /home/pi/flask/sql/init.sql

21 use plantwateringdb;

22. (in mariadb cli) source /home/pi/flask/sql/createtables.sql

23. exit

24. pip3 install mysql-connector-python-rf

24.1 (in flask dir) source appenv/bin/activate

24.2 (in flask dir) pip3 install mysql-connector-python-rf

24.3 (in flask dir) deactivate

25. python3 /home/pi/flask/sql/dbtest.py

if correctly setup it should print Id: 1, Water Amount: 42

### SpiDev Installation

26. cd

27. wget https://github.com/doceme/py-spidev/archive/master.zip 

28. unzip master.zip

29. cd py-spidev-master

30. sudo python3 setup.py install

30.1 (in flask dir) source appenv/bin/activate

30.2 (in flask dir) pip3 install spidev

30.3 (in flask dir) deactivate

### Configure SPI

31. sudo raspi-config

32. interfaces -> SPI -> activate

33. sudo reboot

### Configure Camera

34. sudo raspi-config

35. Interfaces -> Activate Camera

36. sudo reboot

### Python Libraries (Adafruit)

37. cd /home/pi/flask/libraries/Adafruit_Python_DHT

38. sudo python3 setup.py install

38.1 (in flask dir) source appenv/bin/activate

38.2 (in flask dir) pip3 install Adafruit_DHT

38.3 (in flask dir) deactivate


