def test_page_title(browser):
    browser.get(browser.url)
    assert browser.title == "Your Store"
