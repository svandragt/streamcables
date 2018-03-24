import subprocess
p, out = (subprocess.run(["ls", "-l"], stdout=subprocess.PIPE))
print(out)