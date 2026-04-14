import framework_class

if __name__ == "__main__":
    
    loader = framework_class.TestLoader()
    suite = loader.make_suite(framework_class.TestLoaderTest)

    runner = framework_class.TestRunner()
    runner.run(suite)