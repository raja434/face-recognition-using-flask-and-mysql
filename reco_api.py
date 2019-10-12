import pycurl
from io import BytesIO
import json
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://167.71.238.56:5000/api/recognize')
c.setopt(c.POST, 1)
c.setopt(c.HTTPPOST, [("file", (c.FORM_FILE, "ra.jpeg"))])
#c.setopt(c.HTTPPOST, [("parameters", (c.FORM_FILE, "myparams.json"))])
c.setopt(pycurl.HTTPHEADER, ['Accept-Language: en'])
c.setopt(c.WRITEDATA, buffer)
data = c.perform()
body = buffer.getvalue()
responce = json.loads(body)
print responce