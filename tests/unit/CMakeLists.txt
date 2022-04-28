
enable_testing()
add_executable(TestRunner framework/CuTest.c src/HelloWorld.c src/TestRunner.c)
target_include_directories(TestRunner PUBLIC include framework)
add_test(UnitTesting TestRunner)
