# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(height: float, weight: float) -> float:
    """
    compute body-mass-index:  weight / (mass**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2
    """
    return weight / (height ** 2)


def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    # remove any spaces
    row = row.strip()
    # separate into list
    fields = row.split(",")
    
    try: 
        exam_id = int(fields[0])
        date = fields[1]
        patient_name = fields[2]
        weight = float(fields[3])
        height = float(fields[4])
    except:
        print("error")

    return [exam_id, date, patient_name, weight, height]

    
def main():
    input_f = open("data.csv")
    output_f = open("output.csv", "w")

    output_f.write("Exam ID, BMI\n")

    # skip header
    input_f.readline()
    # check each row and write to file
    for row in input_f:
        try:
            exam_id, date, name, weight, height = parse_row(row)
            bmi = compute_BMI(height, weight)    
            output_f.write(f"{exam_id}, {round(bmi, 2)}\n")
        except:
            print("main() error")

    output_f.close()
    input_f.close()
    
main()