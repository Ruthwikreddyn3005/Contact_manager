# 📇 Contact Management App (Flask + React)

A simple **full-stack contact management application** built with **Flask** (Python) for the backend and **React** (JavaScript) for the frontend.

---

## 📌 Features
- Create, view, update, and delete contacts.
- REST API backend using **Flask**.
- Frontend built with **React**.
- Database powered by **SQLite** via **Flask-SQLAlchemy**.
- Cross-Origin Resource Sharing (CORS) enabled using **Flask-CORS**.
- Modern responsive UI.

---

## 🛠️ Tech Stack

### **Frontend**
- React
- JavaScript (ES6+)
- HTML5
- CSS3

### **Backend**
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- SQLite

---

## 📂 Project Structure
project1/
│
├── backend/
│ ├── main.py # Flask app entry point
│ ├── models.py # Database models (Contact)
│ ├── config.py # Flask configurations (DB URI, settings)
│ ├── requirements.txt # Python dependencies
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx # Main React component
│ │ ├── ContactList.jsx # Displays list of contacts
│ │ ├── ContactForm.jsx # Create/Update contact form
│ │ ├── index.js # React entry point
│ ├── package.json # NPM dependencies
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Backend (Flask)
```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python main.py

# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Run React development server
npm run dev

