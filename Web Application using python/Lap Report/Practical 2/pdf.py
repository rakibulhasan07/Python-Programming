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


# -------------------------------
# Create CSV File
# -------------------------------
def save_students_to_csv(filename="students.csv"):

    header = [
        "Student_Id",
        "Name",
        "Roll",
        "Semester",
        "Shift",
        "Department",
        "Date of Birth",
        "Phone No."
    ]

    students = [
        ["101", "Rakib", "1201", "3rd", "Morning", "CST", "2004-01-15", "01711111111"],
        ["102", "Anika", "1202", "5th", "Morning", "CSE", "2003-05-22", "01812345678"],
        ["103", "Tanvir", "1203", "3rd", "Evening", "EEE", "2001-11-10", "01987654321"],
        ["104", "Nabila", "1204", "7th", "Morning", "BBA", "2002-08-14", "01555667788"],
        ["105", "Sajid", "1205", "1st", "Morning", "SWE", "2004-03-30", "01311223344"],
        ["106", "Mehnaz", "1206", "6th", "Evening", "English", "2002-12-05", "01711223344"]
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(students)

    print(f"{filename} created successfully.")


# -------------------------------
# Create PDF From CSV
# -------------------------------
def generate_pdf_from_csv(
    csv_filename="students.csv",
    pdf_filename="student_report.pdf"
):

    if not os.path.exists(csv_filename):
        print("CSV file not found!")
        return

    data = []

    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=landscape(A4)
    )

    styles = getSampleStyleSheet()

    title = Paragraph(
        "<b>Student Information Report</b>",
        ParagraphStyle(
            "Title",
            parent=styles["Heading1"],
            alignment=1,
            fontSize=20,
            textColor=colors.darkblue
        )
    )

    header_style = ParagraphStyle(
        "Header",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        textColor=colors.white,
        alignment=1
    )

    cell_style = ParagraphStyle(
        "Cell",
        parent=styles["Normal"],
        alignment=1,
        fontSize=9
    )

    formatted_data = []

    formatted_data.append(
        [Paragraph(col, header_style) for col in data[0]]
    )

    for row in data[1:]:
        formatted_data.append(
            [Paragraph(col, cell_style) for col in row]
        )

    table = Table(
        formatted_data,
        colWidths=[60,90,60,60,70,90,90,100],
        repeatRows=1
    )

    style = TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.darkblue),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),0.5,colors.black),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("BOTTOMPADDING",(0,0),(-1,0),8),
        ("TOPPADDING",(0,0),(-1,0),8),
    ])

    for i in range(1, len(formatted_data)):
        if i % 2 == 0:
            style.add(
                "BACKGROUND",
                (0, i),
                (-1, i),
                colors.whitesmoke
            )

    table.setStyle(style)

    doc.build([title, table])

    print(f"{pdf_filename} created successfully.")


# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":

    # Step 1: Create CSV
    save_students_to_csv()

    # Step 2: Create PDF
    generate_pdf_from_csv()