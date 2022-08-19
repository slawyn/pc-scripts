import ctypes

# Load DLL into memory.

hllDll = ctypes.WinDLL ("BISS1SL_interface.dll")

# Set up prototype and parameters for the desired function call.
# HLLAPI
'''
hllApiProto = ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
    ctypes.c_void_p,   # Parameters 1 ...
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p)   # ... thru 4.
	'''

hllApiProto = ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
	ctypes.c_void_p,   # Parameters 1 ...
    ctypes.c_void_p,
    ctypes.c_void_p,
)  
#hllApiParams = (1, "p1", 0), (1, "p2", 0), (1, "p3",0), (1, "p4",0),

hllApiParams =(1, "p1", 0), (1, "p2", 0), (1, "p3",0),
# Actually map the call ("HLLAPI(...)") to a Python name.

hllApi = hllApiProto (("BISS_GetInterfaceInfo", hllDll), hllApiParams)

# This is how you can actually call the DLL function.
# Set up the variables and call the Python name with them.

p1 = ctypes.c_int (1)
p2 = ctypes.c_char_p (0)
p3 = ctypes.c_int (1)
p4 = ctypes.c_int (0)
#hllApi (ctypes.byref (p1), p2, ctypes.byref (p3), ctypes.byref (p4))
print(hllApi())