import subprocess
import re
cmd  = subprocess.run(['netsh','wlan','show','profiles'],capture_output=True).stdout.decode()
profiles =  (re.findall("All User Profile     : (.*)\r", cmd))

wifies = []

if len(profiles) != 0:
    for wifiname in profiles:
        wifi = {}
        profile = subprocess.run(['netsh','wlan','show','profile',wifiname],capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile):
            continue
        else:
            wifi['ssid'] = wifiname
            profileInfo = subprocess.run(['netsh','wlan','show','profile',wifiname,'key=clear'],capture_output=True).stdout.decode()
            password = re.search("Key Content            :(.*)\r", profileInfo)
            if password == None :
                wifi['password'] = "No Password"
            else:
                wifi['password'] = password[1]
            wifies.append(wifi)
for w in wifies:
    print(w)


