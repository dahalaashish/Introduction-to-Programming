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
git clone https
