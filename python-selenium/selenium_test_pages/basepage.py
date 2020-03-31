import os
import time

from framework import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

basepagelog = logger.Logger('Basepage').getLogger()


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 退出驱动并关闭所有窗口
    def quit_browser(self):
        self.driver.quit()

    # 关闭当前窗口
    def close_browser(self):
        self.driver.close()

    # 前进
    def for_word(self):
        self.driver.forward()

    # 后退
    def back(self):
        self.driver.back()

    # 最大化窗口
    def max_window(self):
        self.driver.maximize_window()

    # 转向url
    def go_url(self, url):
        self.driver.get(url)

    # 隐式等待
    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 强制等待
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    # 显式等待
    def wait_element(self, seconds, element):
        try:
            WebDriverWait(self.driver, seconds).until(element)
        except TimeoutException as te:
            basepagelog.error('%sLocal the %s element time out' % (element.text))

    # 获取网页标题
    def get_title(self):
        return self.driver.title

    # 获取网页url
    def get_url(self):
        return self.driver.current_url

    # 截图
    def get_windows_img(self):
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        path = os.path.dirname(os.getcwd()) + '/screenshots/'
        screenname = path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screenname)
        except NameError as e:
            basepagelog.error("Failed to take screenshot! %s" % e)
            self.getWindowsImg()

    # 定位元素
    def find_element(self, selector):
        el = ''
        if '=>' not in selector:
            basepagelog.error('Selector format is wrong!')
            return
        else:
            selector_by, selector_value = selector.split('=>')
            if selector_by.lower() == 'id':
                try:
                    el = self.driver.find_element_by_id(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            elif selector_by.lower() == 'class_name':
                try:
                    el = self.driver.find_element_by_class_name(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            elif selector_by.lower == 'tag_name':
                try:
                    el = self.driver.find_element_by_tag_name(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            elif selector_by.lower() == 'name':
                try:
                    el = self.driver.find_element_by_name(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            elif selector_by.lower() == 'link_text':
                try:
                    el = self.driver.find_element_by_link_text(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            elif selector_by.lower() == 'partial_link_text':
                try:
                    el = self.driver.find_element_by_partial_link_text(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            elif selector_by.lower == 'css_selector':
                try:
                    el = self.driver.find_element_by_css_selector(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            elif selector_by.lower() == 'xpath':
                try:
                    el = self.driver.find_element_by_xpath(selector_value)
                except NoSuchElementException as nsee:
                    basepagelog.error('NoSuchElementException: %s' % nsee)
            else:
                basepagelog.error('Have no this method loacl the emlement by %s' % selector_by)
        return el

    # 点击
    def click(self, element):
        element.click()

    # 提交表单
    def submit(self, element):
        element.submit()

    # 清除
    def clear(self, element):
        element.clear()

    # 键入
    def type(self, element, text):
        element.clear()
        element.send_keys(text)

    # 获取文本
    def get_text(self, element):
        return element.text

    # 切换frame
    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    # 从frame中切换到主文档
    def switch_to_content(self):
        self.driver.switch_to.default_content()

    # 从子frame切回到父frame，主要用于嵌套frame的操作
    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    # 切换到对话框
    def switch_to_alter(self):
        return self.driver.switch_to.alert

    # 对话框点击确认
    def accept_alter(self, alter):
        alter.accept()

    # 对话框点击取消
    def dis_miss_alter(self, alter):
        alter.dismiss()

    # 切换window
    def switch_to_window(self, window_hand):
        self.driver.switch_to.window(window_hand)

    # 得到当前window句柄
    def get_current_window_wandle(self):
        return self.driver.current_window_handle

    # 得到所有window句柄
    def get_window_handles(self):
        return self.driver.window_handles

    # 执行JavaScript脚本
    def excute_js(self, js):
        self.driver.execute_script(js)

    # 鼠标右击
    def right_click(self, element):
        ActionChains(self.driver).context_click(element).perform()

    # 鼠标双击
    def double_click(self, element):
        ActionChains(self.driver).double_click(element).perform()

    # 拖拽元素
    def drag_and_drop(self, element1, element2):
        ActionChains(self.driver).drag_and_drop(element1, element2).perform()

    # 移动到元素
    def move_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    # 判断元素是否显示
    def is_displayed(self, element):
        return (element.is_displayed())

    # 刷新
    def F5(self):
        self.driver.refresh()

    # 获取cookie
    def get_cookie(self):
        return self.driver.get_cookie()

    # 删除指定cookie
    def delete_cookie(self):
        self.driver.delete_cookie()

    # 删除所有cookie
    def delete_all_cookie(self):
        self.driver.delete_all_cookie()

    # 向cookie添加会话
    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)
