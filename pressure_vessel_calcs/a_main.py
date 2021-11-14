from b_input_data import PressureVesselType, input_data 
from c_cilinder_calc import CilinderCalcs
from f_torispherical_head_calc import TorisphericalCalcs


open('output.txt', 'w').close()
# PRESSURE VESSEL INITIAL DATA 

print("=-="*10, "PRESSURE VESSEL CALCULATIONS", "=-="*10)

pressure_vessel_input=PressureVesselType()
pressure_vessel_input.choose_design_code() 
pressure_vessel_input.choose_vessel_type()   
pressure_vessel_input.choose_top_head_type() 
pressure_vessel_input.choose_bottom_head_type() 
medium, rho_medium, medium_level, Pwater_col, Temp_proj, Pproj, P, cilinder_material, top_head_material, botton_head_material, Snew_cilinder, Shot_cilinder, Snew_top_head, Shot_top_head, Snew_bottom_head, Shot_bottom_head, E, R, C, Rcor, conf_loss, Sy_cilinder, Sy_top_head, Sy_bottom_head = input_data()  

# SHELL AND HEAD CALCULATION min_thickness_input  

if pressure_vessel_input.design_code == 1: 
    if pressure_vessel_input.shell_type == 1: 
        print("\n\n SHELL CALCULATION: ")
        cilinder_calculation = CilinderCalcs() 
        cilinder_calculation.cilinder_min_thickness_calc(Snew_cilinder, E, P,Pwater_col, Rcor, Shot_cilinder, C)    
        cilinder_calculation.cilinder_pmta_calc(Snew_cilinder, E, Shot_cilinder, Rcor, P)
        cilinder_calculation.cilinder_stress_calc(P,Pwater_col, Rcor, E, Snew_cilinder)
        
    else:
        pass

    if pressure_vessel_input.top_head_type ==1:
        print("\n\n SHELL CALCULATION: ")        
        torispherical_calculation = TorisphericalCalcs()
        torispherical_calculation.tor_top_min_thick_allowed(Rcor, P, Shot_top_head, E, conf_loss, C)
        torispherical_calculation.tor_top_head_pmta (Rcor, Shot_top_head, E)
        torispherical_calculation.tor_top_head_stress_calc(P, E)        
        
    else:
        pass

    if pressure_vessel_input.bottom_head_type == 1:
        torispherical_calculation.tor_bottom_min_thick_allowed(Rcor, P,Pwater_col, Shot_bottom_head, E, conf_loss, C)
        torispherical_calculation.tor_bottom_head_pmta (Rcor, E, Shot_bottom_head)
        torispherical_calculation.tor_bottom_head_stress_calc(Pwater_col, P, E)        
        
    else:
        pass   
    
 














