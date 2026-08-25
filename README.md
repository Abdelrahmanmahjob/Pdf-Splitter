# RequestSplitterPro

Full-stack app (FastAPI backend + React + Vite frontend) that splits PDFs into requests using OCR.

## Development

Prerequisites: Docker (optional), Node 18+, Python 3.12, virtualenv.

Backend (local):

```powershell
cd backend
venv312\Scripts\activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Frontend (local):

```bash
cd frontend
npm install
npm run dev
```

Use `frontend/.env` or root `.env.example` to set `VITE_API_URL` to `http://127.0.0.1:8000` for local development.

## Docker

Bring up both services with:

```bash
docker-compose up --build
```

Frontend will be available at `http://localhost:5173`, backend at `http://localhost:8000`.

## Notes

- Tests under `backend/tests/` are integration scripts that exercise OCR and require large models; they are not unit tests. Consider moving them to `scripts/` (some already moved) and mocking OCR in CI tests.
- For production, host the frontend behind a static server (nginx) and run backend with a process manager; consider GPU/CPU tuning for OCR models.
