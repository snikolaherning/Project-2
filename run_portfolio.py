"""One-command local setup and launch. Run from the repository root."""
from pathlib import Path
import os,subprocess,sys,venv
root=Path(__file__).resolve().parent
folder=root
env=folder/'.venv'
python=env/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
if not python.exists():
    venv.EnvBuilder(with_pip=True).create(env)
subprocess.check_call([str(python),'-m','pip','install','-r',str(folder/'requirements.txt')])
subprocess.check_call([str(python),'-m','streamlit','run',str(folder/'app.py'),'--server.port','8515'],cwd=str(folder))
