from django.contrib import admin


class VotesAdmin(admin.ModelAdmin):
    list_display = (
        'candidate',
        'party',
        'election',
        'division',
        'count',
        'pct',
        'winning',
        'runoff'
    )
    list_editable = ('count', 'pct', 'winning', 'runoff')
    list_filter = (
        'division__level__name',
        'candidate_election__election__election_day__date',
    )
    ordering = (
        'candidate_election__election',
        'division__label',
        'count',
        'candidate_election__candidate__person__last_name',
    )
    search_fields = (
        'candidate_election__election',
        'division__label',
        'candidate_election__candidate__person__last_name'
    )

    fieldsets = (
        ('Tabulation', {
            'fields': ('count', 'pct', 'total', 'winning', 'runoff')
        }),
        ('Relationships', {
            'fields': ('division', 'candidate_election', 'ballot_answer')
        })
    )

    autocomplete_fields = ('division',)

    def candidate(self, obj):
        return obj.candidate_election.candidate.person.full_name

    def party(self, obj):
        return obj.candidate_election.candidate.party

    def election(self, obj):
        return obj.candidate_election.election

    def division(self, obj):
        return obj.division
