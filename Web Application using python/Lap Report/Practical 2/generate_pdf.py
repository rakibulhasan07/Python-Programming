
import csv
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


# ৩. ফাংশন তৈরি করা
def save_students_to_csv(filename="/content/drive/MyDrive/CST 3rd/practical_2/students.csv"):
    header = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone No."]
    students = [
        ["102", "Anika", "1202", "5th", "Morning", "CSE", "2003-05-22", "01812345678"],
        ["103", "Tanvir", "1203", "3rd", "Evening", "EEE", "2001-11-10", "01987654321"],
        ["104", "Nabila", "1204", "7th", "Morning", "BBA", "2002-08-14", "01555667788"],
        ["105", "Sajid", "1205", "1st", "Morning", "SWE", "2004-03-30", "01311223344"],
        ["106", "Mehnaz", "1206", "6th", "Evening", "English", "2002-12-05", "01711223344"]
    ]

    # ড্রাইভের নির্দিষ্ট ফোল্ডারটি যদি তৈরি করা না থাকে, তবে তা তৈরি করে নেবে
    folder_path = os.path.dirname(filename)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # ফাইল রাইট করা
    with open(filename, mode='w', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(students)

    print(f"CSV file '{filename}' Created Successfully.")


def generate_pdf_from_csv(
    csv_filename="students.csv",
    pdf_filename="student_report.pdf"
):
    # CSV ফাইল আছে কিনা চেক করা
    if not os.path.exists(csv_filename):
        print(f"Error: '{csv_filename}' file not found.")
        return

    # CSV থেকে ডেটা পড়া
    data = []
    with open(csv_filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    if not data:
        print("CSV file is empty.")
        return

    # PDF Document তৈরি
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=landscape(A4),
        leftMargin=30,
        rightMargin=30,
        topMargin=30,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontSize=20,
        leading=24,
        alignment=1,
        textColor=colors.darkblue,
        spaceAfter=20,
    )

    title = Paragraph("Student Information Report", title_style)

    header_style = ParagraphStyle(
        "HeaderStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=colors.white,
    )

    cell_style = ParagraphStyle(
        "CellStyle",
        parent=styles["Normal"],
        fontSize=9,
    )

    formatted_data = []

    # Header
    formatted_data.append(
        [Paragraph(cell, header_style) for cell in data[0]]
    )

    # Student Data
    for row in data[1:]:
        formatted_data.append(
            [Paragraph(cell, cell_style) for cell in row]
        )

    # Table
    table = Table(
        formatted_data,
        colWidths=[60, 90, 60, 60, 70, 90, 90, 100],
        repeatRows=1,
    )

    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.red),
        ("ALIGN", (0, 0), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
    ])

    # Alternate Row Color
    for i in range(1, len(formatted_data)):
        if i % 2 == 0:
            style.add(
                "BACKGROUND",
                (0, i),
                (-1, i),
                colors.whitesmoke,
            )

    table.setStyle(style)

    elements = [title, table]

    # PDF তৈরি
    doc.build(elements)

    print(f"PDF Report Created Successfully: {pdf_filename}")


if __name__ == "__main__":
    save_students_to_csv()
    generate_pdf_from_csv()
    