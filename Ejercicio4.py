import urllib.request
url = "http://textfiles.com/adventure/aencounter.txt "
contpalabras = 0
file = urllib.request.urlopen(url)
for line in file:
    contpalabras += len(line)
print(contpalabras)
file = close()
