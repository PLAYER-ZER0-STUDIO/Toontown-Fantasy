from pandac.PandaModules import *
from . import SafeZoneLoader
from . import MMPlayground
from toontown.toonbase import ToontownGlobals


class MMSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(
            self, hood, parentFSM, doneEvent)
        self.playgroundClass = MMPlayground.MMPlayground
        self.musicFile = 'user/resources/default/phase_6/audio/bgm/MM_nbrhood.ogg'
        self.activityMusicFile = 'user/resources/default/phase_6/audio/bgm/MM_SZ_activity.ogg'
        self.dnaFile = 'user/resources/default/phase_6/dna/minnies_melody_land_sz.dna'
        self.safeZoneStorageDNAFile = 'user/resources/default/phase_6/dna/storage_MM_sz.dna'

    def load(self):
        print('loading MM safezone')
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.piano = self.geom.find('**/center_icon')
        if self.piano.isEmpty():
            self.notify.error('Piano not found')
        else:
            hq = self.geom.find('**/*toon_landmark_hqMM_DNARoot')
            hq.wrtReparentTo(self.piano)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.piano
