# Guide d'installation GitLab Runner pour déploiement local

Ce guide vous explique comment installer et configurer GitLab Runner sur votre machine Windows pour déployer automatiquement sur Docker local.

## Prérequis

- Docker Desktop installé et fonctionnel
- GitLab Runner installé (voir ci-dessous)
- Accès à votre projet GitLab

## Installation de GitLab Runner sur Windows

### Option 1: Installation via exécutable (Recommandé)

1. **Télécharger GitLab Runner pour Windows:**
   - Allez sur: https://docs.gitlab.com/runner/install/windows.html
   - Téléchargez l'exécutable pour Windows (amd64)

2. **Installer GitLab Runner:**
   ```powershell
   # Créer un dossier pour GitLab Runner
   New-Item -ItemType Directory -Path "C:\GitLab-Runner"
   
   # Copier l'exécutable dans ce dossier
   # (remplacez gitlab-runner.exe par le chemin de votre fichier téléchargé)
   Copy-Item gitlab-runner.exe C:\GitLab-Runner\
   
   # Installer comme service Windows
   cd C:\GitLab-Runner
   .\gitlab-runner.exe install
   ```

### Option 2: Installation via Chocolatey

```powershell
# Installer Chocolatey si ce n'est pas déjà fait
# Puis installer GitLab Runner
choco install gitlab-runner
```

## Configuration du Runner

1. **Obtenir le token de registration:**
   - Allez sur votre projet GitLab
   - Settings → CI/CD → Runners → Expand
   - Copiez le "Registration token"

2. **Enregistrer le runner:**
   ```powershell
   cd C:\GitLab-Runner
   .\gitlab-runner.exe register
   ```

3. **Répondre aux questions:**
   - **GitLab instance URL:** `https://gitlab.com/` (ou votre instance GitLab)
   - **Registration token:** (collez le token copié)
   - **Description:** `Local Docker Runner`
   - **Tags:** `local-docker` (IMPORTANT: doit correspondre au tag dans .gitlab-ci.yml)
   - **Executor:** `docker`
   - **Default Docker image:** `docker:stable` ou `alpine:latest`

4. **Configurer le runner pour utiliser Docker local:**
   
   Éditez le fichier de configuration (généralement `C:\GitLab-Runner\config.toml`):
   
   ```toml
   [[runners]]
     name = "Local Docker Runner"
     url = "https://gitlab.com/"
     token = "VOTRE_TOKEN"
     executor = "docker"
     [runners.docker]
       tls_verify = false
       image = "docker:stable"
       privileged = true
       volumes = ["/var/run/docker.sock:/var/run/docker.sock"]
   ```
   
   **Pour Windows, la configuration doit être:**
   ```toml
   [[runners]]
     name = "Local Docker Runner"
     url = "https://gitlab.com/"
     token = "VOTRE_TOKEN"
     executor = "shell"
     [runners.custom_build_dir]
       enabled = true
   ```
   
   **OU utiliser l'executor "docker-windows":**
   ```toml
   [[runners]]
     name = "Local Docker Runner"
     url = "https://gitlab.com/"
     token = "VOTRE_TOKEN"
     executor = "docker-windows"
     [runners.docker]
       image = "mcr.microsoft.com/windows/servercore:ltsc2022"
   ```

## Démarrer le Runner

```powershell
# Démarrer le service
.\gitlab-runner.exe start

# Vérifier le statut
.\gitlab-runner.exe status

# Voir les logs
.\gitlab-runner.exe run
```

## Configuration recommandée pour Windows avec Docker Desktop

Pour que le runner puisse utiliser Docker sur Windows, utilisez l'executor `shell`:

1. **Réenregistrer le runner avec executor shell:**
   ```powershell
   .\gitlab-runner.exe unregister --name "Local Docker Runner"
   .\gitlab-runner.exe register
   ```
   - Choisissez `shell` comme executor

2. **Modifier le fichier config.toml:**
   ```toml
   [[runners]]
     name = "Local Docker Runner"
     url = "https://gitlab.com/"
     token = "VOTRE_TOKEN"
     executor = "shell"
     shell = "powershell"
     [runners.custom_build_dir]
       enabled = true
   ```

3. **Modifier le job deploy:local dans .gitlab-ci.yml:**
   Le job doit utiliser `image: docker:stable` mais avec l'executor shell, il exécutera directement les commandes Docker sur votre machine.

## Utilisation

Une fois le runner configuré et démarré:

1. **Pousser votre code sur GitLab:**
   ```bash
   git add .
   git commit -m "Configuration déploiement local"
   git push origin main
   ```

2. **Dans GitLab CI/CD:**
   - Allez dans CI/CD → Pipelines
   - Une fois le build terminé, cliquez sur le job `deploy:local`
   - Cliquez sur "Play" pour lancer le déploiement manuel

3. **Vérifier le déploiement:**
   ```powershell
   docker-compose ps
   # Votre application devrait être accessible sur http://localhost:8000
   ```

## Dépannage

### Le runner ne prend pas les jobs
- Vérifiez que le tag `local-docker` correspond dans GitLab et dans config.toml
- Vérifiez que le runner est actif dans GitLab (Settings → CI/CD → Runners)

### Erreur de connexion Docker
- Vérifiez que Docker Desktop est démarré
- Testez `docker ps` dans PowerShell

### Le runner ne trouve pas docker-compose
- Installez Docker Compose ou utilisez `docker compose` (sans tiret) dans le script

## Notes importantes

- Le job `deploy:local` est configuré avec `when: manual` - vous devez le déclencher manuellement depuis GitLab
- Le job s'exécute uniquement sur les branches `main`, `master`, et `dev`
- Assurez-vous que les variables CI/CD sont configurées dans GitLab (Settings → CI/CD → Variables):
  - `CI_REGISTRY_USER`
  - `CI_REGISTRY_PASSWORD`
  - `CI_REGISTRY`
