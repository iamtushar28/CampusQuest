from django.db import models


#Question paper model
class QuestionPaper(models.Model):
    paper_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='question_papers/')

    def __str__(self):
        return self.paper_name
