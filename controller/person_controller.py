from model.entity.person import Person

person_list = []

class PersonController:
    def save(self, code, name, family, age):
        try:
            person = Person(code, name, family, age)
            person_list.append(person)
            return True, f"Person Saved Successfully {person}"
        except Exception as e:
            return False, f"Person Save Failed\n{e}"

    def edit(self, code, name, family, age):
        try:
            person = Person(code, name, family, age)
            return True, f"Person Edited Successfully {person}"
        except Exception as e:
            return False, f"Person Edit Failed\n{e}"

    def delete(self, code):
        try:
            return True, f"Person Removed Successfully - {code}"
        except Exception as e:
            return False, f"Person Remove Failed\n{e}"

    def find_all(self):
        try:
            return True, person_list
        except Exception as e:
            return False, f"Can't Load Persons"
    # to do
    #def find_by_name_and_family(self,name,family):