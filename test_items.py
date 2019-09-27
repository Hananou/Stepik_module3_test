import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_add_button(browser):
    browser.get(link)
    #time.sleep(30) # <=== раскомментируйте эту строку, чтоб визуально убедиться, что сайт магазина запущен на языке, переданном в параметрах
    assert browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket'), "Cтраница товара на сайте содержит кнопку добавления в корзину"

