# Imports from Django.
from django.contrib import admin


# Imports from vote.
from vote.admin.votes import VotesAdmin
from vote.models import Delegates
from vote.models import ElectoralVotes
from vote.models import Votes


admin.site.register(Delegates)
admin.site.register(ElectoralVotes)
admin.site.register(Votes, VotesAdmin)
