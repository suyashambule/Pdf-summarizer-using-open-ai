import streamlit as st


def main():
    st.set_page_config(page_title='PDF summarizer')
    st.title("PDF summarizer")
    st.write('Summarize your pdf in few seconds')
    st.divider()


    pdf=st.file_uploader('Upload your PDF document',type='pdf')
    submit=st.button("generate summary")


if __name__=='__main__':
    main()
