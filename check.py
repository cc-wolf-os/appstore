import logging,sys
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
                "Invalid: urls",
            )
  except:
    pass
 
sys.exit(valid)
