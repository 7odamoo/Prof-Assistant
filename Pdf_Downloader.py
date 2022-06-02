import requests
import re
from googlesearch import search
from pathlib import Path
from collections import Counter

extension = "ext:pdf"
query = "security" + extension

limit = 10
i = 1
for result in search(query, tld="co.in", pause=2):
	if limit != 0:
		if re.search("pdf$", result):
			print(i)
			print(result)
			counterName = str(i)+".pdf"
			fileName = Path(counterName)
			response = requests.get(result)
			fileName.write_bytes(response.content)
			i = i + 1
			limit = limit - 1
	else:
		break
