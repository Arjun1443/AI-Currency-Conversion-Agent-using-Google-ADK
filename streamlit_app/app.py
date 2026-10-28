import pandas as pd
import streamlit as st
from ui import page
from engine import convert

page('Currency Conversion Studio','A transparent conversion calculator: provide a rate, inspect the arithmetic, and compare fees.','AGENT APPLICATION')
calculator,method=st.tabs(['Conversion calculator','Notebook & design'])
with calculator:
    with st.form('conversion'):
        a,b=st.columns(2)
        source=a.selectbox('From currency',['USD','INR','EUR','GBP','JPY','AUD'])
        target=b.selectbox('To currency',['INR','USD','EUR','GBP','JPY','AUD'])
        amount=a.number_input('Amount',min_value=0.0,value=1250.0,step=50.0)
        rate=b.number_input('Your exchange rate (target per 1 source)',min_value=.000001,value=1.0,format='%.6f')
        fee=st.slider('Conversion fee (%)',0.0,10.0,0.0,.1)
        confirmed=st.checkbox('I have supplied the intended rate; this is not a live market quote.')
        submit=st.form_submit_button('Calculate conversion',type='primary')
    if submit:
        if not confirmed: st.warning('Confirm your supplied exchange rate to continue.')
        else:
            result=convert(amount,rate,fee)
            a,b,c=st.columns(3)
            a.metric('Gross amount',f'{result["gross"]:,} {target}')
            b.metric('Conversion fee',f'{result["fee"]:,} {target}')
            c.metric('Net received',f'{result["net"]:,} {target}')
            st.code(f'{amount} {source} × {rate} = {result["gross"]} {target}\nNet = gross − {fee}% fee = {result["net"]} {target}')
            st.download_button('Download calculation',pd.DataFrame([{**result,'from':source,'to':target,'amount':amount,'rate':rate,'fee_percent':fee}]).to_csv(index=False),'conversion.csv','text/csv')
with method:
    st.markdown("""### Reliable arithmetic, explicit rates
This companion app uses Python Decimal and rounds to two decimal places. Rates are supplied by the visitor, not fetched or invented by a language model. Two decimals are a demonstration convention, not every currency's settlement rule.

The notebook explores Google ADK and Gemini instruction design. This app extracts the practical conversion task into a deterministic calculator. It does not run the notebook's agent or connect to a bank or live exchange-rate provider.
""")
