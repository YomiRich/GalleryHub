# GalleryHub

## Description
This is a gallery application that enables users to view images in the gallery and the image details. For instance, the location the image was taken. They can also share images in the application by copying and pasting the image link to friends and families.

#### By *YomiRich*

The user can:
* See various photos
* View photos by location/category
* Copy link to the photo
* View image details
## Setup/Installation Requirements
### Prerequisites
django 1.11.8
* python3.6
* pip
* Virtual environment(virtualenv)

### Cloning and running
* Clone the application using git clone(this copies the app onto your device). In terminal:

          * git clone https://github.com/YomiRich/GalleryHub.git
          * cd GalleryHub

* Creating the virtual environment

          * python3.6 -m venv --without-pip virtual
          * source virtual/bin/env
          * curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

 * python3.6 -m pip install -r requirements.txt

* Run the application:
        
 * python3 manage.py runserver  
          
### Testing the Application
* To run the tests for the class files:

* python3.6 manage.py test

## Technologies Used
* Python 3.6
* Django1.11.8 

## Behaviour driven development/ Specifications

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| Display Photos | On page load | List of various photos taken |
| Display Photos Details | On click photo | List of photos details |
| Display Photos Based on Location | On location | List of photos taken on that location |
| Display Photos Based on Category | On search photo category | List of photos on that category |
| Copy photo link to clipboard | On click copy | Copy photo link |

## Support and contact details
* Email: ymueni@gmail.com

### License
MIT License
Copyright (c) {2019} (YomiRich) 
[https://github.com/YomiRich/LICENSE/blob/master/LICENSE]
