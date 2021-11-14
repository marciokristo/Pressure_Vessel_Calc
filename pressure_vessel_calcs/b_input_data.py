#TODO Create Functions for other features


class PressureVesselType:
    
       
    def __init__(self):
        self.design_code = None
        self.shell_type = None
        self.top_head_type = None
        self.bottom_head_type = None             
    
    
    def choose_design_code(self):
        self.design_code = int(input("Choose design Code: \n\n[1] ASME VIII Div.1 \n[2] ASME VIII Div.2 \n[3] TEMA \n[4] PED \nDesign Code:"))
        if self.design_code == 1:
            print("DesIgn Code: ASME VIII Div. 1. ")
            output = ["DesIgn Code: ASME VIII Div. 1. "]
            with open('output.txt', 'a') as f:
                f.writelines('\n'.join(output))
            return self.design_code
        else:
            print("Module under development. Please select Design Code again")
            PressureVesselType.choose_design_code(self)       


    def choose_vessel_type(self):    
        self.shell_type = int(input("\nChoose Pressure Vessel Type \n\n[1] Cilindrical \n[2]Spherical \nPressure Vessel Type: "))
        if self.shell_type == 1:
            print("pressure Vessel Type: Cilindrical")
            output = ["pressure Vessel Type: Cilindrical"]
            with open('output.txt', 'a') as f:
                f.writelines('\n'.join(output))
            return self.shell_type
        else:
            print("Module under development. Please select type again")
            PressureVesselType.choose_vessel_type(self)       

    
    def choose_top_head_type(self):
        self.top_head_type = int(input("\nChoose top head type: \n\n[1]Torrispherical \n[2] Eliptical \n[3]Espherical \n[4]Conical \nTop Head Type: "))
        if self.top_head_type == 1:
            print("Top Head Type: Torrispherical")
            output = ["Top Head Type: Torrispherical"]
            with open('output.txt', 'a') as f:
                f.writelines('\n'.join(output))
            return self.top_head_type
        else:
            print("Module under development. Please select type again") 
            PressureVesselType.choose_top_head_type(self)   


    def choose_bottom_head_type(self):
        self.bottom_head_type = int(input("\nChoose Bottom top head type: \n\n[1]Torrispherical  \n[2]Eliptical \n[3]Espherical \n[4]Conical \nBottom Head Type"))
        if self.bottom_head_type == 1:
            print("Top Head Type: Torrispherical")
            output = ["Top Head Type: Torrispherical"]
            with open('output.txt', 'a') as f:
                f.writelines('\n'.join(output))
            
            return self.bottom_head_type
            
        else:
            print("Module under development. Please select type again") 
            PressureVesselType.choose_bottom_head_type(self)  



def input_data():  
    
    global medium, rho_medium, medium_level, Pwater_col, Temp_proj, Pproj, P, cilinder_material, top_head_material, botton_head_material, Snew_cilinder, Shot_cilinder, Snew_top_head, Shot_top_head, Snew_bottom_head, Shot_bottom_head, E, R, C, Rcor, conf_loss, Sy_cilinder, Sy_top_head, Sy_bottom_head
    while True:
        try:    
            medium = str(input("Insert Operation Medium: "))
            rho_medium = float(input("Insert Medium Density [Kg/m3]: "))
            medium_level = float(input("Insert Height of medium level in operation [mm]: "))
            Pwater_col = (rho_medium * (medium_level / 1000))/1000
            Temp_proj = float(input("Insert Design Temp: "))
            Pproj = float(input("Insert Internal Pressure [kPa]: "))
            P = Pproj + Pwater_col
            cilinder_material= str(input("Select material for Cilinder: "))
            top_head_material= str(input("Select material for Top Head: "))
            botton_head_material= str(input("Select material for Bottom Head: "))
            Snew_cilinder = float(input("Insert Cilinder Material Allowable Stress COLD [kPa]: "))
            Shot_cilinder = float(input("Insert Cilinder Material Allowable Stress HOT [kPa]: "))
            Snew_top_head = float(input("Insert Top Head Material Allowable Stress COLD [kPa]: "))
            Shot_top_head = float(input("Insert Top Head Material Allowable Stress HOT [kPa]: "))
            Snew_bottom_head = float(input("Insert Bottom Head Material Allowable Stress COLD [kPa]: "))
            Shot_bottom_head = float(input("Insert Bottom Head Material Allowable Stress HOT [kPa]: "))
            E = float(input("Insert Joint Efficience: "))
            R = float(input("insert inside radius [mm]: "))
            C = float(input("Insert corrosion allowance[mm]: "))
            Rcor = R+C
            conf_loss = float(input("Insert loss of material due conformation [mm]: "))
            Sy_cilinder = float(input("Insert Yield Stress for Cilinder material [kPa]: "))
            Sy_top_head = float(input("Insert Yield Stress for Top Head material [kPa]: "))
            Sy_bottom_head = float(input("Insert Yield Stress for bottom head material [kPa]: "))
        except ValueError:
            print("Sorry, Wrong input.")            
            continue
        else:        
            break
        
    output = ["*-*"*20,"PRESSURE VESSEL DATA:\n",f"Medium: {medium}",f"{medium} Density: {rho_medium} Kg/m3.", f"{medium} level in operation: {medium_level} mm",f"Medium Column Weight: {Pwater_col} kPa", f"Design Temperature: {Temp_proj} C", f"Internal Pressure: {Pproj} kPa",f"Design Pressure: {P} kPa", f"Joint Efficience: {E}", f"Internal Radius: {R} mm", f"Internal Radius Corroded: {Rcor} mm", f"Corrosion Allowance: {C} mm", f"Conformation Material Loss: {conf_loss} mm",f"\n\nMaterial as per ASME Section II Part D: ",f"\nCilinder Material: {cilinder_material}" ,f"Top Head Material: {top_head_material} ",f"Bottom Head Material: {botton_head_material} ",f"Cilinder Allowable Stress Cold: {Snew_cilinder} kPa ",f"Cilinder Allowable Stress Hot: {Shot_cilinder} kPa" ,f"Top Head Allowable Stress Cold: {Snew_top_head} kPa ",f"Top Head Allowable Stress hot: {Shot_top_head} kPa ",f"Bottom Head Allowable Stress Cold: {Snew_bottom_head} kPa",f"Bottom Head Allowable Stress hot: {Shot_bottom_head} kPa",f"Cilinder Yield Stress: {Sy_cilinder} kPa",f"Top Head Yield Stress: {Sy_top_head} kPa",f"Bottom Head Yield Stress: {Sy_bottom_head} kPa","*-*"*20 ] 
    with open('output.txt', 'a') as f:
        f.writelines('\n'.join(output))
       
    return medium, rho_medium, medium_level, Pwater_col, Temp_proj, Pproj, P, cilinder_material, top_head_material, botton_head_material, Snew_cilinder, Shot_cilinder, Snew_top_head, Shot_top_head, Snew_bottom_head, Shot_bottom_head, E, R, C, Rcor, conf_loss, Sy_cilinder, Sy_top_head, Sy_bottom_head
        
          

# print(f"Pressure Vessel as per ASME VIII Div.1 \n\nMedium: {medium} \n{medium} Density: {rho_medium} Kg/m3 \n{medium} level in operation: {medium_level} mm \nMedium Column Weight: {Pwater_col} kPa \nDesign Temperature: {Temp_proj} C \nInternal Pressure: {Pproj} kPa \nDesign Pressure: {P} kPa \nJoint Efficience: {E} \nInternal Radius: {R} mm \nInternal Radius Corroded: {Rcor} mm \nCorrosion Allowance: {C} mm \nConformation Material Loss: {conf_loss} mm \n\n\nMaterial as per ASME Section II Part D... \nCilinder Material: {cilinder_material} \nTop Head Material: {top_head_material} \nBottom Head Material: {botton_head_material} \nCilinder Allowable Stress Cold: {Snew_cilinder} kPa \nCilinder Allowable Stress Hot: {Shot_cilinder} kPa \nTop Head Allowable Stress Cold: {Snew_top_head} kPa \nTop Head Allowable Stress hot: {Shot_top_head} kPa \nBottom Head Allowable Stress Cold: {Snew_bottom_head} kPa \nBottom Head Allowable Stress hot: {Shot_bottom_head} kPa  \nCilinder Yield Stress: {Sy_cilinder} kPa \nTop Head Yield Stress: {Sy_top_head} kPa \nBottom Head Yield Stress: {Sy_bottom_head} kPa") 

#return medium, rho_medium, medium_level, Pwater_col, Temp_proj, Pproj, P, cilinder_material, top_head_material, botton_head_material, Snew_cilinder, Shot_cilinder, Snew_top_head, Shot_top_head, Snew_bottom_head, Shot_bottom_head, E, R, C, Rcor, conf_loss, Sy_cilinder, Sy_top_head, Sy_bottom_head    
    
    

    

    