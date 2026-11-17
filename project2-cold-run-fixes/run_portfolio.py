"""One-command setup and launch. First installation needs PyPI access."""
from pathlib import Path
import os
import subprocess
import sys
import venv
import argparse
from committee import build_fingerprint
parser=argparse.ArgumentParser(description="Install and launch the club committee app.")
parser.add_argument("--port",type=int,default=8515,help="Use another port for an independent fresh-copy check, e.g. 8516.")
args=parser.parse_args()
if not 1024 <= args.port <= 65535:
    parser.error("port must be between 1024 and 65535")
print(f"Launching folder: {Path(__file__).resolve().parent}",flush=True)
print(f"Build fingerprint: {build_fingerprint()[:16]}",flush=True)
print(f"Expected browser URL: http://localhost:{args.port}",flush=True)
root=Path(__file__).resolve().parent
env=root/'.venv'
python=env/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
try:
    if not python.exists():
        venv.EnvBuilder(with_pip=True).create(env)
    subprocess.check_call([str(python),'-m','pip','install','-r',str(root/'requirements.txt')])
except (OSError,subprocess.CalledProcessError) as error:
    print('Setup failed: dependency installation requires access to PyPI (or an approved local package mirror). The browser app has not started.',file=sys.stderr)
    print('For the standard-library engine checks only, run: python3 -m unittest discover -s tests -p test_committee.py -v',file=sys.stderr)
    print('This fallback does not validate the browser app. Preserve the installation error above for the cold-run record.',file=sys.stderr)
    sys.exit(1)
launch_env=dict(os.environ,STREAMLIT_SERVER_HEADLESS='true',STREAMLIT_BROWSER_GATHER_USAGE_STATS='false')
try:
    subprocess.check_call([str(python),'-m','streamlit','run',str(root/'app.py'),'--server.port',str(args.port),'--server.headless=true','--browser.gatherUsageStats=false'],cwd=str(root),env=launch_env)
except (OSError,subprocess.CalledProcessError):
    print(f'App did not start or exited with an error. If port {args.port} is occupied, rerun: python3 run_portfolio.py --port {args.port+1}. Do not treat the pre-existing server as this copy.',file=sys.stderr)
    sys.exit(1)
except KeyboardInterrupt:
    pass
