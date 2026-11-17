"""One-command setup and launch. First installation needs PyPI access."""
from pathlib import Path
import os
import subprocess
import sys
import venv
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
    subprocess.check_call([str(python),'-m','streamlit','run',str(root/'app.py'),'--server.port','8515','--server.headless=true','--browser.gatherUsageStats=false'],cwd=str(root),env=launch_env)
except (OSError,subprocess.CalledProcessError):
    print('App did not start or exited with an error. Record the message above; check whether port 8515 is already in use.',file=sys.stderr)
    sys.exit(1)
except KeyboardInterrupt:
    pass
