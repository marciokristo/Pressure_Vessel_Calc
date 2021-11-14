
class CilinderCalcs:
    
    def __init__(self):
        self.P_circunferencial = None
        self.P_longitudinal = None
        self.t_min_long_thin_cil = None 
        self.t_min_circ_thin_cil = None
        self.t_nom_long_thin_cil = None
        self.t_nom_circ_thin_cil = None
        self.Z_circ = None
        self.Z_long = None
        self.t_min_circ_thick_cil = None
        self.t_min_long_thick_cil = None
        self.t_nom_circ_thick_cil = None
        self.t_nom_long_thick_cil = None
        self.MAWP_thin_cil_circ = None
        self.MAWP_thin_cil_Long = None
        self.a_circ_cil = None
        self.a_long_cil = None
        self.b_circ_cil = None
        self.b_long_cil_= None
        self.MAWP_thick_cil_circ = None
        self.MAWP_thick_cil_long = None
        
        
    def cilinder_min_thickness_calc(self,Snew_cilinder, E, P,Pwater_col, Rcor, Shot_cilinder, C ):
        
        print("\n\nCilinder minimun thickness calculations:")
        self.P_circunferencial = 0.385 * Snew_cilinder * E
        self.P_longitudinal =  1.25 * Snew_cilinder * E

        if P <= self.P_circunferencial and self.P_longitudinal:
            print("P is less than 0.385*S*E.You have a thin wall pressure vessel")
            self.t_min_long_thin_cil = ((P+Pwater_col) * Rcor)/(2 * Shot_cilinder * E - 0.4 * P)
            self.t_min_circ_thin_cil = ((P+Pwater_col) * Rcor)/(Shot_cilinder * E - 0.6 * P)
            self.t_nom_long_thin_cil = self.t_min_long_thin_cil + C 
            self.t_nom_circ_thin_cil = self.t_min_circ_thin_cil + C
            print(f"Cilinder minimun thickness due circuferencial stress is {self.t_min_circ_thin_cil} mm.")
            print(f"Cilinder minimun thickness due longitudinal stress is {self.t_min_long_thin_cil} mm.")
            output = ["\n\nCilinder minimun thickness calculations:","P is less than 0.385*S*E.You have a thin wall pressure vessel",f"Cilinder minimun thickness due circuferencial stress is {self.t_min_circ_thin_cil} mm.",f"Cilinder minimun thickness due longitudinal stress is {self.t_min_long_thin_cil} mm." ]
            with open('output.txt', 'a') as f:
                f.writelines('\n'.join(output))
            if self.t_min_circ_thin_cil > self.t_min_long_thin_cil:
                print(f"Nominal Thickness w/ Corrosion allowance due circunferencial stress is {self.t_nom_circ_thin_cil} mm")
                output2 = [f"Nominal Thickness w/ Corrosion allowance due circunferencial stress is {self.t_nom_circ_thin_cil} mm"]
                with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output2))
                
            else:
                print(f"Nominal Thickness w/ Corrosion allowance due longitudinal stress is {self.t_nom_long_thin_cil} mm") 
            return self.t_min_long_thin_cil, self.t_min_circ_thin_cil, self.t_nom_long_thin_cil, self.t_nom_circ_thin_cil        

        else:
            print("P is higher than 0.385*S*E.You have thick wall pressure vessel")
            self.Z_circ = (Shot_cilinder * E + (P+Pwater_col)) / (Shot_cilinder * E - (P+Pwater_col))
            self.Z_long = ((P+Pwater_col) / (Shot_cilinder * E))+1
            self.t_min_circ_thick_cil = Rcor * (self.Z_circ**(1/2) - 1)
            self.t_min_long_thick_cil = Rcor * (self.Z_long**(1/2) - 1)
            self.t_nom_circ_thick_cil = self.t_min_circ_thick_cil + C
            self.t_nom_long_thick_cil = self.t_min_long_thick_cil + C
            print(f"Cilinder minimun thickness due circuferencial stress is {self.t_nom_circ_thick_cil} mm.")
            print(f"Cilinder minimun thickness due longitudinal stress is {self.t_nom_long_thick_cil} mm.")
            output3 = ["P is higher than 0.385*S*E.You have thick wall pressure vessel",f"Cilinder minimun thickness due circuferencial stress is {self.t_nom_circ_thick_cil} mm.",f"Cilinder minimun thickness due longitudinal stress is {self.t_nom_long_thick_cil} mm."]
            with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output3))
            if self.t_min_circ_thick_cil > self.t_min_long_thick_cil:
                print(f"Cilinder Nominal Thickness w/ Corrosion allowance due circuferencial stress  is {self.t_nom_circ_thick_cil} mm")
                output4 = [f"Cilinder Nominal Thickness w/ Corrosion allowance due circuferencial stress  is {self.t_nom_circ_thick_cil} mm"]
                with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output4))
            else:
                print(f"Cilinder Nominal Thickness w/ Corrosion allowance due longitudinal stress  is {self.t_nom_long_thick_cil} mm") 
                output7 = [f"Cilinder Nominal Thickness w/ Corrosion allowance due longitudinal stress  is {self.t_nom_long_thick_cil} mm"]
                with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output7))
            return self.Z_circ, self.Z_long, self.t_min_circ_thick_cil, self.t_min_long_thick_cil, self.t_nom_circ_thick_cil, self.t_nom_long_thick_cil     


    def cilinder_pmta_calc(self, Snew_cilinder, E, Shot_cilinder, Rcor, P ):

        print("\n\nCilinder PMTA Calculation")
        self.P_circunferencial = 0.385 * Snew_cilinder * E
        self.P_longitudinal =  1.25 * Snew_cilinder * E
        if P <= self.P_circunferencial and self.P_longitudinal:
            print("Pressure is less than 0.385*S*E.MAWP as thin wall pressure vessel")
            self.MAWP_thin_cil_circ = (self.t_min_circ_thin_cil*Shot_cilinder*E)/(Rcor+0.6*self.t_min_circ_thin_cil)
            self.MAWP_thin_cil_Long = (2*self.t_min_long_thin_cil*Shot_cilinder*E)/(Rcor-0.4*self.t_min_long_thin_cil)
            print(f"MAWP due circunferencial stress: {self.MAWP_thin_cil_circ} kPa \nMAWP due longitudinal stress: {self.MAWP_thin_cil_Long}")
            output5 = ["\nCilinder PMTA Calculation", f"MAWP due circunferencial stress: {self.MAWP_thin_cil_circ} kPa", f"MAWP due longitudinal stress: {self.MAWP_thin_cil_Long}"]
            with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output5))
            
            if self.MAWP_thin_cil_circ < self.MAWP_thin_cil_Long:
                print(f"Max. Allowed Work Pressure is {self.MAWP_thin_cil_circ} Kpa due circuferencial stress.")
                output6 = [f"Max. Allowed Work Pressure is {self.MAWP_thin_cil_circ} Kpa due circuferencial stress."]
                with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output6))
            else:    
                print(f"Max. Allowed Work Pressure is {self.MAWP_thin_cil_Long} Kpa due longitudinal stress.")
                output8 = [f"Max. Allowed Work Pressure is {self.MAWP_thin_cil_Long} Kpa due longitudinal stress."]
                with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output8))
                

            return self.MAWP_thin_cil_circ, self.MAWP_thin_cil_Long   
        else:
            
            print("Pressure is higher than 0.385*S*E.MAWP Calculus as thick wall pressure vessel.") 
            self.a_circ_cil = (self.t_min_circ_thin_cil / Rcor)+1
            self.a_long_cil = (self.t_min_long_thin_cil / Rcor)+1
            self.b_circ_cil = (self.t_min_circ_thin_cil/(Rcor+ self.t_min_circ_thin_cil))+1
            self.b_long_cil= (self.t_min_long_thin_cil/(Rcor+ self.t_min_long_thin_cil))+1
            self.MAWP_thick_cil_circ = (Shot_cilinder*E((self.a_long_cil**2)-1))/((self.a_circ_cil**2)+1)
            self.MAWP_thick_cil_long = (Shot_cilinder*E((self.a_long_cil**2)-1))
            print(f"MAWP due circunferencial stress: {self.MAWP_thick_cil_circ} kPa \nMAWP due longitudinal stress: {self.MAWP_thick_cil_long}")
            output9 = ["Pressure is higher than 0.385*S*E.MAWP Calculus as thick wall pressure vessel.",f"MAWP due circunferencial stress: {self.MAWP_thick_cil_circ} kPa","MAWP due longitudinal stress: {self.MAWP_thick_cil_long}"]
            with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output9))
            if self.MAWP_thick_cil_circ < self.MAWP_thick_cil_long:
                print(f"MAWP is {self.MAWP_thick_cil_circ}kPa due circuferencial Stress.")
                output10 = [f"MAWP is {self.MAWP_thick_cil_circ}kPa due circuferencial Stress." ]
                with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output10))
            else:
                print(f"MAWP is {self.MAWP_thick_cil_long}kPa due Longitudinal Stress. ")    
                output11 = [f"MAWP is {self.MAWP_thick_cil_long}kPa due Longitudinal Stress. " ]
                with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output11))        

            return self.MAWP_thick_cil_circ, self.MAWP_thick_cil_long, self.a_circ_cil,self.a_long_cil, self.b_circ_cil, self.b_long_cil 
        
    def cilinder_stress_calc(self,P, Pwater_col, Rcor, E, Snew_cilinder):
        print("\n\nCilinder Stress Calculation")
        self.P_circunferencial = 0.385 * Snew_cilinder * E
        self.P_longitudinal =  1.25 * Snew_cilinder * E
        if P <= self.P_circunferencial and self.P_longitudinal:
            print("Pressure is less than 0.385*S*E. Stress as thin wall pressure vessel")
            self.thin_cil_circ_stress = ((P+Pwater_col)*(Rcor + 0.6 * self.t_min_circ_thin_cil)) / (self.t_min_circ_thin_cil * E)
            self.thin_cil_long_stress = ((P+Pwater_col)*(Rcor - 0.4 * self.t_min_circ_thin_cil)) / (2 * self.t_min_circ_thin_cil * E)
            print(f"Circunferencial stress: {self.thin_cil_circ_stress} kPa \nlongitudinal stress: {self.thin_cil_long_stress}")
            output12 = ["\nCilinder Stress Calculation","Pressure is less than 0.385*S*E. Stress as thin wall pressure vessel",f"Circunferencial stress: {self.thin_cil_circ_stress} kPa","longitudinal stress: {self.thin_cil_long_stress}"]
            with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output12))        
       

            
        else:
            print("Pressure is higher than 0.385*S*E.Stress Calculus as thick wall pressure vessel.") 
            self.thick_cil_circ_stress = (P+Pwater_col) * (self.a_circ_cil**2 + 1) / E * (self.a_circ_cil**2-1)            
            self.thick_cil_long_stress = (P+Pwater_col) / E * (self.a_circ_cil**2 - 1)
            print(f"Circunferencial stress: {self.thick_cil_circ_stress} kPa \nlongitudinal stress: {self.thick_cil_long_stress}")
            output13 = ["\nCilinder Stress Calculation","Pressure is higher than 0.385*S*E.Stress Calculus as thick wall pressure vessel.",f"Circunferencial stress: {self.thick_cil_circ_stress} kPa","longitudinal stress: {self.thick_cil_long_stress}"]
            with open('output.txt', 'a') as f:
                    f.writelines('\n'.join(output13))        
            
                
            
            
                 