class TestCase:
    def __init__(self, specification, expected_output, test_type, *args):
        self.specification = specification
        self.expected_output = expected_output
        self.test_type = test_type
        self.args = args


class LoginTestSuite:
    @staticmethod
    def get_signin_suite():
        suite = []
        testcase = TestCase("TestCase - Local Authentication with Wrong username and password",
                            "The email address or password you entered is incorrect.",
                            "negative",
                            "wrong_username",
                            "wrong_password")
        suite.append(testcase)
        testcase = TestCase("Test case - Local Authentication with right username and password",
                            "https://portal.mayadata.io/",
                            "positive",
                            "aditya@mayadata.io",
                            "adiTYA123@")
        suite.append(testcase)
        return suite

    @staticmethod
    def get_link_suite():
        forgot_password_suite = []
        service_terms_suite = []
        testcase = TestCase("Test Case - Forgot Password link click validation",
                            "https://account.mayadata.io/forgot-password",
                            "positive",
                            "")
        forgot_password_suite.append(testcase)

        testcase = TestCase("Test Case - MayaData’s Terms of Service link validation",
                            "https://mayadata.io/terms",
                            "positive",
                            "")
        service_terms_suite.append(testcase)
        return forgot_password_suite, service_terms_suite

    @staticmethod
    def get_button_suite():
        git_button_suite = []
        google_button_suite = []
        sign_up_button_suite = []
        testcase = TestCase("Test Case - Github button click validation",
                            "https://github.com/login",
                            "positive",
                            "")
        git_button_suite.append(testcase)

        testcase = TestCase("Test Case - Google button click validation",
                            "https://accounts.google.com/signin/oauth/identifier",
                            "positive",
                            "")
        google_button_suite.append(testcase)

        testcase = TestCase("Test Case - SignUp button click validation",
                            "https://account.mayadata.io/signup",
                            "positive",
                            "")
        sign_up_button_suite.append(testcase)
        return git_button_suite, google_button_suite, sign_up_button_suite
