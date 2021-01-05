from django.db import models

# Create your models here.


class Patient(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class ClinicalData(models.Model):
    COMPONENT_NAMES = [('Toxin-based', 'Toxin-based'),
                       ('Genetic mutations', 'Genetic mutations'), ('Others', 'Others')]
    ANIMAL_MODELS = [('MPTP Mice', 'MPTP Mice'), ('MPTP Monkeys',
                                                  'MPTP Monkeys'), ('6-OHDA rat', '6-OHDA rat'),
                     ('Rotenone', 'Rotenone'), ('Paraquat',
                                                'Paraquat'), ('MET/MDMA', 'MET/MDMA'),
                     ('Synuclein', 'Synuclein'), ('LRKK2',
                                                  'LRKK2'), ('PINK1', 'PINK1'),
                     ('PARKIN', 'PARKIN'), ('DJ-1', 'DJ-1'), ('ATP13A2',
                                                              'ATP13A2'), ('SHH', 'SHH'), ('Nurr1', 'Nurr1'),
                     ('Engrailed1', 'Engrailed1'), ('Pitx3', 'Pitx3'), ('C-Rel-NFKB',
                                                                        'C-Rel-NFKB'), ('MitoPark', 'MitoPark'),
                     ('Atg7', 'Atg7'), ('VMAT2', 'VMAT2')]

    componentName = models.CharField(max_length=20, choices=COMPONENT_NAMES)
    animalModel = models.CharField(max_length=45, choices=ANIMAL_MODELS)
    motorbehavior = models.CharField(max_length=100)
    neuronLoss = models.CharField(max_length=30)
    striatalLoss = models.CharField(max_length=30)
    lewyBody = models.CharField(max_length=30)
    measureDateTime = models.DateTimeField(auto_now_add=True)
    model = models.ForeignKey(Patient, on_delete=models.CASCADE)
