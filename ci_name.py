import re

fqdn = "airbusdev001.external@airbus.com"
ci_name = "airbusdev001"

if fqdn.startswith(ci_name):
	print(ci_name)

