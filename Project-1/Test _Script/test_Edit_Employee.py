import pytest
from Page_object_model.Edit_Employee import EditEmployee

@pytest.mark.usefixtures("setup")
class TestEditEmployee:

    def test_validate_edit_employee(self):
        # Create an instance of the EditEmployee class
        edit_emp = EditEmployee(self.driver)

        # Perform the edit operation by calling the appropriate methods
        # Parameters: Username ("Admin"), Password ("admin123"), New Middle Name ("janaki")
        edit_emp.login("Admin", "admin123")
        edit_emp.navigate_to_pim()
        edit_emp.select_employee_record()
        edit_emp.click_edit_employee()
        edit_emp.update_middle_name("janaki")
        edit_emp.save_changes()
        print("Test for editing employee validated successfully")
