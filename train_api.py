import unirest
response = unirest.post("http://167.71.238.56:5000/api/train", headers={"Accept": "application/json"},
  params={
    "name": "va",
    "file": open("ra.jpeg", mode="r")
  }
)
print response.raw_body