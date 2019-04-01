import config

def new_pdb_line(aID, aname, resname, resnumb, x, y, z):
    pdb_format = "ATOM  {:5d} {:4s} {:4s} {:4d}    {:8.3f}{:8.3f}{:8.3f}\n"
    return pdb_format.format(aID, aname, resname, resnumb, x, y, z)


def new_pqr_line(aID, aname, resname, resnumb, x, y, z, charge, radius):
    pdb_format = "ATOM  {:5d} {:4s} {:4s} {:4d}    {:8.3f}{:8.3f}{:8.3f}{:8.3f}{:8.3f}\n"
    return pdb_format.format(aID, aname, resname, resnumb, x, y, z, charge, radius)

def new_gro_line(aID, aname, resname, resnumb, x, y, z):
    gro_format = '{:5}{:5}{:>5}{:5}{:8.3f}{:8.3f}{:8.3f}\n'
    return gro_format.format(resnumb, resname, aname, aID, x, y, z)


def read_pqr_line(line):
    aname   = line[12:16].strip()
    anumb   = int(line[7:11].strip())
    resname = line[17:21].strip()
    resnumb = int(line[23:26])
    x       = float(line[30:38])
    y       = float(line[38:46])
    z       = float(line[46:54])
    charge  = float(line[54:62])
    radius  = float(line[62:70])
    return (aname, anumb, resname, resnumb, x, y, z,
            charge, radius)

def read_pdb_line(line):
    aname   = line[12:16].strip()
    anumb   = int(line[7:11].strip())
    resname = line[17:21].strip()
    chain   = line[21]
    resnumb = int(line[23:26])
    x       = float(line[30:38])
    y       = float(line[38:46])
    z       = float(line[46:54])
    return (aname, anumb, resname, chain, resnumb, x, y, z)

def read_gro_line(line):
    resnumb = int(line[:5].strip())
    resname = line[5:10].strip()
    aname   = line[10:15].strip()
    anumb   = int(line[15:20].strip())
    x = float(line[20:28].strip())
    y = float(line[28:36].strip())
    z = float(line[36:44].strip())
    return (aname, anumb, resname, resnumb, x, y, z)



def pqr2gro(filename_in, filename_out, box, sites, termini):
    """
    Returns
      - aposition (int) of last atom id in filename_out
    """
    NTR_numb = termini.keys()[0]
    NTR_atoms = termini[NTR_numb]
    CTR_numb = termini.keys()[0]
    CTR_atoms = termini[CTR_numb]


    header = 'CREATED within PyPka\n'
    new_pdb_text = ''
    aposition = 0

    sites_pos = sites.keys()
    with open(filename_in) as f:
        for line in f:
            (aname, anumb, resname, resnumb, x, y,
             z, charge, radius) = read_pqr_line(line)
            aposition += 1

            if resnumb in sites_pos:
                if ((resnumb == NTR_numb and
                     aname in NTR_atoms) or
                    (resnumb == CTR_numb and
                     aname in CTR_atoms)):
                    site_numb = resnumb
                    resname = sites[site_numb]

            elif resname == 'HIS' and aname == 'HD1':
                aposition -= 1
                continue

            x /= 10.0
            y /= 10.0
            z /= 10.0
            new_pdb_text += new_gro_line(aposition, aname, resname,
                                         resnumb, x, y, z)

    header += '{0}\n'.format(aposition)
    footer = '{0:10.5f}{1:10.5f}{2:10.5f}\n'.format(box[0] / 10.0,
                                                    box[1] / 10.0,
                                                    box[2] / 10.0)

    new_pdb = header + new_pdb_text + footer
    with open(filename_out, 'w') as f_new:
        f_new.write(new_pdb)

    return aposition


def correct_names(sites_numbs, resnumb, resname, aname, termini, titrating_sites):
    def change_aname(aname, restype, mode='regular'):
        if mode == 'titrating':
            not_correct_names = correct_atoms_sites_table[restype].keys()
        else:
            not_correct_names = correct_atoms_table[restype].keys()
        for not_corrected in not_correct_names:            
            if aname == not_corrected:
                if mode == 'titrating':
                    aname = correct_atoms_sites_table[restype][not_corrected]
                else:
                    aname = correct_atoms_table[restype][not_corrected]

        return aname
    NTR_numb = termini.keys()[0]
    CTR_numb = termini.keys()[1]

    correct_atoms_table = {'CTR': {'O': 'O1',
                                   'OXT': 'O2'},
                           'NTR': {'H': 'H1'},
                           'ILE': {'CD1': 'CD'}}

    correct_atoms_sites_table = {'CYS': {'HG': 'HG1'},
                                 'SER': {'HG': 'HG1'},
                                 'TYR': {'HH': 'HH1'}}

    correct_residues_table = {'HSD': 'HI0',
                              'HSE': 'HI1',
                              'HSP': 'HS2',
                              'ARGN': 'AR0',
                              'ASPH': 'AS0',
                              'CYS2': 'CYS',
                              'CYSH': 'CY0',
                              'GLUH': 'GL0',
                              'HISD': 'HI0',
                              'HISE': 'HI1',
                              'HISH': 'HI2',
                              'HISA': 'HI0',
                              'HISB': 'HI1',
                              'HISP': 'HI2',
                              'LYSH': 'LY3',
                              'LYSN': 'LY0'}

    if resnumb == CTR_numb:
        restype = 'CTR'
        aname = change_aname(aname, restype)

    if resnumb == NTR_numb:
        restype = 'NTR'
        aname = change_aname(aname, restype)

    if resname in correct_atoms_table.keys():
        aname = change_aname(aname, resname)

    if resname in correct_residues_table.keys():
        resname = correct_residues_table[resname]

    if resnumb in titrating_sites and \
       resname in correct_atoms_sites_table.keys():
        aname = change_aname(aname, resname, mode='titrating')


    return aname, resname


def readPBPFile(f_dat):
    with open(f_dat) as f:
        for line in f:
            if line[0] != "#" and len(line) > 1:
                parts = line.strip().split('=')
                param = parts[0].split()[-1]
                value = parts[1].replace('"', '').replace("'", '')
                config.params[param] = value.strip()


def convertTermini(site_numb):
    if site_numb >= config.terminal_offset:
        return site_numb - config.terminal_offset
    return site_numb