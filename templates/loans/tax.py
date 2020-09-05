import requests as req 
​
url = "{"POST":{"scheme":"https","host":"www.kra.go.ke","filename":"/en/individual/calculate-tax/calculating-tax/paye","remote":{"Address":"196.61.52.39:443"}}}"
payload = "option=com_ajax&module=paye_calculator&method=calculatePayee&year=3&period=month&grosssalary=2000000&insurancerelief=&nssf=5000&contributionbenefit=&disability=2&mortgageinterest=&hosp=&format=json"
​
def paye_kra_request():
	income=float(input('Enter Gross Pay: '))
    if income <=5999:
    	nhif=150
    	ouput=income-150
    pass
​
def nhif_calculator():
	income=float(input('Enter Gross Pay: '))
    if income <=5999:
    	nhif=150
    	ouput=income-150
    	print(ouput)
​
def nssf_calculator():
    pass
​
def main():
    pass
​
if __name__ == "__main__":
    main()