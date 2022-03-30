from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import datetime as dt

import time


class BasePage:

    def __init__(self, browser):
        self.browser = browser

        self.base_page_url = 'https://bill.bezlimit.ru/site/login'

        self.username_textbox_id = 'loginform-username'
        self.password_textbox_id = 'loginform-password'
        self.login_button_css = "[type='submit']"

    def authorization_at_billing(self, login='butovich_v', password='Bezlimit2020'):
        """
        This function is needed for authorization at billing.

        :param login: login of user
        :param password: user's password
        :return: nothing
        """

        # self.go_to_site(self.base_page_url)

        login_field = self.find_element('id', self.username_textbox_id)
        self.clear_field(login_field)
        self.enter_at_field(login_field, login)

        password_field = self.find_element('id', self.password_textbox_id)
        self.clear_field(password_field)
        self.enter_at_field(password_field, password)

        login_button = self.find_element('css_selector', self.login_button_css)
        self.click_on_element(login_button)

        time.sleep(5)

    def clear_field(self, element):
        """
        This method is wrapper around the function 'element.clear()'

        :param element: It's your found field on a page
        :return: function 'element.clear()'
        """

        return element.clear()

    def click_on_element(self, element):
        """
        This method is wrapper around the function 'element.click()'.

        You must transfer your element to function as argument for click on web-element.
        """

        return element.click()

    def enter_at_field(self, element, text):
        """
        This method is wrapper around the function 'element.send_keys()'

        :param element: It's your found field on a page
        :param text: It's text, which you want to enter at the field
        :return: function 'element.send_keys(text)'
        """

        return element.send_keys(text)

    def find_element(self, method: str, locator, time=10):
        """
        Function returns web-element, if element is present on the DOM of a page.

        If element is not present on the DOM of a page, function returns error-message.

        At-first, you have to choose method from the list of methods:
        'id' for search element by id,
        'xpath' for search element by xpath,
        'link_text' for search element by link text,
        'partial_link_text' for search element by partial link text,
        'name' for search element by name,
        'tag_name' for search element by tag name,
        'class_name' for search element by class name,
        'css_selector' for search element by css selector,

        Secondly, you must enter a locator of element.

        Third argument of function is waiting time.
        Default value equals 10 seconds.
        """

        if method == 'id':
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.ID, locator)),
                                                           message=f"Can't find element by locator {locator}")
        elif method == 'xpath':
            try:
                WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.XPATH, locator)))
                return self.browser.find_element_by_xpath(locator)
            except Exception:
                print(f"Can't find element by locator {locator}")
                return None

        elif method == 'link_text':
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.LINK_TEXT, locator)),
                                                           message=f"Can't find element by locator {locator}")
        elif method == 'partial_link_text':
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,
                                                                                           locator)),
                                                           message=f"Can't find element by locator {locator}")
        elif method == 'name':
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.NAME, locator)),
                                                           message=f"Can't find element by locator {locator}")
        elif method == 'tag_name':
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.TAG_NAME, locator)),
                                                           message=f"Can't find element by locator {locator}")
        elif method == 'class_name':
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.CLASS_NAME, locator)),
                                                           message=f"Can't find element by locator {locator}")
        elif method == 'css_selector':
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)),
                                                           message=f"Can't find element by locator {locator}")

    def find_elements(self, method, locator, time=10):
        """
        Function returns list of web-elements, if elements are present on the DOM of a page.

        If elements are not present on the DOM of a page, function returns error-message.

        At-first, you have to choose method from the list of methods:
        'xpath' for search element by xpath,
        'link_text' for search element by link text,
        'partial_link_text' for search element by partial link text,
        'name' for search element by name,
        'tag_name' for search element by tag name,
        'class_name' for search element by class name,
        'css_selector' for search element by css selector,

        Secondly, you must enter a locator of elements.

        Third argument of function is waiting time.
        Default value equals 10 seconds.
        """

        if method == 'xpath':
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((By.XPATH, locator)),
                                                           message=f"Can't find elements by locator {locator}")
        elif method == 'link_text':
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((By.LINK_TEXT, locator)),
                                                           message=f"Can't find elements by locator {locator}")
        elif method == 'partial_link_text':
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,
                                                                                                locator)),
                                                           message=f"Can't find elements by locator {locator}")
        elif method == 'name':
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((By.NAME, locator)),
                                                           message=f"Can't find elements by locator {locator}")
        elif method == 'tag_name':
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((By.TAG_NAME, locator)),
                                                           message=f"Can't find elements by locator {locator}")
        elif method == 'class_name':
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                                                                locator)),
                                                           message=f"Can't find elements by locator {locator}")
        elif method == 'css_selector':
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                                                locator)),
                                                           message=f"Can't find elements by locator {locator}")

    @staticmethod
    def get_value_of_element(element):
        """
        This function is for getting text of element.

        :param element: Your element on page.
        :return: Element's text.
        """

        return element.text

    def go_to_site(self, url: str):
        """
        This method is wrapper around the function 'browser.get(url)'.

        You must enter your url as argument of this function for go to needed page.
        """

        return self.browser.get(url)

    @staticmethod
    def press_a_button_on_a_keyboard(element, key: str):
        """
        It is method-wrapper around the function 'browser.send_keys()'
        :param element: Your found web-element at page.
        :param key: 'Enter' for push ENTER or RETURN.
                    'PageUp' for push PAGE_UP.
                    'PageDown' for push PAGE_DOWN.
        :return: element.send_keys(Keys.key)
        """

        if key == 'Enter':
            return element.send_keys(Keys.ENTER)
        elif key == 'PageUp':
            return element.send_keys(Keys.PAGE_UP)
        elif key == 'PageDown':
            return element.send_keys(Keys.PAGE_DOWN)

    @staticmethod
    def calculate_time_difference(time_delta=30, read_time="1980-01-01 00:00:00",
                                  date_format='%Y-%m-%d %H:%M:%S', days=False):
        """
        It is function for calculate difference between two values of date-time.
        :param time_delta:
        :param read_time:
        :param date_format:
        :param days:
        :return:
        """
        if not days:
            now = dt.datetime.now()
            delta = dt.timedelta(minutes=time_delta)
        else:
            now = dt.datetime.today()
            delta = dt.timedelta(days=time_delta)
        read_time = dt.datetime.strptime(read_time, date_format)
        if now-read_time > delta:
            return True
        else:
            return False
