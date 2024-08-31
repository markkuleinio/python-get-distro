# Python 3.6+ required (f-strings)
import csv

RELEASE_DATA = {}

with open("/etc/os-release") as f:
    reader = csv.reader(f, delimiter="=")
    for row in reader:
        if row:
            RELEASE_DATA[row[0]] = row[1]

try:
    name = RELEASE_DATA["NAME"]
except KeyError:
    name = "Unknown"
try:
    version = RELEASE_DATA["VERSION"]
except KeyError:
    version = "(unknown version)"

if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
    with open("/etc/debian_version") as f:
        DEBIAN_VERSION = f.readline().strip()
    try:
        if "." not in DEBIAN_VERSION:
            raise ValueError    # Let the except clause handle
        major_version = DEBIAN_VERSION.split(".")[0]
        version_split = version.split(" ", maxsplit=1)
        if version_split[0] == major_version:
            # Just major version was shown in /etc/os-release, use the full version
            version = f"{DEBIAN_VERSION} {version_split[1]}"
    except:
        # Something went wrong ("xxx/sid"?), just use the info from /etc/debian_version
        version = DEBIAN_VERSION

print(f"{name} {version}")
