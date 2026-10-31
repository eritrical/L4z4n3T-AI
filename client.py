import asyncio
import json
import re
import sys
import os
import requests
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek-coder:6.7b"

def print_banner():
    banner = """[bold cyan]
    ╔══════════════════════════════════════════════════════════════════╗
    ║        L4z4n3T-AI : ADVANCED CYBER PENTESTING PLATFORM           ║
    ║        Autonomous Red Teaming & Exploit Verification Engine      ║
    ╚══════════════════════════════════════════════════════════════════╝
    [/bold cyan]"""
    console.print(banner)

def query_ollama_json(prompt, tools_desc):
    system_prompt = f"""Kamu adalah L4z4n3T-AI, agen otonom keamanan siber senior setingkat Red Teamer di Kali Linux.
Tugasmu adalah menganalisis target secara taktis langkah demi langkah (Recon -> Enumerasi -> Analisis Kerentanan -> Pencarian Exploit).

Daftar Tool MCP yang Tersedia:
{tools_desc}

ATURAN KETAT:
Respons HANYA dalam format JSON murni tanpa teks pembuka/penutup, markdown code block, atau penjelasan di luar struktur ini:
{{
    "thought": "Analisis taktis mengapa memilih tool ini berdasarkan temuan sebelumnya",
    "tool_name": "nama_tool_yang_dipilih atau null jika misi selesai",
    "tool_args": {{"nama_argument": "nilai_argument"}}
}}
"""
    full_prompt = f"{system_prompt}\n\nRiwayat & Target Pengguna:\n{prompt}\n\nRespons JSON:"
    payload = {"model": MODEL_NAME, "prompt": full_prompt, "stream": False, "format": "json"}
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        res_json = response.json().get("response", "{}")
        cleaned_json = re.sub(r"^```json\s*|\s*```$", "", res_json.strip())
        return json.loads(cleaned_json)
    except Exception as e:
        console.print(f"[bold red][-] Error komunikasi/parsing dari Ollama LLM: {e}[/bold red]")
        return {"thought": "Error pada LLM", "tool_name": None, "tool_args": {}}

async def run_l4z4n3t_agent():
    print_banner()
    
    # Deteksi path server.py secara dinamis di direktori yang sama
    current_dir = os.path.dirname(os.path.abspath(__file__))
    server_script_path = os.path.join(current_dir, "server.py")
    python_executable = sys.executable  # Menggunakan python interpreter aktif saat ini

    server_params = StdioServerParameters(
        command=python_executable,
        args=[server_script_path],
    )

    with console.status("[bold green]Menghubungkan ke L4z4n3T Core Server...", spinner="dots"):
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                
    console.print(Panel(f"[bold green][+] Core Berhasil Terhubung![/bold green]\n[cyan]Active Arsenal:[/cyan] {[t.name for t in tools.tools]}", title="HexStrike Status", border_style="cyan"))
    
    tools_desc = "\n".join([f"- {t.name}: {t.description} (Schema: {t.inputSchema})" for t in tools.tools])
    
    user_goal = Prompt.ask("\n[bold yellow][?] Masukkan target IP / Domain / Instruksi Operasi[/bold yellow]")
    current_context = user_goal

    for step in range(8):
        console.print(f"\n[bold magenta]══════════════════════════════════════════════════════════════════[/bold magenta]")
        console.print(f"[bold magenta] 🛡️ [ FASE OPERASI / ITERASI KE-{step+1} ] [/bold magenta]")
        console.print(f"[bold magenta]══════════════════════════════════════════════════════════════════[/bold magenta]")
        
        with console.status("[bold cyan]AI sedang menyusun strategi ofensif...", spinner="monkey"):
            ai_decision = query_ollama_json(current_context, tools_desc)
        
        thought = ai_decision.get('thought', 'Menganalisis situasi...')
        console.print(Panel(f"[yellow]{thought}[/yellow]", title="🧠 AI Cognitive Reasoning", border_style="yellow"))
        
        tool_name = ai_decision.get('tool_name')
        tool_args = ai_decision.get('tool_args', {})
        
        if not tool_name or tool_name == "null":
            console.print("[bold green][+] Misi selesai. Agen menyimpulkan tidak diperlukan tindakan lanjutan.[/bold green]")
            break
        
        table = Table(title=f"Target Eksekusi: {tool_name}", border_style="blue")
        table.add_column("Parameter", style="cyan", no_wrap=True)
        table.add_column("Nilai / Argumen", style="white")
        for k, v in tool_args.items():
            table.add_row(k, str(v))
        console.print(table)
        
        approval = Prompt.ask("\n[bold red][?] Izinkan agen menjalankan perintah ini secara nyata?[/bold red]", choices=["y", "n"], default="y")
        
        if approval == "n":
            console.print("[bold yellow][-] Operasi dibatalkan oleh operator. Menghentikan misi.[/bold yellow]")
            break
        
        try:
            with console.status(f"[bold red]Menjalankan {tool_name} di sistem target...", spinner="bouncingBar"):
                result = await session.call_tool(tool_name, tool_args)
                output_text = result.content[0].text
            
            console.print(Panel(output_text[:3000], title=f"📊 Hasil Output: {tool_name}", border_style="green"))
            current_context += f"\n\n[Hasil Eksekusi {tool_name}]:\n{output_text}"
            
        except Exception as e:
            console.print(f"[bold red][-] Eksekusi Tool Gagal: {e}[/bold red]")
            break

if __name__ == "__main__":
    asyncio.run(run_l4z4n3t_agent())
