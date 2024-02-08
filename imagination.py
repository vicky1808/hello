import  streamlit as st
import pandas as pd
st.title('Flamingo')
st.image('flamingo.gif')
tab1,tab2,tab3=st.tabs(['Visiting Places','Timing',"nearest station"])
with tab1:
    City=st.text_input('City:')
    if City=='Mumbai':
        st.write(' mudflats of Sewri, Bhigwan Bird Sanctuary')
    elif City=='Thane':
        st.write('Thane Creek')
    elif City=='Navi mumbai':
        st.write("coastal regions of Navi Mumbai")
    else:
        st.write('not avail')
with tab2:
    City1=st.text_input('City1:')
    if City1=='Mumbai':
        st.write('5pm-6pm')
    elif City1=='Thane':
        st.write('4pm-9pm')
    elif City1=='Navi mumbai':
        st.write("11am-11pm") 
    else:
        st.write("not found")    

       