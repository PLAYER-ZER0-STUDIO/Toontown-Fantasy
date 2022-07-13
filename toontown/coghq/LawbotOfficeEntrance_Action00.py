from toontown.coghq.SpecImports import *
import random
GlobalEntities = {1000: {'type': 'levelMgr',
                         'name': 'LevelMgr',
                         'comment': '',
                         'parentEntId': 0,
                         'cogLevel': 0,
                         'farPlaneDistance': 1500,
                         'modelFilename': 'user/resources/default/phase_11/models/lawbotHQ/LB_Zone03a',
                         'wantDoors': 1},
                  1001: {'type': 'editMgr',
                         'name': 'EditMgr',
                         'parentEntId': 0,
                         'insertEntity': None,
                         'removeEntity': None,
                         'requestNewEntity': None,
                         'requestSave': None},
                  0: {'type': 'zone',
                      'name': 'UberZone',
                      'comment': '',
                      'parentEntId': 0,
                      'scale': 1,
                      'description': '',
                      'visibility': []},
                  10000: {'type': 'entrancePoint',
                          'name': '<unnamed>',
                          'comment': '',
                          'parentEntId': 0,
                          'pos': Point3(0, 6, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1,
                          'entranceId': 0,
                          'radius': 15,
                          'theta': 20},
                  100000: {'type': 'model',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 10004,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Point3(1, 1, 1),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_torch_lampB'},
                  100001: {'type': 'model',
                           'name': 'copy of <unnamed>',
                           'comment': '',
                           'parentEntId': 100002,
                           'pos': Point3(0, 0, 0),
                           'hpr': Point3(0, 0, 180),
                           'scale': Point3(1, 1, 1),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_torch_lampB'},
                  100004: {'type': 'model',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100003,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Point3(1, 1, 1),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_torch_lampB'},
                  100006: {'type': 'model',
                           'name': 'copy of <unnamed>',
                           'comment': '',
                           'parentEntId': 100005,
                           'pos': Point3(0, 0, 0),
                           'hpr': Point3(0, 0, 180),
                           'scale': Point3(1, 1, 1),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_torch_lampB'},
                  100008: {'type': 'model',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100007,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Point3(1.5, 1.5, 1.5),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_paper_twist_stacks'},
                  100010: {'type': 'model',
                           'name': 'copy of <unnamed>',
                           'comment': '',
                           'parentEntId': 100009,
                           'pos': Point3(0, 0, 0),
                           'hpr': Point3(180, 0, 180),
                           'scale': Point3(1.5, 1.5, 1.5),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_paper_twist_stacks'},
                  100012: {'type': 'model',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100011,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1,
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_CardBoardBox'},
                  100013: {'type': 'model',
                           'name': 'copy of <unnamed>',
                           'comment': '',
                           'parentEntId': 100014,
                           'pos': Point3(0, 0, 0),
                           'hpr': Point3(0, 0, 180),
                           'scale': 1,
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_CardBoardBox'},
                  100016: {'type': 'model',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100015,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Point3(1.5, 1.5, 1.5),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_couchA'},
                  100017: {'type': 'model',
                           'name': 'copy of <unnamed>',
                           'comment': '',
                           'parentEntId': 100018,
                           'pos': Point3(0, 0, 0),
                           'hpr': Point3(0, 0, 180),
                           'scale': Point3(1.5, 1.5, 1.5),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'user/resources/default/phase_11/models/lawbotHQ/LB_couchA'},
                  10002: {'type': 'nodepath',
                          'name': 'props',
                          'comment': '',
                          'parentEntId': 0,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10004: {'type': 'nodepath',
                          'name': 'lamp',
                          'comment': '',
                          'parentEntId': 10002,
                          'pos': Point3(-10.1845, 16.3439, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  100003: {'type': 'nodepath',
                           'name': 'lamp2',
                           'comment': '',
                           'parentEntId': 10002,
                           'pos': Point3(10.3093, 14.7794, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Vec3(1, 1, 1)},
                  100007: {'type': 'nodepath',
                           'name': 'paper',
                           'comment': '',
                           'parentEntId': 10002,
                           'pos': Point3(14.3907, 11.4389, 0),
                           'hpr': Vec3(300.379, 0, 0),
                           'scale': Vec3(1, 1, 1)},
                  100011: {'type': 'nodepath',
                           'name': 'box',
                           'comment': '',
                           'parentEntId': 10002,
                           'pos': Point3(-18.5313, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Vec3(1, 1, 1)},
                  100015: {'type': 'nodepath',
                           'name': 'couch',
                           'comment': '',
                           'parentEntId': 10002,
                           'pos': Point3(14.3585, -9.43671, 0),
                           'hpr': Vec3(270.699, 0, 0),
                           'scale': Vec3(1, 1, 1)},
                  100002: {'type': 'rendering',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 10004,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1,
                           'blending': 'Normal',
                           'colorA': 1.0,
                           'colorB': 1.0,
                           'colorG': 1.0,
                           'colorR': 1.0,
                           'fogOn': 0,
                           'renderBin': 'default'},
                  100005: {'type': 'rendering',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100003,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1,
                           'blending': 'Normal',
                           'colorA': 1.0,
                           'colorB': 1.0,
                           'colorG': 1.0,
                           'colorR': 1.0,
                           'fogOn': 0,
                           'renderBin': 'default'},
                  100009: {'type': 'rendering',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100007,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1,
                           'blending': 'Normal',
                           'colorA': 1.0,
                           'colorB': 1.0,
                           'colorG': 1.0,
                           'colorR': 1.0,
                           'fogOn': 0,
                           'renderBin': 'default'},
                  100014: {'type': 'rendering',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100011,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1,
                           'blending': 'Normal',
                           'colorA': 1.0,
                           'colorB': 1.0,
                           'colorG': 1.0,
                           'colorR': 1.0,
                           'fogOn': 0,
                           'renderBin': 'default'},
                  100018: {'type': 'rendering',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100015,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1,
                           'blending': 'Normal',
                           'colorA': 1.0,
                           'colorB': 1.0,
                           'colorG': 1.0,
                           'colorR': 1.0,
                           'fogOn': 0,
                           'renderBin': 'default'}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
             'scenarios': [Scenario0],
             'titleString': 'MemTag: LawbotOfficeEntrance_Action00 %s' % random.random()}
