#! /bin/bash


# Download necessary libraries and configure the raspberry pi to create a wifi hotspot
read -p 'select a static ipaddress(for example 1892.168.5.2) followed by / subnetmask (24 for example): ' ip_subnet
read -p 'select wifi name : ' wifi_name
read -p 'select a wifi password : ' wifi_password

ip=${ip_subnet%/*} #until the first /
sbnet=${ip_subnet#*/} #from the / till end

gate_net=$(echo $ip | cut -d\. -f1,2,3)
gate_net+=.1

range_one=$(echo $ip | cut -d\. -f1,2,3)
range_one+=.2

range_two=$(echo $ip | cut -d\. -f1,2,3)
range_two+=.20

if [[ "$sbnet" -eq 24 ]]; then
    sbnet=255.255.255.0
elif [[ "$sbnet" -eq 16 ]]; then
    sbnet=255.255.0.0
else sbnet=255.0.0.0
fi

#gateway+=0.1

apt install hostapd -y
systemctl unmask hostapd
systemctl enable hostapd
apt install dnsmasq -y
DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent
echo  "interface wlan0" >> /etc/dhcpcd.conf
echo "static ip_address=$ip_subnet" >> /etc/dhcpcd.conf
echo "nohook wpa_supplicant" >> /etc/dhcpcd.conf
echo "auto wlan0" >> /etc/network/interfaces.d/wlan0
echo "iface wlan0 inet static" >> /etc/network/interfaces.d/wlan0
echo "address $ip" >> /etc/network/interfaces.d/wlan0
echo "netmask $sbnet" >> /etc/network/interfaces.d/wlan0
echo "gateway $gate_net" >> /etc/network/interfaces.d/wlan0
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
echo "interface=wlan0" >> /etc/dnsmasq.conf
echo "dhcp-range=$range_one,$range_two,$sbnet,24h" >> /etc/dnsmasq.conf
echo "domain=wlan" >> /etc/dnsmasq.conf
echo "address=/gw.wlan/$ip" >> /etc/dnsmasq.conf
rfkill unblock wlan
echo "country_code=ES" >> /etc/hostapd/hostapd.conf 
echo "interface=wlan0" >> /etc/hostapd/hostapd.conf 
echo "ssid=$wifi_name" >> /etc/hostapd/hostapd.conf 
echo "hw_mode=g" >> /etc/hostapd/hostapd.conf 
echo "channel=7" >> /etc/hostapd/hostapd.conf 
echo "macaddr_acl=0" >> /etc/hostapd/hostapd.conf 
echo "auth_algs=1" >> /etc/hostapd/hostapd.conf 
echo "ignore_broadcast_ssid=0" >> /etc/hostapd/hostapd.conf 
echo "wpa=2" >> /etc/hostapd/hostapd.conf 
echo "wpa_passphrase=$wifi_password" >> /etc/hostapd/hostapd.conf 
echo "wpa_key_mgmt=WPA-PSK" >> /etc/hostapd/hostapd.conf 
echo "wpa_pairwise=TKIP" >> /etc/hostapd/hostapd.conf 
echo "rsn_pairwise=CCMP" >> /etc/hostapd/hostapd.conf
#systemctl reboot



