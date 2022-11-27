from django.db import models


class Category(models.Model):
    name = models.CharField('категория' ,max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField('Услуги', max_length=200)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    saluns = models.ManyToManyField("Salun")

    def __str__(self):
        return self.title


class Salun(models.Model):
    name = models.CharField(max_length=21)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


'''4 tables'''


class Auto(models.Model):
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    engine = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    warehouse = models.ManyToManyField('Warehouse', related_name='autos')


    def __str__(self):
        return self.model
    # class Meta:
    #     verbose_name = 'Ландровер'
    #     verbose_name_plural = 'Ландровер'
            ############
########def __init__????#############
            ############


class Warehouse(models.Model):
    CHOISE_TYPE_WAREHOUSE = [
        ("Official_dealer", "Official_dealer"),
        ("Market_auto_used", "Market_auto_used"),
        ("Перекуп", "Перекуп"),
    ]
    locate = models.CharField(max_length=250)
    type_warehouse = models.CharField(max_length=250, choices=CHOISE_TYPE_WAREHOUSE)
    # buyers = models.ForeignKey("Buyer", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.locate


class Buyer(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    warehouse = models.ForeignKey("Warehouse", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    CHOISE_STATUS = [
        ("New", "New"),
        ("Used", "Used"),
        ("Include powerfull turbocharge", "Include powerfull turbocharge"),
    ]
    status = models.CharField(max_length=250, verbose_name= "статус",choices=CHOISE_STATUS)
    auto = models.ForeignKey("auto", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.status


'''air'''


class Airboard(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.brand


class Airport(models.Model):
    name = models.CharField(max_length=255)
    airboard = models.ManyToManyField("Airboard")

    def __str__(self):
        return self.name


'''person/house'''


class Person(models.Model):
    name = models.CharField(max_length=250)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.ForeignKey('House', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class House(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address


'''new'''


class Super(models.Model):
    brand = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.brand