#! /bin/bash
# Ask the user the service name and the path
#sudo dpkg-reconfigure tzdata interesting to resync time with local time
echo WARNING: THE WATCHDOG HAS BEEN DEACTIVATED BY DEFAULT IF THE WATHDOG IS REQUIRED AFTER EXITING THE SCRIPT GO TO \'sudo nano /lib/systemd/system/service_name.service\' AND ACTIVATE IT
read -p 'servicename (without .service): ' service
read -p 'python script? (1/0) : ' check_python


if [[ "$check_python" -eq 1 ]]; then
	read -p 'set the python path /example: /usr/bin/python : ' path
	read -p 'set the python script path : ' python_path
	

	printf '%s\n' '-----------------------------------------------------------------------------------------------------------------------'
	echo Now the systemd will be configured to include the python script
	echo "
	[Unit]
	Description= SCP Service
	After=multi-user.target
	[Service]
	Type=idle
	ExecStart="$path" "$python_path"
	#WatchdogSec=15
	Restart=on-failure
	RestartSec=5
	[Install]
	WantedBy=multi-user.target" >> /lib/systemd/system/"$service".service
	chmod 644 /lib/systemd/system/"$service"
	sudo systemctl daemon-reload
	sudo systemctl enable "$service"
	echo Done configuring the systemd "$service"
	printf '%s\n' '-----------------------------------------------------------------------------------------------------------------------'
	read -p 'Do you want to start the service ? (y/n) : ' start
	if [[ "$start" == 'y' ]]; then
		sudo systemctl start "$service.service"
		sudo systemctl status "$service.service"
	fi

else
	echo This part of the script is for configuring command line shell scripts or any other exe archive
	read -p 'set the script path /home/$User/Desktop/random_script : ' script
	read -p 'Is it an executable file already ? (Y/N) : ' check_exe
	if [[ "$check_exe" == 'y' ]]; then

		printf '%s\n' '-----------------------------------------------------------------------------------------------------------------------'
		echo Now the systemd will be configured to include the exe file
		echo "
		[Unit]
		Description= SCP Service
		After=multi-user.target
		[Service]
		Type=idle
		ExecStart="$script"
		#WatchdogSec=15
		Restart=on-failure
		RestartSec=5
		[Install]
		WantedBy=multi-user.target" >> /lib/systemd/system/"$service".service
	else
		printf '%s\n' '-----------------------------------------------------------------------------------------------------------------------'
		echo Now the systemd will be configured to include the script
		echo "
		[Unit]
		Description= SCP Service
		After=multi-user.target
		[Service]
		Type=idle
		ExecStart="/bin/bash/" "$script"
		#WatchdogSec=15
		Restart=on-failure
		RestartSec=5
		[Install]
		WantedBy=multi-user.target" >> /lib/systemd/system/"$service".service
	
	chmod 644 /lib/systemd/system/"$service"
	sudo systemctl daemon-reload
	sudo systemctl enable "$service"
	echo Done configuring the systemd "$service"
	printf '%s\n' '-----------------------------------------------------------------------------------------------------------------------'
	read -p 'Do you want to start the service ? (y/n) : ' start
	if [[ "$start" == 'y' ]]; then
		sudo systemctl start "$service.service"
		sudo systemctl status "$service.service"
	fi
	fi

fi
echo Closing script ...