import os
os.chdir ("C:\Users\user\Desktop\CAnoPY")

import wallCalculations_ABDELAZIMSOLIMAN as WS

wallpara1 = [ 'Outside_Surface_Winter' , 'Gypsum' , 'Glass_Fiber' , 'Common_Brick' , 'Wood_Fiberboard' ,'Wood_Bevel', 'Inside_Surface' ]
wallpara2 = [ 'Outside_Surface_Winter' , 'Gypsum' , 'Wood_Stud' , 'Common_Brick' , 'Wood_Fiberboard' ,'Wood_Bevel', 'Inside_Surface' ]
f = [ 0.7 , 0.3 ]

results_thisWall = WS.wallcalc_withparallel ( wallpara1,wallpara2,f)

#the second function

layerlist_door = [ 'Outside_Surface_Winter' , 'Wood_50mm' , 'Inside_Surface' ]
layerlist_roof = [ 'Outside_Surface_Winter' , 'AsphaltShingleRoofing' ,
'Wood_Fiberboard' ,'Glass_Fiber' , 'Inside_Surface' ]

results_door = WS.wallCalc_onlyInSeries ( layerlist_door )
results_roof = WS.wallCalc_onlyInSeries ( layerlist_roof )

 # the heat transfer

Tin = 20
Tout = -4.8
delta_T = Tin - Tout

Wall_area = 105.8
Roof_area = 20*10
Door_area = 1*2.2

Qwall = Wall_area * delta_T * results_thisWall['Uoverall']
Qdoor = Door_area * delta_T * results_door ['Uoverall']
Qroof = Roof_area * delta_T * results_roof ['Uoverall']

Qtot = Qwall + Qdoor + Qroof

print "Qwall= " + str(Qwall) + "W"
print "Qdoor= " + str(Qdoor) + "W"
print "Qroof= " + str(Qroof) + "W"

print "Qtot= " + str (Qtot) + "W"