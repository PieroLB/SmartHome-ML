import json

# Charger le fichier complet
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

vulns = data.get("vulnerabilities", [])
print(f"Total CVEs in dataset: {len(vulns)}")

# Mots-clés pour détecter les vulnérabilités IoT domestiques
iot_keywords = [
    "iot", "smart home", "smart device", "connected home", "home automation",
    "smart camera", "ip camera", "webcam", "surveillance camera",
    "voice assistant", "amazon echo", "google home", "alexa",
    "nest", "home hub", "thermostat", "sensor", "smart light",
    "smart plug", "smart lock", "doorbell", "hub", "zigbee", "zwave"
]

# Filtrage
filtered_vulns = []
for v in vulns:
    cve = v.get("cve", {})
    descs = " ".join([d.get("value", "").lower() for d in cve.get("descriptions", [])])
    cpes = " ".join([match.get("criteria", "").lower()
                     for config in cve.get("configurations", [])
                     for node in config.get("nodes", [])
                     for match in node.get("cpeMatch", [])])
    
    if any(keyword in descs or keyword in cpes for keyword in iot_keywords):
        filtered_vulns.append(v)

print(f"Filtered IoT-related CVEs: {len(filtered_vulns)}")

# Sauvegarde
output = {
    "resultsPerPage": len(filtered_vulns),
    "totalResults": len(filtered_vulns),
    "vulnerabilities": filtered_vulns
}

with open("data_iot.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("data_iot.json saved successfully.")
