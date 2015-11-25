#!/usr/bin/python3
###############################################################################
###############################################################################
	# LICENSE: GNU General Public License, version 2 (GPLv2)
	# Copyright 2015, Charlie J. Smotherman
	#
	# This program is free software; you can redistribute it and/or
	# modify it under the terms of the GNU General Public License v2
	# as published by the Free Software Foundation.
	#
	# This program is distributed in the hope that it will be useful,
 	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.
	#
	# You should have received a copy of the GNU General Public License
	# along with this program; if not, write to the Free Software
	# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
###############################################################################
###############################################################################
import logging
from pymongo import MongoClient
client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class SongView():
	def create_songView_db(self, OFC):
		count = 0
		page = 1	
		songalphaoffsetlist = []
		songviewlist = []
		for s in db.tags.find({}, {'song':1, 'songid':1, 'artist':1, '_id':0}):
			x = {}
			count += 1
			if count == OFC:
				page += 1
				count = 0
			songalphaoffsetlist.append(page)
			x['page'] = page
			x['song'] = s['song']
			x['songid'] = s['songid']
			x['artist'] = s['artist']
			songviewlist.append(x)
		songalphaoffsetlist = list(set(songalphaoffsetlist))
		viewsdb.songalpha.insert(dict(songalpha=songalphaoffsetlist))
		viewsdb.songView.insert(songviewlist)
		logging.info('get_song_offset is complete')