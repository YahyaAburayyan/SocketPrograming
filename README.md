# ENCS3320 – Socket Programming & Web Server Project

## 👨‍💻 Team Project Overview
This project demonstrates the use of **socket programming** (TCP and UDP) and a **custom web server** using Python. The system includes communication between clients and a server using different protocols and a fully functional HTTP server that handles various types of requests.

---

## 📦 Contents

### ✅ Task 2: Socket Programming

1. **TCP Client-Server:**
   - Client sends text to the server.
   - Server replaces all vowels (`a, e, i, o, u` - upper/lower case) with `#`.
   - Server sends the modified text back to the client.

2. **UDP Peer-to-Peer Chat:**
   - Server listens on a port number derived from a student ID.
   - Multiple clients can send messages.
   - Server logs and displays the last received message from each client.
   - Each client sees only their own messages to/from the server.

---

### 🌐 Task 3: Custom Web Server

- Handles requests such as `/`, `/en`, `/ar`, `.html`, `.css`, `.jpg`, `.png`
- Supports English and Arabic versions of the homepage.
- Includes:
  - External CSS for styling
  - JPG and PNG images
  - Link to local HTML file (`mySiteSTDID.html`)
  - Link to Birzeit University website
- Implements:
  - `307 Temporary Redirect` for `/so` → StackOverflow and `/itc` → itc.birzeit.edu
  - Custom `404 Not Found` error page with styling and client info
  - Logs all HTTP requests in the terminal

---

## ⚙️ Technologies Used

- **Language:** Python
- **Protocols:** TCP, UDP, HTTP
- **Tools:** Python socket, HTML, CSS

---

## 📌 Usage

1. Run TCP/UDP server and clients from terminal using Python scripts.
2. Start the web server:
