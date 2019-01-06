# Defeway Camera Scraper
Load file of Defeway IPs and retrieves snapshots for all cameras 
Reads in IPs from `IP.txt`

Requires:
- Selenium 
- Python 3.6 or newer
- PhantomJS in PATH

Loads `IP.txt` file containing IPs in the format `IP:PORT` seperated by new lines (Example file provided). Opens the DVR web UI, logging in with default credentials and then finding camera count. Uses default Defeway snapshot URL `http://IP:PORT/cgi-bin/snapshot.cgi?chn=1&u=USERNAME&p=BLANK&q=0&d=0` to retrieve snapshots from the DVR for each camera. Writes working IPs to `WorkingDefewayIPs.txt` and saves snapshots to /Snapshots/ Directory

**For educational use only. I take no responsibility for any damages caused by misuse of this software.** 
