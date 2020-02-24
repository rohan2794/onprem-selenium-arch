import strategy.drivers.strategy as wb


def select_web_driver(web_driver_choice):
    if web_driver_choice == 1:
        web_context = wb.WebContextClass(wb.ConcreteStrategyChrome())
        print(f'Chrome set as default Web-Driver')
        return web_context.execute_web_driver_strategy()
    else:
        web_context = wb.WebContextClass(wb.ConcreteStrategyFireFox())
        print(f'FireFox set as default Web-Driver')
        return web_context.execute_web_driver_strategy()
