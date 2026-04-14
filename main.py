import framework_class

if __name__ == "__main__":
    
    loader = framework_class.TestLoader()
    test_case_suite = loader.make_suite(framework_class.TestCaseTest)
    test_suite_suite = loader.make_suite(framework_class.TestSuiteTest)
    test_load_suite = loader.make_suite(framework_class.TestLoaderTest)

    suite = framework_class.TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = framework_class.TestRunner()
    runner.run(suite)