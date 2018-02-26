from django.contrib import admin
from vote.models import Delegates, ElectoralVotes, Votes


class VotesAdmin(admin.ModelAdmin):
    list_filter = (
        'candidate_election__election__division__level',
    )


admin.site.register(Delegates)
admin.site.register(ElectoralVotes)
admin.site.register(Votes, VotesAdmin)
