import streamlit as st

# To do: 
# - Split the results section into its own page (maybe)
# - Put each of the sections together rather than results report and recommendations
# - Make it in normal English

# Heading dividers
def h4_divider(text):
    st.markdown(f"<h5 style='margin-bottom: 0; color: #404040'>{text}</h5>", unsafe_allow_html=True)
    st.markdown("<hr style='margin-top: 0; border: none; height: 1px; background-color: black;'>", unsafe_allow_html=True)

st.set_page_config(page_title='Cardiometabolic Calculator', page_icon = "favicon.ico")

# Center align the title and subheader
col1, col2 = st.columns([1,3], gap = "large")
with col1:
    # Add the logo
    st.image("mg_logo.png", use_column_width='auto')
with col2:
    st.markdown("""<h2 style='margin-top: -1; text-align: center; color: #404040;'>Positive Cardiometabolic Health Resource - Calculator</h2>""", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #404040;'>An early intervention framework for people on psychotropic medication</h4>", unsafe_allow_html=True)

#Explainer text
h4_divider("How to use the calculator:")
st.markdown("""<p style='text-align: justify; color: #404040;'>This is a tool to help you identify people on psychotropic medications who may be at risk of poor cardiometabolic health and provide them with early intervention. It is not a diagnostic tool and should not be used to diagnose CMD. It is also not a substitute for clinical judgement. If you have any concerns about a person's health, please contact your local GP or mental health clinician.</p>""", unsafe_allow_html=True)

# Demographic questions
st.markdown("")
st.markdown("")
h4_divider("Demographics")
patient_name = st.text_input(label = "What is the person's name or initials? (optional)", help = "This will be used to personalise the report at the end and will not be stored or shared with anyone else.")
col1, col2, col3 = st.columns(3)
with col1:
    sex = st.radio("What is the person's sex?", ["Male", "Female", "Other"])
with col2:
    age = st.number_input(label="What is the person's age?", step=1, min_value=0, max_value=120, help = "This is to determine which risk calculations and recommendations should be made as they vary between age groups.")
with col3:
    ethnicity = st.radio("Is the person of any of the following ethnicities? South Asian, Chinese, Japanese, Ethnic South and Central Americans", ["Yes", "No"])

# Lifestyle questions
st.markdown("""---""")
st.header("Lifestyle")
col1, col2, col3 = st.columns(3)
with col1:
    smoking = st.radio("Is the person a current smoker (including tobacco, THC, vaping, shisha)?", ["Yes", "No"])
with col2:
    diet = st.radio(label="Does the person have a poor diet?", options = ["Yes", "No"], help="Poor diet includes high intake of processed foods, red meat, sugar-sweetened beverages, and low intake of vegetables, fruit, wholegrains, legumes/beans, and fish. See https://dietitiansaustralia.org.au/sites/default/files/2022-02/DA_NationalNutritionStrategy_Brief.pdf for more information.")
with col3:
    activity = st.radio("Does the person have more than 30 minutes physical activity on most days?", ["Yes", "No"])

# Obesity questions
st.markdown("""---""")
st.header("Obesity")
col1, col2, col3 = st.columns(3)
with col1:
    bmi_options = ['<25','25-29','30-34','≥35']
    if ethnicity == "Yes":
        bmi_options = ['<23','≥23', '23-30','30-34','≥35']
    bmi = st.radio(label = "What is the person's BMI?", options = bmi_options)
with col2:
    weight_increase = st.radio("Has the person had a weight increase of greater than 5kg over the past 3 months?", ["Yes", "No"])
with col3:
    waist_options = ['<80','≥80']
    if sex == 'Male':
        if ethnicity == "Yes":
            waist_options = ['<90','≥90'] 
        else:
            waist_options = ['<94','≥94']
    
    waist_circ = st.radio(label = "What is the person's waist circumference in cm?", options=waist_options)
col1, col2 = st.columns(2)
with col1:
    waist_increase = st.radio("Has the person had an increase in waist circumference of over 5cm in the past 3 months?", ["Yes", "No"])

# Blood pressure questions
st.markdown("""---""")
st.header("Blood Pressure")
col1, col2 = st.columns(2)
with col1:
    sys_bp_options = ['<140 mmHg','≥140 mmHg']
    systolic_bp = st.radio(label = "What is the person's systolic blood pressure?", options = sys_bp_options)
with col2:
    dia_bp_options = ['<90 mmHg','≥90 mmHg']
    diastolic_bp = st.radio(label = "What is the person's diastolic blood pressure?", options = dia_bp_options)

# Glucose questions
st.markdown("""---""")
st.header("Glucose")
col1, col2, col3, col4 = st.columns(4)
with col1:
    hba1c_options = ['<6.0% (<42 mmol/mol)','6.0%-6.4% (42-47 mmol/mol)','≥6.4% (48 mmol/mol)']
    hba1c = st.radio(label = "What is the person's HbA1c?", options = hba1c_options)
with col2:
    fpg_options = ['<5.6 mmol/L','5.6-6.9 mmol/L','≥7.0 mmol/L']
    fpg = st.radio(label = "What is the person's FPG?", options = fpg_options)
with col3:
    ausdrisk_options = ['<12','≥12']
    ausdrisk = st.radio(label = "What is the person's [AUSDRISK](%s)?" % 'https://www.health.gov.au/resources/apps-and-tools/the-australian-type-2-diabetes-risk-assessment-tool-ausdrisk', options = ausdrisk_options)
with col4:
    rpg_options = ['<11 mmol/L','>11 mmol/L']
    rpg = st.radio(label = "What is the person's RPG?", options = rpg_options)

# Blood lipids questions
st.markdown("""---""")
st.header("Blood Lipids")
col1, col2, col3 = st.columns(3)
with col1:
    tc_options = ['<4 mmol/L','≥4 mmol/L']
    tc = st.radio(label = "What is the person's TC?", options = tc_options)
with col2:
    ldl_options = ['<2 mmol/L','≥2 mmol/L']
    ldl = st.radio(label = "What is the person's LDL?", options = ldl_options)
with col3:
    hdl_options = ['<1 mmol/L','≥1 mmol/L']
    hdl = st.radio(label = "What is the person's HDL?", options = hdl_options)
col1, col2, col3 = st.columns(3)
with col1:
    non_hdl_options = ['<2.5 mmol/L','≥2.5 mmol/L']
    non_hdl = st.radio(label = "What is the person's non-HDL?", options = non_hdl_options)
with col2:
    trig_options = ['<1.7 mmol/L','≥1.7 mmol/L']
    trig = st.radio(label = "What is the person's TRIG?", options = trig_options)
with col3:
    placeholder = st.empty()

# Sleep questions
st.markdown("""---""")
st.header("Sleep")
col1, col2, col3 = st.columns(3)
with col1:
    neck_circ_options = ['<40 cm','≥40 cm']
    neck_circ = st.radio(label="What is the person's neck circumference in cm?", options = neck_circ_options)
with col2:
    daytime_tiredness = st.radio("Does the person have daytime tiredness?", ["Yes", "No"])
with col3:
    snoring = st.radio("Does the person have loud snoring or stop breathing during sleep?", ["Yes", "No"])


submit = st.button("Submit")

# Recommendations
if submit:
    start = False
    #st.write("**Cardiometabolic Calculator Recommendations**")


    #st.write("**Current Values:**")
    # Table of the current values that were entered by the user that are not blank
    #col1, col2, col3 = st.columns(3)
    #with col1:
    #    st.write("**Lifestyle:**")
    #    st.write("Smoking: ", smoking)
    #    st.write("Diet: ", diet)
    #    st.write("Activity: ", activity)
    #    st.write("Weight Increase: ", weight_increase)
    #    st.write("Waist Increase: ", waist_increase)   
    #with col2:
    #    st.write("**Obesity:**")
    #    st.write("BMI: ", bmi)
    #    st.write("Waist Circumference: ", waist_circ)
    #    st.write("Waist Increase: ", waist_increase)
    #    st.write("Weight Increase: ", weight_increase)
    #with col3:
    #    st.write("**Blood Pressure:**")
    #    st.write("Systolic BP: ", systolic_bp)
    #    st.write("Diastolic BP: ", diastolic_bp)
    #col1, col2, col3 = st.columns(3)
    #with col1:
    #    st.write("**Glucose:**")
    #    st.write("HbA1c: ", hba1c)
    #    st.write("FPG: ", fpg)
    #    st.write("AUSDRISK: ", ausdrisk)
    #with col2:
    #    st.write("**Blood Lipids:**")
    #    st.write("TC: ", tc)
    #    st.write("LDL: ", ldl)
    #    st.write("HDL: ", hdl)
    #    st.write("RPG: ", rpg)
    #    st.write("non-HDL: ", non_hdl)
    #    st.write("TRIG: ", trig)
    #with col3:
    #    st.write("**Sleep:**")
    #    st.write("Neck Circumference: ", neck_circ)
    #    st.write("Daytime Tiredness: ", daytime_tiredness)
    #    st.write("Snoring: ", snoring)

    st.write(" ")
    st.markdown("""---""")
    st.write("# **Personalised Recommendations Report:**")
    st.write("Persons Name: ", patient_name)
    st.write("Age: ", str(age))
    st.write("Sex: ", sex)

    st.write("Intensify and individualise structured nutritional counselling and lifestyle interventions. Refer for investigation, diagnosis and treatment by appropriate clinician if necessary.")
    st.write("Medication review (consider antipsychotic switching; review medications and rationalise any polypharmacy).")

    if smoking == "Yes":
        st.markdown("""---""")
        st.markdown(body = """
        ### **Smoking:**
        As the person is a smoker, it is recommended that they quit smoking. This will help to reduce their risk of developing cardiovascular disease.
        #### *Interventions:*
        <li>Individualised smoking cessation program</li>
        <li>Use Mindgardens Tobacco Treatment Framework</li>
        <li>quitnow.gov.au</li>
        <li>icanquit.com.au</li>

        #### *Targets:*
        <li>Smoking prevention or cessation</li>
        """, unsafe_allow_html = True)

    if diet == "Yes":
        st.markdown("""---""")
        st.markdown(body ="""
        ### **Diet:**
        As the person has a poor diet, it is recommended that they improve their diet. This will help to reduce their risk of developing cardiovascular disease.
        #### *Interventions:*
        <li>Decrease in discretionary foods</li>
        <li>Increase in vegetables and legumes/beans</li>
        <li>Consider referral to a Dietitian</li>
        <li>eatforhealth.gov.au</li>
        
        #### *Targets:*
        <li>Improve quality of diet</li>
        <li>Contain energy intake (to stabilise weight)</li>
        """, unsafe_allow_html = True)
    if activity == "No":
        st.markdown("""---""")
        st.markdown(body = """
        ### **Activity:**
        As the person is sedentary, it is recommended that they increase their physical activity. This will help to reduce their risk of developing cardiovascular disease.
        #### *Interventions:*
        <li>Decrease sedentariness</li>
        <li>Increase physical activity</li>
        <li>Refer to the Physical Activity Guidelines</li>
        <li>Consider referral to an Exercise Physiologist</li>
        
        #### *Targets:*
        <li>Physical activity (at least 30 mins on most, preferably all days)</li>
        """, unsafe_allow_html = True)

    if (bmi in ['25-29','30-34','≥35'] or (bmi in ['≥23', '23-30','30-34','≥35']) and ethnicity=='Yes') or (weight_increase == "Yes") or (sex == "Male" and waist_circ >= 94) or (sex == "Female" and waist_circ >= 80) or (ethnicity == "Yes" and sex == "Male" and waist_circ >= 90) or waist_increase == "Yes":
        st.markdown("""---""")
        st.markdown(body = f"""
        ### **Weight and BMI:**
        As the person has a BMI of {bmi} kg/m2, it is recommended that they lose weight. This will help to reduce their risk of developing cardiovascular disease.
        #### *Interventions:*
        <li>Consider metformin and/or GLP receptor agonist</li>""", unsafe_allow_html = True)
        if bmi in ["30-34","≥35"]:
            st.markdown(body = """Consider intensive intervention if BMI is greater than or equal to 30""", unsafe_allow_html = True)
        st.markdown(body = """#### *Targets:*""", unsafe_allow_html = True)
        st.markdown(body = """<li>BMI 20-24.9 kg/m2 (<23 kg/m2) </li>
        <li>Waist circumference: <94 cm male (<90 cm) and <80 cm female </li>""", unsafe_allow_html = True)

    if systolic_bp == '≥140 mmHg' or diastolic_bp == '≥90 mmHg':
        st.markdown("""---""")
        st.markdown(body = f"""
        ### **Blood Pressure:**
        As the person has a systolic blood pressure of {systolic_bp} and a diastolic blood pressure of {diastolic_bp}, it is recommended that they lower their blood pressure. This will help to reduce their risk of developing cardiovascular disease.
        #### *Interventions:*
        <li>Consider antihypertensive medication</li>
        <li>Limit salt intake in diet</li>
        
        #### *Targets:*
        <li><140 mmHg systolic and/or <90 mmHg diastolic</li>
        <li>(<130/80 if CVD or diabetes)</li>
        """, unsafe_allow_html = True)

    if (hba1c == ['6.0%-6.4% (42-47 mmol/mol)','≥6.4% (48 mmol/mol)']) or (fpg in ['5.6-6.9 mmol/L','≥7.0 mmol/L']) or ausdrisk == '≥12':
        if hba1c == "≥6.4% (48 mmol/mol)" or fpg == "≥7.0 mmol/L" or rpg == "≥11.1 mmol/L":
            st.markdown("""---""")
            st.markdown(body = f"""
            ### **Glucose:**
            The person has a HbA1c of {hba1c}, a FPG of {fpg} and a RPG of {rpg}. This indicates that they meet the criteria for diabetes and intervention is recommended.
            #### *Interventions:*
            <li>{patient_name} meets the criteria for diabetes</li>
            <li> Consider metformin</li>
            <li>Consider referral to an endocrinologist</li>
            
            #### *Targets:*
            <li>HbA1c individualised to the consumer's circumstances</li>
            <li>Generally <7% As per [RACGP Handbook](https://www.racgp.org.au/clinical-resources/clinical-guidelines/key-racgp-guidelines/view-all-racgp-guidelines/diabetes/introduction)</li>
            """, unsafe_allow_html = True)
        else:
            st.markdown("""---""")
            st.markdown(body = f"""
            ### **Glucose:**
            The person has a HbA1c of {hba1c}, a FPG of {fpg} and a RPG of {rpg}. This indicates that they are at risk of diabetes and intervention is recommended.
            #### *Interventions:*
            <li>Consider metformin</li>
            <li>Consider referral to an endocrinologist if necessary</li>
            
            #### *Targets:*
            It is vital to prevent or delay onset of diabetes by targeting:
            <li>HbA1c <6.0% (<42 mmol/mol)</li>
            <li>FPG <5.6 mmol/L</li>

            """, unsafe_allow_html = True)

    if tc == "≥4 mmol/L" or ldl == "≥2 mmol/L" or hdl == "≥1 mmol/L" or non_hdl == "≥2.5 mmol/L" or trig == "≥1.7 mmol/L":
        st.markdown("""---""")
        st.markdown(body = f"""
        ### **Blood Lipids:**
        As the person has a TC of {tc}, a LDL of {ldl}, a HDL of {hdl}, a non-HDL of {non_hdl} and a TRIG of {trig}, it is recommended that they lower their blood lipids. This will help to reduce their risk of developing cardiovascular disease.
        #### *Interventions:*
        <li>Consider lipid lowering therapy</li>

        #### *Targets:*
        <li>TC <4 mmol/L</li>
        <li>LDL <2.0 mmol/L (<1.8 if CVD or diabetes) </li>
        <li>HDL ≥1.0 mmol/L</li>
        <li>non-HDL <2.5 mmol/L</li>
        <li>TRIG <1.7 mmol/L</li>
        """, unsafe_allow_html = True)

    if bmi == '≥35' or neck_circ == "≥40 cm" or daytime_tiredness == "Yes" or snoring == "Yes":
        st.markdown("""---""")
        st.markdown(body = f"""
        ### **Sleep:**
        As the person has a BMI of {bmi} kg/m2, a neck circumference of {neck_circ} cm, daytime tiredness and snoring, it is recommended that they be assessed for obstructive sleep apnoea.
        #### *Interventions:*
        <li>Consider referral for a sleep study</li>
        <li>If mild-moderate sleep apnoea is diagnosed, target weight loss</li>
        <li>If severe sleep apnoea is diagnosed, consider CPAP</li>
        
        #### *Targets:*
        <li>Improved alertness</li>
        <li>Reduced or resolved OSA</li>
        """, unsafe_allow_html = True)


markdown_body = f"""Cardiometabolic Calculator Recommendations

"""

markdown_body += "Intensify and individualise structured nutritional counselling and lifestyle interventions. Refer for investigation, diagnosis and treatment by appropriate clinician if necessary."
markdown_body += """
Medication review (consider antipsychotic switching; review medications and rationalise any polypharmacy).

"""

if smoking == "Yes":
    markdown_body += """
    Smoking:
    As the person is a smoker, it is recommended that they quit smoking. This will help to reduce their risk of developing cardiovascular disease.
    Interventions:
    • Individualised smoking cessation program
    • Use Mindgardens Tobacco Treatment Framework
    • quitnow.gov.au
    • icanquit.com.au

    Targets:
    • Smoking prevention or cessation
    
    """

if diet == "Yes":
    markdown_body += """
    Diet:
    As the person has a poor diet, it is recommended that they improve their diet. This will help to reduce their risk of developing cardiovascular disease.
    Interventions:
    • Decrease in discretionary foods
    • Increase in vegetables and legumes/beans
    • Consider referral to a Dietitian
   • eatforhealth.gov.au
    
    Targets:
    • Improve quality of diet
    • Contain energy intake (to stabilise weight)

    """

if activity == "No":
    markdown_body += """
    Activity:
    As the person is sedentary, it is recommended that they increase their physical activity. This will help to reduce their risk of developing cardiovascular disease.
    Interventions:
    • Decrease sedentariness
    • Increase physical activity
    • Refer to the Physical Activity Guidelines
    • Consider referral to an Exercise Physiologist
    
    Targets:
    • Physical activity (at least 30 mins on most, preferably all days)

    """

if (bmi in ['25-29','30-34','≥35'] or (bmi in ['≥23', '23-30','30-34','≥35']) and ethnicity=='Yes') or (weight_increase == "Yes") or (sex == "Male" and waist_circ >= 94) or (sex == "Female" and waist_circ >= 80) or (ethnicity == "Yes" and sex == "Male" and waist_circ >= 90) or waist_increase == "Yes":
    markdown_body += f"""
    Weight and BMI:
    As the person has a BMI of {bmi} kg/m2, it is recommended that they lose weight. This will help to reduce their risk of developing cardiovascular disease.
    Interventions:
    • Consider metformin and/or GLP receptor agonist
    """
    if bmi in ["30-34","≥35"]:
        markdown_body += """Consider intensive intervention if BMI is greater than or equal to 30"""
    markdown_body += """Targets:"""
    markdown_body += """<li>BMI 20-24.9 kg/m2 (<23 kg/m2)
    • Waist circumference: <94 cm male (<90 cm) and <80 cm female """

if systolic_bp == '≥140 mmHg' or diastolic_bp == '≥90 mmHg':
    markdown_body += f"""
    Blood Pressure:
    As the person has a systolic blood pressure of {systolic_bp} and a diastolic blood pressure of {diastolic_bp}, it is recommended that they lower their blood pressure. This will help to reduce their risk of developing cardiovascular disease.
    Interventions:
    • Consider antihypertensive medication
    • Limit salt intake in diet
    
    Targets:
    • <140 mmHg systolic and/or <90 mmHg diastolic
    • (<130/80 if CVD or diabetes)

    """

if (hba1c == ['6.0%-6.4% (42-47 mmol/mol)','≥6.4% (48 mmol/mol)']) or (fpg in ['5.6-6.9 mmol/L','≥7.0 mmol/L']) or ausdrisk == '≥12':
    if hba1c == "≥6.4% (48 mmol/mol)" or fpg == "≥7.0 mmol/L" or rpg == "≥11.1 mmol/L":
        markdown_body += f"""
        Glucose:
        The person has a HbA1c of {hba1c}, a FPG of {fpg} and a RPG of {rpg}. This indicates that they meet the criteria for diabetes and intervention is recommended.
        Interventions:
        • {patient_name} meets the criteria for diabetes
        •  Consider metformin
        • Consider referral to an endocrinologist
        
        Targets:
        • HbA1c individualised to the consumer's circumstances
        • Generally <7% As per RACGP Handbook - https://www.racgp.org.au/clinical-resources/clinical-guidelines/key-racgp-guidelines/view-all-racgp-guidelines/diabetes/introduction

        """
    else:
        markdown_body += f"""
        Glucose:
        The person has a HbA1c of {hba1c}, a FPG of {fpg} and a RPG of {rpg}. This indicates that they are at risk of diabetes and intervention is recommended.
        Interventions:
        • Consider metformin
        • Consider referral to an endocrinologist if necessary
        
        Targets:
        It is vital to prevent or delay onset of diabetes by targeting:
        • HbA1c <6.0% (<42 mmol/mol)
        • FPG <5.6 mmol/L

        """

if tc == "≥4 mmol/L" or ldl == "≥2 mmol/L" or hdl == "≥1 mmol/L" or non_hdl == "≥2.5 mmol/L" or trig == "≥1.7 mmol/L":
    markdown_body += f"""
    Blood Lipids:
    As the person has a TC of {tc}, a LDL of {ldl}, a HDL of {hdl}, a non-HDL of {non_hdl} and a TRIG of {trig}, it is recommended that they lower their blood lipids. This will help to reduce their risk of developing cardiovascular disease.
    Interventions:
    • Consider lipid lowering therapy

    Targets:
    • TC <4 mmol/L
    • LDL <2.0 mmol/L (<1.8 if CVD or diabetes)
    • HDL ≥1.0 mmol/L
    • non-HDL <2.5 mmol/L
    • TRIG <1.7 mmol/L

    """

if bmi == '≥35' or neck_circ == "≥40 cm" or daytime_tiredness == "Yes" or snoring == "Yes":
    markdown_body += f"""
    Sleep:
    As the person has a BMI of {bmi} kg/m2, a neck circumference of {neck_circ} cm, daytime tiredness and snoring, it is recommended that they be assessed for obstructive sleep apnoea.
    Interventions:
    • Consider referral for a sleep study
    • If mild-moderate sleep apnoea is diagnosed, target weight loss
    • If severe sleep apnoea is diagnosed, consider CPAP
    
    Targets:
    • Improved alertness
    • Reduced or resolved OSA
    
    """

#st.code(markdown_body, language='markdown', line_numbers=False)