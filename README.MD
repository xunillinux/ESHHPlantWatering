
# ESHH Plant Watering

Flask App and Webinterface for a plant watering system with a Raspberry Pi 3


## Setup and Installation:

1. Install Raspbian Buster with desktop and recommended software
https://www.raspberrypi.org/downloads/raspbian/

2. Clone this repository to Raspberry Pi to /home/pi/flask

3. sudo apt-get update && sudo apt-get install nginx

4. sudo pip3 install virtualenv

5. cd flask

6. virtualenv appenv
7. source appenv/bin/activate
8. pip install uwsgi flask rpi.gpio
9. deactivate

10. cp app.service /etc/systemd/system

11. sudo systemctl start app
12. sudo systemctl enable app
13. sudo systemctl status app (should be active)

14. sudo vim /etc/nginx/sites-available/default

-> add the following to the file below the line with "server_name _;"

location /app/ {
	include uwsgi_params;
	uswgi_pass unix:/home/pi/flask/app.sock;
}


15. sudo reboot

16. sudo cp /home/pi/flask/www/* /var/www/html



