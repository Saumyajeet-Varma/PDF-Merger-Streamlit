import streamlit as st
from PyPDF2 import PdfMerger
from streamlit_sortables import sort_items
from io import BytesIO

st.set_page_config(page_title="PDF Merger", page_icon="📄", layout="centered")

st.title("PDF Merger Tool")
st.write("Upload multiple PDFs, arrange items in order (drag and drop), and merge into a single file")

uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:

    st.subheader("Uploaded PDFs")

    items = [file.name for file in uploaded_files]

    st.write("Drag and drop to reorder")

    sorted_items = sort_items(items, direction="vertical")
    sorted_files = [next(f for f in uploaded_files if f.name == name) for name in sorted_items]

    st.write("Current order")

    for i, f in enumerate(sorted_files, 1):
        st.write(f"{i}. {f.name}")

    if st.button("Merge PDFs"):
        try:
            merger = PdfMerger()

            for file in sorted_files:
                merger.append(file)
            
            merged_pdf = BytesIO()
            merger.write(merged_pdf)
            merger.close()
            merged_pdf.seek(0)

            st.success("✅ PDFs merged successfully :)")

            st.download_button("Download Merged PDF", merged_pdf, file_name="merged.pdf", mime="application/pdf")

        except Exception as e:
            st.error(f"❌ Error while merging: {e}")