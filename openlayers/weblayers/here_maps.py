# -*- coding: utf-8 -*-
"""
/***************************************************************************
OpenLayers Plugin
A QGIS plugin

                             -------------------
begin                : 2009-11-30
copyright            : (C) 2009 by Pirmin Kalberer, Sourcepole
email                : pka at sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from .weblayer import WebLayer3857


class OlHereMapsLayer(WebLayer3857):

    emitsLoadEnd = True

    def __init__(self, name, html):
        WebLayer3857.__init__(self, groupName="HERE Maps",
		                      groupIcon="here_icon.png",
                              name=name, html=html)


class OlHereNormalStreetMap(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Normal Street Map', html='OlHereNormalStreetMap.html')
		
class OlHereNormalStreetMapCHT(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Normal Street Map (CHT)', html='OlHereNormalStreetMapCHT.html')
		
class OlHereNormalStreetMapChina(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Normal Street Map (China)', html='OlHereNormalStreetMapChina.html')


class OlHereSatelliteMap(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Satellite Map', html='OlHereSatelliteMap.html')


class OlHereHybridMap(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Hybrid Map', html='OlHereHybridMap.html')
		
class OlHereHybridMapCHT(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Hybrid Map (CHT)', html='OlHereHybridMapCHT.html')
		
class OlHereHybridMapChina(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Hybrid Map (China)', html='OlHereHybridMapChina.html')
		
class OlHereNormalTrafficDayLayer(OlHereMapsLayer):

    def __init__(self):
        OlHereMapsLayer.__init__(self, name='HERE Normal Traffic Day Map', html='OlHereNormalTrafficDayLayer.html')
