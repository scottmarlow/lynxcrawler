import subprocess
import threading

def kill_lynx(pid):
    os.kill(pid, signal.SIGKILL)
    os.waitpid(-1, os.WNOHANG)
    print("lynx killed")
 
def get_url(url, outfile):
    print("get_url")
    web_data = ""
 
    cmd = "lynx -dump -nolist -notitle \"{0}\"".format(url)
    lynx = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    t = threading.Timer(300.0, kill_lynx, args=[lynx.pid])
    t.start()
 
    web_data = lynx.stdout.read()
    t.cancel()
 
    web_data = web_data.decode("utf-8", 'replace')
    f = open(outfile, "w")
    f.write(web_data);
    return web_data

# get_url("https://jakarta.ee/specifications/faces/4.0")

get_url("https://jakarta.ee/specifications/faces/4.0/jakarta-faces-4.0", "faces_spec-4.0.txt")
get_url("https://jakarta.ee/specifications/activation/2.1/jakarta-activation-spec-2.1", "activation_spec-2.1.txt")
