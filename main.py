import subprocess
import json
print("Conifer Server Launcher")
try:
    with open('config.json') as f:
        settings = json.load(f)
except:
    print("Malformed config.json. Run setup.py again to fix")
    exit()


operating_sys = settings["os"]
architecture = settings["architecture"]
if(settings["extracted"] and settings["executable"]):
    print(f"Running pocketbase for {operating_sys} on {architecture}")
    print("Press ^ + c to stop, or close terminal window")
    process = subprocess.run([f"./pocketbase-{operating_sys}-{architecture}", "serve"])
if not settings["extracted"]:
    print("Pocketbase not extracted yet. Re-run setup.py to fix")
if not settings["executable"] and settings["os"] != "Windows":
    print("Pocketbase executable does not have proper permission. Run setup.py again to fix this")