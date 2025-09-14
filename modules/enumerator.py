import nmap
import socket

def enumerate_target(target_url):
    """Performs Nmap and DNS lookups."""
    results = {}
    hostname = target_url.replace("http://", "").replace("https://", "").split("/")[0]
    
    # 1. DNS Lookups
    try:
        results['dns_lookup'] = socket.gethostbyname_ex(hostname)
        results['reverse_dns_lookup'] = socket.gethostbyaddr(results['dns_lookup'][2][0])
    except socket.gaierror as e:
        results['dns_error'] = f"DNS lookup failed: {e}"
    except socket.herror as e:
        results['reverse_dns_error'] = f"Reverse DNS lookup failed: {e}"

    # 2. Nmap Scan
    try:
        nm = nmap.PortScanner()
        # Scan common ports and detect services
        nm.scan(hostname, '21,22,80,443,8080', arguments='-sV -sS -O') 
        
        scan_results = nm[hostname]
        results['open_ports'] = [f"{port}/{proto}" for proto in scan_results.all_protocols() for port in scan_results[proto]]
        results['os_details'] = scan_results.get('osmatch', 'Not Found')
        results['services'] = {port: scan_results['tcp'][int(port)]['name'] for port in results['open_ports']}
        
    except nmap.nmap.PortScannerError as e:
        results['nmap_error'] = f"Nmap scan failed. Make sure you have Nmap installed and are running with sudo/administrator privileges."
    
    return results