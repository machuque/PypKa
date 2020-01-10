"""
Rules for force field conversion
"""
gromos2amber = {
    'ASP': {0: {'HD11': 'HD2',
                'OD1': 'OD2',
                'OD2': 'OD1'},
            1: {'HD21': 'HD2'},
            2: {'HD12': 'HD2',
                'OD1': 'OD2',
                'OD2': 'OD1'},
            3: {'HD22': 'HD2'}
    },
    'CYS': {0: {'HG1': 'HG'},
            1: {'HG2': 'HG'},
            2: {'HG3': 'HG'}
    },
    'GLU': {0: {'HE11': 'HE2',
                'OE1': 'OE2',
                'OE2': 'OE1'},
            1: {'HE21': 'HE2'},
            2: {'HE12': 'HE2',
                'OE1': 'OE2',
                'OE2': 'OE1'},
            3: {'HE22': 'HE2'}
    },
    'HIS': {},
    'TYR': {0: {'HH1': 'HH'},
            1: {'HH2': 'HH'}
    },
    'LYS': {0: {'HZ3': 'HZ1'},
            1: {'HZ3': 'HZ2'}},
    'SER': {0: {'HG1': 'HG'},
            1: {'HG2': 'HG'},
            2: {'HG3': 'HG'}
    },
    'THR': {0: {'HG1': 'HG1'},
            1: {'HG2': 'HG1'},
            2: {'HG3': 'HG1'}
    },
    'NTR': {0: {'H3': 'H1'},
            1: {'H3': 'H2'}},
    'CTR': {0: {'HO11': 'HO',
                'O1': 'O',
                'O2': 'OXT',
                'CT': 'C'},
            1: {'HO21': 'HO',
                'O2': 'O',
                'O1': 'OXT',
                'CT': 'C'},
            2: {'HO12': 'HO',
                'O1': 'O',
                'O2': 'OXT',
                'CT': 'C'},
            3: {'HO22': 'HO',
                'O2': 'O',
                'O1': 'OXT',
                'CT': 'C'},
            4: {'O1': 'O',
                'O2': 'OXT',
                'CT': 'C'}
    }
}


ffconversions = {'GROMOS': {'AMBER': gromos2amber}}

AMBER_Hs = {
    'NTR': ('H1', 'H2', 'H3'),
    'CTR': ('HO'),
    'ASP': ('HD2'),
    'CYS': ('HG'),
    'GLH': ('HE2'),
    'HIP': ('HD1', 'HE2'),
    'HID': ('HD1'),
    'HIE': ('HE2'),
    'LYS': ('HZ1', 'HZ2', 'HZ3'),
    'LYN': ('HZ2', 'HZ3'),
    'SER': ('HG'),
    'THR': ('HG1'),
    'TYR': ('HH')
}

AMBER_mainchain_Hs = ['H', 'HA']
mainchain_Hs = {}

AMBER_protomers = {'ASP': {'ASH': {0: ('HD21', 'HD12', 'HD22'), 1: ('HD11', 'HD12', 'HD22'),
                                   2: ('HD11', 'HD21', 'HD22'), 3: ('HD11', 'HD21', 'HD21')},
                           'ASP': {4: ('HD11', 'HD12', 'HD21', 'HD22')}},
                   'CYS': {'CYS': {0: ('HG2', 'HG3'), 1: ('HG1', 'HG3'), 2: ('HG1', 'HG2')},
                           'CYM': {3: ('HG1', 'HG2', 'HG3')}},
                   'GLU': {'GLH': {0: ('HE21', 'HE12', 'HE22'), 1: ('HE11', 'HE12', 'HE22'),
                                   2: ('HE11', 'HE21', 'HE22'), 3: ('HE11', 'HE12', 'HE21')},
                           'GLU': {4: ('HE11', 'HE12', 'HE21', 'HE22')}},
                   'HIS': {'HID': {0: ('HE2')},
                           'HIE': {1: ('HD1')},
                           'HIP': {2: ('')}},
                   'TYR': {'TYR': {0: ('HH2'), 1:('HH1')},
                           'TYM': {2: ('HH1', 'HH2')}},
                   'LYS': {'LYN': {0: ('HZ1'), 1: ('HZ2'), 2: ('HZ3')},
                           'LYS': {3: ('')}},
                   'SER': {'SER': {0: ('HG2', 'HG3'), 1: ('HG1', 'HG3'), 2: ('HG1', 'HG2')},
                           'SEM': {3: ('HG1', 'HG2', 'HG3')}},
                   'THR': {'THR': {0: ('HG2', 'HG3'), 1: ('HG1', 'HG3'), 2: ('HG1', 'HG2')},
                           'THM': {3: ('HG1', 'HG2', 'HG3')}},
                   'NTR': {'NTR': {0: ('H1'), 1: ('H2'), 2: ('H3')},
                           'NTN': {3: ('')}},
                   'CTR': {'CTH': {0: ('HO21', 'HO12', 'HO22'), 1: ('HO11', 'HO12', 'HO22'),
                                   2: ('HO11', 'HO21', 'HO22'), 3: ('HO11', 'HO12', 'HO21')},
                           'CTR': {4: ('HO11', 'HO12', 'HO21', 'HO22')}},
}
