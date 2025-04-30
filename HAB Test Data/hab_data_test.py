#Plots Voltage and Temperature data from test log file


import re
import matplotlib.pyplot as plt

# Replace with the path to your file
filename = "Overnight_Test.txt"


#Change temp_sensor and module to plot temperatures from different sensors
# and voltage from different modules

temp_sensor = 0     #available temp sensors (0, 1, 3, 4, 6)
module = 1          #available modules (1, 2)

solar_cell_voltages = []
temps = []

with open(filename, 'r') as file:
    for line in file:
        # Extract the first temperature reading
        temp_list_match = re.search(r"Temperature Readings: \[([^\]]+)\]", line)
        # Extract Solar Cell 1 voltage
        volt_match = re.search(r"Solar Cell " + str(module) + ": \[Voltage: ([\d.]+)V", line)

        if temp_list_match and volt_match:
            # Split temperatures and take the second one (index 1)
            temp_values = [float(x.replace('v','')) for x in temp_list_match.group(1).split(',') if 'v' not in x]
            if len(temp_values) > 1:
                temperature = temp_values[temp_sensor]
            else:
                continue
            voltage = float(volt_match.group(1))

            temps.append(temperature)
            solar_cell_voltages.append(voltage)

# Plotting

fig, ax = plt.subplots(2)

plt.figure(figsize=(20, 10))


ax[0].plot(temps, color='blue')
ax[0].set(xlabel='Sample', ylabel='Temperature (C)')

ax[1].plot(solar_cell_voltages, color='green')
ax[1].set(xlabel='Sample', ylabel='Voltage (V)')

#plt.title("Solar Cell 1 Voltage Readings")
#plt.xlabel("Temperature")
#plt.ylabel("Voltage (V)")
#plt.grid(True)
#plt.tight_layout()
