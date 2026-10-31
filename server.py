import subprocess
import json
import shlex
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("L4z4n3T-FullSuite-Core")

def get_wordlist():
    """Mencari wordlist umum yang tersedia di sistem secara otomatis."""
    common_paths = [
        "/usr/share/wordlists/dirb/common.txt",
        "/usr/share/wordlists/seclists/Discovery/Web-Content/common.txt",
        "/usr/share/dirb/wordlists/common.txt"
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path
    return "common.txt"  # Fallback

@mcp.tool()
def intelligent_nmap_scan(target: str, intensity: str = "comprehensive") -> str:
    """Melakukan pemindaian port, servis, dan skrip kerentanan dasar menggunakan Nmap."""
    cmd_str = f"nmap -sV -sC -T4 -Pn {target}" if intensity == "comprehensive" else f"nmap -T4 -F -Pn {target}"
    try:
        result = subprocess.run(shlex.split(cmd_str), capture_output=True, text=True, timeout=180)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error Nmap: {str(e)}"

@mcp.tool()
def web_directory_fuzzing(target_url: str) -> str:
    """Melakukan pencarian direktori/file tersembunyi pada aplikasi web menggunakan Gobuster."""
    wordlist = get_wordlist()
    cmd_str = f"gobuster dir -u {target_url} -w {wordlist} -q -t 30 -k"
    try:
        result = subprocess.run(shlex.split(cmd_str), capture_output=True, text=True, timeout=240)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error Gobuster: {str(e)}"

@mcp.tool()
def vulnerability_scanner_nikto(target_url: str) -> str:
    """Memindai kerentanan web spesifik (misal: miskonfigurasi, file berbahaya) menggunakan Nikto."""
    cmd_str = f"nikto -h {target_url} -Tuning 123b -nointeractive"
    try:
        result = subprocess.run(shlex.split(cmd_str), capture_output=True, text=True, timeout=300)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error Nikto: {str(e)}"

@mcp.tool()
def search_and_verify_exploits(service_keyword: str) -> str:
    """Mencari referensi exploit publik dan kode verifikasi menggunakan searchsploit."""
    cmd_str = f"searchsploit --json {service_keyword}"
    try:
        result = subprocess.run(shlex.split(cmd_str), capture_output=True, text=True, timeout=45)
        data = json.loads(result.stdout)
        exploits = data.get("RESULTS_EXPLOIT", [])
        summary = [{"Title": e['Title'], "Path": e['Path'], "EDB-ID": e.get('EDB-ID', 'N/A')} for e in exploits[:8]]
        return json.dumps(summary, indent=2)
    except Exception as e:
        return f"Tidak ada exploit ditemukan atau error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
