from django.db import models
# python code -> sql command -------- ORM (Object-Realtional Mapping)
# ar vwer sql querebs da vwer pythonur kodebs shemdeg es orm gardaqmnis am pitonur kods sql querebad 


# Productebis cxrili -> name, price, in_stock

class Product(models.Model): # create table ....
    name = models.CharField(max_length=100)  # varchar(100)
    price = models.DecimalField(max_digits=6, decimal_places=2) #Decimal(6, 2)
    in_stock = models.BooleanField(default=True) # BOOLEAN
    description = models.TextField() 

    def __str__(self):
        return self.name
    
    


