import re

log_file = "sample_logs.txt"

pattern = re.compile(
    r"tls_version=(TLSv1\.0|TLSv1\.1)|"
    r"cipher=(3DES|DES-CBC3-SHA|AES128-SHA)",
    re.IGNORECASE
)

with open(log_file, "r") as file:
    for line in file:
        if pattern.search(line):
            print("[ALERT] Possible SSL/TLS configuration weakness:")
            print(line.strip())
