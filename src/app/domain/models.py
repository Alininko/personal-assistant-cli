# TODO (Dev 1):
#
# class Contact(SQLModel, table=True): ...
# class Phone(SQLModel, table=True): ...


from __future__ import annotations

from datetime import date

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class Contact(SQLModel, table=True):
    # Primary key for SQLite table
    id: int | None = Field(default=None, primary_key=True)

    # Contact name, indexed for faster search
    name: str = Field(index=True)

    # Birthday is stored as date object, not string
    birthday: date | None = None

    # One contact can have many phones
    phones: list["Phone"] = Relationship(
        back_populates="contact",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )


class Phone(SQLModel, table=True):
    # Primary key for phone row
    id: int | None = Field(default=None, primary_key=True)

    # Phone number value
    value: str

    # Foreign key to contact table
    contact_id: int = Field(foreign_key="contact.id")

    # Back reference to owning contact
    contact: Contact = Relationship(back_populates="phones")

    @field_validator("value")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        # Keep original homework validation:
        # phone must contain exactly 10 digits
        if not v.isdigit() or len(v) != 10:
            raise ValueError("Phone must contain exactly 10 digits")
        return v
    

# TODO (Dev 2):
#
# class NoteTagLink(SQLModel, table=True): ...
# class Tag(SQLModel, table=True): ...
# class Note(SQLModel, table=True): ...
