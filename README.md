# Customer-feedback-to-jira
Automate Play Store review analysis with LLMs and create detailed Jira tickets! 🎯 Extract insights like sentiment, bugs, and feature requests, then generate structured issues in Jira with labels, priorities, and assignees. Streamline product feedback management effortlessly! 🚀
---

![Smaple_output](https://github.com/mohammed97ashraf/Customer-feedback-to-jira/blob/main/images/Screenshot2.png)
---

## Features  
- 📥 **Play Store Review Extraction**: Fetch reviews directly from the Play Store web page.  
- 🤖 **LLM-Powered Analysis**: Use OpenAI’s LLM to identify negative feedback and generate concise summaries.  
- 📝 **Automated Jira Ticket Creation**: Generate Jira issues with titles, descriptions, priorities, and labels.  
- 🔄 **End-to-End Workflow**: Seamlessly integrate with Jira to keep track of issues in real time.

---

## Installation  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/customer-feedback-to-jira.git
   cd customer-feedback-to-jira
   ```
2. Set up the environment
  ```bash
    python -m venv env  
    source env/bin/activate  # For Linux/macOS  
    env\Scripts\activate  # For Windows  
    pip install -r requirements.txt
  ```
3. Set up environment variables 
## Run
  ```python
     streamlit run app.py
  ```

## Contact  
For support, feature requests, or inquiries, reach out via:  

- **Email**: [Mohammed97ashraf@gmail.com](mohammed97ashraf@gmail.com) 
- **GitHub**: [GitHub Profile](https://github.com/mohammed97ashraf)  
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/mohammed97ashraf)  

---

## References  
-  [OpenAI Python API Documentation](https://beta.openai.com/docs)  
-  [Jira REST API v3 Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)  
-  [Create an API Token in Atlassian](https://docs.searchunify.com/Content/Content-Sources/Atlassian-Jira-Confluence-Authentication-Create-API-Token.htm)
-  [streamlit](https://streamlit.io/)
-  [Python-langchain](https://python.langchain.com/docs/introduction/)

