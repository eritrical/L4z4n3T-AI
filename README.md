# L4z4n3T-AI: Advanced Cyber Pentesting Platform

L4z4n3T-AI adalah platform keamanan siber otonom berbasis **Model Context Protocol (MCP)** dan **Ollama (LLM lokal)** yang dirancang untuk membantu Red Teamer dalam melakukan Reconnaissance, Enumerasi, Pemindaian Kerentanan, dan Pencarian Exploit secara terstruktur dan interaktif.

## 🚀 Fitur Utama
- **Autonomous Reasoning:** Didukung oleh LLM lokal (seperti `deepseek-coder`) untuk membuat keputusan taktis langkah demi langkah.
- **MCP Architecture:** Pemisahan tegas antara Client UI dan Server Tools menggunakan protokol MCP standar.
- **Human-in-the-Loop:** Membutuhkan persetujuan operator sebelum menjalankan perintah berbahaya pada sistem target.
- **Rich Terminal UI:** Antarmuka terminal interaktif yang rapi menggunakan library `rich`.

## 🛠️ Prasyarat Sistem
Pastikan Anda menggunakan sistem berbasis Linux (disarankan **Kali Linux**) dengan tool berikut terinstal:
- Python 3.10+
- Ollama (berjalan di `http://localhost:11434`)
- Tool CLI Pentesting: `nmap`, `gobuster`, `nikto`, `exploitdb` (`searchsploit`)

## 📦 Instalasi & Cara Menjalankan

1. Clone repository ini:
   ```bash
   git clone [https://github.com/username/l4z4n3T-AI.git](https://github.com/username/l4z4n3T-AI.git)
   cd l4z4n3T-AI
