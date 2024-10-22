import streamlit as st
from langchain_helper import get_page_content, get_negative_comments, tagging_chain_web_parse, get_jira_tickets
from jira_helper import create_ticket

st.set_page_config(
    page_title="Create Jira Ticket",
    page_icon="🤖"
)



url = st.text_input("Enter the PlayStore url:", "")

if st.button("Start 🪄🪄"):
    with st.spinner("Getting Information"):
        page_text = get_page_content(url)
        st.toast("Link extraction done....!!!!")
        page_comments = tagging_chain_web_parse(page_text)
        st.toast("Bug details created .... !!!")
        nagetive_commets = get_negative_comments(page_comments)
        st.toast("Negative comments created .... !!!")
        jira_ticket_details = get_jira_tickets(nagetive_commets)
        #st.json(jira_ticket_details)
    with st.spinner("Creating The Ticket For You"):
        new_ticket_info = []
        for i in jira_ticket_details['tickets']:
            status , details = create_ticket(i['title'],i['description'])
            if status:
                new_ticket_info.append({"jira_id":details['id'],
                                        "jira_bug_key":details['key'],
                                        "jira_ticket_titel":i['title'],
                                        "jira_tiket_link":details['self']})
            st.toast(f"Ticket Created for {i['title']} ")
        st.success("All Tickets Are Created On Your Space Thank You....!!!")
        st.table(new_ticket_info)
        