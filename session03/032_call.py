from subprocess import call

call(['ls','-l'])
call("ls -l > f.md", shell=True)
