"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from podrum.plugin.PluginLoader import PluginLoader

class PluginBase:
    @staticmethod
    def onStart(): pass

    @staticmethod
    def onStarted(): pass

    @staticmethod
    def onStop(): pass

    @staticmethod
    def onStopped(): pass

    @staticmethod
    def getName():
        return PluginLoader.name

    @staticmethod
    def getDescription():
        return PluginLoader.description

    @staticmethod
    def getAuthor():
        return PluginLoader.author

    @staticmethod
    def getVersion():
        return PluginLoader.version

    @staticmethod
    def getApiVersion():
        return PluginLoader.apiVersion
