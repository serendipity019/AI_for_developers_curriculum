from sqlmodel import Field, Relationship, SQLModel

class Team(SQLModel, table=True):
    # primary key
    id: int | None = Field(default=None, primary_key=True)
    name: str

    # one-to-many relationship
    heroes: list["Hero"] = Relationship(back_populates="team")

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = None
    power: str
    # foreign key
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")

# Schema
class HeroUpdate(SQLModel):
    name: str | None = None
    power: str | None = None
    age: int | None = None
    team_id: int | None = None