import os
import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup_login(request,browser):
    driver=webdriver.Chrome(executable_path=r"C:\Users\new\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def url(request):
    return request.config.getoption("--url")


