from django.contrib import admin
from vote.models import Delegates, ElectoralVotes, Votes

admin.site.register(Delegates)
admin.site.register(ElectoralVotes)
admin.site.register(Votes)
