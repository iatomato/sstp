#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# v2rayT 2.1-master
# Author: eqporyan (Ryan William)
# Build ++

import sys
import os
import requests
import base64
import json
import subprocess
import re

class v2rayT:
    def __init__(self):
        self.v2rayTerminal_path = os.path.expandvars("$HOME") + "/.v2rayTerminal"
        self.subscription_path = self.v2rayTerminal_path + "/v2rayTerminal.subscription"
        self.server_node_config_path = self.v2rayTerminal_path + "/v2rayTerminal.config"
        self.user_config = self.v2rayTerminal_path + "/User"
        
    def Logo(self, value):
    	if (value in "on"):
        	print(r'''
                                                             _______
                              ___   __   __                _/
            ___              | __| |_ | |_ | -----------  / 
           |   |------------ |__ | | _| | _|             | freedom
           |CIL|             | __| |_ | |_ |             |     world
           |___|             |   |server|  |
              
              ''')
        
    def Exitd(self, value):
        pass

    def CheckFiles(self):
        if not os.path.exists(self.v2rayTerminal_path):
            os.mkdir(self.v2rayTerminal_path, mode=0o777)
        for get in (self.subscription_path, self.server_node_config_path):
            if not os.path.exists(get):
                open(get, "w+")
        if not os.path.exists(self.user_config):
            os.mkdir(self.user_config, mode=0o777)
        if not os.path.exists(self.user_config + "/settings.json"):
            settings = {"Logo": "on"}
            json.dump(settings, open(self.user_config + "/settings.json", "w"), indent=2)
          
    def AddSubscriptionURL(self):
        subscription_url = input("\nURL: ")
        getfile = open(self.subscription_path, "w+")
        getfile.write(subscription_url)
        getfile.close()
        return subscription_url
        
    def AddConfig(self, content):
        config =str(base64.urlsafe_b64decode(content), encoding="utf-8")
        getfile =open(self.server_node_config_path, "w+")
        getfile.write(config)
        getfile.close()
        return config
        
    def ReadConfig(self):
        getfile =open(self.server_node_config_path, "r")
        self.config = getfile.read().strip()
        getfile.close()
        return self.config
        
    def LoadSubscriptionContent(self, url):
        try:
            content = requests.get(url).content
            missingpadding = 4- len(content) % 4
            if missingpadding:
                content += b"=" *missingpadding
            print("Done!")
            return content
        except:
            print("\033c")
            print("\nAddress error please check it\n")
            os.remove(self.subscription_path)
            os.remove(self.server_node_config_path)
            exit()
            
class User(v2rayT):
    def __init__(self):
        v2rayT.__init__(self)
        self.path = os.path.expandvars("/") + "etc/v2ray"
        self.CheckFiles()
        subscription_file = open(self.subscription_path, "r")
        subscription_url = subscription_file.read().strip()
        subscription_file.close()
        while True:
            if not subscription_url:
                while True:
                    print("\033c")
                    with open(self.user_config + "/settings.json", "r") as get_config:
                        config = json.load(get_config)
                    self.value = config["Logo"]
                    self.Logo(self.value)
                    option_point = ["[1] Subscription URL\n", "[2] About\n", "[3] Settings <Reset>\n"]
                    for get_point in option_point:
                    	print(get_point)
                    branch = input(": ")
                    if branch in '1':
                        subscription_url = self.AddSubscriptionURL()
                        self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url))
                        break
                    elif branch in '2':
                        os.system("google-chrome https://github.com/Eqpoqpe/v2rayT.git")
                    elif branch in '3':
                        self.Settings()
                    elif branch in "back":
                        pass
                    #elif branch in ["EXIT", "exit", "Exit", 'E', 'e']:
                    #    self.Exit(int(1))
            else:
                while True:
                    print("\033c")
                    with open(self.user_config + "/settings.json", "r") as get_config:
                        config = json.load(get_config)
                    self.value = config["Logo"]
                    self.Logo(self.value)
                    #self.Tips()
                    option_point = ["[1] Resubscription\n", "[2] Refresh Config\n", "[3] Continue\n", "[4] Settings <Reset>\n"]
                    for get_point in option_point:
                    	print(get_point)
                    branch = input(": ")
                    if branch in '1':
                        subscription_url = self.AddSubscriptionURL()
                        self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url))
                        break
                    elif branch in '2':
                        self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url))
                        break
                    elif branch in '3':
                        self.config = self.ReadConfig()
                        self.ServerNode()
                        self.SetConfigFile()
                        break
                    elif branch in '4':
                        self.Settings()
                    #elif branch in ["EXIT", "exit", "E", "e"]:
                    #    self.Exit(int(1))
                    
        self.ServerNode()
        self.SetConfigFile()
        
    def ServerNode(self):
        print("$" + "=" * 60 + "$")
        self.server_list =str.encode(self.config).splitlines()
        for get_list in self.server_list:
            if len(get_list) == 0:
                self.server_list.remove(get_list)
        for get in range(len(self.server_list)):
            self.server_node = json.loads(base64.b64decode(bytes.decode(self.server_list[get]).replace("vmess://", "")))
            print("[" + str(get) + "]" + self.server_node["ps"])
            print("$" + "=" * 60 + "$")
            self.server_list[get] = self.server_node
      
    def SetConfigFile(self):
        checked_node_id = int(input("SERVER NODE NUMBER\n\n: "))
        address = self.server_list[checked_node_id]["add"]
        port = int(self.server_list[checked_node_id]["port"])
        alter_id = self.server_list[checked_node_id]["aid"]
        users_id =self.server_list[checked_node_id]["id"]
        get_path = input("SEVA FILE PATH: /")
        config_format = {
		  "dns": {
			"hosts": {
			  "domain:googleapis.cn": "googleapis.com"
			},
			"servers": [
			  "1.1.1.1"
			]
		  },
		  "inbounds": [
			{
			  "listen": "127.0.0.1",
			  "port": 10806,
			  "protocol": "socks",
			  "settings": {
				"auth": "noauth",
				"udp": True,
				"userLevel": 8
			  },
			  "sniffing": {
				"destOverride": [
				  "http",
				  "tls"
				],
				"enabled": True
			  },
			  "tag": "socks"
			},
			{
			  "listen": "127.0.0.1",
			  "port": 10805,
			  "protocol": "http",
			  "settings": {
				"userLevel": 8
			  },
			  "tag": "http"
			}
		  ],
		  "log": {
			"loglevel": "warning"
		  },
		  "outbounds": [
			{
			  "mux": {
				"concurrency": -1,
				"enabled": False
			  },
			  "protocol": "vmess",
			  "settings": {
				"vnext": [
				  {
				    "address": address,
				    "port": port,
				    "users": [
				      {
				        "alterId": alter_id,
				        "id": users_id,
				        "level": 8,
				        "security": "auto"
				      }
				    ]
				  }
				]
			  },
			  "streamSettings": {
				"network": "ws",
				"security": "",
				"wssettings": {
				  "connectionReuse": True,
				  "headers": {
				    "Host": ""
				  },
				  "path": "/qwert001"
				}
			  },
			  "tag": "proxy"
			},
			{
			  "protocol": "freedom",
			  "settings": {},
			  "tag": "direct"
			},
			{
			  "protocol": "blackhole",
			  "settings": {
				"response": {
				  "type": "http"
				}
			  },
			  "tag": "block"
			}
		  ],
		  "policy": {
			"levels": {
			  "8": {
				"connIdle": 300,
				"downlinkOnly": 1,
				"handshake": 4,
				"uplinkOnly": 1
			  }
			},
			"system": {
			  "statsInboundUplink": True,
			  "statsInboundDownlink": True
			}
		  },
		  "routing": {
			"domainStrategy": "IPIfNonMatch",
			"rules": [
			  {
				"domain": [
				  "domain:googleapis.cn"
				],
				"outboundTag": "proxy",
				"type": "field"
			  },
			  {
				"ip": [
				  "geoip:private"
				],
				"outboundTag": "direct",
				"type": "field"
			  },
			  {
				"ip": [
				  "geoip:cn"
				],
				"outboundTag": "direct",
				"type": "field"
			  },
			  {
				"domain": [
				  "geosite:cn"
				],
				"outboundTag": "direct",
				"type": "field"
			  }
			]
		  },
		  "stats": {}
		}
        v2ray_config_path = os.path.expandvars("/") + get_path + "/config.json"
        print('''
            "http"
            "listen": 127.0.0.1
            "port": 10806
            "protocol": "socks"
            ___________________
            "socks"
            "listen": 127.0.0.1
            "port": 10805
              ''')
        json.dump(config_format, open(v2ray_config_path, "w"), indent=2)
        exit()
			
    def Settings(self):
        print("\033c")
        self.Logo(self.value)
        with open(self.user_config + "/settings.json", "r") as get_config:
            config = json.load(get_config)
        if config["Logo"] in "on":
            option_point = ["[1] OFF LOGO\n", "[2] *CLEAN\n"]
            for value in option_point:
                print(value)
            branch = input(": ")
            if branch in '1':
                with open(self.user_config + "/settings.json", "r") as get_config:
                    config = json.load(get_config)
                config["Logo"] = "off"
                json.dump(config, open(self.user_config + "/settings.json", "w"), indent=2)
                return config
            if branch in '2':
                print("Warning: will delete all user config files,\nincluod subscription and server node config")
                care = input("\nGo on? [Yes] or [No]: ")
                if care in ["YES", "yes", 'Y', 'y']:
                    os.remove(self.subscription_path)
                    os.remove(self.server_node_config_path)
                    exit()
        if config["Logo"] in "off":
            branch = input("[1] On LOGO\n[2] *Clean\n\n: ")
            if branch in '1':
                with open(self.user_config + "/settings.json", "r") as get_config:
                    config = json.load(get_config)
                config["Logo"] = "on"
                json.dump(config, open(self.user_config + "/settings.json", "w"), indent=2)
                return config
            if branch in '2':
                print("Warning: will delete all user config files,\n incluod subscription and server node config")
                care = input("\nGo on? [Yes] or [No]: ")
                if care in ["YES", "yes", 'Y', 'y']:
                    os.remove(self.subscription_path)
                    os.remove(self.server_node_config_path)
                    exit()

if __name__ == "__main__":
    A = User()
