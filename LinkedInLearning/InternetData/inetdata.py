# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request

def main():
    weburl = urllib.request.urlopen("https://github.com/JovemPedr0")
    print("result code:", weburl.getcode())
    data = weburl.read()
    print(data)

if __name__ == "__main__":
    main()
