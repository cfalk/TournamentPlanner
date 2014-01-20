from django.http import HttpResponse
from django.shortcuts import render

from models import *

import random
import re

def remove_whitespace(string):
 string = re.sub("[;,]+",";",string) #Remove multiple separators
 string = re.sub("[\s\t]+[;,]",";",string) #Remove preceding cwhitespace
 string = re.sub("[;,][\s\t]+",";",string) #Remove trailing whitespace
 string = re.sub("[\s\t]+"," ",string) #Remove any large areas of whitespace
 return string

def get_clean_list(string):
 #Remove whitespace, simplify separators, and remove empty entries.
 return [entry for entry in remove_whitespace(string).split(";") if entry or entry==" "]

#Model Construction Views
def make_Tournament_with_Participants(request):
 u = request.user
 if u.is_authenticated() and request.method=="POST":
  #Get the tournament information from the request.
  try:
   tournament_name = request.POST["tournament_name"]
   participants = request.POST["participants"]
  except:
   return HttpResponse("Form missing fields!")  

  #Clean up the participants data and attempt to make Django objects.
  try:
   part_list = get_clean_list(participants)

   #Make the Tournament.   
   tournament = Tournament()
   tournament.name = tournament_name
   tournament.user = u
   tournament.save()

   #Make the Participants.
   for entry in part_list:
    participant = Participant()
    participant.name = entry
    participant.tournament = tournament
    participant.save()

  except:
   return HttpResponse("Tournament construction failed!")
 return HttpResponse("TODO: Add form!")


def sort_games(string_peeps):
        list_peeps = string_peeps.split(",")
        games = [[]]
        num_games = 0
        while list_peeps:
                person = random.choice(list_peeps)
                list_peeps.remove(person)
                if len(games[num_games]) < 4:
                        games[num_games].append(person)
                        print games
                else:
                        num_games+=1
                        games.append([])
        for game in games:
                print "Game {}".format(num_games)
                for player in game:
                        print "{}\n".format(player)
                print "\n"


def home(request):
 return render(request, "index.html", {})
