from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import pages.loginpage.test_suite as test_suite
import helpers.auxillary_modules as helper


# OK
def sign_in_validator(driver, testcase, test_result):
    if testcase.test_type == "positive":
        if driver.current_url.find(testcase.expected_output) == 0:
            print(f'{testcase.specification} successful !')
            test_result.pass_result_update()
        else:
            print(f'{testcase.specification} failed !')
            test_result.pass_result_update()
    elif testcase.test_type == "negative":
        alert_message = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div[1]/div").text
        if alert_message == testcase.expected_output:
            print(f'{testcase.specification} successful !')
            test_result.pass_result_update()
        else:
            print(f'{testcase.specification} failed !')
            test_result.fail_result_update()


def sign_in_test(driver, sign_in_test_suite_object, test_result):
    driver.get("https://account.mayadata.io/login")
    helper.AuxillaryModules.job_hold(2)
    for testcase in sign_in_test_suite_object:
        # Logging the test case specification
        print(f'Executing {testcase.specification}')

        # Checking the Work Email
        work_email_input_field = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[3]/div/div[1]/form/div[1]/input")
        work_email_input_field.clear()
        work_email_input_field.send_keys(testcase.args[0])
        helper.AuxillaryModules.job_hold(2)

        # Checking the Password
        password_input_field = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[3]/div/div[1]/form/div[2]/input")
        password_input_field.clear()
        password_input_field.send_keys(testcase.args[1])
        helper.AuxillaryModules.job_hold(2)

        # Checking the Sign In button
        sign_in_button = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[3]/div/div[1]/form/button").click()
        helper.AuxillaryModules.job_hold(6)
        sign_in_validator(driver, testcase, test_result)


# OK
def link_validator(driver, testcase, test_result):
    if testcase.test_type == "positive":
        if driver.current_url == testcase.expected_output:
            print(f'{testcase.specification} successful !')
            test_result.pass_result_update()
        else:
            print(f'{testcase.specification} failed !')
            test_result.fail_result_update()


def link_test(driver, forgot_password_test_suite_object, service_terms_suite_object, test_result):
    driver.get("https://account.mayadata.io/login")
    helper.AuxillaryModules.job_hold(2)

    for testcase in forgot_password_test_suite_object:
        forgot_password_link = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div[1]/form/div[2]/div/span")
        forgot_password_link.click()
        helper.AuxillaryModules.job_hold(5)
        print(f'Executing {testcase.specification}')
        link_validator(driver, testcase, test_result)

    driver.get("https://account.mayadata.io/login")
    helper.AuxillaryModules.job_hold(2)

    for testcase in service_terms_suite_object:
        service_terms_link = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div[4]/span/a")
        service_terms_link.click()
        helper.AuxillaryModules.job_hold(3)
        driver.switch_to.window(driver.window_handles[1])
        print(f'Executing {testcase.specification}')
        link_validator(driver, testcase, test_result)


# OK
def button_validator(driver, testcase, test_result):
    if testcase.test_type == "positive":
        url = driver.current_url
        if url.find(testcase.expected_output) == 0:
            print(f'{testcase.specification} successful !')
            test_result.pass_result_update()
        else:
            print(f'{testcase.specification} failed !')
            test_result.fail_result_update()


def button_test(driver, git_button_suite_object, google_button_suite_object, sign_up_button_test_suite_object,
                test_result):
    for testcase in git_button_suite_object:
        driver.get("https://account.mayadata.io/login")
        helper.AuxillaryModules.job_hold(5)

        print(f'Executing {testcase.specification}')

        git_button = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[3]/div/div[3]/div/div/div[1]/div/button"
        )
        git_button.click()
        helper.AuxillaryModules.job_hold(5)
        button_validator(driver, testcase, test_result)

    driver.get("https://account.mayadata.io/login")
    helper.AuxillaryModules.job_hold(2)
    for testcase in google_button_suite_object:
        print(f'Executing {testcase.specification}')

        google_button = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[3]/div/div[3]/div/div/div[2]/div/button"
        )
        google_button.click()
        helper.AuxillaryModules.job_hold(5)
        button_validator(driver, testcase, test_result)

    driver.get("https://account.mayadata.io/login")
    helper.AuxillaryModules.job_hold(2)
    for testcase in sign_up_button_test_suite_object:
        print(f'Executing {testcase.specification}')

        sign_up_button = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[3]/div/div[5]/div/button"
        )
        sign_up_button.click()
        button_validator(driver, testcase, test_result)


def driver_job(driver):
    sign_in_test_suite_object = test_suite.LoginTestSuite.get_signin_suite()
    forgot_password_test_suite_object, service_terms_suite_object = test_suite.LoginTestSuite.get_link_suite()
    git_button_suite_object, google_button_suite_object, sign_up_button_test_suite_object = test_suite.LoginTestSuite.get_button_suite()

    total = sign_in_test_suite_object.__len__() + \
            forgot_password_test_suite_object.__len__() + \
            git_button_suite_object.__len__() + \
            google_button_suite_object.__len__() + \
            sign_up_button_test_suite_object.__len__() + \
            service_terms_suite_object.__len__()

    test_result = helper.TestResults(total)

    # Checking the Forgot Password? Link
    link_test(driver, forgot_password_test_suite_object, service_terms_suite_object, test_result)

    # Checking for the click validation for the Github button and the Google button
    button_test(driver, git_button_suite_object,
                google_button_suite_object, sign_up_button_test_suite_object,
                test_result)

    # Checking for the Sign-In functionality
    sign_in_test(driver, sign_in_test_suite_object, test_result)

    test_result.print_result()


def loginpage_test(driver):
    print('Executing page_test.py')
    driver_job(driver)

    # Checking MayaData’s Terms of Service link

    # Checking Sign Up button
