# Guide de Démarrage Rapide

## Installation Rapide

### 1. Cloner le projet
```bash
git clone <repository-url>
cd transaction-analytics
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Lancer l'application

#### Option 1: Script automatique (Linux/Mac)
```bash
chmod +x start.sh
./start.sh
```

#### Option 2: Script automatique (Windows)
```bash
start.bat
```

#### Option 3: Lancer manuellement

Terminal 1 - Démarrer l'API:
```bash
python -m uvicorn transaction_api.main:app --reload --workers 1
```

Terminal 2 - Démarrer Streamlit:
```bash
streamlit run app.py
```