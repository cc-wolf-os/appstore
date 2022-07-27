import logging
import programs
valid = 0
programslist = list(programs.programs.keys())
sorted_programs_list = sorted(programslist)

# Ensure the list is sorted.
if programslist != sorted_programs_list:
  valid = 1
  logging.error(
                "Invalid",
            )
sys.exit(valid)
