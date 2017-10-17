# -*- coding: utf-8 -*-

#
def wallcalc_withparallel ( wallpara1,wallpara2,f):
    
    
    #Definition of the material library as a dictionnary
    Material_library = { 'Outside_Surface_Winter' : 0.03 , 'Inside_Surface' : 0.12 , 'Wood_25mm' : 0.22 ,
    'Wood_Bevel' : 0.14 , 'Wood_Fiberboard' : 0.23 , 'Glass_Fiber' : 2.52 , 'Wood_Stud' : 0.63 , 'Gypsum' : 0.079 ,
    'Cement_Mortar' : 0.018 , 'Common_Brick' : 0.12 , 'Wood_Fiberboard' : 0.23 }
   
    #output a dictionnary with the resistances of all layers
    layers_wall_complete = wallpara1 + wallpara2
    
    RValues_layers = []
    for anylayer in layers_wall_complete:
        RValue_layers = Material_library[anylayer]
        RValues_layers.append(RValue_layers)
        print "this layer is: "+ anylayer
        print " Resist for this layer = "+ str(RValue_layers)
        
    
    #Unit thermal resistance and overall heat transfer in serie between studs
    R1_Studs = 0

    for anylayer in wallpara1 : 
        Studs_library = Material_library [anylayer]
        R1_Studs = R1_Studs + Studs_library
    U1_Studs = 1 / R1_Studs
    print U1_Studs

    #Unit thermal resistance and overall heat transfer in serie at studs

    R2_Studs = 0

    for anylayer in wallpara2 : 
        At_Studs_library = Material_library [anylayer]
        R2_Studs = R2_Studs + At_Studs_library
    U2_Studs = 1 / R2_Studs
    print U2_Studs

    #Calculation of the global overall heat transfer and the global resistance

    U_TOT = f[0] * U1_Studs + f[1] * U2_Studs
    R_TOT = 1 / U_TOT
    print "The overall Resistance R = " + str(R_TOT) + "m2°C/W"
    print "The overall heat transfer U = " + str(U_TOT) + "W/m2°C"

    results = { "Roverall" : R_TOT, "Rvalue of all layers" : RValue_layers , "Uoverall" : U_TOT}
    return results

#Informations for the function

wallpara1 = [ 'Outside_Surface_Winter' , 'Gypsum' , 'Glass_Fiber' , 'Common_Brick' , 'Wood_Fiberboard' ,'Wood_Bevel', 'Inside_Surface' ]
wallpara2 = [ 'Outside_Surface_Winter' , 'Gypsum' , 'Wood_Stud' , 'Common_Brick' , 'Wood_Fiberboard' ,'Wood_Bevel', 'Inside_Surface' ]
f = [ 0.7 , 0.3 ]

results_thisWall = wallcalc_withparallel ( wallpara1,wallpara2,f)

#**********************************************************************
#The second function “wallCalc_onlyInSeries” is a simplified version of the first function,

def wallCalc_onlyInSeries (layerlist) :
    
     #Definition of the material library as a dictionnary
    Material_library = { 'Outside_Surface_Winter' : 0.03 , 'Inside_Surface' : 0.12 , 'Wood_25mm' : 0.22 ,
    'Wood_Bevel' : 0.14 , 'Wood_Fiberboard' : 0.23 , 'Glass_Fiber' : 2.52 , 'Wood_Stud' : 0.63 , 'Gypsum' : 0.079 ,
    'Cement_Mortar' : 0.018 , 'Common_Brick' : 0.12 , 'Wood_Fiberboard' : 0.23 , 'AsphaltShingleRoofing' : 0.077}
    
    R_sr = 0
    
    for anylayer in layerlist :
        if (anylayer == 'Wood_50mm') :                          
            R_anylayer = Material_library [ 'Wood_25mm' ] * 50 / 25 
        else :
            R_anylayer = Material_library [ anylayer ] 
        R_sr = R_sr + R_anylayer
        print R_sr
        
        
    U_sr = 1 / R_sr
    print " the global overall Resistance R= " + str (R_sr) + "m2°C/W"

    print "the value of the global overall heat transfer U=" + str (U_sr) + "W/m2°C"
    
    results = {"Roverall" : R_sr , "Uoverall" : U_sr }
    return results
    
    
  
layerlist_door = [ 'Outside_Surface_Winter' , 'Wood_50mm' , 'Inside_Surface' ]
layerlist_roof = [ 'Outside_Surface_Winter' , 'AsphaltShingleRoofing' ,
'Wood_Fiberboard' ,'Glass_Fiber' , 'Inside_Surface' ]

results_door = wallCalc_onlyInSeries( layerlist_door )
results_roof = wallCalc_onlyInSeries ( layerlist_roof )







