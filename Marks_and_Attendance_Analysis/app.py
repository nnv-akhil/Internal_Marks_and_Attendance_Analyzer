import streamlit as st
import openpyxl
import matplotlib.pyplot as plt
import pandas as pd,seaborn as sns
import matplotlib.patches as patches
import numpy as np
import streamlit.components.v1 as components
def main():
    st.sidebar.title("Select your Analyzer")
    selected_option=""
    selected_option = st.sidebar.selectbox("Select an option", ["Select an option","External Marks Analyzer","Internal Marks Analyzer", "Attendance Analyzer"])
    print(selected_option)
    if selected_option == "External Marks Analyzer":
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
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
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
                st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
            st.title("Select your desired subject to get Pass-Fail Ratio\n")
            sub_choice = st.selectbox("Select your subject", subjects,key=10)
            l=df[sub_choice]
            x=0
            y=0
            for m in l:
                if(m=='F'):
                    x+=1
                else:
                    y+=1
            fig, ax = plt.subplots(figsize=(6,4))
            fig.set_facecolor('#dd99ff')
            ax.set_facecolor('#ccffff')
            ax.pie([y,x], labels=['PASS','Fail'], colors=['green','red'], autopct='%1.1f%%', shadow=False, startangle=140)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
            d=d.sort_values('CGPA',ascending=False)
            d.index=[i for i in range(1,len(d)+1)]
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
            selected_value = st.slider('Select a value', min_value=1, max_value=len(df), value=10)
            st.title(f"Top {selected_value} Performers of current semester")
            st.write(d.head(selected_value))
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
            st.title("Select your desired subject to get its stats\n")
            sub_choice1 = st.selectbox("Select your subject", subjects,key=11)
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
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
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
            x3={'9-10':0,'8-9':1,'7-8':2,'6-7':3,'5-6':4,'1-5':5}
            y3=[[],[],[],[],[],[]]
            for index, row in d.iterrows():
                if(row['CGPA']>9):
                    y3[0].append(row[roll])
                elif(row['CGPA']>8):
                    y3[1].append(row[roll])
                elif(row['CGPA']>7):
                    y3[2].append(row[roll])
                elif(row['CGPA']>6):
                    y3[3].append(row[roll])
                elif(row['CGPA']>5):
                    y3[4].append(row[roll])
                else:
                    y3[5].append(row[roll])
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
            choice=st.selectbox("Select your range", x3.keys(),key=13)
            st.title(f'Students having cgpa in {choice} range')
            d3=pd.DataFrame(y3[x3[choice]],columns=['ROLL_NO'],index=[i for i in range(1,len(y3[x3[choice]])+1)])
            st.write(d3)
            df.drop([roll],axis=1, inplace=True)
            df = df.rename_axis(roll)
            # st.markdown("---")
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
            st.title('Students Count with Backlogs')
            x4=[0,1,2,3,4,5,6]
            y4=[0,0,0,0,0,0,0]
            for index, row in df.iterrows():
                p=0 
                for m in subjects:
                    if(row[m]=='F'):
                        p+=1
                y4[p]+=1
            fig4, ax4 = plt.subplots()
            fig4.set_facecolor('#dd99ff')
            ax4.set_facecolor('#ccffff')
            ax4.bar(x4,y4)
            for i, v in enumerate(y4):
                ax4.text(i, v //2, str(v), ha='center',bbox=dict(facecolor='white', alpha=0.5))
            ax4.set_xlabel('No of Backlogs',color='#3333ff')
            ax4.set_ylabel('Count',color='#3333ff')
            ax4.set_title('Count of students vs Backlogs',color='#3333ff')
            ax4.grid(False)
            st.pyplot(fig4)
        else:
            print("li")
    if selected_option == "Internal Marks Analyzer":
        st.title("Your INSIGHTS")
        uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=['xlsx'],key=1)
        if uploaded_file is not None:
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            l=df.columns
            l1=[l[0]]
            for i in range(5,11):
                l1.append(l[i])
            for i in range(14,len(l)):
                if((i-3)%9!=0):
                    if((i-4)%9!=0):
                        if((i-11)%9!=0):
                            l1.append(l[i])
            df.drop(l1,axis=1,inplace=True)
            df.drop(df.index[1], inplace=True)
            l=df.iloc[0]
            l=l.to_dict()
            df.drop(df.index[0], inplace=True)
            l1=[i for i in l.keys()]
            for x in l1:
                if pd.isna(l[x]):
                    del l[x]
            df.drop(df.index[0], inplace=True)
            l1=df.columns
            i=2
            j=0
            sub=[i.replace(" ","_") for i in l.values()]
            col=['Roll_No','Name']
            for i in sub:
                col.append(i+"_1")
                col.append(i+"_2")
                col.append(i+"_Int")
            df.columns=col
            st.title("Select subject to get failures")
            sub_choice = st.selectbox("Select your subject", sub,key=10)
            sub_choice+="_Int"
            ans=[[],[]]
            for index, row in df.iterrows():
                if(row[sub_choice]<12):
                    ans[0].append(row[col[0]])
                    ans[1].append(row[sub_choice])
            st.title(f"Students failed in {sub_choice[:-4]}")
            d=pd.DataFrame(list(zip(ans[0],ans[1])),columns=[col[0],sub_choice])
            st.write(d)
            st.markdown("""<hr width='100%' style='height:10px;border:none;border-style:'dashed';background-color:#333;' /> """, unsafe_allow_html=True)
            st.title("Select subject and your choice")
            sub_choice1 = st.selectbox("Select your subject", sub,key=11)
            ans1=[[],[]]
            for index, row in df.iterrows():
               #st.write(type(row[sub_choice1+"_1"]),row[sub_choice1+"_2"])
                if(row[sub_choice1+"_1"]<row[sub_choice1+"_2"]):
                    ans1[0].append(row[col[0]])
                elif(row[sub_choice1+"_1"]>row[sub_choice1+"_2"]):
                    ans1[1].append(row[col[0]])
            #st.title("Select your choice")
            choice1 = st.selectbox("Select your choice",['Mid_1<Mid_2','Mid_2<Mid_1'],key=110)
            st.title(f"Students whose performance is {choice1}")
            if(choice1=='Mid_1<Mid_2'):
                d=pd.DataFrame(ans1[0],columns=[col[0]])
            else:
                d=pd.DataFrame(ans1[1],columns=[col[0]])
            d.index=[i for i in range(1,len(d)+1)]
            st.write(d)



    elif selected_option == "Attendance Analyzer":
        print("ki")

if __name__ == "__main__":
    main()
 
    