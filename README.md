# Minecraft List Backend

Backend API do listy serwerów Minecraft, napisany w Pythonie (Django). Obsługuje kluczowe zasoby, takie jak użytkownicy, logowania, typy serwerów, wersje, serwery, polubienia i recenzje. 
Hostowane na Render: https://minecraft-list-backend.onrender.com/api/

---

##  Spis treści

- [Opis](#opis)  
- [Stack technologiczny](#stack-technologiczny)  
- [Endpointy API](#endpointy-api)  

---

##  Opis

API służy do zarządzania listą serwerów Minecraft. Umożliwia:  
- rejestrację i logowanie użytkowników  
- przeglądanie dostępnych typów i wersji serwerów  
- przeglądanie serwerów, dodawanie recenzji i polubień

---

##  Stack technologiczny

- Python (Django)  
- PostgreSQL
- Uruchamianie: `python manage.py` 
- Hostowane: Render — https://minecraft-list-backend.onrender.com/api/
---

##  Endpointy API

```json
{
  "users": "…/api/users/",
  "logins": "…/api/logins/",
  "server-types": "…/api/server-types/",
  "server-versions": "…/api/server-versions/",
  "liked-server": "…/api/liked-server/",
  "minecraft-server": "…/api/minecraft-server/",
  "review-server": "…/api/review-server/"
}
```

### Opis zasobów:

- **`/api/users/`** – zarządzanie użytkownikami (GET, POST, PUT, DELETE)  
- **`/api/logins/`** – logowania: autoryzacja użytkowników  
- **`/api/server-types/`** – typy serwerów (np. Survival, PvP)  
- **`/api/server-versions/`** – wersje serwerów (np. 1.16, 1.20)  
- **`/api/minecraft-server/`** – CRUD serwerów  
- **`/api/liked-server/`** – polubienia serwerów przez użytkowników  
- **`/api/review-server/`** – recenzje serwerów

---

##  License

Licencja MIT
