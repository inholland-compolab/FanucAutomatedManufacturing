After performing the initial start the factory-set mastering data is also erased.
To get this back you have to load the "sysmast.sv" file (in the back-up folder of the robot) in the controlled start menu.


CALIBRATING THE ROBOT:

 after that you have to calibrate (not mastering!) the robot again.

	Menu -> [0] -- NEXT -- -> [6] SYSTEM -> [3] Master/Cal -> [7] CALIBRATE

  		- If the [3] Master/Cal is not visible in the system menu you have to enable the MASTER.
     	 	Menu -> [0] -- NEXT -- -> [6] SYSTEM -> [2] Variables -> [319] MASTER_ENB 
    	  	set system variable $MASTER_ENB to 1, and perform the previous step again.


		# Afer calibration you are able to jog the robot in WORLD coördinates.

ALARM CODES SOLVING:

	Hand Broken Alarm: SRVO-006 SERVO Hand broken.
	The robot will give a broken hand alarm, we have to disable this alarm.
	- Menu -> [0] -- NEXT -- -> [6] SYSTEM -> [2] Variables -> [569] $SCR_GRP -> [F2] DETAIL -> [99]$HBK_ENBL
	Set system variable $HBK_ENBL to FALSE

RUNNING DRIVERS:

	To run the driver you have to run a KAREL programm (.PC)
	Check if the KAREL option is enabled in the system variables.
	- Menu -> [0] -- NEXT -- -> [6] SYSTEM -> [2] Variables -> [287] $KAREL_ENB
	  set system variable $KAREL_ENB to 1








