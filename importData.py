import requests
import json
import time

# URL de base de l'API NVD
BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
RESULTS_PER_PAGE = 2000

# Fichier de sortie
OUTPUT_FILE = "data.json"

# Initialisation
all_vulnerabilities = []
start_index = 0
total_results = None

print("Starting CVE data download from NVD...")

while True:
    # Construction de l’URL avec pagination
    params = {
        "resultsPerPage": RESULTS_PER_PAGE,
        "startIndex": start_index
    }
    print(f"Fetching records {start_index} - {start_index + RESULTS_PER_PAGE}...")

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching data at index {start_index}: {e}")
        time.sleep(10)
        continue

    # Ajout des vulnérabilités
    vulnerabilities = data.get("vulnerabilities", [])
    all_vulnerabilities.extend(vulnerabilities)

    # Nombre total de CVEs à récupérer
    if total_results is None:
        total_results = data.get("totalResults", 0)
        print(f"Total CVEs to download: {total_results}")

    # Si plus de pages à récupérer
    start_index += RESULTS_PER_PAGE
    if start_index >= total_results:
        break

    # Pause entre les requêtes pour éviter le rate limiting
    time.sleep(1.2)

# Sauvegarde des données dans un fichier JSON
print(f"\nSaving {len(all_vulnerabilities)} CVEs to {OUTPUT_FILE}...")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump({
        "resultsPerPage": RESULTS_PER_PAGE,
        "totalResults": total_results,
        "vulnerabilities": all_vulnerabilities
    }, f, ensure_ascii=False, indent=2)

print("Download complete.")
