# Facial recognition demo in python

Displays the realsense f450 frames in real time and the functions: enroll, authenticate and delete.
Elevator calls are managed by the insight API.

## Description

Added a python 3.8 VENV with all the required libraries.

The required libraries for the python version of the realsense face id are installed as well.


## Getting Started

Only available for linux based distributions, unable to configure the realsense project with windows based devices.

If the device has an ARM distro such a raspberry pi it is recommended to do the following:

1. Check the cmake version it should at least be 3.12
 ```
 cmake --version
 ```
2. Clone the RealSenseID repository and compile the required libraries
```
cd /home/$USER/Desktop && git clone http://github.com/IntelRealSense/RealSenseID.git

cd RealSenseID && mkdir build && cd build

cmake -DRSID_SAMPLES=1 -DRSID_PY=ON -DRSID_PREVIEW=ON ..

make -j 
```
2.1 Prior to compiling the compiler tools are required as well as developer tools in python.
```
sudo apt-get install python-dev

sudo apt-get install build-essential

```

3. Create the project directory by cloning the FacialRecognition folder from this project:
 ```
 cd /home/$USER/Desktop && mkdir fac_rec && cd fac_rec
 
 git init
 
 git remote add -f origin http://github.com/josedev9/Additional-scripts.git
 
 git config core.sparseCheckout true
 
 echo "FacialRecognition" >> .git/info/sparse-checkout
 
 git pull origin main
 ```
 
 4. Copy the adequate realsense libraries into this folder:
 ```
 cd /home/$USER/Desktop/RealSenseID/build/lib && cp librsid.so /home/$USER/Desktop/fac_rec/FacialRecognition && cp rsid_py*.so /home/$USER/Desktop/fac_rec/FacialRecognition
 
 ```


## Authors

Contributors names and contact info

Jose Ángel Rodríguez  

## Version History

* 0.1
    * Initial Release
