### **README.md**

# ReconAIzer 🤖

ReconAIzer is an AI-powered automated reconnaissance tool for penetration testing. It streamlines the initial information-gathering phase by automating OSINT, web server fingerprinting, content enumeration, and report generation. The project is designed to be a proof-of-concept demonstrating how AI can act as a force multiplier in cybersecurity, handling repetitive tasks so a human tester can focus on more complex analysis.


## **Features** \*
**Automated OSINT:** Performs Google Dork searches and pulls data from public sources to find exposed files, directories, and sensitive information.

  * **Web Server & Application Fingerprinting:** Identifies the web server type, version details, and application frameworks by analyzing HTTP headers and public metafiles.
  * **Sensitive Data Discovery:** Scans HTML and JavaScript source code for potentially sensitive information like API keys, email addresses, and hidden comments.
  * **Network & DNS Enumeration:** Integrates with `nmap` to identify open ports and services, and performs DNS lookups to map the target's infrastructure.
  * **Automated Reporting:** Generates a professional PDF report summarizing all findings, providing a clear overview of the reconnaissance results.


## **Installation** 💻

### **Prerequisites**

  * **Python 3.x:** Ensure you have Python installed.
  * **Nmap:** The tool relies on Nmap for network scanning. Download and install it from the [official Nmap website](https://nmap.org/download.html).

### **Setup Steps**

1.  Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/ReconAIzer.git
    cd ReconAIzer
    ```

2.  Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3.  Create the necessary file structure:

    ```bash
    mkdir modules
    mkdir data
    # Create an empty config.json file to prevent errors
    echo "{}" > config.json
    ```

4.  Copy the provided Python scripts into the correct directories.

      * `main.py` goes in the root directory.
      * `osint.py`, `fingerprint.py`, `enumerator.py`, and `report_generator.py` go into the `modules/` directory.


## **Usage** To run the tool, simply execute the `main.py` script from your terminal. You will be prompted to enter the target URL.

```bash
python main.py
```

**Example:**

```
Enter the target URL (e.g., http://example.com): http://demo.owasp-juice.shop
[*] Starting reconnaissance for http://demo.owasp-juice.shop...
...
[*] Reconnaissance complete. Report saved to recon_report.pdf
```

The final report, `recon_report.pdf`, will be saved in the same directory.


## **Disclaimer** ⚠️

This tool is for **educational and ethical purposes only**. You **must** have explicit permission from the owner of the target system before running any form of reconnaissance or penetration test. Unauthorized use is illegal. The creator and contributors of this tool are not responsible for any misuse or damage caused.


## **Future Enhancements (AI Component)** 🚀

  * **Intelligent Dork Generation:** Implement an AI model to dynamically generate custom Google Dorks based on initial findings.
  * **Vulnerability Prediction:** Train a machine learning model on a dataset of vulnerabilities to predict potential weaknesses based on the identified web server and application versions.
  * **Automated Fuzzing:** Use a machine learning-based fuzzer to discover hidden directories and injection points more efficiently.
