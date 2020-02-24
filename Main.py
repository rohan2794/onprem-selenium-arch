import pages.loginpage.page_test as login
import strategy.pkg_strategy as pkg

if __name__ == '__main__':

    print(f'Setting Up WebDrivers : \n1. Chrome(default)\n2. FireFox\nEnter your choice: ')
    # web_driver_choice = input()
    web_driver = {
        1: "Chrome",
        2: "FireFox",
    }
    web_driver_choice = 1
    if web_driver_choice == 1:
        print('Selecting Chrome as WebDriver')
    elif web_driver_choice == 2:
        print('Selecting FireFox as WebDriver')
    else:
        web_driver_choice = 1
        print('Selecting Chrome as default WebDriver')
    driver = pkg.select_web_driver(web_driver_choice)

    print(f'Executing Selenium Test on Director On-Prem Login Page')
    login.loginpage_test(driver)

    # # Closing the browser
    # print(f'Closing down {web_driver[web_driver_choice]} headless service')
    # driver.close()
    # Tearing down the connection
    print('Tearing down the connection')
    driver.quit()
