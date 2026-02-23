# Network Security Scanner (TCP Connect Scan)

A comprehensive laboratory demonstration of TCP Connect Port Scanning using Python sockets.  
This project simulates a real-world network reconnaissance scenario where open ports are identified through full TCP three-way handshakes.

## Overview

This project demonstartes:

- TCP Connect scan implementation.
- Socket programming using Python.
- Basic service detection technique.
- GUI Based interaction.
- Fundamental network seccurity concepts.
- Ethical investigation practices.

--- 

## Learning Objectives

- Understand TCP three-way handshake.
- Implement port scanning using socket programming.
- Identify open and close ports.
- Understanding basic vulnerability exposure.
- Recognize ethical consierations in network scan.

---

## Features

- TCP connect sccanning technique is demonstrated.
- Custorm target IP input
- Custom port range selection(1-65535)
- Optional GUI interface
- Basic service detection(common ports)
- Lightweight and beginner friendly
- Educational focused.

---

## Project Structure

```
introduction-to-programming/
│
├── README.md
└── program/
    ├── scanner.py      # Core scanning logic
    ├── gui.py          # Graphical interface
    ├── test.py         # Testing module
    └── main.py         # Entry point
```

## Technical Bacground

### TCP Connect Scan

The TCP Connect Scan completes the full three-way handshake:

1. SYN → Sent to target port  
2. SYN-ACK ← Received if port is open  
3. ACK → Connection established  

If connection succeeds → Port is **OPEN**  
If connection fails → Port is **CLOSED / FILTERED**

This is the most reliable but most detectable scanning method.

------

## Quick Start

### 1. clone the repository
```
git clone https://github.com/dahalaashish/Introduction-to-Programming.git
cd Introduction-to-Programming/Program
```
---

### 2. Check Requirements

This project requires:

- Python 3.8+
- Git

Check Python:

Windows:
```
python --version
```

macOS / Linux:
```
python3 --version
```

Check Git:
```
git --version
```

---

### 3. Install Python (If Needed)

#### Windows

```
winget install Python.Python.3
winget install Git.Git
```

---

#### macOS

If Homebrew is not installed:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Python and Git:
```
brew install python
brew install git
```

---

#### Linux (Debian/Ubuntu)

```
sudo apt update
sudo apt install python3 python3-pip git -y
```

---

### 4. Run the scanner

Comman Line Interface(CLI) Version:
Windows:
```
python main.py
```

macOS / Linux:
```
python3 main.py
```

GUI Version (if applicable):

Windows:
```
python gui.py
```

macOS / Linux:
```
python3 gui.py
```
---

## How It Works

1. User inputs target IP address(Only use personal system or others with proper permission )
2. User selects port range(0-65535)
3. Program creates TCP socket
4. Attempts connection to each port(Time duration for each port = 0.3 sec)
5. Displays open ports in result box

## Example Output (CLI)

```
Starting TCP Connect Scan on 192.168.1.1
Scanning ports 20–100...

Port 22  → OPEN  (SSH)
Port 80  → OPEN  (HTTP)
Port 443 → OPEN  (HTTPS)
Port 23  → CLOSED

Scan Completed.
```
## Security & Ethical Notice

This tool is made strictly for:

- Educational use
- Academic assignments
- Authorized lab environments

Do NOT scan networks or systems without proper permission.  
Unauthorized scanning may violate cybersecurity laws.

---

## Results

Key Findings:

- Successfully detects open TCP ports
- Demonstrates real-world reconnaissance methodology
- Shows practical implementation of networking theory
- Reinforces ethical hacking fundamentals

---

## Future Improvements

- Implement SYN Scan using Scapy
- Add OS fingerprinting
- Export scan results to CSV
- Add logging system
- Add banner grabbing
- Improve GUI visualization

---

## Author

Aashish Dahal  
BSc (Hons) Cybersecurity & Ethical Hacking  
Academic Project – Network Security Scanner(TCP Scanner)

---

