# 🛡️ Antivirus Scanner

A simple Python-based Antivirus Scanner that detects malicious files using signature-based scanning, generates file hashes, quarantines infected files, and creates detailed scan reports.

## 📌 Features

- Scan files and folders recursively
- Detect known malware signatures
- Generate MD5 hashes for scanned files
- Automatically quarantine infected files
- Generate detailed scan reports
- Color-coded terminal output
- Lightweight and beginner-friendly cybersecurity project

## 🛠️ Technologies Used

- Python 3
- OS Module
- Hashlib
- Shutil
- Datetime
- Colorama

## 📂 Project Structure

```
Antivirus-Scanner/
│
├── scanner.py
├── scan_target/
├── quarantine/
├── scan_report.txt
└── README.md
```

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/antivirus-scanner.git
cd antivirus-scanner
```

### Install Dependencies

```bash
pip install colorama
```

## ▶️ Usage

1. Place files to be scanned inside the `scan_target` folder.
2. Run the scanner:

```bash
python scanner.py
```

3. Results will be displayed in the terminal.
4. Infected files will be moved to the `quarantine` folder.
5. A scan report will be generated as:

```text
scan_report.txt
```

## 🔍 Detection Method

The scanner identifies potentially malicious files using predefined malware signatures such as:

- VIRUS_CODE
- MALWARE_DETECTED
- TROJAN_HORSE
- rm -rf /
- exec(base64_decode
- DROP TABLE
- wget http://evil
- shell_exec

If any signature is found inside a file, the file is marked as infected and moved to quarantine.

## 📊 Sample Output

```text
=======================================================
Antivirus Scanner Starting...
=======================================================

[CLEAN] document.txt
[INFECTED] malware.txt

=======================================================
Scan Complete
Files scanned : 10
Clean         : 9
Infected      : 1
Time taken    : 0.32 seconds
=======================================================
```

## ⚠️ Disclaimer

This project is created for educational and learning purposes. It demonstrates the basic concepts of antivirus software using signature-based malware detection and should not be considered a replacement for professional antivirus solutions.

## 👨‍💻 Author

Krushnagopal Agnihotri

Cybersecurity & Networking Enthusiast
