# 🛡️ L4z4n3T-AI: Advanced Cyber Pentesting Platform

**L4z4n3T-AI** adalah platform keamanan siber otonom berbasis **Model Context Protocol (MCP)** dan **Ollama (Local LLM)**. Platform ini dirancang khusus untuk membantu *Red Teamer* dan *Security Researcher* dalam melakukan Reconnaissance, Enumerasi Subdomain, Pemindaian Kerentanan, dan Pencarian Exploit secara terstruktur, interaktif, dan cerdas.

---

## 🚀 Fitur Utama

- **Autonomous Reasoning:** Didukung oleh LLM lokal (`deepseek-coder`) untuk menganalisis target dan mengambil keputusan taktis langkah demi langkah.
- **MCP Architecture:** Pemisahan tegas berbasis arsitektur *Client-Server* menggunakan Model Context Protocol standar industri.
- **Fast Subdomain Enumeration:** Modul pencarian subdomain paralel dan *live host prober* untuk mempercepat fase awal investigasi.
- **Human-in-the-Loop:** Sistem keamanan interaktif yang meminta persetujuan operator (`y/n`) sebelum mengeksekusi perintah ofensif apa pun.
- **Automated HTML Reporting:** Secara otomatis merangkum seluruh hasil operasi menjadi laporan keamanan siber berformat HTML yang elegan dan profesional.
- **Rich Terminal UI:** Antarmuka baris perintah (CLI) yang futuristik, rapi, dan informatif menggunakan library `rich`.

---

## 🛠️ Arsenal Tools yang Tersedia

1. **`intelligent_subdomain_enum`**: Pencarian subdomain paralel & pengecekan status host aktif.
2. **`intelligent_nmap_scan`**: Pemindaian port, layanan, dan skrip kerentanan mendalam (`nmap`).
3. **`web_directory_fuzzing`**: Pencarian direktori/file tersembunyi pada aplikasi web (`gobuster`).
4. **`vulnerability_scanner_nikto`**: Pemindai miskonfigurasi web spesifik (`nikto`).
5. **`search_and_verify_exploits`**: Pencarian referensi exploit publik dan verifikasi (`searchsploit`).

---

## 📦 Prasyarat Sistem

Pastikan Anda menggunakan sistem berbasis Linux (disarankan **Kali Linux**) dengan komponen berikut:
- Python 3.10+
- Ollama (berjalan di `http://localhost:11434`)
- Tool Pentesting CLI: `nmap`, `gobuster`, `nikto`, `exploitdb` (`searchsploit`)

---

## ⚙️ Instalasi & Cara Menjalankan

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/username/L4z4n3T-AI.git](https://github.com/username/L4z4n3T-AI.git)
   cd L4z4n3T-AI
