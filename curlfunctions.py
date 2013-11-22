import pycurl
import io


#Class to buffer the input from cURL
class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf

def get_http(mURL):
    #output = io.FileIO
    t = Test()
    #output = Writer()
    c = pycurl.Curl()

    c.setopt(c.URL, mURL)
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.setopt(c.CONNECTTIMEOUT, 5)
    c.setopt(c.TIMEOUT, 10)
    c.perform()
    c.close()
    return t.contents