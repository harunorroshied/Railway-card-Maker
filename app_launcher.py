import os
import sys
import webbrowser
import subprocess

def launch():
    html_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    url = f"file:///{html_file}"
    
    # Try Edge in App mode (Native window look without browser bars)
    edge_paths = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
    ]
    for ep in edge_paths:
        if os.path.exists(ep):
            try:
                subprocess.Popen([ep, f"--app={url}", "--start-maximized"])
                return
            except Exception:
                pass

    # Try Chrome App mode
    chrome_paths = [
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    ]
    for cp in chrome_paths:
        if os.path.exists(cp):
            try:
                subprocess.Popen([cp, f"--app={url}", "--start-maximized"])
                return
            except Exception:
                pass

    # Fallback to default browser
    webbrowser.open(url)

if __name__ == "__main__":
    launch()
