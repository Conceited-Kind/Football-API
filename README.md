# Football API

A RESTful API for managing football player data, built with Flask and Flask-RESTful.

## Features

- Add, update, delete, and list football players
- Swagger UI documentation with Flasgger
- Modular resource structure

## Requirements

- Python 3.8+
- pip

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Football-API.git
   cd Football-API
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the API:**
   - API endpoints: `http://localhost:5000/`
   - Swagger UI: `http://localhost:5000/apidocs/`

## Project Structure

```
Football-API/
├── app.py
├── requirements.txt
├── resources/
│   └── player.py
│   └── team.py
├── static
│   └── swagger.json
├── .gitignore
├── .venv/
└── README.md
```

> **Note:**  
> - `app.py`: Main application entry point  
> - `resources/`: Contains resource files for API endpoints  
> - `data.py`: Shared data or models  
> - `.venv/`: Virtual environment (should not be committed)  
> - `requirements.txt`: Python dependencies  
> - `README.md`: Project documentation  

## Example Endpoints

- `GET /players` — List all players
- `POST /players` — Add a new player
- `GET /players/<id>` — Get a specific player
- `PUT /players/<id>` — Update a player
- `DELETE /players/<id>` — Delete a player

