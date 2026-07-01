import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("senegal_merged.csv")

st.markdown ("Research Paper")
st.title("The Relationship Between GDP per Capita and Basic Access to Water in Senegal")

st.markdown (""" 
**Fatim Diagne**
             
*Master's Student in Public and International Affairs, University of Ottawa*.

Disclaimer: According to the World Bank’s definition, basic access to water is considered to be met when the time required to collect water is less than 30 minutes round trip (World Bank, 2023).
"""
)

st.header("Abstract")
st.info( """
This project explores the relationship between GDP per capita and basic drinking water access in Senegal (2000–2024), using World Bank data. 
        A full econometric analysis, including control variables (urbanization, population, agricultural share of GDP) and both levels and first-difference models, is available in the complete paper. 
        The visualization presented here offers a descriptive view of the relationship: while economic growth is generally associated with improved water access, this chart alone does not control for other factors and should not be read as causal.
""")

st.header("Data")

with st.expander("View underlying data"):
    st.dataframe(data)

# --- Chart ---
st.header("Visualization")

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=data["year"], y=data["gdp_per_capita"],
    name="GDP per capita (US$)", line=dict(color="royalblue")
))
fig.add_trace(go.Scatter(
    x=data["year"], y=data["water_access_pct"],
    name="Water access (%)", yaxis="y2", line=dict(color="seagreen")
))

fig.update_layout(
    xaxis=dict(title="Year", dtick=2),
    yaxis=dict(title=dict(text="GDP per capita (US$)", font=dict(color="royalblue"))),
    yaxis2=dict(title=dict(text="Water access (%)", font=dict(color="seagreen")),
                overlaying="y", side="right"),
    template="plotly_white",
    height = 600,
)
st.plotly_chart(fig, use_container_width=True)

st.caption("This chart shows a descriptive relationship between GDP per capita and basic water access in Senegal (2000–2024). " \
"It does not control for other factors like urbanization or population growth. " \
"See the full paper for the complete econometric analysis.")


st.title("Conclusion")

st.markdown (""" 
<div style="text-align: justify;">
This visualization illustrates a positive association between GDP per capita and basic water access in Senegal between 2000 and 2024. As the country's economy has grown, access to basic drinking water has generally improved alongside it.
This relationship, however, should be read as descriptive rather than causal. The chart does not account for other contributing factors such as urbanization, population growth, or the structure of the economy. A full econometric analysis, including these control variables, is available in the accompanying research paper.
Taken together, this suggests that economic growth is a favorable condition for expanding access to basic services, but not a guarantee of universal or equitable access on its own, underscoring the need for targeted public investment and policy alongside economic development.
</div> """,
unsafe_allow_html=True
)