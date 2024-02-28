from django.db import models

class Question(models.Model):
    """ 
    A class representing a choiced based question with attributes question_text, pub_date and candidate's biographies.
    """
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    candidate_biography_1 = models.CharField(max_length = 300, default = "Enter Bio")
    candidate_biography_2 = models.CharField(max_length = 300, default = "Enter Bio")
    candidate_biography_3 = models.CharField(max_length = 300, default = "Enter Bio")
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    """ 
    Initializing the question along with models.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.IntegerField(default=1)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    