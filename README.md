Self-Adaptive-Captcha
=====================

This project is a self-adaptive Captcha platform that provides several CAPTCHAs from different platforms according the user's environment and the perceived risk of attacks.

Python 2.7, Flask and SQLite3 are required to run our platform.

The demo folder contains a SAC folder which is our library written in PHP that communicate with our API.
The choice of PHP to implement our API has been made for showing that our API can be used with any language as it works by webservice and HTTP requests.
The index.php file is here as example for showing how our library can be used. You need an apache server to run it.
