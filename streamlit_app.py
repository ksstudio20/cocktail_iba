#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

import streamlit as st

from cocktail_app_zh import COCKTAILS


st.set_page_config(page_title="鸡尾酒酒谱库", page_icon="🍸", layout="wide")
st.title("鸡尾酒酒谱库")
st.caption(f"共 {len(COCKTAILS)} 条酒谱（离线内嵌数据）")


def show_detail(cocktail: dict) -> None:
    st.subheader(cocktail["name"])
    st.write(f"**基酒：**{cocktail['base']}  |  **分类：**{cocktail['taste']}")
    st.markdown("**配料**")
    for x in cocktail["ingredients"]:
        st.write(f"- {x}")
    st.markdown("**步骤**")
    for i, step in enumerate(cocktail["steps"], start=1):
        st.write(f"{i}. {step}")


col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    base_options = ["全部"] + sorted({c["base"] for c in COCKTAILS})
    base = st.selectbox("按基酒筛选", base_options, index=0)

with col2:
    taste_options = ["全部"] + sorted({c["taste"] for c in COCKTAILS})
    taste = st.selectbox("按分类筛选", taste_options, index=0)

with col3:
    random_clicked = st.button("随机推荐", use_container_width=True)


filtered = COCKTAILS
if base != "全部":
    filtered = [c for c in filtered if c["base"] == base]
if taste != "全部":
    filtered = [c for c in filtered if c["taste"] == taste]

st.divider()
st.write(f"筛选结果：{len(filtered)} 条")

if random_clicked and filtered:
    st.session_state["random_pick"] = random.choice(filtered)

if "random_pick" in st.session_state and st.session_state["random_pick"] in filtered:
    st.info("随机推荐")
    show_detail(st.session_state["random_pick"])
    st.divider()

names = [c["name"] for c in filtered]
selected_name = st.selectbox("选择鸡尾酒查看详情", ["请选择"] + names)
if selected_name != "请选择":
    target = next(c for c in filtered if c["name"] == selected_name)
    show_detail(target)

if not filtered:
    st.warning("没有匹配结果，请调整筛选条件。")
