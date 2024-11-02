import openvsp as vsp

opt = {
    # Flow conditons
    'alphaStart': 0,
    'betaStart': 0,
    'alphaEnd': 5,
    'betaEnd': 0,    
    'mach': 0.1,
    'ReCref': 1e+04,
    'Vinf': 10,
    'Rho': 1.227,

    # Refenrence values
    'Sref': 1.0,
    'bref': 1.0,
    'cref': 1.0,
    'Machref': 0.1,
    'ReCref': 1e+07,
    'Xcg': 0.5,
    'Ycg': 0,
    'Zcg': 0,    
    'Vref': 10,

    #VLM Analysis parametres       
    "AnalysisMethod" : 0,
    'fardist': 10,
    "NumWakeNodes" : 8,
    "WakeNumIter" : 5,  
    "NCPU" : 16,
    "Precondition" : 0,
    'TimeStepSize': 0.1,
    "NumTimeSteps" : 100,
    "UnsteadyType" : 0,     

    # Parasite Drag analysis parameters  
    "Altitude" : 0,
    "Pressure" : 80000,
    "Temperature" : 305,
    "AltLengthUnit" : 1, #m
    "ExportSubCompFlag" : 0,
    "FreestreamPropChoice" : 3,
    "LamCfEqnChoice" : 0,   #blasius
    "LengthUnit" : 2,   #m
    "PresUnit" : 3, #pa
    "RecomputeGeom" : 1,
    "TempUnit" : 0, #Kelvin
    "TurbCfEqnChoice" : 10, #Sch Compressible
    "VelocityUnit" : 1, #m/s

    #Sweep analysis number of points
    "AlphaNpts" : 5,
    "BetaNpts" : 1,
    "MachNpts" : 1,
    "ReCrefNpts" : 1,    

    #Flags
    "RefFlag" : 0,
    "KTCorrection" : 1,
    "Symmetry" : 0,
    "FixedWakeFlag" : 0,
    "NoiseCalcFlag" : 0,   
    "AutoTimeStepFlag" : 0, 
    "2DFEMFlag" : 0,
    "ActuatorDiskFlag" : 0,    
    "AlternateInputFormatFlag" : 0,            
    "GroundEffectToggle": 0,
    "ManualVrefFlag" : 0,    
    "ClmaxToggle" : 0,
    "FarDistToggle" : 1,   
    "HoverRampFlag" :0 , 
    "MaxTurnToggle" : 0,
        
    "CGGeomSet" : 0,        
    "FromSteadyState" : 0,
    "GeomSet" : 0,                    
    "MassSliceDir" : 0
}

# double type analysis inputs:
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "AlphaStart", (opt['alphaStart'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "BetaStart", (opt['betaStart'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "AlphaEnd", (opt['alphaEnd'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "BetaEnd", (opt['betaEnd'],) )    
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "FarDist", (opt['fardist'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "MachStart", (opt['mach'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Machref", (opt['Machref'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "ReCref", (opt['ReCref'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Rho", (opt['Rho'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Sref", (opt['Sref'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "TimeStepSize", (opt['TimeStepSize'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Vinf", (opt['Vinf'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Vref", (opt['Vref'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Xcg", (opt['Xcg'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Ycg", (opt['Ycg'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "Zcg", (opt['Zcg'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "bref", (opt['bref'],) )
vsp.SetDoubleAnalysisInput( "VSPAEROSweep", "cref", (opt['cref'],) )

# integer type analysis inputs:
vsp.SetIntAnalysisInput("VSPAEROSweep","CGGeomSet", (opt["CGGeomSet"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","2DFEMFlag", (opt["2DFEMFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","ActuatorDiskFlag", (opt["ActuatorDiskFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","AlphaNpts", (opt["AlphaNpts"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","AlternateInputFormatFlag", (opt["AlternateInputFormatFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","AnalysisMethod", (opt["AnalysisMethod"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","AutoTimeStepFlag", (opt["AutoTimeStepFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","BetaNpts", (opt["BetaNpts"],) )    
vsp.SetIntAnalysisInput("VSPAEROSweep","ClmaxToggle", (opt["ClmaxToggle"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","FarDistToggle", (opt["FarDistToggle"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","FixedWakeFlag", (opt["FixedWakeFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","FromSteadyState", (opt["FromSteadyState"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","GeomSet", (opt["GeomSet"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","GroundEffectToggle", (opt["GroundEffectToggle"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","HoverRampFlag", (opt["HoverRampFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","KTCorrection", (opt["KTCorrection"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","MachNpts", (opt["MachNpts"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","ManualVrefFlag", (opt["ManualVrefFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","MassSliceDir", (opt["MassSliceDir"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","MaxTurnToggle", (opt["MaxTurnToggle"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","NCPU", (opt["NCPU"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","NoiseCalcFlag", (opt["NoiseCalcFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","NumTimeSteps", (opt["NumTimeSteps"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","NumWakeNodes", (opt["NumWakeNodes"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","Precondition", (opt["Precondition"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","ReCrefNpts", (opt["ReCrefNpts"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","RefFlag", (opt["RefFlag"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","Symmetry", (opt["Symmetry"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","UnsteadyType", (opt["UnsteadyType"],) )
vsp.SetIntAnalysisInput("VSPAEROSweep","WakeNumIter", (opt["WakeNumIter"],) )

vsp.ExecAnalysis("VSPAEROComputeGeometry")
vsp.ExecAnalysis("VSPAEROSweep")