#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include "first/second-a/module-helpers.h"

int32_t main()
{
	uint32_t ui32ResultOfSum;
	ui32ResultOfSum = ui32SafeAddValues(1, 2);

	printf("ui32ResultOfSum: %d\n",ui32ResultOfSum);
	scanf("%d", &ui32ResultOfSum);
	return 0;
}

/*** End of File ****/
