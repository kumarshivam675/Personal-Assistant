import subprocess
import time

while(1):
	p = subprocess.Popen(["python", "run.py", ""])
	print "Process ID of subprocess %s" % p.pid
	# Send SIGTER (on Linux)
	time.sleep(300)
	p.terminate()
	# Wait for process to terminate
	returncode = p.wait()
	print "Returncode of subprocess: %s" % returncode
	q = subprocess.Popen(["python", "run.py", ""])
	time.sleep(10)
	q.terminate()
	returncode = q.wait()
