
#include <stdio.h>
#include <stdlib.h>
#include "CuTest.h"

CuSuite *HelloSuite();

int RunAllTests(){
	CuString *output = CuStringNew();
	CuSuite* suite = CuSuiteNew();

	CuSuiteAddSuite(suite, HelloSuite());

	CuSuiteRun(suite);
	CuSuiteSummary(suite, output);
	CuSuiteDetails(suite, output);
	printf("%s\n", output->buffer);
	return suite->failCount;
}

int main(){
	return RunAllTests();
}
