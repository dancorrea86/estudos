import sys

class SimplesTaxCalculator():
    def __init__(self, revenues_twelve_months, attachment, revenue_month):
        self.ANEXOI = {     'faixa1': [0.040, 0	    ],
                            'faixa2': [0.073, 5940  ],
                            'faixa3': [0.095, 13860 ],
                            'faixa4': [0.107, 22500 ],
                            'faixa5': [0.143, 87300 ],
                            'faixa6': [0.190, 378000]}           

        self.ANEXOII = {    'faixa1': [0.045, 0     ],
                            'faixa2': [0.078, 5940  ],
                            'faixa3': [0.100, 13860 ],
                            'faixa4': [0.112, 22500 ],
                            'faixa5': [0.147, 85500 ],
                            'faixa6': [0.300, 720000]}  

        self.ANEXOIII = {   'faixa1': [0.060, 0     ],
                            'faixa2': [0.112, 9360  ],
                            'faixa3': [0.135, 17640 ],
                            'faixa4': [0.160, 35640 ],
                            'faixa5': [0.210, 125640],
                            'faixa6': [0.330, 648000]}

        self.ANEXOIV = {    'faixa1': [0.045, 0     ],
                            'faixa2': [0.090, 8100	],
                            'faixa3': [0.102, 12420 ],
                            'faixa4': [0.140, 39780 ],
                            'faixa5': [0.220, 183780],
                            'faixa6': [0.330, 828000]} 

        self.ANEXOV =   {   'faixa1': [0.155, 0     ],
                            'faixa2': [0.180, 4500  ],
                            'faixa3': [0.195, 9900  ],
                            'faixa4': [0.205, 17100 ],
                            'faixa5': [0.230, 62100 ],
                            'faixa6': [0.305, 540000]}

        self.revenues_twelve_months = float(revenues_twelve_months)
        self.revenue_month = float(revenue_month)
        self.attachment = getattr(self, attachment)
        self.tax_range = self.get_tax_range_simple()
        print(self.tax_range)
        print(type(self.tax_range))
        print(self.attachment)
        print(type(self.attachment))
        self.rate = float(self.attachment['faixa' + self.tax_range][0])
        self.deduction = float(self.attachment['faixa' + self.tax_range][1])
        self.effective_rate = float(self.get_effective_rate())

    def get_tax_range_simple(self):
        if (self.revenues_twelve_months <= 180000):
            tax_range_simple = '1'
        elif (self.revenues_twelve_months <= 360000):
            tax_range_simple = '2'
        elif (self.revenues_twelve_months <= 720000):
            tax_range_simple = '3'
        elif (self.revenues_twelve_months <= 1800000):
            tax_range_simple = '4'
        elif (self.revenues_twelve_months <= 3600000):
            tax_range_simple = '5'
        elif (self.revenues_twelve_months <= 4800000):
            tax_range_simple = '6'
        else:
            sys.exit('Excluída')
        return tax_range_simple

    def get_effective_rate(self):
        effective_rate = ( ( self.revenues_twelve_months * self.rate ) - self.deduction ) / self.revenues_twelve_months
        # effective_rate = format(effective_rate, '.2f')
        return effective_rate

    def calculate_tax(self):
        tax_without_retention = self.revenue_month * self.effective_rate
        total_tax = tax_without_retention

        return total_tax

    def return_results(self):
        effective_rate = self.format_numbers(self.get_effective_rate() * 100)
        tax = self.format_numbers(self.calculate_tax())
        return effective_rate, tax

    def format_numbers(self, number):
        number = format(number, '.2f').replace('.',',')
        return number


faturamento_12meses = 180000
anexo = "ANEXOV"
folha_pagamento_12meses = 50400
faturamento_mes = 20000
faturamento_mes_retenção = 10000

app = SimplesTaxCalculator(faturamento_12meses, anexo, faturamento_mes)
print (app.return_results())

