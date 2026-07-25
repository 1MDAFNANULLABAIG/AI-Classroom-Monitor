import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="AI Classroom Dashboard",
    layout="wide"
)

st.title("🎓 AI Classroom Monitoring Dashboard")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("classroom.db")

# -----------------------------
# Load Data
# -----------------------------
try:
    students = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )

    attendance = pd.read_sql_query(
        "SELECT * FROM attendance",
        conn
    )

except Exception as e:
    st.error(e)
    st.stop()

# -----------------------------
# Dashboard Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Students",
        len(students)
    )

with col2:
    st.metric(
        "Attendance Records",
        len(attendance)
    )

with col3:

    if "status" in attendance.columns:
        present = len(
            attendance[
                attendance["status"] == "Present"
            ]
        )
    else:
        present = len(attendance)

    st.metric(
        "Present Students",
        present
    )

st.divider()

# -----------------------------
# Student Table
# -----------------------------
st.subheader("Registered Students")

if len(students):

    st.dataframe(
        students,
        use_container_width=True
    )

else:
    st.warning("No students registered.")

st.divider()

# -----------------------------
# Attendance Table
# -----------------------------
st.subheader("Attendance Records")

if len(attendance):

    st.dataframe(
        attendance,
        use_container_width=True
    )

else:
    st.warning("No attendance found.")

st.divider()

# -----------------------------
# Charts
# -----------------------------
if len(attendance):

    left, right = st.columns(2)

    with left:

        st.subheader("Attendance Status")

        if "status" in attendance.columns:

            st.bar_chart(
                attendance["status"].value_counts()
            )

    with right:

        st.subheader("Student Attendance")

        if "student_name" in attendance.columns:

            st.bar_chart(
                attendance.groupby("student_name").size()
            )

st.divider()

# -----------------------------
# Refresh
# -----------------------------
if st.button("🔄 Refresh Dashboard"):
    st.rerun()

conn.close()