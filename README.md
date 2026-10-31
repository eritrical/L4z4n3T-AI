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

## ⚙️ Instalasi

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/L4z4n3T/L4z4n3T-AI.git](https://github.com/L4z4n3T/L4z4n3T-AI.git)
   cd L4z4n3T-AI
2. Pastikan Ollama & Model AI Aktif

Platform ini digerakkan oleh LLM lokal via Ollama. Pastikan layanan Ollama sudah berjalan dan model deepseek-coder:6.7b sudah terunduh:

    Di terminal pertama (atau jalankan di background):
    Bash

    ollama serve

    Di terminal kedua, pastikan modelnya ada:
    Bash

    ollama pull deepseek-coder:6.7b

3. Instal Dependensi Python (Pertama Kali Saja)

Jika Anda belum menginstal library pendukung (mcp, rich, requests), jalankan:
Bash

pip install -r requirements.txt

4. Jalankan Platform L4z4n3T-AI

Eksekusi file client utama untuk memulai program:
Bash

python client.py

5. Berinteraksi dengan Agen AI

    Setelah banner keren buatan L4z4n3T muncul, agen akan otomatis terhubung ke MCP Server (server.py).

    Anda akan diminta memasukkan target pada prompt:
    Plaintext

    [?] Masukkan target IP / Domain / Instruksi Operasi

    (Contoh input: scan domain target.com dan cari kerentanannya atau 192.168.1.10)

    Human-in-the-Loop: Setiap kali AI memilih sebuah tool (seperti Nmap atau Subdomain Enum), terminal akan menampilkan tabel parameter dan bertanya:
    Plaintext

    [?] Izinkan L4z4n3T-AI mengeksekusi perintah ini secara nyata? (y/n):

    Tekan y untuk mengizinkan agen melanjutkan eksekusi, atau n untuk membatalkan.

    Hasil Otomatis: Setelah misi selesai atau dihentikan, agen L4z4n3T-AI akan otomatis merangkum seluruh hasil temuannya dan menghasilkan file laporan berformat HTML di dalam folder proyek (contoh: L4z4n3T_Report_target.com.html).
