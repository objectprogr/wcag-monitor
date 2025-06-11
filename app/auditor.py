import subprocess

def run_pa11y(url):
    try:
        result = subprocess.run(["pa11y", url, "--reporter", "json"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
