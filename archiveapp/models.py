from django.db import models

SEMESTER_CHOICES =[
    ('S1', 'Semester1'),
    ('S2', 'Semester2'),
    ('S3', 'Semester3'),
    ('S4', 'Semester4'),
    ('S5', 'Semester5'),
    ('S6', 'Semester6'),
]
FILIERE_CHOICES =[
    ('FC', 'Finance & Comptabilité (FC)'),
    ('GRH', 'Gestion des Ressources Humaines (GRH)'),
    ('BA', 'Banques & Assurances (BA)'),
    ('TCM', 'Techniques Commerciales et Marketing (TCM)'),
    ('SAE', 'Statistique Appliquée á Economie (SAE)'),
    ('DI', 'Développement Informatique (DI)'),
    ('IG', 'Informatique de Gestion (IG)'),
    ('RT', 'Réseaux informatiques et Télécommunications (RT)'),
    
    
    
]
class Archive(models.Model):
    filiere = models.CharField(max_length=20 ,choices = FILIERE_CHOICES, default='FC')
    semester = models.CharField(max_length=20 ,choices = SEMESTER_CHOICES, default='S1')
    file_name = models.CharField(max_length=255)
    files = models.FileField(upload_to='files/', null=True, blank=True)
    
    def __str__(self):
         return self.file_name
