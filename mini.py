from datetime import datetime
from reportlab.pdfgen import canvas
import os

import mysql.connector as conn

con = conn.Connect(host="localhost", user="root", password="Sparsh@08", database="mehta")
cur = con.cursor()


def checklist():
    #  check and create a list for mini statement
    a = 'select ID, DETAILS, AMOUNT, TOTAL from credit;'
    cur.execute(a)
    m = cur.fetchall()
    for i in range(0, len(m)):
        id = m[i][0]
        details = m[i][1]
        amount = m[i][2]
        Total = m[i][3]

        print("ID - {0}".format(id))
        print("DETAILS - {0}".format(details))
        print("AMOUNT - {0}".format(amount))
        print("TOTAL - {0}".format(Total))
        print("\n")

#
# def main():
#     dir_path = r'E:\ministatement'
#     count = 0
#     # Iterate directory
#     for path in os.listdir(dir_path):
#         # check if current path is a file
#         if os.path.isfile(os.path.join(dir_path, path)):
#             count += 1
#     print('Invoice Number:', count + 1)
#
#     local = datetime.now()
#     t = local.strftime("%d-%m-%Y %H-%M-%S")
#
#     file_path = "E:/ministatement/" + t + " CreditMehta.pdf"
#     print(file_path)
#     company_name = '455 R KHANNAS'
#     company_address = 'Model Town.'
#     company_city = 'JALANDHAR'
#     message = 'Thanks for shopping with us today!'
#
#     # Create a PDF document
#     pdf = canvas.Canvas(file_path)
#     #
#     # Set the title of the PDF
#     pdf.setTitle(file_path)
#     #
#     # Add text to the PDF
#     pdf.drawString(100, 750, '*' * 75)
#     #
#     pdf.drawString(240, 730, '{}'.format(company_name.title()))
#     pdf.drawString(240, 720, '{}'.format(company_address.title()))
#     pdf.drawString(240, 710, '{}'.format(company_city.title()))
#
#     pdf.drawString(100, 685, '*' * 75)
#
#     pdf.drawString(100, 670, "Date : {}".format(t))
#     pdf.drawString(370, 670, "Invoice : {}".format(count + 1))
#     pdf.drawString(100, 655, "Location : {}".format("MEHTA"))
#
#     pdf.drawString(100, 635, '*' * 75)
#
#     pdf.drawString(100, 625, "PRODUCT DETAILS")
#     pdf.drawString(320, 625, "QUANTITY")
#     pdf.drawString(400, 625, "AMOUNT")
#
#     pdf.drawString(100, 610, '*' * 75)
#
#     # pdf.drawString(100, 590, '{}'.format(name))
#     # pdf.drawString(250, 590, '{}'.format(title))
#     # pdf.drawString(330, 590, 'Rs.{}'.format(price))
#     # pdf.drawString(100, 580, '({})'.format(card))
#     #
#     # pdf.drawString(100, 560, '*' * 60)
#     #
#     # if product1_name == "DEPOSIT":
#     #     pdf.drawString(100, 530, "Amount Deposited : ")
#     #     pdf.drawString(100, 540, "Previous Balance : ")
#     #     pdf.drawString(100, 520, "Total Balance : ")
#     #
#     #     pdf.drawString(310, 540, "      Rs.{}".format(pb))
#     #     pdf.drawString(320, 530, "+ Rs.{}".format(cash))
#     #     pdf.drawString(310, 520, "   = Rs.{}".format(tam))
#     #
#     # else:
#     #     pdf.drawString(100, 540, "Previous Balance : ")
#     #     pdf.drawString(100, 530, "Amount Debited : ")
#     #     pdf.drawString(100, 520, "Total Balance : ")
#     #
#     #     pdf.drawString(310, 540, "      Rs.{}".format(pb))
#     #     pdf.drawString(320, 530, " - Rs.{}".format(cash))
#     #     pdf.drawString(310, 520, "   = Rs.{}".format(tam))
#     #
#     pdf.drawString(100, 490, '*' * 75)
#     pdf.drawString(150, 470, "{}".format(message))
#     pdf.drawString(100, 450, '*' * 75)
#     #
#     # Save the PDF
#     pdf.save()
#     # print(f"INVOICE : {file_path}")
#     # openpdf.main(file_path)
#     # return file_path


if __name__ == '__main__':
    checklist()
