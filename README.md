# SoftDesk Support - API REST

API REST pour le suivi de problèmes techniques dans des projets logiciels.

## 📋 Description

SoftDesk Support est une application B2B permettant aux équipes de :
- Créer et gérer des projets (backend, frontend, iOS, Android)
- Suivre des issues (bugs, fonctionnalités, tâches) avec priorités et statuts
- Ajouter des contributeurs aux projets
- Commenter les issues pour faciliter la communication

## 🛠️ Technologies utilisées

- Python 3.14.0
- Django 6.0.3 
- Django REST Framework 3.16.1
- Poetry 2.3.2

## 📦 Installation

### Prérequis

Avant de commencer, vous devez avoir installé :
- **Python 3.14** : [python.org/downloads](https://www.python.org/downloads/)
- **Poetry 2.3.2** : Gestionnaire de dépendances Python


### Installation du projet

**1. Cloner le repository**
```bash
git clone https://github.com/myriamdesporte/Softdesk-support.git
cd Softdesk-support
```

**2. Installer les dépendances**
```bash
poetry install --no-root
```

**3. Créer la base de données**
```bash
poetry run python manage.py migrate
```

**4. Créer un utilisateur administrateur**
```bash
poetry run python manage.py createsuperuser
```

Suivez les instructions (username, email, password).

**5. Lancer le serveur de développement**
```bash
poetry run python manage.py runserver
```

Le serveur est maintenant accessible sur : **http://127.0.0.1:8000/**

L'interface d'administration est accessible sur : **http://127.0.0.1:8000/admin/**


## 📡 Endpoints API disponibles

### Utilisateurs

| Méthode     | Endpoint         | Description |
|-------------|------------------|-------------|
| POST        | `/api/user/`     | Créer un utilisateur (signup) |
| GET         | `/api/user/`     | Lister tous les utilisateurs |
| GET         | `/api/user/{id}/` | Détails d'un utilisateur |
| PUT / PATCH | `/api/user/{id}/` | Modifier un utilisateur |
| DELETE      | `/api/user/{id}/` | Supprimer un utilisateur |

### Exemple de requête (création d'utilisateur)
```
POST http://127.0.0.1:8000/api/user/

{
    "username": "alice",
    "email": "alice@example.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!",
    "date_of_birth": "2000-05-15",
    "can_be_contacted": true,
    "can_data_be_shared": false
}
```