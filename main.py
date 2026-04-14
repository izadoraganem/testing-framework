import framework_class

if __name__ == "__main__":
    
        result = framework_class.TestResult()

        test = framework_class.TestCaseTest('test_result_success_run')
        test.run(result)

        test = framework_class.TestCaseTest('test_result_failure_run')
        test.run(result)

        test = framework_class.TestCaseTest('test_result_error_run')
        test.run(result)

        test = framework_class.TestCaseTest('test_result_multiple_run')
        test.run(result)

        test = framework_class.TestCaseTest('test_was_set_up')
        test.run(result)

        test = framework_class.TestCaseTest('test_was_run')
        test.run(result)

        test = framework_class.TestCaseTest('test_was_tear_down')
        test.run(result)

        test = framework_class.TestCaseTest('test_template_method')
        test.run(result)

        print(result.summary())