import requests
import re

def get_server_details(target_url):
    """Fingerprints the web server by analyzing HTTP headers."""
    details = {}
    try:
        response = requests.get(target_url)
        headers = response.headers
        
        details['server_type'] = headers.get('Server', 'Not Found')
        details['x_powered_by'] = headers.get('X-Powered-By', 'Not Found')
        details['framework'] = headers.get('X-Frame-Options', 'Not Found')
        
        # A simple check for common metafiles
        for file in ['robots.txt', 'sitemap.xml', 'humans.txt', 'security.txt']:
            file_url = f"{target_url.rstrip('/')}/{file}"
            res = requests.get(file_url)
            details[file] = "Found" if res.status_code == 200 else "Not Found"
            
    except Exception as e:
        details['error'] = str(e)
    
    return details

def review_web_content(target_url):
    """Scans page source for sensitive information."""
    results = {}
    try:
        response = requests.get(target_url)
        source_code = response.text
        
        # Regex patterns for common sensitive data
        patterns = {
            "API Keys": r'(api_key|secret_key|token|auth_token).*?[\'"][0-9a-fA-F]{32,64}[\'"]',
            "Emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            "Comments": r''
        }
        
        for name, pattern in patterns.items():
            found = re.findall(pattern, source_code)
            results[name] = found if found else "Not Found"
            
        # Check for autocomplete on login forms
        autocomplete_check = "autocomplete='off'" not in source_code.lower()
        results['Autocomplete Enabled?'] = "Yes, possible risk" if autocomplete_check else "No"
        
    except Exception as e:
        results['error'] = str(e)
        
    return results