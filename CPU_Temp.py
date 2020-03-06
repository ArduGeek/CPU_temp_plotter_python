#!/usr/bin/env python3
import subprocess

def cpu_temp():
	output = subprocess.getoutput("sensors | grep Core")
	core1 = float(output[15:19])
	core2 = float(output[71:75])
	core3 = float(output[127:131])
	core4 = float(output[183:187])
	average = (core1+core2+core3+core4)/4
	return  average

if __name__=="__main__":
	print("Average CPU temeprature is : "+str(cpu_temp())+"°C")
