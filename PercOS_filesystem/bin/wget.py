import urllib.request

from command import Command


class Wget(Command):
    name = "wget"
    desc = "A command for downloading files from he internet"
    usage = "wget <url> [filename]"
    author = "ThePerkinrex"

    @staticmethod
    def call(dire, usr, args=None):
        if args == None or len(args) == 0:
            print("I need at least the url to work")
        else:
            url = args[0]
            filename = "error"
            if len(args) == 1:
                filename = url.split("/")[len(url.split("/"))-1]
                print("no filename specified")
                print("downloading as " + filename)
            else:
                filename = args[1]
                print("filename specified")
                print("downloading as " + filename)
            f = open(dire.realdir + "/" + filename, 'w')
            f.write(Wget.getINetTextFile(url))
            f.flush()
            f.close()
            print("downloaded")

    @staticmethod
    def getINetTextFile(url):
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        return text
