# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:54:51 2023

@author: harin
"""

import numpy as np
import pickle 
import streamlit as st

lod=pickle.load(open("C:/Users/harin/Pictures/placement_model.sav","rb"))


def status( vari ):
    vari1=np.asarray(vari)
    vari2=vari1.reshape(1,-1)
    predi=lod.predict(vari2)
    print(predi)
    
    if(predi[0]==1):
        return "HE/SHE WILL NOT PLACED"
    else:
        return "HE/SHE WILL  PLACED"
    
def main():
     st.title("CAMPUS PLACEMENT")
     gender=st.text_input('GENDER(M-1,F-0)')
     sslc_p=st.text_input('SSLC PERCENTAGE')
     sslc_b=st.text_input('SSLC BOARD(Central-0/Others-1)')
     hsc_p=st.text_input('HSC PERCENTAGE')
     hsc_b=st.text_input('HSC BOARD(Central-0/Others-1)')
     hsc_s=st.text_input('HSC SUBJECT(SCIENCE-2/COMMERCE-1/ARTS-3)')
     degree_p=st.text_input('DEGREE PERCENTAGE')
     degree_t=st.text_input('DEGREE TYPE(Sci&Tech-1/Others-3/Comm&Mgmt-2)')
     workex=st.text_input('WORK EXPERIENCE(NO-0/YES-1)')
     etest_p=st.text_input('E-TEST PERCENTAGE')
     specialisation=st.text_input('SPECIALIZATION(Mkt&HR-1/Mkt&Fin-0)')
     mba_p=st.text_input('MBA PERCENTAGE')
     
     vari3=""
     
     if(st.button("predict")):
         vari3=status([gender,sslc_p,sslc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation, mba_p])
         
         
         
     st.success(vari3)
         
         
if __name__=='__main__':
    main()
     
     
     