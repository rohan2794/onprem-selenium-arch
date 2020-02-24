import helpers.auxillary_modules as helper


def sign_up_page(driver, sign_up_test_suite_object, test_result):
    driver.get("https://account.mayadata.io/login")
    helper.AuxillaryModules.job_hold(2)
    pass
