import framework_class

if __name__ == "__main__":
    
    result = framework_class.TestResult()
    loader = framework_class.TestLoader()
    suite = loader.make_suite(framework_class.TestLoaderTest)
    suite.run(result)
    print(result.summary())