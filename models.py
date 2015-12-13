from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.TextField()
    multiple_choice = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def has_voted(self, user):
        return UserChoice.objects.filter(poll=self, user=user).count() > 0

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-votes', 'choice_text')

    @property
    def percentage(self):
        choices = self.poll.choice_set

        vote_count = sum([choice.votes for choice in choices.all()])

        if vote_count > 0:
            return Decimal(self.votes) / vote_count * 100
        return 0

    def __unicode__(self):
        return self.choice_text


class UserChoice(models.Model):
    user = models.ForeignKey(User)
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'choice')

    def __unicode__(self):
        return '%s: %s' % (self.user, self.choice)


class AnonymousUserChoice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s: %s' % (self.poll, self.choice)
