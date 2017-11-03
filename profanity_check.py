import urllib

def read_file():
    f = open("movie_quotes.txt")
    contents = f.read()
    f.close()
    result = profanity_check(contents)
    if "true" in result:
        print("Profanity Alert!")
    elif "false" in result:
        print("There is no curse word in the document.")
    else:
        print("Could not scan the document")

def profanity_check(text):
    response = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    return response.read()

read_file()
