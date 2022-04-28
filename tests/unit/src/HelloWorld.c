
#include "CuTest.h"

void TestHelloWorld(CuTest *test){
	CuAssertIntEquals(test, 100, 100);
}

CuSuite *HelloSuite(){
	CuSuite* suite = CuSuiteNew();
	SUITE_ADD_TEST(suite, TestHelloWorld);
	return suite;
}
