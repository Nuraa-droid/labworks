import json
with open(r"C:\Users\Nurai\pp2\Labworks\Lab4\sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data.get("imdata", []):
    interface = item.get("l1PhysIf", {}).get("attributes", {})
    dn = interface.get("dn", "N/A")
    desc = interface.get("descr", "inherit")
    speed = interface.get("speed", "inherit")
    mtu = interface.get("mtu", "N/A")

    print("{:<50} {:<15} {:<10} {:<10}".format(dn, desc, speed, mtu))