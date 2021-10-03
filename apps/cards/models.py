from django.db import models

from apps.decks.models import Deck

class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class QuestionTypes(models.IntegerChoices):
        MCQs = 1
        FILL_IN_BLANK = 2
        TRUE_OR_FALSE = 3
        SHORT_ANSWER = 4

    question_type = models.IntegerField(choices=QuestionTypes.choices, default=1)

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question
