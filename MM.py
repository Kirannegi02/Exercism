def is_criticality_balanced(temperature, neutrons_emitted):
    return (temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000)
    



def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power)*100
    return ('green' if 80 <= efficiency else 'orange' if 60 <= efficiency else 'red' if 30 <= efficiency else 'black')




def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second
    return('LOW' if product < (threshold * .9) else 'NORMAL' if product <= threshold * 1.1 else 'DANGER')