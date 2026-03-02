#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

import streamlit as st

from cocktail_app import COCKTAILS


st.set_page_config(page_title="Cocktail Recipe Explorer", page_icon="🍸", layout="wide")
st.title("Cocktail Recipe Explorer")
st.caption(f"{len(COCKTAILS)} recipes loaded (offline embedded data)")


def show_detail(cocktail: dict) -> None:
    st.subheader(cocktail["name"])
    st.write(f"**Base spirit:** {cocktail['base']}  |  **Category:** {cocktail['taste']}")
    st.markdown("**Ingredients**")
    for item in cocktail["ingredients"]:
        st.write(f"- {item}")
    st.markdown("**Steps**")
    for idx, step in enumerate(cocktail["steps"], start=1):
        st.write(f"{idx}. {step}")


col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    base_options = ["All"] + sorted({c["base"] for c in COCKTAILS})
    base = st.selectbox("Filter by base spirit", base_options, index=0)

with col2:
    taste_options = ["All"] + sorted({c["taste"] for c in COCKTAILS})
    taste = st.selectbox("Filter by category", taste_options, index=0)

with col3:
    random_clicked = st.button("Random Pick", use_container_width=True)


filtered = COCKTAILS
if base != "All":
    filtered = [c for c in filtered if c["base"] == base]
if taste != "All":
    filtered = [c for c in filtered if c["taste"] == taste]

st.divider()
st.write(f"Results: {len(filtered)}")

if random_clicked and filtered:
    st.session_state["random_pick_en"] = random.choice(filtered)

if "random_pick_en" in st.session_state and st.session_state["random_pick_en"] in filtered:
    st.info("Random recommendation")
    show_detail(st.session_state["random_pick_en"])
    st.divider()

names = [c["name"] for c in filtered]
selected_name = st.selectbox("Select a cocktail", ["Select one"] + names)
if selected_name != "Select one":
    target = next(c for c in filtered if c["name"] == selected_name)
    show_detail(target)

if not filtered:
    st.warning("No matches found. Try different filters.")
