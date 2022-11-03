# HW : could use system sleep#

#Input

custumer_name = input("You name: ")
custumer_address = input("You address: ")

# indicatori per month

calcule_energy_index_0 = int(input("before  (kWh): "))
calcule_energy_index_1 = int(input("Month 1  (kWh): "))
calcule_energy_index_2 = int(input("Month 2  (kWh): "))
calcule_energy_index_3 = int(input("Month 3  (kWh): "))

#ctrl + shift + d
#Atom Keymap - pentru a scrie rapid codu extensie vs

# Operations

electric_price_company = 5 #lei

consum_energy_month_1kWh = calcule_energy_index_1 - calcule_energy_index_0
consum_energy_month_2kWh = calcule_energy_index_2 - calcule_energy_index_1
consum_energy_month_3kWh = calcule_energy_index_3 - calcule_energy_index_2

# consum energy bill

consum_energy_bill_month1 = consum_energy_month_1kWh * electric_price_company
consum_energy_bill_month2 = consum_energy_month_2kWh * electric_price_company
consum_energy_bill_month3 = consum_energy_month_3kWh * electric_price_company

#consum total kWh

consum_energy_total_kWh = consum_energy_month_1kWh + consum_energy_month_2kWh + consum_energy_month_3kWh

consum_energy_total_bill = consum_energy_bill_month1 + consum_energy_bill_month2 + consum_energy_bill_month3

# grafica energy
koeficient_month1 = int(100 * consum_energy_month_1kWh / consum_energy_total_kWh)
koeficient_month2 = int(100 * consum_energy_month_2kWh / consum_energy_total_kWh)
koeficient_month3 = int(100 * consum_energy_month_3kWh / consum_energy_total_kWh)

#Output
print("Consumption:")
print("Month 1: ", consum_energy_month_1kWh,"kWh = ", consum_energy_bill_month1)
print("Month 2: ", consum_energy_month_2kWh,"kWh = ", consum_energy_bill_month2)
print("Month 3: ", consum_energy_month_3kWh,"kWh = ", consum_energy_bill_month3)
print("-" * 30)
print("Total:", consum_energy_total_kWh,"kWh =", consum_energy_total_bill)

#grafice
print("User graf")
print("first month in %", koeficient_month1,
      "second month in %", koeficient_month2, 
      "third month in %", koeficient_month3)
print("first month")
print("#" * koeficient_month1)
print("second month")
print("#" * koeficient_month2)
print("third month")
print("#" * koeficient_month3)
