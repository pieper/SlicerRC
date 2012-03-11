"""Helper functions for developing - see bottom for key bindings"""

def load_default_volume():
  if not getNodes().has_key('moving'):
    #fileName = slicer.app.slicerHome + "/share/MRML/Testing/TestData/moving.nrrd"
    fileName = os.environ['HOME'] + "/Dropbox/data/faces/neutral.nrrd"
    vl = slicer.modules.volumes.logic()
    volumeNode = vl.AddArchetypeScalarVolume (fileName, "moving", 0)

    # automatically select the volume to display
    appLogic = slicer.app.applicationLogic()
    selNode = appLogic.GetSelectionNode()
    selNode.SetReferenceActiveVolumeID(volumeNode.GetID())
    appLogic.PropagateVolumeSelection()


def multivolume():
  print "SlicerRC - multivolume setup..."
  import imp, sys, os
  path = '%s/../../Slicer4/Modules/Scripted/Scripts' % slicer.app.slicerHome
  if not sys.path.__contains__(path):
    sys.path.insert(0,path)

  mod = "multivolume"
  sourceFile = path + "/MultiVolume.py"
  fp = open(sourceFile, "r")
  globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
  fp.close()

  globals()['sd'] = globals()[mod].MultiVolumeWidget()

def endoscopy():
  print "SlicerRC - endoscopy setup..."
  import imp, sys, os
  scriptPath = '%s/../../Slicer4/Modules/Scripted/Scripts' % slicer.app.slicerHome
  if not sys.path.__contains__(scriptPath):
    sys.path.insert(0,scriptPath)

  mod = "Endoscopy"
  sourceFile = scriptPath + "/Endoscopy.py"
  fp = open(sourceFile, "r")
  globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
  fp.close()

  globals()['e'] = e = globals()[mod].EndoscopyWidget()

def labelStatistics():
  print "SlicerRC - labelStatistics setup..."
  import imp, sys, os
  scriptPath = '%s/../../Slicer4/Modules/Scripted/Scripts' % slicer.app.slicerHome
  if not sys.path.__contains__(scriptPath):
    sys.path.insert(0,scriptPath)

  mod = "LabelStatistics"
  sourceFile = scriptPath + "/LabelStatistics.py"
  fp = open(sourceFile, "r")
  globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
  fp.close()

  globals()['l'] = l = globals()[mod].LabelStatisticsWidget()


def editor():
  print "SlicerRC - editor setup..."
  import imp, sys, os
  import slicer
  tcl("set ::guipath %s/../../Slicer4/Base/GUI/Tcl" % slicer.app.slicerHome )
  tcl("if { [lsearch $::auto_path $::guipath] == -1 } { set ::auto_path [list %s/../../Slicer4/Base/GUI/Tcl $::auto_path] } " % slicer.app.slicerHome)
  tcl("package forget SlicerBaseGUITcl")
  tcl("package require SlicerBaseGUITcl")
  tcl("EffectSWidget::RemoveAll")
  tcl("EffectSWidget::Add DrawEffect")

  if not getNodes().has_key('2006-spgr'):
    slicer.mrmlScene.SetURL('/home/pieper/data/edit/edit-small.mrml')
    slicer.mrmlScene.Connect()

  if 0 and not getNodes().has_key('CTA-cardio'):
    slicer.mrmlScene.SetURL('/home/pieper/data/edit/edit.mrml')
    slicer.mrmlScene.Connect()

  editorLibPath = '%s/../../Slicer4/Modules/Scripted/EditorLib' % slicer.app.slicerHome
  if not sys.path.__contains__(editorLibPath):
    sys.path.insert(0, editorLibPath)
  editorPath = '%s/../../Slicer4/Modules/Scripted/Scripts' % slicer.app.slicerHome
  if not sys.path.__contains__(editorPath):
    sys.path.insert(0,editorPath)


  modules = (
      "EditColor", "EditOptions", "EditBox", "ColorBox", "HelperBox",
      "PaintEffect", 
      )
  for mod in modules:
    sourceFile = editorLibPath + "/" + mod + ".py"
    fp = open(sourceFile, "r")
    globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
    fp.close()
    exec("globals()['EditorLib'].%s = globals()['%s'].%s" % (mod,mod,mod))

  mod = "Editor"
  sourceFile = editorPath + "/Editor.py"
  fp = open(sourceFile, "r")
  globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
  fp.close()

  globals()['e'] = e = globals()[mod].EditorWidget()

def fileScan():
  print "SlicerRC - fileScan setup..."
  import imp, sys, os
  p = '%s/../../Slicer4/Modules/Scripted/Scripts' % slicer.app.slicerHome
  if not sys.path.__contains__(p):
    sys.path.insert(0,p)


  mod = "FileScan"
  sourceFile = p + "/FileScan.py"
  fp = open(sourceFile, "r")
  globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
  fp.close()

  globals()['e'] = e = globals()[mod].FileScanWidget()

def performance():
  print "SlicerRC - performance setup..."
  import os
  execfile(slicer.app.slicerHome + "/../../Slicer4/Base/Testing/Performance.py")
  load_default_volume()

  reslicing(10)
  #timeProbe()
  #global slt
  #slt = sliceLogicTest()

def slicr_setup():
  print "slicr - server setup..."

  load_default_volume()
  import imp, sys, os
  p = '/home/pieper/Dropbox/webgl/slicr'
  if not sys.path.__contains__(p):
    sys.path.insert(0,p)


  mod = "slicr"
  sourceFile = p + "/slicr.py"
  fp = open(sourceFile, "r")
  globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
  fp.close()

  globals()['s'] = globals()[mod].slicr_command_processor()
  globals()['s'].start()

def DICOM():
  print "SlicerRC - DICOM setup..."
  import imp, sys, os
  path = '%s/../../Slicer4/Modules/Scripted/Scripts' % slicer.app.slicerHome
  if not sys.path.__contains__(path):
    sys.path.insert(0,path)

  if False:
    # TODO: reload dicomlib
    dicomLibPath = '%s/../../Slicer4/Modules/Scripted/DICOMLib' % slicer.app.slicerHome
    if not sys.path.__contains__(dicomLibPath):
      sys.path.insert(0, dicomLibPath)


    modules = ("DICOMServers", "DICOMDataExchange", "DICOMWidgets")
    for mod in modules:
      sourceFile = dicomLibPath + "/" + mod + ".py"
      fp = open(sourceFile, "r")
      globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
      fp.close()
      exec("globals()['DICOMLib'].%s = globals()['%s'].%s" % (mod,mod,mod))

  mod = "DICOM"
  sourceFile = path + "/DICOM.py"
  fp = open(sourceFile, "r")
  globals()[mod] = imp.load_module(mod, fp, sourceFile, ('.py', 'r', imp.PY_SOURCE))
  fp.close()

  globals()['DICOM'] = globals()[mod].DICOMWidget()


def setupMacros():
  """Set up hot keys for various development scenarios"""
  
  import qt
  global load_default_volume, multivolume, endoscopy, editor, fileScan, performance, slicr_setup, DICOM
  
  print "SlicerRC - Install custom keyboard shortcuts"
  
  macros = (
    ("Shift+Ctrl+0", loadSlicerRCFile),
    ("Shift+Ctrl+1", multivolume),
    ("Shift+Ctrl+2", labelStatistics),
    ("Shift+Ctrl+2", endoscopy),
    ("Shift+Ctrl+3", editor),
    ("Shift+Ctrl+4", fileScan),
    ("Shift+Ctrl+5", performance),
    ("Shift+Ctrl+6", slicr_setup),
    ("Shift+Ctrl+7", DICOM),
    )
      
  for keys,f in macros:
    k = qt.QKeySequence(keys)
    s = qt.QShortcut(k,mainWindow())
    s.connect('activated()', f)
    s.connect('activatedAmbiguously()', f)
    print "SlicerRC - '%s' -> '%s'" % (keys, f.__name__)

# Install macros
if mainWindow(verbose=False): setupMacros()


# Display current time
from time import gmtime, strftime
print "Slicer RC file loaded [%s]" % strftime("%d/%m/%Y %H:%M:%S", gmtime())

# always show shell when using macros
pythonShell()
