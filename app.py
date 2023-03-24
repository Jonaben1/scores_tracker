import streamlit as st
from fixtures import df, teams
import pandas as pd
from table import table
from stats import goals, assists, all_time_goals, all_time_assists

def main():
    st.sidebar.header('English Premier League')
    st.sidebar.info('Welcome to the English Premier League. Choose the options below')
    option = st.sidebar.selectbox('Choose your option', ['Scores', 'Table', 'Stats'])
    if option == 'Scores':
        get_scores()
    elif option == 'Table':
        get_table()
    else:
        get_stats()





def get_scores():
    st.header('English Premier League LiveScores')
    st.info('Check the latest fixtures')
    op = st.radio('Which fixtures do you want to check?', ['All', 'Team'])
    if op == 'All':
        st.dataframe(df)
    else:
        team = st.selectbox('Select a team', teams)
        team_select = df[(df.Home == team) | (df.Away == team)]
        st.dataframe(team_select)


def get_table():
    st.header('English Premier League Table - 2022/2023')
    st.info('Check current standings')
    st.dataframe(table)


def get_stats():
    st.header('English Premier League Stats')
    op = st.selectbox('Choose an option', ['Goals', 'Assists'])
    if op == 'Goals':
        s = st.radio('Choose an option', ['Current', 'All Time'])
        if s == 'Current':
            st.dataframe(goals)
        else:
            st.dataframe(all_time_goals)
    else:
        opt = st.radio('Choose an option', ['Current', 'All Time'])
        if opt == 'Current':
            st.dataframe(assists)
        else:
            st.dataframe(all_time_assists)



if __name__ == '__main__':
    main()
