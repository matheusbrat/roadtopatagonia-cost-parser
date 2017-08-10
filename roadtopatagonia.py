import re

f = open("roadtopatagonia.txt")

x = 0
ar_match = re.compile('AR\$([0-9]+)')
clp_match = re.compile('CLP\$([0-9]+)')
uy_match = re.compile('UY\$([0-9]+)')
br_match = re.compile('[^AU]R\$([0-9]+)')
ar_total = 0
clp_total = 0
uy_total = 0
br_total = 0
for line in f.readlines():
	if line.startswith("Total"):
		line = line.replace(',', '').strip()
		x = x + 1
		ar_search = ar_match.search(line)
		if ar_search:
			ar_total = ar_total + int(ar_search.group(1))
		clp_search = clp_match.search(line)
		if clp_search:
			clp_total = clp_total + int(clp_search.group(1))
		uy_search = uy_match.search(line)
		if uy_search: 
			uy_total = uy_total + int(uy_search.group(1))
		br_search = br_match.search(line)
		if br_search:
			br_total = br_total + int(br_search.group(1))
			
			
print("AR total:", ar_total)
print("CLP total:", clp_total)
print("UY total:", uy_total)
print("BR total:", br_total)

ar_convertion = 5.61
clp_convertion = 205.42
uy_convertion = 9.12

print("BR global total", br_total + (ar_total / ar_convertion) + (clp_total / clp_convertion) + (uy_total / uy_convertion))
