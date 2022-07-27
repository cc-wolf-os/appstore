import logging,sys,requests
import programs
from urllib.parse import urlparse
valid = 0
programslist = list(programs.programs.keys())
sorted_programs_list = sorted(programslist)

# Ensure the list is sorted.
if programslist != sorted_programs_list:
  valid = 1
  logging.error(
                "Invalid: programs not sorted",
            )
for i in programslist:
  try:
    url = urlparse(programs.programs[i]["docs"])
    if not (url.scheme == "http" or url.scheme == "https"):
      valid = 1
      logging.error(
                "Invalid:  docs url",
            )
    url = urlparse(programs.programs[i]["download"])
    if not (url.scheme == "http" or url.scheme == "https"):
      valid = 1
      logging.error(
                "Invalid:  download url",
            )
    doc = open(f"apps/{i}.docs.html", mode="w")
    docs = requests.get(programs.programs[i]["docs"])
    doc.write(docs.text)
    doc.close()
    down = open(f"apps/{i}.code",  mode="w")
    code = requests.get(programs.programs[i]["docs"])
    down.write(code.text)
    down.close()
  except:
    pass
 
sys.exit(valid)
