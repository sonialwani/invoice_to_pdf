import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF





filepaths = glob.glob("*.xlsx")

for filepath in filepaths:
        pdf = FPDF()
        pdf.add_page()
        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        file_name = Path(filepath).stem
        invoice_number = file_name.split("-")[0]
        date = file_name.split("-")[1]
        invoice_logo = f"Invoice No. : {invoice_number}"
        date_logo = f"Date : {date}"
        pdf.set_font(family="Times", style="B", size=10)
        pdf.cell(w=30, h=8, txt=str(invoice_logo), ln=1)
        pdf.cell(w=30, h=8, txt=date_logo, ln=1)
        for column in df.columns.values:
            pdf.set_font(family="Times", style="B", size=10)
            pdf.cell(w=40, h=8, txt=str(column), border=1)
        pdf.cell(w=40, h=8, ln=1)
        for index, row in df.iterrows():

            for value in  row:
                pdf.set_font(family="Times", style="", size=10)

                pdf.cell(w=40, h=8, txt=str(value),border=1)

            pdf.cell(w=40, h=8, ln=1)
        for column in df.columns.values:
            pdf.set_font(family="Times", style="B", size=10)
            if column == "total_price":
                 pdf.cell(w=40, h=8, txt=str(df["total_price"].sum()), border=1)
            else:
                 pdf.cell(w=40, h=8, txt="", border=1)
        pdf.cell(w=100, h=20, ln=1)
        pdf.set_font(family="Times", style="B", size=10)
        pdf.cell(w=40, h=8, txt="Total Amount due is :"+str(df["total_price"].sum()))
        pdf.output(f"{file_name}.pdf")



