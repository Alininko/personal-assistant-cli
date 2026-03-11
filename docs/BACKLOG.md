# Backlog

Кожен розробник працює паралельно в окремій `feature/` гілці.

---

### Dev 1 — Contacts + Birthdays

Гілка: `feature/contacts`

- [ ] SQLModel-моделі в `domain/models.py`: Contact, Phone, Email (з relationships)
- [ ] `contacts_repository.py`: add, get_by_id, list_all, search, update, delete
- [ ] Метод `get_upcoming_birthdays(days)` в репозиторії
- [ ] Валідатори в `common/validators.py`: phone, email, birthday
- [ ] Unit-тести

---

### Dev 2 — Notes + Tags

Гілка: `feature/notes`

- [ ] SQLModel-моделі в `domain/models.py`: Note, Tag, NoteTagLink (many-to-many)
- [ ] `notes_repository.py`: add, get_by_id, list_all, search, search_by_tag, update, delete
- [ ] Unit-тести

---

### Dev 3 — CLI

Гілка: `feature/cli`

- [ ] CLI-команди в `contacts_commands.py`: add, list, search, delete, birthdays
- [ ] CLI-команди в `notes_commands.py`: add, list, search, by-tag, delete
- [ ] Rich-вивід в `presenters.py`: таблиці для контактів та нотаток
- [ ] Підключити sub-commands в `app.py`

---

### Dev 4 (Tech Lead) — Architecture + Services

- [x] Структура проєкту, pyproject.toml, requirements.txt
- [x] config.py, db.py, bootstrap.py
- [x] BaseRepository ABC, exceptions
- [x] .pre-commit-config.yaml, README, BACKLOG
- [ ] `contacts_service.py`: CRUD через репозиторій + валідація
- [ ] `notes_service.py`: CRUD через репозиторій
- [ ] `calendar_service.py`: upcoming birthdays через репозиторій
- [ ] Code review + інтеграція гілок
- [ ] Integration-тести

---

## Порядок мерджу

1. `feature/contacts` → `develop`
2. `feature/notes` → `develop`
3. `feature/cli` → `develop` (залежить від 1 і 2)
4. `develop` → `main`

## Важливо

- **models.py** — спільний файл, Dev 1 і Dev 2 домовляються про поля заздалегідь
- Pre-commit hooks мають проходити перед кожним комітом
