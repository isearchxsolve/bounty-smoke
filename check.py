import subprocess, sys
out = subprocess.run([sys.executable, 'hello.py'], capture_output=True, text=True).stdout
assert 'world' in out, 'output was %r' % out
print('CHECK OK')
