import pandas as pd
def load_data(filename="examples/testcase0.def"):
    # filename = "examples/example_input.def"
    with open(filename) as file_in:
        driver_text = []
        pin_text = []
        new_pin = False
        is_fix_line = 0
        for line in file_in:
            if new_pin:
                if is_fix_line==2:
                    driver_text.append(line)
                    new_pin=False
                    is_fix_line=0
                else:
                    is_fix_line+=1

            if line.__contains__('DRIVERPIN_'):
                new_pin = True
                is_fix_line+=1
                driver_text.append(line)

            if line.__contains__('im_psyched_VDD_IN'):
                pin_text.append(line)


        drivers = pd.DataFrame(columns=['driver_id', 'input_output', 'x','y'])
        pins = pd.DataFrame(columns=['pin_id','x','y'])

        for i in range(0,len(driver_text),2):
            driver_text[i] = driver_text[i].split(' ')
            driver_text[i+1] = driver_text[i+1].split(' ')
            drivers.loc[len(drivers.index)]=[driver_text[i][1],driver_text[i][7],driver_text[i+1][5],driver_text[i+1][6]]

        for i in range(len(pin_text)):
            pin_text[i]=pin_text[i].split(' ')
            pins.loc[len(pins.index)] = [pin_text[i][0],pin_text[i][5],pin_text[i][6]]
        return drivers, pins