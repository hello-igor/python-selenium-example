from selenium.webdriver.common.by import By


class LoginPageLocators:

    login = (By.ID, 'username')
    password = (By.ID, 'password')
    button = (By.ID, 'loginbtn')
    error = (By.ID, 'loginerrormessage')


class NavbarLocators:

    username = (By.XPATH, '//*[@id="action-menu-toggle-1"]/span/span[1]')
    dropdown = (By.XPATH, '//*[@id="action-menu-toggle-1"]')
    dropdown_profile = (By.XPATH, '//*[@id="actionmenuaction-2"]')


class LeftMenuLocators:
    site_administration = (By.XPATH, '//*[@id="nav-drawer"]/nav[2]/ul/li/a/div/div/span[2]')


class ProfilePageLocators:

    edit_profile = (By.XPATH, '//*[@id="region-main"]/div/div/div/section[1]/div/ul/li[1]/span/a')


class EditProfilePageLocators:

    name = (By.ID, 'id_firstname')
    surname = (By.ID, 'id_lastname')
    submit_button = (By.ID, 'id_submitbutton')


class SiteAdministrationLocators:

    courses = (By.XPATH, '//*[@id="region-main"]/div/ul/li[3]/a')
    add_new_course = (By.XPATH, '//*[@id="linkcourses"]/div/div[1]/div[2]/ul/li[4]/a')


class AddNewCoursePageLocators:

    course_full_name = (By.ID, 'id_fullname')
    course_short_name = (By.ID, 'id_shortname')
    save = (By.ID, 'id_saveanddisplay')


class CoursePageLocators:

    header = (By.XPATH, '//*[@id="page-header"]/div/div/div/div[1]/div[1]/div/div/h1')

