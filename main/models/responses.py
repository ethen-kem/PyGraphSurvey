from django.db import models
from main.models.questions import Question


# for questions that have option
class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=50)


class ImageReponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="image_responses"
    )
    response = models.ImageField(upload_to="ImageResponses")


class FileReponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="file_responses"
    )
    response = models.FileField(upload_to="FileResponses")


class SelectionResponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="selection_responses"
    )
    response = models.ForeignKey(Options, on_delete=models.CASCADE)
