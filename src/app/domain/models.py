from sqlmodel import Field, Relationship, SQLModel

# TODO (Dev 1):
#
# class Contact(SQLModel, table=True): ...
# class Phone(SQLModel, table=True): ...


# ── Notes + Tags (Dev 2) ──────────────────────────────────────────────


class NoteTagLink(SQLModel, table=True):
    """Link-таблиця для зв'язку many-to-many між Note і Tag."""

    note_id: int = Field(foreign_key="note.id", primary_key=True)
    tag_id: int = Field(foreign_key="tag.id", primary_key=True)


class Tag(SQLModel, table=True):
    """Тег для нотаток. Ім'я унікальне."""

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    notes: list["Note"] = Relationship(back_populates="tags", link_model=NoteTagLink)


class Note(SQLModel, table=True):
    """Нотатка з заголовком, тілом та тегами."""

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    body: str = ""

    tags: list[Tag] = Relationship(back_populates="notes", link_model=NoteTagLink)
