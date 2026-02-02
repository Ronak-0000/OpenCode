#using socket(as mentioned in task)
import datetime
import os
import socket

#saving log file with date and time
with open("watchdog_log.txt", 'a') as f:

# OS check and then acc ping command
  if os.name == "nt":
    ping_cmd = os.popen("ping -n 5 google.com").read()
  else:
    ping_cmd = os.popen("ping -c 5 google.com").read()

  now = datetime.datetime.now()
  print("\n[*] Network Watchdog Initiated... ",file=f)
  print(now,file=f)
  print("OS -",os.name,file=f) 

  print("\n[*] Network Watchdog Initiated... ")
  print(now)
  print("OS -",os.name) 

  domain = "nitrkl.ac.in"
  ip = socket.gethostbyname(domain)
  print("Resolved IP Address:", ip,file=f)
  print("Resolved IP Address:",ip)

  print("'Google.com will be pinged 5 times'",file=f)
  print("'Google.com will be pinged 5 times'")
  
  print(ping_cmd, file=f)
  print(ping_cmd)

  print("'END OF LOG'\n")
  print("'END OF LOG'\n",file=f)