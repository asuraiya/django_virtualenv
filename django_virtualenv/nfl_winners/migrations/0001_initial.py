# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'nfl_winners_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'nfl_winners', ['Player'])

        # Adding model 'PlayerRecord'
        db.create_table(u'nfl_winners_playerrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nfl_winners.Player'])),
            ('wins', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('losses', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('draws', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'nfl_winners', ['PlayerRecord'])

        # Adding model 'Team'
        db.create_table(u'nfl_winners_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nfl_winners.Player'])),
            ('nfl_team_name', self.gf('django.db.models.fields.CharField')(default='NA', max_length=3)),
            ('team_wins', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('team_losses', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('team_draws', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'nfl_winners', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'nfl_winners_player')

        # Deleting model 'PlayerRecord'
        db.delete_table(u'nfl_winners_playerrecord')

        # Deleting model 'Team'
        db.delete_table(u'nfl_winners_team')


    models = {
        u'nfl_winners.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'nfl_winners.playerrecord': {
            'Meta': {'object_name': 'PlayerRecord'},
            'draws': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nfl_winners.Player']"}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'nfl_winners.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nfl_team_name': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '3'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nfl_winners.Player']"}),
            'team_draws': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'team_losses': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'team_wins': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['nfl_winners']