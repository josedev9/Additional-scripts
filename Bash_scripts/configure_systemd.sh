
#!/bin/bash
# Ask the user the service name and the path
read -p 'servicename: ' service
read -p 'python script?(1/0) : ' check_python

if [[ "$check_python" -eq 1 ]]; then
	read -p 'set the python path : ' path
	read -p 'set the python script path : ' python_path
	

	printf '%s\n' '-----------------------'
	echo Now the systemd will be configured to include the python script
	echo sudo nano /lib/systemd/system/"$service".service
	echo "[Unit]
	Description= SCP Service
	After=multi-user.target
	[Service]
	Type=idle
	ExecStart="$path" "$python_path"
	#WatchdogSec=15
	Restart=on-failure
	RestartSec=5
	[Install]
	WantedBy=multi-user.target"
	echo "chmod 644 /lib/systemd/system/"$service"
	sudo systemctl daemon-reload
	sudo systemctl enable "$service""
	echo Done configuring the systemd "$service"
	printf '%s\n' '-----------------------'
	echo Exiting script 

else
echo To be implemented
echo Closing script
fi

