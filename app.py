import streamlit as st
from graph.workflow import graph

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Assistant")
st.write("Powered by LangGraph + LangChain + Groq + Tavily")

question = st.text_area(
    "Enter your research question",
    height=120
)

if st.button("Start Research"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Research in progress..."):

            state = {
                "question": question,
                "plan": "",
                "research": "",
                "news": "",
                "paper": "",
                "merged": "",
                "draft": "",
                "final": "",
                "need_research": False,
                "research_done": False,
                "news_done": False,
            }

            config = {
                "configurable": {
                    "thread_id": "streamlit-thread"
                }
            }

            result = graph.invoke(state, config={"configurable": {"thread_id": "streamlit"}})

            st.success("Research Completed")

            st.divider()

            st.subheader("📌 Planner Output")
            st.write(result.get("plan", "No plan generated."))

            st.divider()

            st.subheader("🔍 Web Research")
            st.write(result.get("research", "No research available."))

            st.divider()

            st.subheader("📰 Latest News")
            st.write(result.get("news", "No news available."))

            st.divider()

            st.subheader("📚 Research Papers")
            st.write(result.get("paper", "No research papers available."))

            st.divider()

            st.subheader("🔀 Merged Research")
            st.write(result.get("merged", "No merged research available."))

            st.divider()

            st.subheader("📝 Draft Report")
            st.write(result.get("draft", "No draft generated."))

            st.divider()

            st.subheader("✅ Final Report")
            st.write(result.get("final", "No final report generated."))