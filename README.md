# Primerjava: Delnice (S&P 500) vs. Stanovanja

Aplikacija za primerjavo donosnosti investicij v nepremičnine (stanovanja v Ljubljani) in delniški indeks S&P 500 skozi leta.

## Navodila za zagon

Projekt je razdeljen na dva dela: **Backend** (FastAPI) in **Frontend** (Vue.js + Vite).

---

### 1. Backend (FastAPI)

Backend skrbi za izračune in serviranje podatkov iz JSON datotek.

1.  Pojdi v mapo `backend`:
    ```bash
    cd backend
    ```
2.  Ustvari in aktiviraj virtualno okolje:
    ```bash
    python -m venv .venv
    # Na macOS/Linux:
    source .venv/bin/activate
    # Na Windows:
    .venv\Scripts\activate
    ```
3.  Namesti potrebne knjižnice:
    ```bash
    pip install -r requirements.txt
    ```
4.  Zaženi strežnik:
    ```bash
    uvicorn main:app --reload
    ```
    Backend bo dosegljiv na: `http://127.0.0.1:8000`

---

### 2. Frontend (Vue.js + Vite)

Frontend poskrbi za uporabniški vmesnik in vizualizacijo podatkov.

1.  Pojdi v mapo `frontend`:
    ```bash
    cd frontend
    ```
2.  Namesti pakete (Node.js mora biti nameščen):
    ```bash
    npm install
    ```
3.  Zaženi razvojni strežnik:
    ```bash
    npm run dev
    ```
    Frontend bo dosegljiv na: `http://localhost:3001` (kot je nastavljeno v `package.json`)

---
