# Run this script instead of sparxicba.py
import requests
from pathlib import Path
import subprocess

owner, repo, filename = "DeactivatedMan", "sparxicba", "sparxicba.py"
url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{filename}"
response = requests.get(url)

if response.status_code == 200:
    print("Got data from repo")
    content = response.text
    with open(Path.cwd() / filename, "r") as file:
        fLines = file.readlines()
        repoContent = content.replace(" ", "")
        fileContent = "".join(fLines).replace(" ","")

        if fileContent != repoContent:
            yn = str.lower(input("Update detected, would you like to update? Y // N\n"))
            if "y" in yn:
                print("Attempting to update")
        else:
            print("No update required")
            subprocess.run(["python", filename])
            exit()
    with open(Path.cwd() / filename, "w") as file:
        file.write(content)
        print(f"Updated file, see https://github.com/{owner}/{repo} for logs")

            


else:
    print(f"Error of status code {response.status_code}, check https://github.com/{owner}/{repo}")