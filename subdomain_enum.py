import socket
import urllib.parse
import concurrent.futures
import json
import sys

def check_host(subdomain):
    """Memeriksa apakah subdomain dapat disolusi ke IP (aktif) dan merespons web."""
    try:
        ip = socket.gethostbyname(subdomain)
        active_url = None
        status_code = "N/A"
        
        for proto in ["https", "http"]:
            url = f"{proto}://{subdomain}"
            try:
                import urllib.request
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=3) as response:
                    active_url = url
                    status_code = response.status
                    break
            except Exception:
                continue
                
        return {
            "subdomain": subdomain,
            "ip": ip,
            "status": "Alive",
            "active_url": active_url or f"http://{subdomain}",
            "http_status": status_code
        }
    except socket.gaierror:
        return None
    except Exception:
        return {"subdomain": subdomain, "ip": "Unknown", "status": "Resolvable", "active_url": None, "http_status": "N/A"}

def run_subdomain_enumeration(domain: str, wordlist_file: str = None) -> str:
    """
    Melakukan enumerasi subdomain tingkat lanjut dan memfilter host yang aktif secara paralel.
    """
    default_subdomains = [
        "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webadmin",
        "dns", "ns2", "imap", "test", "blog", "msk", "www2", "admin", "secure",
        "vpn", "api", "dev", "staging", "portal", "dashboard", "auth", "login",
        "shop", "store", "cloud", "app", "status", "support", "git", "jenkins"
    ]
    
    subdomains_to_check = default_subdomains
    
    if wordlist_file:
        try:
            with open(wordlist_file, "r") as f:
                custom_words = [line.strip() for line in f if line.strip()]
                if custom_words:
                    subdomains_to_check = custom_words
        except Exception as e:
            print(f"[-] Gagal membaca wordlist kustom: {e}")

    full_targets = [f"{sub}.{domain}" for sub in subdomains_to_check]
    print(f"[*] L4z4n3T Subdomain Engine memindai: {domain} ({len(full_targets)} kandidat)...")
    
    active_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_host, sub): sub for sub in full_targets}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                active_results.append(res)
                
    return json.dumps(active_results, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan: python subdomain_enum.py <domain.com>")
        sys.exit(1)
    print(run_subdomain_enumeration(sys.argv[1]))
