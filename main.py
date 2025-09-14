import os
import json
from modules import osint, fingerprint, enumerator, report_generator

def run_reconnaissance(target_url):
    """Orchestrates the entire reconnaissance process."""
    print(f"[*] Starting reconnaissance for {target_url}...")

    # Load configuration
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("[!] config.json not found. Using default settings.")
        config = {}

    # 1. OSINT and Open-Source Reconnaissance
    print("\n--- Phase 1: OSINT & Google Dorks ---")
    dorks_results = osint.perform_google_dorks(target_url, config.get("google_api_key"))
    
    # 2. Web Server Fingerprinting
    print("\n--- Phase 2: Web Server Fingerprinting ---")
    fingerprint_results = fingerprint.get_server_details(target_url)

    # 3. Enumeration and Mapping
    print("\n--- Phase 3: Enumeration & Mapping ---")
    enumeration_results = enumerator.enumerate_target(target_url)
    
    # 4. Content Review & Sensitive Info
    print("\n--- Phase 4: Reviewing Web Contents ---")
    content_results = fingerprint.review_web_content(target_url)

    # 5. Report Generation
    print("\n--- Phase 5: Generating Report ---")
    all_results = {
        "Target": target_url,
        "OSINT Results": dorks_results,
        "Fingerprint Results": fingerprint_results,
        "Enumeration Results": enumeration_results,
        "Content Review": content_results
    }
    report_generator.generate_pdf_report(all_results, "recon_report.pdf")

    print(f"[*] Reconnaissance complete. Report saved to recon_report.pdf")

if __name__ == "__main__":
    target = input("Enter the target URL (e.g., http://example.com): ")
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    run_reconnaissance(target)