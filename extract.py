from bplist.bplist import BPListReader

import os
import sys

if len(sys.argv) != 3:
    print("Usage: python extract.py \"C:\\.....\\Street Fighter 30th Anniversary Collection\\Bundle\" \"C:\\...your extraction folder...\"")
    exit(1)

root_dir = sys.argv[2]+"\\"
root_bundles = sys.argv[1]+"\\"

if not os.path.exists(root_bundles + 'Manifest.plist'):
    print("Cant find the bundles, are you sure you're using this correctly? Read the README.")
    exit(2)
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

with open(root_bundles + 'Manifest.plist', 'rb') as fp:
    read = fp.read()
    reader = BPListReader(read)
    parsed = reader.parse()
    for d, content in parsed["bundles"].items():

        extract_dir = root_dir+d.replace(".mbundle", "").replace("bundle", "")
        if not os.path.exists(root_bundles + d):
            print("Missing bundle", d)
            continue
        print("Extracting", d)
        if not os.path.exists(extract_dir):
            os.mkdir(extract_dir)
        extract_dir += "\\"
        with open(root_bundles + d, "rb") as bundle:
            for name, offsets in content["files"].items():
                bundle.seek(offsets["offset"])
                file_content = bundle.read(offsets["size"])
                print("\t", name)
                with open(extract_dir+name, "wb") as f:
                    f.write(file_content)
