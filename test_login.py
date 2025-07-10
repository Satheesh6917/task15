import pytest
from utils import driver_setup, excel_util
from pages.login_page import LoginPage

excel = excel_util.ExcelUtil("test_data.xlsx")
test_data = excel.get_test_data()

@pytest.mark.parametrize("test_id,username,password,date,time,tester,result", test_data)
def test_login(test_id, username, password, date, time, tester, result):
    driver = driver_setup.get_driver()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    success = login_page.is_login_successful()
    row_num = int(test_id) + 1
    if success:
        excel.write_result(row_num, "Test Passed")
    else:
        excel.write_result(row_num, "Test Failed")
    driver.quit()
