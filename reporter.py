import os
import datetime
from rich.console import Console

console = Console()

def generate_html_report(target_name: str, execution_log: str) -> str:
    """
    Mengubah log eksekusi agen L4z4n3T-AI menjadi laporan HTML keamanan siber profesional.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_filename = f"L4z4n3T_Report_{target_name.replace('://', '_').replace('/', '_')}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L4z4n3T-AI Security Assessment Report</title>
    <style>
        body {{
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: auto;
            background: #161b22;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            border: 1px solid #30363d;
        }}
        h1 {{
            color: #58a6ff;
            text-align: center;
            border-bottom: 2px solid #30363d;
            padding-bottom: 15px;
        }}
        .meta {{
            background: #21262d;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 20px;
            border-left: 4px solid #58a6ff;
        }}
        pre {{
            background: #0d1117;
            color: #7ee787;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            border: 1px solid #30363d;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            color: #8b949e;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ L4z4n3T-AI Autonomous Pentest Report</h1>
        <div class="meta">
            <p><strong>Target:</strong> {target_name}</p>
            <p><strong>Waktu Eksekusi:</strong> {timestamp}</p>
            <p><strong>Engine:</strong> L4z4n3T-AI Core + DeepSeek-Coder (MCP)</p>
        </div>
        <h2>Execution & Findings Log</h2>
        <pre>{execution_log}</pre>
        <div class="footer">
            <p>Generated automatically by L4z4n3T-AI Platform. For authorized security testing only.</p>
        </div>
    </div>
</body>
</html>
"""
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        console.print(f"[bold green][+] Laporan HTML berhasil dibuat: {report_filename}[/bold green]")
        return report_filename
    except Exception as e:
        console.print(f"[bold red][-] Gagal membuat laporan: {e}[/bold red]")
        return None
