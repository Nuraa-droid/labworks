og_file = input()
copy = input()
with open(og_file, "r", encoding="utf-8") as src, open(copy, "w", encoding="utf-8") as dest:
   dest.write(src.read())
print(f"Contents copied from '{og_file}' to '{copy}'")