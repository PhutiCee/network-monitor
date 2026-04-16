# 🌐 Network Traffic Monitoring Dashboard (Real-Time Observability System)

## 📌 Overview

This project is a **real-time network traffic monitoring and observability system** designed to capture, process, analyze, and visualize live network packets.

It functions as a lightweight **Network Operations Center (NOC) / SOC-style dashboard**, providing insights into:

- Bandwidth usage (real-time + historical)
- Protocol distribution (TCP, UDP, ICMP, etc.)
- Top IP talkers
- Active connections
- Live traffic rates (bytes/sec, packets/sec)
- Network anomaly alerts (spikes & unusual activity)

The system is built with a **full-stack real-time architecture** using Python (backend) and React (frontend), connected via WebSockets for live updates.

---

## 🚀 Key Features

### 📡 Packet Capture

- Real-time packet sniffing using **Scapy**
- Captures live network traffic from the host machine
- Extracts source/destination IP, protocol, and packet size

### ⚙️ Backend Processing

- Multi-threaded packet processing pipeline
- Centralized metrics aggregation engine
- Sliding window analytics for real-time computation
- Efficient in-memory data structures (deque, dict)

### 📊 Real-Time Metrics

- Bandwidth usage tracking
- Bandwidth rate (bytes/second)
- Packets per second (PPS)
- Active connection tracking
- Top talker IP analysis

### 🚨 Alert System (Anomaly Detection)

- Traffic spike detection (threshold-based)
- Unusual IP activity detection
- Real-time alert generation
- Alert streaming via WebSockets

### 🌐 API Layer

- REST API built with **FastAPI**
- WebSocket endpoint for live streaming
- `/stats` endpoint for snapshot metrics
- `/ws` endpoint for real-time updates

### 🖥️ Frontend Dashboard (React)

- Live updating UI using WebSockets
- Bandwidth visualization (Recharts line chart)
- Protocol distribution (pie chart)
- Top talkers ranking
- KPI cards (connections, PPS, bandwidth rate)
- Alert banner system (real-time warnings)

---

## 🧱 System Architecture

`````text
                 ┌─────────────────────┐
                 │   Network Traffic   │
                 └─────────┬───────────┘
                           │
                     [ Scapy Sniffer ]
                           │
                           ▼
                ┌─────────────────────┐
                │ Packet Processing   │
                │ - Parser            │
                │ - Aggregator        │
                └─────────┬───────────┘
                           │
                           ▼
             ┌──────────────────────────┐
             │ Metrics + Alert Engine   │
             │ - KPIs                  │
             │ - Anomaly Detection     │
             └─────────┬──────────────┘
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
  REST API (/stats)         WebSocket (/ws)
                                      │
                                      ▼
                         ┌─────────────────────┐
                         │ React Dashboard     │
                         │ - Charts            │
                         │ - Alerts            │
                         │ - KPI Cards         │
                         └─────────────────────┘



````markdown
## ▶️ Running the Project Locally

### 📦 Prerequisites

Before running the project, ensure you have the following installed:

#### Backend Requirements
- Python 3.10+
- pip
- Windows users: Install **Npcap** for packet capturing (required by Scapy)

👉 Download Npcap:
https://npcap.com/#download
✔ Make sure to enable **“WinPcap API-compatible mode”**

---

#### Frontend Requirements
- Node.js (LTS recommended)
- npm (or yarn)

---

## ⚙️ Backend Setup (FastAPI + Packet Sniffer)

### 1. Navigate to backend folder

```bash
cd backend
`````

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

#### Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If needed (recommended for stability):

```bash
pip install "uvicorn[standard]" scapy
```

---

### 4. Run backend server

```bash
uvicorn app.main:app --reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

WebSocket endpoint:

```
ws://127.0.0.1:8000/ws
```

---

### 📡 Test backend (optional)

Open in browser:

```
http://127.0.0.1:8000/stats
```

---

## 🌐 Frontend Setup (React Dashboard)

### 1. Navigate to frontend folder

```bash
cd frontend
```

---

### 2. Install dependencies

```bash
npm install
```

---

### 3. Start frontend development server

```bash
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

## 🔗 System Architecture Flow

```
Backend (FastAPI + Scapy)
        ↓
WebSocket (/ws real-time stream)
        ↓
React Frontend Dashboard
        ↓
Live Charts + Alerts + KPIs
```

---

## ⚠️ Important Notes

### 🧠 1. Start order matters

Always start backend before frontend.

---

### 🧠 2. Windows permissions

Packet capture may require Administrator privileges.

---

### 🧠 3. No traffic appearing?

Generate network activity:

- Open YouTube
- Browse websites
- Run ping commands

---

### 🧠 4. Firewall warnings

This is expected due to low-level packet sniffing (Scapy).
Allow access if prompted.

---

## 🚀 Quick Start Summary

```bash
# Backend
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

---

```

```
