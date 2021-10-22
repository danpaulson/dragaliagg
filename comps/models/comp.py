from django.db import models

from comps.enums import AdventurerSlotEnum
from core.models import SlugModel
from game_data.models import Adventurer


class Comp(SlugModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    creator = models.CharField(max_length=100)
    game_version = models.CharField(max_length=100)
    clear_time = models.CharField(max_length=50)
    clear_rate = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    discussion_link = models.URLField()
    video_link = models.URLField()

    section = models.ForeignKey('CompSection', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    quest = models.ForeignKey('CompQuest', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    difficulty = models.ForeignKey('CompDifficulty', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)

    shared_skill_1 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    shared_skill_2 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_2', on_delete=models.DO_NOTHING, blank=True, null=True)

    def slug_name(self):
        return self.title
    
    def get_team(self):
        comp_slots = {}
        for build in self.builds.all():
            comp_slots[build.slot] = build.adventurer
        
        return comp_slots
    
    def get_lead(self):
        return self.builds.get(slot=AdventurerSlotEnum.LEAD_UNIT.value).adventurer
    
    def get_rest_of_team(self):
        rest_of_team = {}
        for build in self.builds.exclude(slot=AdventurerSlotEnum.LEAD_UNIT.value):
            rest_of_team[build.slot] = build.adventurer
        
        return rest_of_team

    def __str__(self):
        return self.title
