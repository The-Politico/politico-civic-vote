# Imports from Django.
from django.contrib import admin
from django import forms


# Imports from other dependencies.
from election.models import CandidateElection


# class CustomModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return "{} ({}): {} {}".format(
#             obj.candidate.person.full_name,
#             obj.candidate.party.ap_code,
#             obj.race.label,
#             obj.election_type.label,
#         )
#
#
# class VotesAdminForm(forms.ModelForm):
#     candidate_election = CustomModelChoiceField(
#         queryset=CandidateElection.objects.all(), required=False
#     )


class VotesAdmin(admin.ModelAdmin):
    # form = VotesAdminForm
    list_display = (
        "candidate",
        "party",
        "office",
        "election_date",
        "division",
        "count",
        "pct",
        "winning",
        "runoff",
    )
    list_editable = ("count", "pct", "winning", "runoff")
    list_filter = (
        "division__level__name",
        "__".join(
            [
                "candidate_election",
                "election",
                "election_ballot",
                "election_event",
                "election_day",
                "date",
            ]
        ),
    )
    ordering = (
        "__".join(
            [
                "-candidate_election",
                "election",
                "election_ballot",
                "election_event",
                "election_day",
                "date",
            ]
        ),
        "division__label",
        "candidate_election__election__election_ballot__party__label",
        "count",
        "candidate_election__candidate__person__last_name",
    )
    search_fields = (
        "candidate_election__election__race__label",
        "__".join(
            [
                "candidate_election",
                "election",
                "election_ballot",
                "election_event",
                "election_day",
                "date",
            ]
        ),
        "__".join(
            [
                "candidate_election",
                "election",
                "election_ballot",
                "election_event",
                "election_day",
                "slug",
            ]
        ),
        "division__label",
        "candidate_election__candidate__person__last_name",
    )

    fieldsets = (
        (
            "Tabulation",
            {"fields": ("count", "pct", "total", "winning", "runoff")},
        ),
        (
            "Relationships",
            {"fields": ("division", "candidate_election", "ballot_answer")},
        ),
    )

    autocomplete_fields = ("division",)

    def candidate(self, obj):
        return obj.candidate_election.candidate.person.full_name

    def office(self, obj):
        return obj.candidate_election.election.race.office

    def election_date(self, obj):
        elex_ballot = obj.candidate_election.election.election_ballot
        return elex_ballot.election_event.election_day.date

    def party(self, obj):
        return obj.candidate_election.candidate.party

    def election(self, obj):
        return obj.candidate_election.election

    def division(self, obj):
        return obj.division
