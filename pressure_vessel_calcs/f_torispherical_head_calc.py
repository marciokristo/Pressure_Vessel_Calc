

#TODO Create Functions for PMTA

## TORISPHERICAL TOP HEAD 2:1 - Min thickness allowed and PMTA

class TorisphericalCalcs:
    
    def __init__(self):
        self.L_top_head = None
        self.r_top_head = None
        self.ratio_L_r_top = None
        self.M_factor_top_head = None
        self.t_min_top_head = None
        self.t_nom_top_head_plate =None 
        self.t_top_head_nom_after_conf = None
        self.top_head_pmta = None
        self.L_bottom_head = None
        self.r_bottom_head = None
        self.ratio_L_r_bottom = None
        self.M_factor_bottom_head = None
        self.t_min_bottom_head = None
        self.t_nom_bottom_head_plate = None
        self.t_bottom_head_nom_after_conf = None
        self.bottom_head_pmta = None
    
    def tor_top_min_thick_allowed(self,Rcor, P, Shot_top_head, E, conf_loss, C):
        self.L_top_head = 0.904 * (2 * Rcor)
        self.r_top_head = 0.173 * (2 * Rcor)
        self.ratio_L_r_top = self.L_top_head/self.r_top_head
        self.M_factor_top_head = (1/4) * (3 + (self.ratio_L_r_top)**(1/2))
        self.t_min_top_head = (P * self.L_top_head * self.M_factor_top_head) / ((2 * Shot_top_head * E) - 0.2 * P)
        self.t_nom_top_head_plate = self.t_min_top_head + conf_loss + C
        self.t_top_head_nom_after_conf = self.t_min_top_head + C
        print(f"\n\nTorispherical Top Head Min thickness allowed: \n\nTop Head radius (L) is {self.L_top_head} mm \nTop Head Toroidal radius (r)  is {self.r_top_head} mm \nTop Head M factor (M) is {self.M_factor_top_head}")
        print(f"Top Head minimun thickness due circuferencial stress is {self.t_min_top_head} mm.")
        print(f"Top Head plate  Thickness w/ Corrosion allowance and conf. loss is {self.t_nom_top_head_plate} mm. Ps.: Choose equal or higher comercial plate")
        print(f"Top Head Nominal Thicknes after conformation is {self.t_top_head_nom_after_conf} mm")
        
        return self.L_top_head, self.r_top_head, self.ratio_L_r_top , self.M_factor_top_head, self.t_nom_top_head_plate, self.t_top_head_nom_after_conf, self.t_min_top_head  

    def tor_top_head_pmta (self,Rcor, Shot_top_head, E):
        self.L_top_head = 0.904 * (2 * Rcor)
        self.r_top_head = 0.173 * (2 * Rcor)
        self.ratio_L_r_top = self.L_top_head/self.r_top_head
        self.M_factor_top_head = (1/4) * (3 + (self.ratio_L_r_top)**(1/2))
        self.top_head_pmta = (2*self.t_min_top_head*Shot_top_head*E)/(self.L_top_head*self.M_factor_top_head + 0.2*self.t_min_top_head)
        print(f"Top Head MAWP is: {self.top_head_pmta} kPa")
        return self.top_head_pmta 
    
    def tor_top_head_stress_calc(self, P, E):
        self.top_head_stress = P * (self.L_top_head * self.M_factor_top_head + 0.2 * self.t_min_top_head) / (2 * self.t_min_top_head * E)
        print(f"Top head stress is {self.top_head_stress} kPa")
        return self.top_head_stress
        
               


    ## TORISPHERICAL BOTTOM HEAD 2:1 - Min thickness allowed and PMTA
    def tor_bottom_min_thick_allowed(self,Rcor,Pwater_col, P, Shot_bottom_head, E, conf_loss, C ):
        self.L_bottom_head = 0.904 * (2 * Rcor)
        self.r_bottom_head = 0.173 * (2 * Rcor)
        self.ratio_L_r_bottom = self.L_bottom_head/self.r_bottom_head
        self.M_factor_bottom_head = (1/4) * (3 + (self.ratio_L_r_bottom)**(1/2))
        self.t_min_bottom_head = ((P+Pwater_col) * self.L_bottom_head * self.M_factor_bottom_head) / ((2 * Shot_bottom_head * E) - 0.2 * P)
        self.t_nom_bottom_head_plate = self.t_min_bottom_head + conf_loss + C
        self.t_bottom_head_nom_after_conf = self.t_min_bottom_head + C
        print(f"\n\nTorispherical Bottom Head Min thickness allowed: \n\nBottom Head radius (L) is {self.L_bottom_head} mm \nBottom Head Toroidal radius (r)  is {self.r_bottom_head} mm \nBottom Head M factor  (M) is {self.M_factor_bottom_head}")
        print(f"Bottom Head minimun thickness due circuferencial stress is {self.t_min_bottom_head} mm.")
        print(f"Bottom Head plate  Thickness w/ Corrosion allowance and conf. loss is {self.t_nom_bottom_head_plate} mm. Ps.: Choose equal or higher comercial plate")
        print(f"Bottom Head Nominal Thicknes after conformation is {self.t_bottom_head_nom_after_conf} mm")

        return self.L_bottom_head, self.r_bottom_head, self.ratio_L_r_bottom, self.M_factor_bottom_head, self.t_min_bottom_head, self.t_nom_bottom_head_plate, self.t_bottom_head_nom_after_conf 

    def tor_bottom_head_pmta (self,Rcor, E, Shot_bottom_head):
        self.L_bottom_head = 0.904 * (2 * Rcor)
        self.r_bottom_head = 0.173 * (2 * Rcor)
        self.ratio_L_r_bottom = self.L_bottom_head/self.r_bottom_head
        self.M_factor_bottom_head = (1/4) * (3 + (self.ratio_L_r_bottom)**(1/2))
        self.bottom_head_pmta = (2*self.t_min_bottom_head*Shot_bottom_head*E)/(self.L_bottom_head*self.M_factor_bottom_head + 0.2*self.t_min_bottom_head)
        print(f"Bottom Head MAWP is: {self.bottom_head_pmta} kPa")
        return self.bottom_head_pmta 
    
    def tor_bottom_head_stress_calc(self,Pwater_col, P, E):
        self.bottom_head_stress = (P+Pwater_col) * (self.L_bottom_head * self.M_factor_bottom_head + 0.2 * self.t_min_bottom_head) / (2 * self.t_min_bottom_head * E)
        print(f"Bottom head stress is {self.bottom_head_stress} kPa")  
        return self.bottom_head_stress         