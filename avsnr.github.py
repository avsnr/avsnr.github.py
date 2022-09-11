import requests
ll = input("Enter Github Repo Link :")
url = requests.get(f"{ll}/archive/refs/heads/main.zip").content
with open(f"Source.zip","wb")as new:
    new.write(url)
print("[!] Done Download.")
