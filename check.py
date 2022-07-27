import logging
valid = 1
domain_list = list(domains.keys())
sorted_domain_list = sorted(domain_list)

# Ensure the list is sorted.
if domain_list != sorted_domain_list:
  valid = 0
  logging.error(
                "Invalid",
            )
sys.exit(valid)
