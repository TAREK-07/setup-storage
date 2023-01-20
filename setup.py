import os
import sys
import time
os.system("clear")
def pkg():
  print("\033[1;33m")
  os.system("apt uninstall python")
  os.system("apt install python")
  os.system("pkg update")
  os.system("pkg upgrade")
  os.system("pkg install python ")
  os.system("pkg install python2")
  os.system("pkg install python3")
  os.system("pip install requests")
  os.system("pip install machanize")
  os.system("pkg install ruby")
  os.system("gem install lolcat")
  os.system("pip install bs4")
  os.system("pkg install git")
  os.system("pip install rich")
  print("\033[1;31m    [√]ALL PACKAGE INSTALL SUCCESSFUL")
logo="""

\033[1;36m╔═════════════════════════════════════════╗
•           \033[1;33m<🌺Assalamu Alaikum🌺>        •
\033[1;36m╚═════════════════════════════════════════╝
\033[1;32m████████╗ █████╗ ██████╗ ███████╗██╗  ██╗
\033[1;33m╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
 \033[1;34m  ██║   ███████║██████╔╝█████╗  █████╔╝ 
 \033[1;35m  ██║   ██╔══██║██╔══██╗██╔══╝  ██╔═██╗ 
  \033[1;31m ██║   ██║  ██║██║  ██║███████╗██║ ██╗
 \033[1;36m  ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═╝
\033[1;32m╔═════════════════════════════════════════╗
║  \033[1;32m[√] DEVOLPER    :     TAREK ISLAM      ║
\033[1;32m║  \033[1;33m[√] FACEBOOK    :     TAREK ISLAM      \033[1;32m║
\033[1;32m║  \033[1;34m[√] WHATAPP     :     01952260226     \033[1;32m ║
\033[1;32m║  \033[1;35m[√] GITHUB      :     TAREK-07         \033[1;32m║
\033[1;32m║  \033[1;31m[√] VERSION     :     1.0              \033[1;32m║
\033[1;32m║  \033[1;36m[√] SERVER      :     DATA WORKING    \033[1;32m ║ 
\033[1;32m╚═════════════════════════════════════════╝
"""
print(logo)
ab=input("\033[1;31mSTART CRACKING......(y/n)")
per=ab.replace(" ","")
yes=["y" "Y"]
if ab in yes:
  install()
elif per=="n":
  print("SOMETHING WRONG")
  sys.exit()
else:
  print("CRACKING COMPLETE")
  sys.exit()