
import streamlit as st
import pandas as pd
import plotly.express as px
from database_utils import run_query

st.set_page_config(
    page_title="Education Policy Explorer",
    page_icon="📊",
    layout="wide"
)

st.title("India Education Policy Explorer")
st.write(
    "Explore state-level pupil–teacher ratios "
    "from UDISE+ 2023–24."
)

@st.cache_data
def load_data():
    data = pd.read_csv("data/processed/education_ptr.csv")
    data["state"] = data["state"].astype("string").str.strip()

    for col in [
        "ptr_primary",
        "ptr_secondary",
        "ptr_upper_secondary",
        "ptr_higher_secondary"
    ]:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    return data.dropna(subset=["state"])

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "Cleaned CSV not found. Save it to "
        "data/processed/education_ptr.csv."
    )
    st.stop()

labels = {
    "ptr_primary": "Primary",
    "ptr_secondary": "Secondary",
    "ptr_upper_secondary": "Upper Secondary",
    "ptr_higher_secondary": "Higher Secondary"

}

indicator = st.selectbox(
    "Select school level",
    options=list(labels.keys()),
    format_func=lambda value: labels[value]
)

states = sorted(df["state"].dropna().unique().tolist())

selected_states = st.multiselect(
    "Filter states and union territories",
    options=states,
    default=states
)

filtered = df[df["state"].isin(selected_states)].copy()
available = filtered.dropna(subset=[indicator]).copy()

if available.empty:
    st.warning("No valid values for the selected filters.")
    st.stop()

mean_value = available[indicator].mean()
median_value = available[indicator].median()

c1, c2, c3 = st.columns(3)

c1.metric("Regions with data", len(available))
c2.metric("Mean PTR", f"{mean_value:.2f}")
c3.metric("Median PTR", f"{median_value:.2f}")

st.subheader("State-level comparison")

chart_data = available.sort_values(indicator)

fig = px.bar(
    chart_data,
    x=indicator,
    y="state",
    orientation="h",
    labels={
        indicator: "Pupils per teacher",
        "state": "State / UT"
    },
    title=f"{labels[indicator]} pupil–teacher ratio"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Data table")

st.dataframe(
    available[["state", indicator]].sort_values(indicator),
    use_container_width=True,
    hide_index=True
)

csv = available.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download filtered data",
    data=csv,
    file_name="filtered_education_ptr.csv",
    mime="text/csv"
)

st.caption(
    "Source: UDISE+ 2023–24, via data.gov.in. "
    "PTR is descriptive and does not independently measure "
    "teaching quality or educational outcomes."
)

Query1 = run_query("Query1.sql")
Query2 = run_query("Query2.sql")
Query3 = run_query("Query3.sql")
Query4 = run_query("Query4.sql")

print(Query1)
print('\n',Query2)
print('\n',Query3)
print('\n',Query4)