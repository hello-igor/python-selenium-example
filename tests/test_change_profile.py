import pytest
import allure
from src.pages import *
from data.users import *


@pytest.mark.usefixtures("setup")
class TestChangeProfile:

    @allure.feature('Проверка изменения данных профиля')
    @allure.story('Изменение данных студента')
    def test_change_student_profile(self):
        builder = StudentBuilder()
        student = builder.build() 
        page = LoginPage(self.driver)
        page.login(student.login, student.password)
        with allure.step('Проверка успешного входа студента'):
            assert page.check_username()
        page = HomePage(self.driver)
        page.goto_profile()
        page = ProfilePage(self.driver)
        page.goto_edit_profile()
        page = EditProfilePage(self.driver)
        page.change_profile(student.name, student.surname)
        with allure.step('Проверка изменения имени и фамилии студента'):
            assert page.check_username(student.name, student.surname)