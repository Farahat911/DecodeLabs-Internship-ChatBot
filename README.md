# Rule-Based AI Chatbot API

A high-performance, production-ready Rule-Based Chatbot built as a RESTful API using **FastAPI**. Developed as Project 1 for the DecodeLabs Artificial Intelligence Internship.

## 🚀 Features

* **O(1) Time Complexity:** Completely eliminates `if-elif` ladders by utilizing Hash Maps (Dictionaries) for instant intent matching and response retrieval.
* **Separation of Concerns (Data & Logic):** The knowledge base is strictly separated from the application logic and stored in a lightweight `data.json` file.
* **Production-Ready Backend:** Built on top of FastAPI, providing automatic interactive API documentation (Swagger UI).
* **Sanitization & Fallbacks:** Includes built-in text sanitization and atomic lookup operations with automatic fallback mechanisms for unknown inputs.
* **Clean Code Architecture:** Developed with strict adherence to clean code principles.

## 🛠️ Tech Stack

* **Language:** Python 3
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Data Format:** JSON

## 📂 Project Structure

├── main.py
├── data.json
└── README.md

## ⚙️ Installation & Setup

1. **Clone the repository:**
   git clone <your-repository-url>
   cd DecodeLabs-Internship/Project_1

2. **Install dependencies:**
   pip install fastapi uvicorn

3. **Run the API server:**
   uvicorn main:app --reload

## 🔌 API Usage

**Endpoint:** `POST /chat`

**Request Payload:**
{
    "message": "hello"
}

**Response:**
{
    "reply": "Hi there! Welcome to DecodeLabs."
}

## 📝 License

This project was developed for the DecodeLabs Industrial Training Kit (Batch 2026).
