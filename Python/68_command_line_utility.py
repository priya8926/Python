import argparse
import requests

def download_file(url , local_Filename):
    with requests.get(url , stream = True) as r:
        r.raise_for_status()
        with open(local_Filename , 'wb') as f:
            for chunk in r.iter_content(chunk_size = 8192):
                f.write(chunk)
    return local_Filename

parser = argparse.ArgumentParser(description="A command line utility for downloading files.")
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("output", help="By which name you want to save your file")
args = parser.parse_args()
print(args.url)
print(args.output)
download_file(args.url , args.output)