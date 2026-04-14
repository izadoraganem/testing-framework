import framework_class

if __name__ == "__main__":
    
    result = framework_class.TestResult()

    test = framework_class.MyTest('test_a')
    test.run(result)

    test = framework_class.MyTest('test_b')
    test.run(result)

    test = framework_class.MyTest('test_c')
    test.run(result)

    print(result.summary())