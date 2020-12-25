import pytest
import allure
from src.pages import *
from data.users import *
from data.courses import *


@pytest.mark.usefixtures("setup")
class TestAddCourse:

    @allure.feature('Проверка создания нового курса курса')
    @allure.story('Создание курса "Программирование"')
    def test_add_course(self):
        builder = AdminBuilder()
        admin = builder.build()
        page = LoginPage(self.driver) 
        page.login(admin.login, admin.password)
        with allure.step('Проверка входа администратора'):
            assert page.check_username()
        builder = ProgrammingCourseBuilder()
        programming_course = builder.build()
        page = HomePage(self.driver)
        page.goto_site_administration()
        page = SiteAdministrationPage(self.driver)
        page.goto_add_new_course()
        page = AddNewCoursePage(self.driver)
        page.add_new_course(programming_course.full_name, programming_course.short_name)
        with allure.step('Проверка создания курса'):
            assert page.check_course(programming_course.full_name)