{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'tdl_wxGUI_bgTemplate',
          'title':u'PDS',
          'size':(633, 408),
          'statusBar':1,
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFile_CD',
                   'label':u'&Change Directory\tCtrl+C',
                  },
                  {'type':'MenuItem',
                   'name':'menuFile_Save',
                   'label':u'&Save\tCtrl+S',
                  },
                  {'type':'MenuItem',
                   'name':'menuFile_SaveAs',
                   'label':u'S&aveAs\tCtrl+A',
                  },
                  {'type':'MenuItem',
                   'name':'menuFile_Restore',
                   'label':u'&Restore\tCtrl+R',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':u'E&xit\tCtrl+X',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuOptions',
             'label':u'Options',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuOptionsEditSiteStartup',
                   'label':u'Edit site startup',
                  },
                  {'type':'MenuItem',
                   'name':'menuOptionsEditHomeStartup',
                   'label':u'Edit user startup',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuShell',
             'label':'Shell',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuShellStart',
                   'label':'Shell',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuApps',
             'label':u'Applications',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuAppsPlotSelection',
                   'label':u'PlotSelection',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsSpecData',
                   'label':u'Spec Data',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsCtrData',
                   'label':u'Ctr Data',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsScanSelect',
                   'label':u'Scan Selector',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsFilter',
                   'label':u'HDF Filter',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsIntegrator',
                   'label':u'HDF Integrator',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsXRF',
                   'label':u'XRF Fitting',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsXRRBuild',
                   'label':u'XRR Model Builder',
                  },
                  {'type':'MenuItem',
                   'name':'menuAppsXRRModel',
                   'label':u'XRR Interface Model',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':u'Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpUse',
                   'label':u'Help on use',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpDocumentation',
                   'label':u'Documentation',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticLine', 
    'name':'Sep1', 
    'position':(3, 281), 
    'size':(620, 3), 
    'font':{'faceName': 'Microsoft Sans Serif', 'family': 'sansSerif', 'size': 8}, 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'Prompt', 
    'position':(3, 285), 
    'font':{'style': 'bold', 'faceName': u'Microsoft Sans Serif', 'family': 'sansSerif', 'size': 11}, 
    'text':'>>>', 
    },

{'type':'TextField', 
    'name':'ShellCmd', 
    'position':(40, 285), 
    'size':(580, 26), 
    'font':{'faceName': u'Microsoft Sans Serif', 'family': 'sansSerif', 'size': 10}, 
    },

{'type':'TextArea', 
    'name':'ShellText', 
    'position':(4, 7), 
    'size':(617, 270), 
    'editable':False, 
    'font':{'faceName': 'Lucida Console', 'family': 'sansSerif', 'size': 9}, 
    },

] # end components
} # end background
] # end backgrounds
} }
