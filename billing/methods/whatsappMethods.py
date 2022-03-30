from billing.locators.greenApiLocators import GreenApiLocators
from billing.baseApp import BasePage


class WhatsappMethods(GreenApiLocators, BasePage):

    def go_to_green_api_page(self):
        self.go_to_site(self.green_api_page_url)

    def authorize_green_api(self, login='karzovtest@bezlimit.ru', password='Bezlimit2022'):
        login_field = self.find_element('id', self.input_login_id)
        self.enter_at_field(login_field, login)

        password_field = self.find_element('id', self.input_password_id)
        self.enter_at_field(password_field, password)

        login_button = self.find_element('id', self.button_id)
        self.click_on_element(login_button)

    def go_to_first_project_url(self):
        self.go_to_site(self.green_api_first_project_url)

    def go_to_second_project_url(self):
        self.go_to_site(self.green_api_second_project_url)

    def chek_status(self):
        status_field = self.find_element('xpath', self.status_xpath)
        status_value = str(self.get_value_of_element(status_field))
        return status_value
