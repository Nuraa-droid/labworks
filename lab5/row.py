import re
import json

with open (r"C:\Users\Nurai\pp2\labworks\lab5\row.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

cleaned_lines = []
buffer = ""
for line in lines:
    line = line.replace("\xa0", " ").strip() 
    if re.match(r"^\d+\.", line):  
        if buffer:
            cleaned_lines.append(buffer) 
        buffer = line 
    else:
        buffer += " " + line  
if buffer:
    cleaned_lines.append(buffer)

receipt = {
    "branch": None,
    "bin": None,
    "nds_series": None,
    "kassa": None,
    "smena": None,
    "sequence_number": None,
    "kassir": None,
    "items": []
}

branch_pattern = re.compile(r"Филиал\s+(.+)")
bin_pattern = re.compile(r"БИН\s+(\d+)")
nds_pattern = re.compile(r"НДС\s+Серия\s+(\d+)")
kassa_pattern = re.compile(r"Касса\s+([\d-]+)")
smena_pattern = re.compile(r"Смена\s+(\d+)")
sqnc_pattern = re.compile(r"Порядковый\s+номер\s+чека\s+№(\d+)")
kassir_pattern = re.compile(r"Кассир\s+Аптека\s+([\d-]+)")

for line in lines:
    line = line.strip()

    if branch_match := branch_pattern.search(line):
        receipt["branch"] = branch_match.group(1)

    if bin_match := bin_pattern.search(line):
        receipt["bin"] = bin_match.group(1)

    if nds_match := nds_pattern.search(line):
        receipt["nds_series"] = nds_match.group(1)

    if kassa_match := kassa_pattern.search(line):
        receipt["kassa"] = kassa_match.group(1)

    if smena_match := smena_pattern.search(line):
        receipt["smena"] = smena_match.group(1)

    if sqnc_match := sqnc_pattern.search(line):
        receipt["sequence_number"] = sqnc_match.group(1)

    if kassir_match := kassir_pattern.search(line):
        receipt["kassir"] = kassir_match.group(1)
   
    pattern = re.compile(r"(\d+)\.\s+(.+)\s+(\d+,\d+)\s+x\s+([\d\s,]+)\s+([\d\s,]+)")
    for line in cleaned_lines:
        match = pattern.search(line)
        if match:
            id = match.group(1)
            name = match.group(2)
            price = match.group(3)
            quantity = match.group(4)
            sum = match.group(5) 

            receipt["items"].append({
            "id": id,
            "name": name,
            "price": price,
            "quantity": quantity,
            "sum": sum
        })

if "Банковская карта:" in lines:
    receipt["payment_method"] = "Банковская карта"

with open("receipt.json", "w", encoding="utf-8") as json_file:
    json.dump(receipt, json_file, indent=4, ensure_ascii=False)

print("Done!!")

