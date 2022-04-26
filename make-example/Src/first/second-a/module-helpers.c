

#include "first/second-a/module-helpers.h"




/*********************************************
*
*             Macros
*
**********************************************/
#define defHalfOfUint32 (~((((uint32_t)0)-1)>>1))



/*********************************************
*
*             Functions
*
**********************************************/



uint32_t ui32SafeAddValues(uint32_t ui32Value0, uint32_t ui32Value1)
{
	uint32_t ui32Result;

  ui32Result = ui32Value0 + ui32Value1;
	if((ui32Value0>defHalfOfUint32 || ui32Value1>defHalfOfUint32) && (ui32Result<defHalfOfUint32))
	{
			ui32Result = 0;
	}

	return ui32Result;
}

/*** End of File ****/
