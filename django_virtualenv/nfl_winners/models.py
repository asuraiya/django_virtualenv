from django.db import models

class Player(models.Model):
  player_name = models.CharField(max_length=50)
  team_name = models.CharField(max_length=50) 
  
  def __unicode__(self):
    return self.player_name + " - " + self.team_name

class PlayerRecord(models.Model):
  player = models.ForeignKey(Player)
  wins = models.PositiveIntegerField()
  losses = models.PositiveIntegerField()
  draws = models.PositiveIntegerField()

  def __unicode__(self):
    return self.player + ": " + self.wins + "-" + self.losses + "-" + self.draws
  
class Team(models.Model):
  owner = models.ForeignKey(Player)
  NFL_TEAM_CHOICES = (
      ('AFC East', (
        ('BUF', 'Buffalo Bills'),
        ('MIA', 'Miami Dolphins'),
        ('NE',  'New England Patriots'),
        ('NYJ', 'New York Jets')
        )
      ),
      ('AFC North', (
        ('BAL', 'Baltimore Ravens'),
        ('CIN', 'Cincinnati Bengals'),
        ('CLE', 'Cleveland Browns'),
        ('PIT', 'Pittsburgh Steelers')
        )
      ),
      ('AFC South', (
        ('HOU', 'Houston Texans'),
        ('IND', 'Indianapolis Colts'),
        ('JAX', 'Jacksonville Jaguars'),
        ('TEN', 'Tennessee Titans')
        )
      ),
      ('AFC West', (
        ('DEN', 'Denver Broncos'),
        ('KC',  'Kansas City Chiefs'),
        ('OAK', 'Oakland Raiders'),
        ('SD',  'San Diego Chargers')
        )
      ),
      ('NFC East', (
        ('DAL', 'Dallas Cowboys'),
        ('NYG', 'New York Giants'),
        ('PHI', 'Philadelphia Eagles'),
        ('WAS', 'Washington Redskins')
        )
      ),
      ('NFC North', (
        ('CHI', 'Chicago Bears'),
        ('DET', 'Detroit Lions'),
        ('GB',  'Green Bay Packers'),
        ('MIN', 'Minnesota Vikings')
        )
      ),
      ('NFC South', (
        ('ATL', 'Atlanta Falcons'),
        ('CAR', 'Carolina Panthers'),
        ('NO',  'New Orleans Saints'),
        ('TB',  'Tampa Bay Buccaneers')
        )
      ),
      ('NFC West', (
        ('ARI', 'Arizona Cardinals'),
        ('STL', 'St. Louis Rams'),
        ('SF',  'San Francisco 49ers'),
        ('SEA', 'Seattle Seahawks')
        )
      ),
      ('NA', 'None') 
  )
  nfl_team_name = models.CharField(max_length=3,
                          choices=NFL_TEAM_CHOICES,
                          default='NA'
                         )
  team_wins = models.PositiveIntegerField()
  team_losses = models.PositiveIntegerField()
  team_draws = models.PositiveIntegerField()
  
  def __unicode__(self):
    return (self.get_nfl_team_name_display()
            + " (" + str(self.team_wins) + "-" 
            + str(self.team_losses) + "-" 
            + str(self.team_draws) + ")"
    )
