"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""

from podrum.network.protocol.types.PlayerPermissions import PlayerPermissions
from podrum.network.protocol.AdventureSettingsPacket import AdventureSettingsPacket
from podrum.network.PacketPool import PacketPool
from podrum.Server import Server

class Player:

    SURVIVAL = 0
    CREATIVE = 1
    ADVENTURE = 2
    SPECTATOR = 3
    VIEW = self.SPECTATOR

    connection = None
    server = None
    logger = None
    address = None
    name = None
    username = ""
    displayName = ""
    locale = None
    randomId = None
    uuid = None
    xuid = None
    skin = None
    viewDistance = None
    gamemode = 0
    pitch = 0
    yaw = 0
    headYaw = 0
    onGround = False
    platformChatId = ''
    deviceOS = None
    deviceModel = None
    deviceId = None
    gamemode = None
    autoJump = True
    allowFlight = False
    flying = False
    inAirTicks = 0

    def __init__(self, connection, address, logger, server):
        self.connection = connection
        self.address = address
        self.logger = logger
        self.server = server

    def getClientId(self):
        return self.randomId

    def isAuthenticated(self):
        return self.xuid != ""

    def getXuid(self):
        return self.xuid

    def getPlayer(self):
        return self

    def getName(self):
        return self.username

    def getDisplayName(self):
        return self.displayName

    def isOp():
        return Server.isOp(self.getName())

    def setAllowedFlight(self, value):
        self.allowFlight = value
        self.sendSettings()

    def getAllowedFlight(self):
        return self.allowFlight

    def setFlying(self, value):
        if self.flying != value:
            self.flying = value
            self.resetFallDistance()
            self.sendSettings()

    def isFlying(self):
        return self.flying

    def resetFallDistance(self):
        self.inAirTicks = 0

    def getViewDistance(self):
        return self.viewDistance

    def getInAirTicks(self):
        return self.inAirTicks

    def isSpectator(self):
        return self.gamemode == self.SPECTATOR

    def sendSettings(self):
        AdventureSettingsPacket.setFlag(AdventureSettingsPacket.WORLD_IMMUTABLE, self.isSpectator())
        AdventureSettingsPacket.setFlag(AdventureSettingsPacket.NO_PVP, self.isSpectator())
        AdventureSettingsPacket.setFlag(AdventureSettingsPacket.AUTO_JUMP, self.autoJump)
        AdventureSettingsPacket.setFlag(AdventureSettingsPacket.ALLOW_FLIGHT, self.allowFlight)
        AdventureSettingsPacket.setFlag(AdventureSettingsPacket.NO_CLIP, self.isSpectator())
        AdventureSettingsPacket.setFlag(AdventureSettingsPacket.FLYING, self.flying)

        AdventureSettingsPacket.commandPermission = AdventureSettingsPacket.PERMISSION_OPERATOR if self.isOp() else AdventureSettingsPacket.PERMISSION_NORMAL
        AdventureSettingsPacket.playerPermission = PlayerPermissions.OPERATOR if self.isOp() else PlayerPermissions.MEMBER
        AdventureSettingsPacket.entityUniqueId = self.getId()