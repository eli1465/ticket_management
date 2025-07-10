from model.entity.person import Person
from model.repository.file_manager import *
from model.tools.validation import *

person_list = read_persons()

class PersonController:
    def save(self,person_id, name, family, age,username,password,is_locked,role):
        try:
            id_validator(person_id)
            name_validator(name)
            family_validator(family)
            age_validator(age)
            username_validator(username)
            password_validator(password)
            bool_validator(is_locked)
            role_validator(role)

            person = Person(person_id, name, family, age, username, password, is_locked, role)
            person_list.append(person)
            write_persons(person_list)
            return True, f"Person Saved Successfully: {person}"
        except:
            return False, f"Person Save Failed"

    def edit(self,person_id, name, family, age,username,password,is_locked,role):
        try:
            for index, p in enumerate(person_list):
                if p.person_id == person_id:
                    person_list[index] = Person(person_id, name, family, age, username, password, is_locked, role)
                    write_persons(person_list)
                    return True, f"Person Edited Successfully: {person_list[index]}"
            return False, "Person not found"
        except:
            return False, f"Person Edit Failed"

    def delete(self, person_id):
        try:
            for person in person_list:
                if person.person_id == person_id:
                    person_list.remove(person)
                    write_persons(person_list)
                return True, f"Person Removed Successfully - {person_id}"
        except :
            return False, f"Person Remove Failed"

    def find_all(self):
        try:
            return True, person_list
        except :
            return False, f"Can't Load Persons"

    def find_by_name_and_family(self,name,family):
        try:
            result = []
            for person in person_list:
                if person.name == name and person.family == family:
                    result.append(person)
            return True, result
        except :
            return False,f"Search Failed"