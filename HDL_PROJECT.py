#!/usr/bin/env python
#===========================================================================
# File       : HDLProject.py
# Author     : Andrew Carter
# Created    : 2015-10-17
#===========================================================================
# Description: 
#   Sublime Text 3 wrapper for the HDLProject plugin. 
#
#===========================================================================
# Copyright 2015 sublime_hdl_project
#===========================================================================
import sublime
import sys
import os
import importlib
from sys import platform as _platform

curr_dir = os.path.dirname(os.path.realpath(__file__))
#print(curr_dir)
if curr_dir not in sys.path:
  sys.path.append(curr_dir)

if _platform == "win32":
  package_name = curr_dir.split('\\')[-1]
else:
  package_name = curr_dir.split('/')[-1]  

modules_l = [
  'hdl_project',
  'hdl_project.error',
  'hdl_project.util',
  'hdl_project.views',
  'hdl_project.commands',
  'hdl_project.hdl_file',
  'hdl_project.hdl_project',
  'hdl_project.threads',
]

from imp import reload
for module in modules_l:
  module_name = package_name + '.' + module
  if module_name not in sys.modules:
    importlib.import_module(module_name)
  else:
    reload(sys.modules[package_name + '.' + module])

from hdl_project.commands import (
  CreateHdlProjectCommand,
  RefreshHdlProjectCommand,
  OpenHdlProjectCommand,
  ContextOpenOriginalContainingFolderCommand,
  SidebarOpenOriginalContainingFolderCommand,
  HdlProjectSetStatusCommand,
  DoTclBuildCommand,
  CancelTclBuildCommand,
  GenerateHdlCompileOrderCommand,
  HdlProjectRevealInSidebarCommand,
  HdlProjectEventListenerRevealInSidebarCommand,
  SidebarRevealInSidebarFileSysCommand,
  SidebarRevealInSidebarHierarchyCommand,
  SignalPopupEventListenerCommand,
  ToggleHdlPopupsCommand,
  ConstantPopoupEventListenerCommand,
  OpenHdlProjectFileCommand,
  CheckHdlSyntaxEventListenerCommand,
  CheckHdlSyntaxCommand,
  CreateHdlSyntaxErrorRegionsCommand,
  GoToPrevHdlSyntaxErrorCommand,
  GoToNextHdlSyntaxErrorCommand,
  HdlSyntaxErrorPopupCommand,
  CleanupModuleAmbiguityCommand,
  SetAmbiguityStatusCommand,
  OpenReferenceProjectCommand,
  InstancePopoupEventListenerCommand,
  CommentSelectionCommand,
  UncommentSelectionCommand,
  GenericPopupEventListenerCommand,
  OpenHdlPanelCommand,
  OpenModuleByFilenameCommand,
  GenerateFileListCommand,
  OpenOutputPathCommand,
  OpenModuleByHierarchyCommand,
  DeleteHdlProjectCommand,
  ExploreFileSystemInQuickPanelCommand,
  HdlProjectWebsiteCommand,
  HdlProjectIssuesCommand,
  HdlProjectGetLicenseCommand,
  HdlProjectDocsCommand,
  OpenHdlParentCommand,
  UpdateHdlProjectSettingCommand,
  CreateDataStructureJsonCommand,
  UpdateProjectGenericsCommand,
  ToggleSplitPanelCommand,
  ExtendHdlCompletionsCommand,
  CreateHdlWorkspaceCommand,
  #CheckHdlWorkspaceSyntaxCommand,
  ParseProjectGenericsProcessEventListenerCommand,
  ParseConstantsProcessEventListenerCommand
)

#Commands that require v3.1 API support. 
if int(sublime.version()) > 3170:
  from hdl_project.commands import (
    AddNewProjectEntryCommand,
    UpdateProjectEntryCommand,
    RemoveProjectEntryCommand
  )


#Required to write to custom panel
from hdl_project.views import (
  HdlProjectInsertTextCommand,
  HdlProjectEraseViewCommand
)
