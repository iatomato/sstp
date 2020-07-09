#!/usr/bin/python3

'''FREEDOM ISN'T FREE'''
# -*- coding: UTF-8 -*-
# (C) copyright 2020 eqporyan (Ryan William)
# v2rayT vsersion 2020
# Build ++

'''new build'''

from time import sleep
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
        self.subscription_path = self.v2rayTerminal_path + "/v2rayTerminal.sub"
        self.server_node_config_path = self.v2rayTerminal_path + "/v2rayTerminal.conf"
        self.server_node_config_backup = self.v2rayTerminal_path + "/v2rayTerminal.conf.backup"
        self.user_config = self.v2rayTerminal_path + "/User"
        
    def Logo(self, logo_paremeter):
    	if (logo_paremeter in "on"):
        	print(r'''
                                                             _______
                              ___   __   __                _/
            ___              | __| |_ | |_ | -----------  / 
           |   |------------ |__ | | _| | _|             | freedom
           |CIL|             | __| |_ | |_ |             |     world
           |___|             |   |server|  |

              ''')

    # ----------------------------- files system --------------------------
    def CheckFiles(self):
        if not os.path.exists(self.v2rayTerminal_path):
            os.mkdir(self.v2rayTerminal_path, mode=0o777)
        for get in (self.subscription_path, self.server_node_config_path):
            if not os.path.exists(get):
                open(get, "w+")
        if not os.path.exists(self.user_config):
            os.mkdir(self.user_config, mode=0o777)
        if not os.path.exists(self.user_config + "/settings.json"):
            settings = {"v2rayT": {"Settings": {"Logo": "on"},"Paremeter": {"SYS_1": 0,"SYS_1": 1}}}
            json.dump(settings, open(self.user_config + "/settings.json", "w"), indent=4)
        if os.path.exists(self.server_node_config_backup):
            self.SYS_PARTY_VALUE_0 = 1
        else:
            self.SYS_PARTY_VALUE_0 = 0
        #if os.path.exists(self.server_node_config_backup):
        #    self.SYS_PARTY_VALUE_1 = 1
        #else:
        #   self.SYS_PARTY_VALUE_1 = 0
        if os.path.exists(self.server_node_config_path):
            self.SYS_PARTY_VALUE_2 = 1
        else:
            self.SYS_PARTY_VALUE_2 = 0
            
    # ----------------------------- files system --------------------------

    def paremeter(self, paremeter):
        if paremeter in "init":
            with open(self.user_config + "/settings.json", 'r') as config:
                CONFIG = json.load(config)
            self.LOGO_X = CONFIG["v2rayT"]["Settings"]["Logo"]
            return self.LOGO_X
        elif paremeter in '1':
            with open(self.user_config + "/settings.json", 'r') as config:
                CONFIG = json.load(config)
            CONFIG["v2rayT"]["Settings"]["Logo"] = "off"
            json.dump(CONFIG, open(self.user_config + "/settings.json", "w"), indent=4)
        elif paremeter in '0':
            with open(self.user_config + "/settings.json", 'r') as config:
                CONFIG = json.load(config)
            CONFIG["v2rayT"]["Settings"]["Logo"] = "on"
            json.dump(CONFIG, open(self.user_config + "/settings.json", "w"), indent=4)

    # ----------------------------- basic verson 2020 ------------------------
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
        
    def ReadConfig(self, paremeter):
        if paremeter == 1:
            getfile = open(self.server_node_config_path, "r")
            self.config = getfile.read().strip()
            getfile.close()
            return self.config
        else:
            getfile_backup = open(self.server_node_config_backup, 'r')
            self.config = getfile_backup.read().strip()
            getfile_backup.close()
            return self.config
        
    def LoadSubscriptionContent(self, url, paremeter):
        try:
            content = requests.get(url).content
            missingpadding = 4- len(content) % 4
            if missingpadding:
                content += b"=" *missingpadding
            return content
        except:
            print("\nAddress error please check it\n")
            if paremeter == 0:
              os.remove(self.subscription_path)
              os.remove(self.server_node_config_path)
            elif paremeter == 1:
                os.remove(self.subscription_path)
                os.rename(self.server_node_config_path, self.server_node_config_backup)
                os.remove(self.server_node_config_path)
            exit()
     # ----------------------------- basic version 2020------------------------

class User(v2rayT):
    def __init__(self):
        v2rayT.__init__(self)
        self.path = os.path.expandvars("/") + "etc/v2ray"
        # ----- init paremeter and check basic files -----
        self.CheckFiles()
        subscription_file = open(self.subscription_path, "r")
        subscription_url = subscription_file.read().strip()
        subscription_file.close()
        print("Program Init")
        # ------------------------------------------------

        while True:
            if not subscription_url:
                while True:
                    print("\033c")
                    self.CheckFiles()
                    self.paremeter("init")
                    if self.LOGO_X in "on":
                        self.LOGO_PAREMETER = '1'
                    else:
                        self.LOGO_PAREMETER = '0'
                    self.Logo(self.LOGO_X)
                    OPTION_LIST = []
                    SYS_VALUE = 0
                    DEFUALT_VALUE = 0
                    with open(self.user_config + "/settings.json", "r") as get_config:
                        config = json.load(get_config)
                    if self.SYS_PARTY_VALUE_0 == 1:
                        MAX_OPTION = 4
                        DEFUALT_OPTION = [" Subscription URL\n", " About\n", " Continue <Backup>\n", " Settings <Reset>\n"]
                    else:
                        MAX_OPTION = 3
                        DEFUALT_OPTION = [" Subscription URL\n", " About\n", " Settings <Reset>\n"]
                    for get_value in range(1, (MAX_OPTION + 1)):
                        GET_STRING = "{}{}{}".format("[", get_value, "]")
                        OPTION_LIST.append(GET_STRING)
                    for get_list_string in OPTION_LIST:
                        OPTION_LIST[OPTION_LIST.index(get_list_string)] = get_list_string +  DEFUALT_OPTION[DEFUALT_VALUE]
                        DEFUALT_VALUE += 1
                    for GET_STRING in OPTION_LIST:
                        print(GET_STRING)
                    if MAX_OPTION == 3:
                        branch = input(": ")
                        if branch == '1':
                            subscription_url = self.AddSubscriptionURL() # new subscription definition
                            self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE))
                            break
                        elif branch == '2':
                            os.system("google-chrome https://github.com/Eqpoqpe/v2rayT")
                        elif branch == '3':
                            self.Settings()
                    elif MAX_OPTION == 4:
                        branch = input(": ")
                        if branch == '1':
                            subscription_url = self.AddSubscriptionURL()
                            self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE))
                            break
                        elif branch == '2':
                            os.system("google-chrome https://github.com/Eqpoqpe/v2rayT")
                        elif branch == '3':
                            self.config = self.ReadConfig(0)
                            self.ServerNode()
                            self.SetConfigFile()
                            break
                        elif branch == '4':
                            self.Settings()
            else:
                while True:
                    print("\033c")
                    self.CheckFiles()
                    self.paremeter("init")
                    if self.LOGO_X in "on":
                        self.LOGO_PAREMETER = '1'
                    else:
                        self.LOGO_PAREMETER = '0'
                    self.Logo(self.LOGO_X)
                    SYS_VALUE = 1
                    with open(self.user_config + "/settings.json", "r") as get_config:
                        config = json.load(get_config)
                    option_point = ["[1] Resubscription\n", "[2] Refresh Config\n", "[3] Continue\n", "[4] Settings <Reset>\n"]
                    for get_point in option_point:
                    	print(get_point)
                    branch = input(": ")
                    if branch in '1':
                        subscription_url = self.AddSubscriptionURL()
                        self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE))
                        break
                    elif branch in '2':
                        self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE))
                        break
                    elif branch in '3':
                        self.config = self.ReadConfig(1)
                        self.ServerNode()
                        self.SetConfigFile()
                        break
                    elif branch in '4':
                        self.Settings()

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
          "port": 10809,
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
        json.dump(config_format, open(v2ray_config_path, "w"), indent=2)
        exit()

    def Settings(self):
        print("\033c")
        self.Logo(self.LOGO_X)
        OPTION_LIST = []
        if self.LOGO_X in "on":
            OPTION_LIST.append("[1] OFF LOGO\n")
        else:
            OPTION_LIST.append("[1] ON LOGO\n")
        OPTION_LIST.append("[2] *CLEAN\n")
        #if self.SYS_PARTY_VALUE_0 == 1:
        #    OPTION_LIST.append("[3] RECOVER BACKUP\n")
        for get_point in OPTION_LIST:
            print(get_point)
        branch = input(": ")
        if branch in '1':
            self.paremeter(self.LOGO_PAREMETER)
        elif branch in '2':
            print("\033c")
            print("Warning: will delete all user config files,\nincluod subscription and server node config")
            care = input("\nGo on? [Yes] or [No]: ")
            if care in ["YES", "yes", 'Y', 'y']:
                os.remove(self.subscription_path)
                os.remove(self.server_node_config_path)
                exit()
        # Recover Backup
        #elif len(OPTION_LIST) == 3:
        #    if branch == '3':
        #        list_number = []
        #        for get in range(6):
        #            get_string = str(get) + ".. "
        #            list_number.append(get_string)
        #        output_string = ".. "
        #        for get_string in list_number:
        #            output_string += get_string
        #            print("\033c")
        #            print("Press \"Ctrl + C\" to stop recover\n")
        #            print(output_string)
        #            sleep(1)
        #        os.remove(self.server_node_config_path)
        #        os.rename(self.server_node_config_backup, self.server_node_config_path)
        #        print("Done!")

if __name__ == "__main__":
    A = User()
