import subprocess
import hashlib
import pickle

# Hardcoded password
PASSWORD = "admin123"

# Insecure subprocess
subprocess.call("ls -la", shell=True)

# Weak cryptography
print(hashlib.md5(b"password").hexdigest())

# Insecure eval
user_input = "2 + 3"
print(eval(user_input))

# Insecure deserialization
data = pickle.loads(b"cos\nsystem\n(S'echo hacked'\ntR.")
print(data)
