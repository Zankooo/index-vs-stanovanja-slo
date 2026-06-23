# Comparison: Stocks (S&P 500) vs. Real Estate

[🇸🇮 Preberi v slovenščini](./slo-readme/README.md)

An application for comparing the investment returns of real estate (apartments in Ljubljana) and the S&P 500 stock index from a selected year to the present day.

## 🌐 Live Website

https://index-vs-stanovanja-slo.vercel.app/

## Running the Project Locally

The project is divided into two parts: **Backend** (FastAPI) and **Frontend** (Vue.js + Vite).

### 1. Backend (FastAPI)

The backend handles calculations and serves data from JSON files.

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows:
    .venv\Scripts\activate
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Start the server:
    ```bash
    uvicorn main:app --reload
    ```
    The backend will be available at: `http://127.0.0.1:8000`


### 2. Frontend (Vue.js + Vite)


1.  Navigate to folder `frontend`:
    ```bash
    cd frontend
    ```
2.  Install dependencies (Node.js mora biti nameščen):
    ```bash
    npm install
    ```
3.  Run development server:
    ```bash
    npm run dev
    ```
    Frontend will be available on: `http://localhost:3001` (is set in file `package.json`)
