import logging
import programs
valid = 1
programlist = list(programs.programs.keys())
sorted_programs_list = sorted(programslist)

# Ensure the list is sorted.
if programslist != sorted_programs_list:
  valid = 0
  logging.error(
                "Invalid",
            )
sys.exit(valid)
