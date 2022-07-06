from dotenv import load_dotenv
load_dotenv()
import os
# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
ip = os.getenv("POSTGRE_IP")
