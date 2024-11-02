## This function calculates the propeller coefficients for a given geometry.

import openvsp as vsp
import numpy as np
import time

def prop_calc(vspfile_path, U_inf, rpm):

    """
    Responsible for calculating the propeller coefficients for a given geometry.

    beam_file_path: Path to the BEM file, string
    U_inf: Freestream velocity, np.array, 
    rpm: Revolutions per minute, int

    """
    print("Running cases RPM = " + str(rpm)+  " U = " + str(U_inf))

    for i in range(len(U_inf)):
        # # start = time.time() 
        # # Check the VSP setup
        vsp.VSPCheckSetup()
        vsp.VSPRenew()
        vsp.ClearVSPModel()
        vsp.DeleteAllResults()
        stdout = vsp.cvar.cstdout
        errorMgr = vsp.ErrorMgrSingleton.getInstance()

        # Load the VSP file
        vsp.ReadVSPFile(vspfile_path)
        vsp.SetParmVal(vsp.FindParm(vsp.FindUnsteadyGroup(0),"RPM","UnsteadyGroup"), rpm)

        # Compute Geometry
        analysis_name = "VSPAEROComputeGeometry"
        vsp.SetAnalysisInputDefaults(analysis_name)
        analysis_method = list(vsp.GetIntAnalysisInput(analysis_name, "AnalysisMethod" ))
        analysis_method[0] = vsp.VORTEX_LATTICE
        vsp.SetIntAnalysisInput(analysis_name, "AnalysisMethod", analysis_method)

        # Analysis Setup
        analysis_name="VSPAEROSweep"
        vsp.SetAnalysisInputDefaults("VSPAEROSweep")

        u = int(U_inf[i])
        recref=[50000]
        vref = [u]
        vinf = [u]

        blades_flag = [1]
        rho = [1.225]
        auto_time_flag = [1]
        num_rev_flag = [3]
        ncpu = [8]
        num_timesteps=[20]
        num_wake_nodes = [128]
        # timestepsizes=[0.00042]

        vsp.SetDoubleAnalysisInput(analysis_name,"ReCref",recref,0)
        vsp.SetIntAnalysisInput(analysis_name,"NCPU", ncpu, 0)
        vsp.SetDoubleAnalysisInput(analysis_name,"Vref", vref, 0)
        vsp.SetIntAnalysisInput(analysis_name,"RotateBladesFlag",blades_flag,0)
        vsp.SetDoubleAnalysisInput(analysis_name,"Vinf", vinf,0)
        vsp.SetDoubleAnalysisInput(analysis_name,"Rho", rho,0)
        vsp.SetIntAnalysisInput(analysis_name,"AutoTimeStepFlag",auto_time_flag,0)
        vsp.SetIntAnalysisInput(analysis_name,"AutoTimeNumRevs", num_rev_flag,0)
        vsp.SetDoubleAnalysisInput(analysis_name,"NumTimeSteps",num_timesteps,0)
        vsp.SetDoubleAnaylsisInput(analysis_name,"NumWakeNodes",num_wake_nodes,0)
        # vsp.SetDoubleAnalysisInput(analysis_name,"TimeStepSize",timestepsizes,0)
        

        vsp.Update()
        vsp.PrintAnalysisInputs(analysis_name)
        vsp.ExecAnalysis(analysis=analysis_name)
        errorMgr.PopErrorAndPrint(stdout)

        print("Finished execution!")
        rotor_res = vsp.FindResultsID("VSPAERO_Rotor", 0)
        vsp.WriteResultsCSVFile(rotor_res, "./results/apc_bem_10x10_"+ "U" + str(u) + "RPM" + str(rpm) +".csv")





        # # Import the propeller geometry
        # prop_id = vsp.ImportFile(bem_file_path, vsp.IMPORT_BEM, "")
        
        # vsp.SetParmVal(prop_id, "ConstructXoC", "Design", 0.0)  # Construct x/c at 0.0
        # vsp.SetParmVal(prop_id, "FeatherAxisXoC", "Design", 0.125)  # Set the feather axis to 0.125

        # # Set up root airfoil section
        # xsec_surf = vsp.GetXSecSurf(prop_id, 0)
        # vsp.ChangeXSecShape(xsec_surf, 0, vsp.XS_FILE_AIRFOIL)

        # xsec = vsp.GetXSec(xsec_surf, 0)
        # vsp.ReadFileAirfoil(xsec, "./geometry/e63.dat")

        # # Set up tip airfoil section
        # xsec_surf = vsp.GetXSecSurf(prop_id, 1)
        # vsp.ChangeXSecShape(xsec_surf, 1, vsp.XS_FILE_AIRFOIL)

        # xsec = vsp.GetXSec(xsec_surf, 1)
        # vsp.ReadFileAirfoil(xsec, "./geometry/n4412.dat")

        # # Set tesselation
        # vsp.SetParmVal(prop_id, "Tess_U", "Shape", 32)  # Num_U 
        # vsp.SetParmVal(prop_id, "Tess_W", "Shape", 32)  # Num_W

       

        # vsp.Update()
        # vsp.WriteVSPFile("apc_bem_10x10.vsp3"