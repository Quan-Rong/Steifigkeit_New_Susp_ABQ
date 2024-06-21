Steifigkeit Bearbeitung

## Note:

Hi Claudia, bitte mal überprüfen, ob es richtig bearbeiten kann. Code befindet sich in Stiffness_Claudia.py, wichtig bitte mal checken die Berechnungen wie folgende:

* Seitenkraft_Vorspur = np.arcsin(((N87_X0 + a) - (N89_X0 + d)) / 
                                        np.sqrt(((N87_X0 + a) - (N89_X0 + d))**2 + ((N87_Y0 + b) - (N89_Y0 + e))**2)) * 180 / np.pi
        
* Seitenkraft_Sturz = np.arcsin(((N87_Z0 + c) - (N89_Z0 + f)) / 
                                      np.sqrt(((N87_X0 + a) - (N89_X0 + d))**2 + ((N87_Y0 + b) - (N89_Y0 + e))**2)) * 180 / np.pi
        
* Brake_Vorspur = np.arcsin(((N87_X0 + g) - (N89_X0 + j)) / 
                                  np.sqrt(((N87_X0 + g) - (N89_X0 + j))**2 + ((N87_Y0 + h) - (N89_Y0 + k))**2)) * 180 / np.pi
        
* Brake_Sturz = np.arcsin(((N87_Z0 + i) - (N89_Z0 + l)) / 
                                np.sqrt(((N87_X0 + g) - (N89_X0 + j))**2 + ((N87_Y0 + h) - (N89_Y0 + k))**2)) * 180 / np.pi
        
* AT_Vorspur = np.arcsin(((N87_X0 + m) - (N89_X0 + p)) / 
                               np.sqrt(((N87_X0 + m) - (N89_X0 + p))**2 + ((N87_Y0 + n) - (N89_Y0 + q))**2)) * 180 / np.pi
        
* AT_Sturz = np.arcsin(((N87_Z0 + o) - (N89_Z0 + r)) / 
                             np.sqrt(((N87_X0 + m) - (N89_X0 + p))**2 + ((N87_Y0 + n) - (N89_Y0 + q))**2)) * 180 / np.pi
        
* Orig_Vorspur = np.arcsin((N87_X0 - N89_X0) / 
                                 np.sqrt((N87_X0 - N89_X0)**2 + (N87_Y0 - N89_Y0)**2)) * 180 / np.pi
        
* Orig_Sturz = np.arcsin((N87_Z0 - N89_Z0) / 
                               np.sqrt((N87_X0 - N89_X0)**2 + (N87_Y0 - N89_Y0)**2)) * 180 / np.pi
