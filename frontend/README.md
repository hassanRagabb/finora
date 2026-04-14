## Required To Run

### 1) Set env in project root (`.env`)

```env
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/finora
OPENROUTER_API_KEY=sk-or-v1-...
```

### 2) Start backend

```powershell
cd D:\challengeAccepted\agentic\projects\FinoraLAST\smsm_github
python -m pip install -r requirements.txt
cd backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8001
```

### 3) Start frontend

```powershell
cd D:\challengeAccepted\agentic\projects\FinoraLAST\smsm_github\frontend
npm install
npm run dev
```

### 4) Open app

`http://localhost:3000`
