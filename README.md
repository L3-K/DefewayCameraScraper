# Defeway Camera Scraper
Load file of Defeway IPs and retrieves snapshots for all cameras 
Reads in IPs from `IP.txt`

Requires:
- Selenium 
- Python 3.6 or newer
- PhantomJS in PATH

Works by opening the DVR web UI, logging in with default credentials, then finding out how many cameras the DVR has. Then uses Defeway snapshot URL to retrieve snapshots from the DVR. Writes working IPs to other txt file. 

For educational use only. 
