# Colour Classifier - Python

This algorithm can be used to classify an RGB code to it's named colour, key features include:
* Written in Python
* Processing data from CSV file
* 1 Nearest Neighbour Classification using Euclidian Distance

This project was first written in Swift for an iOS app developed for my A Level CS course, it has been modified to run as a Python algorithm for this repository.

# Flask Web App

This project is hosted as a Flask web app [here](https://jtom03.pythonanywhere.com/)

# Flask API

This project is accessible as an API by calling the following with appropriate variables:
https://jtom03.pythonanywhere.com/api?red=0&green=0&blue=0

The JSON response will come back with a 'colourName' variable if the call was a success and 'error' otherwise.
