import streamlit as st
import openpyxl
import preprocssing
import helper
import matplotlib.pyplot as plt
import pandas as pd,seaborn as sns
import matplotlib.patches as patches
import numpy as np
def main():
    st.sidebar.title("Select your Analyzer")
    selected_option=""
    selected_option = st.sidebar.selectbox("Select an option", ["Select an option", "Internal Marks Analyzer", "Attendance Analyzer"])
    print(selected_option)
    if selected_option == "Internal Marks Analyzer":
        st.title("Your INSIGHTS")
        uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=['xlsx'],key=1)
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            subjects=df.columns[1:]
            u=len(df)
            credits=df.iloc[u-1]
            del credits[df.columns[0]]
            roll=df.columns[0]
            df.drop(df.index[-1], inplace=True)
            grades=['A+','A','B','C','D','E','F']
            grade_map={'A+':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':4}
            tot_sum=[credits[i] for i in credits.keys()]
            tot_sum=sum(tot_sum)
            cgpa=[]
            cgpa_sel=True
            st.title("Cgpa are as follows")
            if cgpa_sel:
                u=len(df)
                for i in range(u):
                    x=0
                    for j in subjects:
                        x+=credits[j]*grade_map[df.loc[i][j]]
                    x/=tot_sum
                    x=round(x,2)
                    cgpa.append(x)
                d=pd.DataFrame(list(zip(df[roll],cgpa)),columns=[roll,'CGPA'])
                st.write(d)
            st.title("Select your desired subject to get Pass-Fail Ratio\n")
            sub_choice = st.selectbox("Select your subject", ['NLP','DL','BDA','ML','AI','DSA'],key=10)
            l=df[sub_choice]
            x=0
            y=0
            for m in l:
                if(m=='F'):
                    x+=1
                else:
                    y+=1
            fig, ax = plt.subplots(figsize=(8, 4))
            fig.set_facecolor('#dd99ff')
            ax.set_facecolor('#ccffff')
            ax.pie([y,x], labels=['PASS','Fail'], colors=['green','red'], autopct='%1.1f%%', shadow=False, startangle=140)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
            d=d.sort_values('CGPA',ascending=False)
            d.index=[i for i in range(1,len(d)+1)]
            st.title("Top Performers of current semester")
            st.write(d.head(10))
            st.title("Select your desired subject to get its stats\n")
            sub_choice1 = st.selectbox("Select your subject", ['NLP','DL','BDA','ML','AI','DSA'],key=11)
            l1=df[sub_choice1]
            c=[0 for i in range(7)]
            for m in l1:
                if(m=="A+"):
                    c[0]+=1
                else:
                    c[ord(m)-64]+=1
            fig1, ax1 = plt.subplots()
            fig1.set_facecolor('#dd99ff')
            ax1.set_facecolor('#ccffff')
            cmap = plt.get_cmap('coolwarm')  
            colors = [cmap(i / len(grades)) for i in range(len(grades))]
            ax1.bar(grades,c,color=colors)
            for i, v in enumerate(c):
                ax1.text(i, v //2, str(v), ha='center',bbox=dict(facecolor='white', alpha=0.5))
            ax1.set_xlabel('Grades',color='#3333ff')
            ax1.set_ylabel('Count',color='#3333ff')
            ax1.set_title('Bar Plot to show stats of a subject',color='#3333ff')
            ax1.grid(False)
            st.pyplot(fig1)
            roll_list=df[roll]
            st.title("Select Roll Number\n")
            roll_choice=st.selectbox("Select roll_number", roll_list,key=12)
            df.index=roll_list
            d2=df.loc[roll_choice]
            print(type(d2))
            del d2[roll]
            x2=d2.keys()
            y2=[d2[i] for i in x2]
            y_mapping = {'A':6,'A+':7,'B':5,'C':4,'D':3,'E':2,'F':1}
            mp={6:'A',7:'A+',5:'B',4:'C',3:'D',2:'E',1:'F'}
            y_labels = ['A+', 'A', 'B', 'C', 'D', 'E', 'F',' ']
            y_labels=y_labels[::-1]
            y2=[y_mapping[f] for f in y2]
            l=[i for i in range(8)]
            fig2, ax2 = plt.subplots(figsize=(8, 4))
            fig2.set_facecolor('#dd99ff')
            ax2.set_facecolor('#ccffff')
            ax2.bar(x2,y2,width=0.3,color='Green')
            for i, v in enumerate(y2):
                ax2.text(i, v, mp[v], ha='center',bbox=dict(boxstyle='square,pad=0.3', facecolor='Red', edgecolor='blue', linewidth=0.2))
                 
            ax2.set_xlabel('Grade',color='#3333ff')
            ax2.set_ylabel('Subjects',color='#3333ff')
            ax2.set_title('Result of a Student',color='#3333ff')
            ax2.grid(False)
            ax2.set_yticks(l, y_labels)
            st.pyplot(fig2)
            
        else:
            print("li")
    elif selected_option == "Attendance Analyzer":
        print("ki")

if __name__ == "__main__":
    main()
 
    