# FastAPI + React Full Stack Tutorial

This project demonstrates how to build a full-stack application using FastAPI for the backend and React (Vite) for the frontend. The application is a simple fruit management system where users can add and view fruits.

## Project Structure

```
/fast-api-test
├── backend/           # FastAPI server
│   ├── main.py       # Main server file
│   └── requirements.txt
└── frontend/         # React application
    ├── src/
    ├── package.json
    └── vite.config.js
```

## Prerequisites

- Python 3.11+
- Node.js 16+
- npm or yarn

## Backend Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   python main.py
   ```
   The server will run on http://localhost:8000

## Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will run on http://localhost:5173

## API Endpoints

- `GET /fruits` - Get all fruits
- `POST /fruits` - Add a new fruit
  ```json
  {
    "name": "string"
  }
  ```

## Features

- FastAPI backend with CORS support
- React frontend with Vite
- Real-time updates
- Simple and clean UI
- RESTful API design

## Development

1. The backend uses FastAPI's built-in Pydantic models for data validation
2. CORS is configured to allow requests from the frontend (http://localhost:5173)
3. The frontend uses React hooks and custom components
4. API calls are abstracted into a separate `api.js` file

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
