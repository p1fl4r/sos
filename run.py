import subprocess
import os

def run(i, f, naloga, timeout=None):
    script_path = f"naloge/{naloga}/code/{f.filename}"
    os.system(f"chmod +x ./naloge/{naloga}/code/{f.filename}")
    input_file_path = f"naloge/{naloga}/in/{i}.in"
    with open(input_file_path, 'r') as input_file:
        input_data = input_file.read()
    process = subprocess.Popen(['python', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data, timeout=timeout)
    with open(f"naloge/{naloga}/res/{i}.res", "w") as output:
        output.write(stdout)
    with open(f"naloge/{naloga}/err/{i}.err", "w") as output:
        output.write(stderr)