import time
import datetime as dt

class BillingFunction(object):
    def authorize(self):
        self.get('https://bill.bezlimit.ru/site/login')

        time.sleep(7)

        login_input = self.find_element_by_id('loginform-username')

        login_input.send_keys('morozov_i')

        password_input = self.find_element_by_id('loginform-password')

        password_input.send_keys('Takkurwatak1')

        button_enter = self.find_element_by_xpath('//*[@id="login-form"]/div[4]/div[2]/div[1]/button')

        button_enter.click()


    def get_element(self, xpath):
        element = self.find_element_by_xpath(xpath)

        element_num = float(element.text)

        element_num = abs(int(element_num))

        return element_num


    def get_element_string(self, xpath):
        element = self.find_element_by_xpath(xpath)

        element_num = element.text

        return element_num


    def calculate_time_difference(self, time_delta=30, read_time="1980-01-01 00:00:00",
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
