from django.contrib import admin
from vote.models import Delegates, ElectoralVotes, Votes
from .votes import VotesAdmin

admin.site.register(Delegates)
admin.site.register(ElectoralVotes)
admin.site.register(Votes, VotesAdmin)
