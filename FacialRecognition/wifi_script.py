import os
import platform
import getpass
class Wifi:
    '''
    Class for stablishing quick wifi connections.
    ===
    
        Main functions:


            1 createNewConnection -> Creates a new xml file with the name, SSID and key of the network.

            2 connect -> Connects through the adequate command to the already created wifi address, no need to provide platform information.

            3 displayAvailableNetworks -> Runs the appropriate command to display the wifi addresses available information for every OS.

            4 wifi_conn -> Main function to create and connect to a wifi address or to connect to an already created one. It runs 1 and 2 in order if new address is inputted.
              Starts at __init__
            '''
    def __init__(self):
        """ self.name=input("Introduce the wifi's name: ")
        self.password=input("Introduce the wifi's password: ") """
        self.name,self.password="TKQR2020","QRApp2020"
        self.wifi_conn(self.name,self.password)

    def createNewConnection(self,name, SSID, key):
        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>"""+name+"""</name>
        <SSIDConfig>
            <SSID>
                <name>"""+SSID+"""</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>"""+key+"""</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
        if platform.system() == "Windows":
            command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
            with open(name+".xml", 'w') as file:
                file.write(config)
        elif platform.system() == "Linux":
            command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
        os.system(command)
        if platform.system() == "Windows":
            os.remove(name+".xml")

    def connect(self,name, SSID):
        if platform.system() == "Windows":
            command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
        elif platform.system() == "Linux":
            command = "nmcli con up "+SSID
        os.system(command)

    def displayAvailableNetworks(self,):
        if platform.system() == "Windows":
            command = "netsh wlan show networks interface=Wi-Fi"
        elif platform.system() == "Linux":
            command = "nmcli dev wifi list"
        os.system(command)

    def wifi_conn(self,name,password):
        try:
            #displayAvailableNetworks()
            option = input("New connection (y/N)? ")
            if option == "N" or option == "":
                name = input("Name: ")
                self.connect(name, name)
                print("If you aren't connected to this network, try connecting with correct credentials")
            elif option == "y":
                name = name
                key = password
                self.createNewConnection(name, name, key)
                self.connect(name, name)
                print("If you aren't connected to this network, try connecting with correct credentials")
        except KeyboardInterrupt as e:
            print("\nExiting...")

