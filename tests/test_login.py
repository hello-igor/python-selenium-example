import pytest
import allure
from src.pages import *
from data.users import *


@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.feature('Проверка авторизации')
    @allure.story('Авторизация ученика')
    def test_student_login(self):
        builder = StudentBuilder()
        student = builder.build()
        page = LoginPage(self.driver) 
        page.login(student.login, student.password)
        assert page.check_username()

    @allure.feature('Проверка авторизации')
    @allure.story('Авторизация администратора')
    def test_admin_login(self):
        builder = AdminBuilder()
        admin = builder.build()
        page = LoginPage(self.driver) 
        page.login(admin.login, admin.password)
        assert page.check_username()

    @allure.feature('Проверка авторизации')
    @allure.story('Авторизация несуществующего пользователя')
    def test_invalid_user_login(self):
        builder = InvalidUserBuilder()
        invalid_user = builder.build()
        page = LoginPage(self.driver) 
        page.login(invalid_user.login, invalid_user.password)
        assert page.check_error()
