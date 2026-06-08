import os
import shutil
import hashlib
import datetime
from colorama import init, Fore

init(autoreset=True)

VIRUS_SIGNATURES = [
    "VIRUS_CODE",
    "MALWARE_DETECTED",
    "TROJAN_HORSE",
    "rm -rf /",
    "exec(base64_decode",
    "DROP TABLE",
    "wget http://evil",
    "shell_exec",
]

def get_file_hash(filepath):
    try:
        hasher = hashlib.md5()
        with open(filepath, "rb") as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    except:
        return "unreadable"

def scan_file(filepath):
    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()
        for signature in VIRUS_SIGNATURES:
            if signature in content:
                return True, signature
        return False, None
    except:
        return False, None

def quarantine_file(filepath, quarantine_dir):
    filename = os.path.basename(filepath)
    dest = os.path.join(quarantine_dir, filename)
    shutil.move(filepath, dest)
    return dest

def write_report(log_file, scanned, clean_files,
                  infected_files, start_time, elapsed):
    with open(log_file, "w") as f:
        f.write("ANTIVIRUS SCAN REPORT")
        f.write("=" * 50 + "")
        f.write(f"Scan date    : {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        f.write(f"Files scanned: {scanned}")
        f.write(f"Time taken   : {elapsed:.2f} seconds")
        f.write(f"CLEAN FILES ({len(clean_files)})")
        f.write("-" * 30 + "")
        for name, md5 in clean_files:
            f.write(f"  OK  {name}  [{md5}]")
        f.write(f"INFECTED FILES ({len(infected_files)})")
        f.write("-" * 30 + "")
        for name, sig, md5, dest in infected_files:
            f.write(f"  INFECTED  {name}")
            f.write(f"  Signature : {sig}")
            f.write(f"  MD5       : {md5}")
            f.write(f"  Moved to  : {dest}")
        f.write("=" * 50 + "END OF REPORT")
    print(Fore.WHITE + f"Report saved to: {log_file}")

def run_scan(target_dir, quarantine_dir, log_file):
    print(Fore.CYAN + "=" * 55)
    print(Fore.CYAN + "  Antivirus Scanner Starting...")
    print(Fore.CYAN + "  Target: " + target_dir)
    print(Fore.CYAN + "=" * 55 + "")
    scanned = 0
    infected_files = []
    clean_files = []
    start_time = datetime.datetime.now()
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            scanned += 1
            file_hash = get_file_hash(filepath)
            is_infected, matched_sig = scan_file(filepath)
            if is_infected:
                print(Fore.RED + f"[INFECTED] {filename}")
                print(Fore.RED + f"           Signature: '{matched_sig}'")
                print(Fore.RED + f"           MD5: {file_hash}")
                dest = quarantine_file(filepath, quarantine_dir)
                infected_files.append((filename, matched_sig, file_hash, dest))
            else:
                print(Fore.GREEN + f"[CLEAN]    {filename}")
                clean_files.append((filename, file_hash))
    elapsed = (datetime.datetime.now() - start_time).total_seconds()
    print(Fore.CYAN + "" + "=" * 55)
    print(Fore.CYAN + "  Scan Complete")
    print(Fore.WHITE + f"  Files scanned : {scanned}")
    print(Fore.GREEN + f"  Clean         : {len(clean_files)}")
    print(Fore.RED   + f"  Infected      : {len(infected_files)}")
    print(Fore.WHITE + f"  Time taken    : {elapsed:.2f} seconds")
    print(Fore.CYAN + "=" * 55)
    write_report(log_file, scanned, clean_files,
                 infected_files, start_time, elapsed)

TARGET_DIR     = "scan_target"
QUARANTINE_DIR = "quarantine"
LOG_FILE       = "scan_report.txt"

os.makedirs(QUARANTINE_DIR, exist_ok=True)
run_scan(TARGET_DIR, QUARANTINE_DIR, LOG_FILE)