import csv
from fpdf import FPDF

# Function to read data from a CSV file
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skipping the header
        for row in reader:
            data.append(row)
    return data

# Function to perform basic analysis on the data
def analyze_data(data):
    total = 0
    count = len(data)
    for row in data:
        total += float(row[1])  # Assuming the second column has numeric data
    average = total / count if count > 0 else 0
    return total, average

# Function to generate a PDF report
def generate_pdf(data, total, average, output_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title of the report
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Automated Report", ln=True, align='C')
    
    # Summary of analysis
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, f"Total: {total}", ln=True)
    pdf.cell(200, 10, f"Average: {average}", ln=True)

    # Data table
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "ID", border=1)
    pdf.cell(100, 10, "Description", border=1)
    pdf.cell(40, 10, "Value", border=1)
    pdf.ln(10)

    pdf.set_font("Arial", '', 12)
    for row in data:
        pdf.cell(40, 10, row[0], border=1)
        pdf.cell(100, 10, row[2], border=1)  # Assuming the description is in column 3
        pdf.cell(40, 10, row[1], border=1)  # Assuming value is in column 2
        pdf.ln(10)

    pdf.output(output_file)

# Main function to tie everything together
def main():
    file_path = 'sample_data.csv'  # Path to your data file
    output_file = 'report.pdf'  # Output PDF file name
    
    # Read and analyze data
    data = read_data(file_path)
    total, average = analyze_data(data)
    
    # Generate the PDF report
    generate_pdf(data, total, average, output_file)
    print(f"Report generated successfully: {output_file}")

if __name__ == "__main__":
    main()
