def change_function_name(func, *args):
    func_name = func.__name__.title().replace('_', ' ')
    print('Имя функции: ' + func_name + '. Значение аргументов: ', *args)


def open_browser(browser_name):
    change_function_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    change_function_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    change_function_name(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://stepik.org/catalog")
find_registration_button_on_login_page(page_url="https://stepik.org/catalog", button_text="Войти")
