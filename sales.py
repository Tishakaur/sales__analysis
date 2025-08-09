import pandas as pd
import matplotlib.pyplot as plt

# Function to read Excel and save chart as PDF
def chart_visualisation(excel_file, pdf_file):
    # Step 1: Read Excel data
    data = pd.read_excel(r"C:\Users\DELL\Downloads\sales (1).xlsx")
    
    # Step 2: Make bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(data['Item'], data['Sales'], color='Blue')
    plt.xlabel('Item')
    plt.ylabel('Sales')
    plt.title('Sales Report')
    
    # Step 3: Save as PDF
    plt.savefig(pdf_file)
    plt.close()

# Run the function
chart_visualisation("sales.xlsx", "sales_chart.pdf")
print("PDF created successfully!")
