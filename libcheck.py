import logging,sys,requests
import programs
from urllib.parse import urlparse
valid = 0
programslist = list(programs.libs.keys())
sorted_programs_list = sorted(programslist)

# Ensure the list is sorted.
if programslist != sorted_programs_list:
  valid = 1
  logging.error(
                "Invalid: libs not sorted",
            )
for i in programslist:
  try:
    url = urlparse(programs.libs[i]["docs"])
    if not (url.scheme == "http" or url.scheme == "https"):
      valid = 1
      logging.error(
                f"Invalid:  docs url of {i}",
            )
    url = urlparse(programs.libs[i]["download"])
    if not (url.scheme == "http" or url.scheme == "https"):
      valid = 1
      logging.error(
                f"Invalid:  download url of {i}",
            )
    doc = open(f"libs/{i}.docs.html", mode="w")
    docs = requests.get(programs.libs[i]["docs"])
    doc.write(docs.text)
    doc.close()
    down = open(f"libs/{i}.code.txt",  mode="w")
    code = requests.get(programs.libs[i]["download"])
    down.write(code.text)
    down.close()
  except:
    pass
  


  
sys.exit(valid)
