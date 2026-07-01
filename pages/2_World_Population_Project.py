import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv("world_pop_data.csv")

data = pd.read_csv("world_pop_data.csv")
data = data.rename(columns={"density (km²)": "density (km2)", "area (km²)": "area (km2)"})


st.title("World Population Analysis")
st.markdown("*Exploring global population distribution, top countries, and density patterns by continent.*")

# --- Population change over time ---
st.header("Population Growth by Continent (1970–2023)")
continent_totals = data.groupby("continent")[
    ["1970 population", "1980 population", "1990 population",
     "2000 population", "2010 population", "2015 population",
     "2020 population", "2022 population", "2023 population"]
].sum().T
continent_totals.index = ["1970", "1980", "1990", "2000", "2010", "2015", "2020", "2022", "2023"]

fig3 = px.line(
    continent_totals, x=continent_totals.index, y=continent_totals.columns,
    title="Population Growth by Continent (1970–2023)",
    template="plotly_white"
)
fig3.update_layout(xaxis_title="Year", yaxis_title="Total Population")
st.plotly_chart(fig3, use_container_width=True)

# --- Bar chart top 10 countries ---
st.header("Top 10 Most Populous Countries")
top_10 = data.sort_values(by="2023 population", ascending=False).head(10)
fig2 = px.bar(
    top_10, x="2023 population", y="country", orientation="h",
    title="Top 10 Countries by Population in 2023",
    template="plotly_white"
)
fig2.update_layout(xaxis_title="Population", yaxis_title="Country",
                    yaxis=dict(categoryorder="total ascending"))
st.plotly_chart(fig2, use_container_width=True)

# --- World Map ---
st.header("Global Population by Country")
fig1 = px.choropleth(
    data,
    locations="country",
    locationmode="country names",
    color="2023 population",
    color_continuous_scale="Reds",
    title="2023 Population by Country",
    height= 650
)
st.plotly_chart(fig1, use_container_width=True)

with st.expander("View underlying data"):
    st.dataframe(data)