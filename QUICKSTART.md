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

## Accès aux Applications

- **API FastAPI**: http://localhost:8000
- **Documentation API**: http://localhost:8000/docs
- **Interface Streamlit**: http://localhost:8501

## Premiers Pas

### 1. Vérifier la santé de l'API
```bash
curl http://localhost:8000/api/system/health
```

### 2. Obtenir les statistiques
```bash
curl http://localhost:8000/api/stats/overview
```

### 3. Lister les clients
```bash
curl http://localhost:8000/api/customers?page=1&limit=10
```

### 4. Accéder à l'interface Streamlit
Ouvrir http://localhost:8501 dans votre navigateur

## Exécuter les Tests

```bash
# Tous les tests
pytest

# Avec rapport de couverture
pytest --cov=transaction_api --cov-report=html

# Tests spécifiques
pytest tests/integration/ -v
pytest tests/unit/ -v
```

## 📁 Structure des Fichiers Importants

```
├── app.py                    # Application Streamlit
├── requirements.txt          # Dépendances Python
├── README.md                 # Documentation complète
├── QUICKSTART.md            # Ce fichier
├── start.sh                 # Script de démarrage (Linux/Mac)
├── start.bat                # Script de démarrage (Windows)
├── transaction_api/
│   ├── main.py              # Application FastAPI
│   ├── repository.py        # Accès aux données
│   ├── routes/              # Endpoints API
│   └── services/            # Logique métier
├── tests/                   # Tests
│   ├── integration/
│   ├── unit/
│   └── properties/
└── data/
    └── transactions.csv     # Données
```

## Configuration

```

### Fichier de données
Le fichier `data/transactions.csv` doit contenir les colonnes:
- id, date, client_id, card_id, amount, use_chip, merchant_id, merchant_city, merchant_state, zip, mcc, errors

## Dépannage

### L'API ne démarre pas
```bash
# Vérifier que le port 8000 est libre
lsof -i :8000  # Linux/Mac
netstat -ano | findstr :8000  # Windows

# Vérifier les logs
python -m uvicorn transaction_api.main:app --reload --log-level debug
```

### Streamlit ne se connecte pas
- Vérifier que l'API est en cours d'exécution
- Vérifier l'URL dans `app.py` (ligne: `API_BASE_URL = "http://localhost:8000/api"`)
- Vérifier la connectivité réseau

### Erreurs de données
- Vérifier que `data/transactions.csv` existe
- Vérifier le format du CSV (encodage UTF-8)
- Vérifier que les dates sont au format `YYYY-MM-DD HH:MM:SS`
