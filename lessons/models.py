from django.db import models


class Lesson(models.Model):
    topic = models.CharField(max_length=100)
    exercises_number = models.PositiveIntegerField()
    requirement = models.ForeignKey("self", null=True, blank=True)
    publish = models.BooleanField(default=False)

    def get_fixed_order_exercises(self):
        """
        Get the exercises that have fixed order only
        """
        return self.exercise_set.filter(number__isnull=False)

    def clean_exercises_number(self):
        """
        Verify that exercises number is between the number of related fixed order exercises
        and the number of all related exercises, inclusively.
        If not, set exercises number to closest valid.
        If number is outside this range, lesson action will crash during initialization (ie. when trying to learn)
        :return:
        """
        fixed_order_exercises_count = self.get_fixed_order_exercises().count()
        total_exercises_count = self.exercise_set.count()
        if self.exercises_number < fixed_order_exercises_count:
            self.exercises_number = fixed_order_exercises_count
            self.save()
        elif self.exercises_number > total_exercises_count:
            self.exercises_number = total_exercises_count
            self.save()

    def __str__(self):
        return self.topic

