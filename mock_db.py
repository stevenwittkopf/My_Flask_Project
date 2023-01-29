import json


class DRGWeaponIdea:

    VALID_WEAPON_SLOTS: set[str] = \
        {"Primary", "Secondary"}
    VALID_CHARACTER_CLASSES: set[str] = \
        {"Engineer", "Scout", "Gunner", "Driller"}

    @classmethod
    def _validate_working_title(cls, db_drg_weapon_idea: object) -> str:
        if "workingTitle" not in db_drg_weapon_idea:
            raise KeyError("A working title is missing!")
        elif not isinstance(db_drg_weapon_idea["workingTitle"], str):
            raise ValueError("The working title provided is " +
                             "not of type `str`!")
        else:
            return db_drg_weapon_idea["workingTitle"]

    @classmethod
    def _validate_character_class(cls, db_drg_weapon_idea: object) -> str:
        if "characterClass" not in db_drg_weapon_idea:
            raise KeyError("A character class is missing!")
        elif not isinstance(db_drg_weapon_idea["characterClass"], str):
            raise ValueError("The character class provided is " +
                             "not of type `str`!")
        elif db_drg_weapon_idea["characterClass"] not in \
                cls.VALID_CHARACTER_CLASSES:
            raise ValueError("The character class provided must be in the " +
                             f"set {cls.VALID_CHARACTER_CLASSES}!")
        else:
            return db_drg_weapon_idea["characterClass"]

    @classmethod
    def _validate_weapon_slot(cls, db_drg_weapon_idea: object) -> str:
        if "weaponSlot" not in db_drg_weapon_idea:
            raise KeyError("A weapon slot is missing!")
        elif not isinstance(db_drg_weapon_idea["weaponSlot"], str):
            raise ValueError("The weapon slot attribute is not of type `str`")
        elif db_drg_weapon_idea["weaponSlot"] not in \
                cls.VALID_WEAPON_SLOTS:
            raise ValueError("The weapon slot provided must be " +
                             f" in the set {cls.VALID_WEAPON_SLOTS}")
        else:
            return db_drg_weapon_idea["weaponSlot"]

    @classmethod
    def _validate_description(cls, db_drg_weapon_idea: object) -> str:
        if "description" not in db_drg_weapon_idea:
            raise KeyError("A description is missing")
        elif not all(isinstance(line, str)
                     for line in db_drg_weapon_idea["description"]):
            raise ValueError("At least one line of the description is " +
                             "not a string!")
        else:
            return "".join(db_drg_weapon_idea["description"])

    def __init__(self, db_drg_weapon_idea: object) -> None:
        self.working_title = \
            self._validate_working_title(db_drg_weapon_idea)
        self.character_class = \
            self._validate_character_class(db_drg_weapon_idea)
        self.weapon_slot = \
            self._validate_weapon_slot(db_drg_weapon_idea)
        self.description = \
            self._validate_description(db_drg_weapon_idea)

    def __str__(self):
        return f"working title: {self.working_title}\n" + \
               f"character class: {self.character_class}\n" + \
               f"weapon slot: {self.weapon_slot}\n" + \
               f"description: {self.description}\n"


drg_weapon_idea_file = \
    open("mock_db/drg_weapon_ideas.json")
drg_weapon_idea_data: list[dict] = \
    json.load(drg_weapon_idea_file)

drg_weapon_idea_table: list[DRGWeaponIdea] = \
    [DRGWeaponIdea(drg_weapon_idea)
     for drg_weapon_idea in drg_weapon_idea_data]
for drg_weapon_idea in drg_weapon_idea_table:
    print(drg_weapon_idea)
