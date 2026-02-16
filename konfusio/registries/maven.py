import requests

def exists(pkg):
    try:
        group, artifact = pkg.split(":")
    except:
        return True

    group_path = group.replace(".", "/")
    url = f"https://repo1.maven.org/maven2/{group_path}/{artifact}/"
    r = requests.get(url, timeout=5)
    return r.status_code == 200
