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
    
    exam_id = fields[0]
    if len(fields) != 5:
        raise TextFormatException()

    exam_id, date, patient_name, weight, height = fields

    exam_id = int(exam_id)

    if weight.strip() == "" or height.strip() == "":
        raise MissingValueException()

    weight = float(weight)
    height = float(height)

    if height <= 0 or height > 3:
        raise MeasurementUnitException()

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
        except TextFormatException:
            print(f"{exam_id}: row does not have 5 fields")
        except MissingValueException:
            print(f"{exam_id}: weight or height missing")
        except MeasurementUnitException:
            print(f"{exam_id}: incorrect measurement for height") 

    output_f.close()
    input_f.close()
    
main()