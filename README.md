# Additional-scripts
Additional scripts for raspberry pi config

TODO

<p align="center">
    <b>Information about how to clone a single file from a git repository</b><br>
  <b>https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository</b> 
  <br><br>
</p>


---------------------------------------------------------READ BEFORE LAUNCHING THE SCRIPTS--------------------------------------------

The configure_systemd script allows the user to create a service which will be run from the systemd once the raspberry pi has booted. In this script the user can specify the python directory in which the additional libraries are installed, the service name, and the path in which the python script is located.

The wifi_configuration script creates a wifi gateway with the raspberry, wifi connection should be available beforehand, the user can specify the static IP the subnet mask, the wifi name and the required password
