from selenium import webdriver
from src.locators import *


class BasePage(object):

    def __init__ (self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def set_login(self, login):
        login_element = self.driver.find_element(*LoginPageLocators.login)
        login_element.send_keys(login)

    def set_password(self, password):
        password_element = self.driver.find_element(*LoginPageLocators.password)
        password_element.send_keys(password)

    def submit(self):
        submit_element = self.driver.find_element(*LoginPageLocators.button)
        submit_element.click()

    def check_username(self):
        username_element = self.driver.find_element(*NavbarLocators.username)
        if username_element.is_displayed():
            return True

    def check_error(self):
        error_element = self.driver.find_element(*LoginPageLocators.error)
        if error_element.is_displayed():
            return True

    def login(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.submit()


class HomePage(BasePage):

    def goto_profile(self):
        dropdown_element = self.driver.find_element(*NavbarLocators.dropdown)
        dropdown_element.click()
        profile_element = self.driver.find_element(*NavbarLocators.dropdown_profile)
        profile_element.click()

    def goto_site_administration(self):
        site_administration_element = self.driver.find_element(*LeftMenuLocators.site_administration)
        site_administration_element.click()


class ProfilePage(BasePage):

    def goto_edit_profile(self):
        edit_profile_element = self.driver.find_element(*ProfilePageLocators.edit_profile)
        edit_profile_element.click()


class EditProfilePage(BasePage):

    def set_name(self, name):
        name_element = self.driver.find_element(*EditProfilePageLocators.name)
        name_element.clear()
        name_element.send_keys(name)

    def set_surname(self, surname):
        surname_element = self.driver.find_element(*EditProfilePageLocators.surname)
        surname_element.clear()
        surname_element.send_keys(surname)

    def submit(self):
        submit_element = self.driver.find_element(*EditProfilePageLocators.submit_button)
        submit_element.click()

    #TODO: изменить проверку имени пользователя 
    def check_username(self, name, surname):
        username_element = self.driver.find_element(*NavbarLocators.username)
        if name in username_element.text and surname in username_element.text:
            return True

    def change_profile(self, name, surname):
        self.set_name(name)
        self.set_surname(surname)
        self.submit()


class SiteAdministrationPage(BasePage):

    def goto_add_new_course(self):
        courses_element = self.driver.find_element(*SiteAdministrationLocators.courses)
        courses_element.click()
        add_new_course_element = self.driver.find_element(*SiteAdministrationLocators.add_new_course)
        add_new_course_element.click()


class AddNewCoursePage(BasePage):

    def set_full_name(self, full_name):
        full_name_element = self.driver.find_element(*AddNewCoursePageLocators.course_full_name)
        full_name_element.send_keys(full_name)

    def set_short_name(self, short_name):
        short_name_element = self.driver.find_element(*AddNewCoursePageLocators.course_short_name)
        short_name_element.send_keys(short_name)

    def save(self):
        save_element = self.driver.find_element(*AddNewCoursePageLocators.save)
        save_element.click()

    def check_course(self, full_name):
        header_element = self.driver.find_element(*CoursePageLocators.header)
        if header_element.text == full_name:
            return True

    def add_new_course(self, full_name, short_name):
        self.set_full_name(full_name)
        self.set_short_name(short_name)
        self.save()




