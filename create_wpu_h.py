PARFILE = ".\parameters_HeatPump.mdb"
PASSWORD = 'itho_parameters'
MDB = PARFILE
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'


import pyodbc, re
from collections import defaultdict
import slugify
# import "hand translated" StatusLabels

import handmadelabels
handmadelabels.StatusLabels[:5]

# globals

# Read from mdb file:
# WPUStatusLabels[2][:3]  Labels for firware '2' first 3 rows:
# [(0, 'T_out', 'Buitentemp', '°C', None, None),
# (1, 'T_BoilDwn', 'Boiler laag', '°C', None, None),
# (2, 'T_BoilTop', 'Boiler hoog', '°C', None, None)]
WPUStatusLabels = defaultdict(list)
# Setting labels per firmware version:
WPUSettingsLabels = defaultdict(list)
fw_versions = {} # fw_versions['datalabel'] = [2, 4, ... 34, 37, 41]

# Translated labels, to export into wpu.h
StatusLabelNames = []

#
# Read MDB
#

def get_version(s):
    x = re.findall('\d+', s)
    assert len(x) == 1
    return int(x[0])


def read_mdb(DRV=DRV, PARFILE=PARFILE, PASSWORD=PASSWORD):
    # connect to db
    conn = pyodbc.connect(f'DRIVER={DRV};DBQ={PARFILE};PWD={PASSWORD}')
    conn.setencoding("UTF-8")
    conn.setdecoding(pyodbc.SQL_CHAR, encoding="UTF-8")
    cur = conn.cursor()


    tables = []
    for table_info in cur.tables(tableType="TABLE"):
        if re.match("^(VersieBeheer|Data[Ll]abel|Parameterlijst|Handbed|Counters)", table_info.table_name):
            tables.append(table_info.table_name)
    Versies = []

    StatusLabelNames = []  # "Naam" column in DataLabel_Vxx tables StatusLabelName['T_out'] = 0
    StatusLabels = {}  # StatusLabels['T_out'] = ('Outside Temp (C)', 'outside-temp-c') 


    for table in sorted(tables):
        #print(table)
        
        if re.match("^Parameterlijst", table):
            fw_ver = get_version(table)
            cur.execute(f"select Index, Naam, Tekst_NL, Tekst_GB, Eenheid_NL, Eenheid_GB from {table}") 
            rows = cur.fetchall()
            for r in sorted(rows):
                WPUSettingsLabels[fw_ver].append((r.Index, r.Naam, r.Tekst_NL, r.Eenheid_NL, r.Tekst_GB, r.Eenheid_GB))
        if re.match("^Data[Ll]abel", table):
            fw_ver = get_version(table)
            cur.execute(f"select Index, Naam, Tekst_NL, Tekst_GB, Eenheid_NL, Eenheid_GB from {table}")
            rows = cur.fetchall()
            for r in sorted(rows):
                WPUStatusLabels[fw_ver].append((r.Index, r.Naam, r.Tekst_NL, r.Eenheid_NL, r.Tekst_GB, r.Eenheid_GB))          
        if re.match("^VersieBeheer", table):
            cur.execute(f"select VersieNummer, DataLabel, ParameterLijst, Handbed, Counters from {table}")
            rows = cur.fetchall()
            for r in sorted(rows):
                Versies.append((r.VersieNummer, r.DataLabel, r.ParameterLijst, r.Handbed, r.Counters))        
    #sorted(WPUSettingsLabels.keys()), sorted(WPUStatusLabels.keys())    
                
    DataLabels = {}
    SettingLabels = {}
    for versie in Versies:
        fw, datalabel, setting, handbed, counter = versie
        DataLabels[datalabel] = datalabel
        SettingLabels[setting] = setting

    # fw_versions is global
    fw_versions['datalabels'] = sorted([int(x) for x in DataLabels.keys()])
    fw_versions['settings'] = sorted([int(x) for x in SettingLabels.keys()])
    

#
# StatusLabels
# 
def itho_WPU_status_line(fw_ver, l):
    # const uint8_t itho_WPUstatus42[]{0, 1, 255};
    indices_str = ', '.join(str(x) for x in l)
    return f'const uint8_t itho_WPUstatus{fw_ver}[]{{{indices_str}, 255}};'


# Generate the index tables 'itho_WPUstatus' from the parameter tables
def print_itho_WPU_status_lines():
    for fw_ver in fw_versions['datalabels']:
        fw_ver = int(fw_ver)
        #print(fw_ver)
        label_list = []
        for label in WPUStatusLabels[fw_ver]:
            idx, name, _,_,_,_ = label
            #print(idx, name)
            if name not in StatusLabelNames:
                StatusLabelNames.append(name)
            list_idx = StatusLabelNames.index(name)
            label_list.append(list_idx)
        print(itho_WPU_status_line(fw_ver, label_list))


def create_lookup_table_statuslabels():
    Labels = {}

    # create lookup tabel for Statuslabels, based on most recent firmware
    for fw in fw_versions['datalabels']:
        for label in WPUStatusLabels[fw]:
            idx, name, nl_tekst, nl_unit, gb_tekst, gb_unit = label
            #print(name, gb_tekst, gb_unit)
            if gb_tekst is None:
                gb_tekst = nl_tekst
                gb_unit = nl_unit
            if gb_unit is None:
                unit = ""
            else:
                unit = " ("+gb_unit+")"
            desc = (gb_tekst+unit).capitalize()
            # create a slug. Hand generated slugs use C instead of degc for temperature units
            slug = str(slugify.slugify(desc)).replace('degc', 'c')
            Labels[name] = (desc,slug)
    return Labels


def print_ithoWPUStatusLabels(show_index=True):
    # print the StatusLabels, import the handmade translations first
    #  generate new one from tekst_gb if new

    # Lookup table 'Naam' -> ('tekst_gb', 'eenheid_gb')
    Labels = create_lookup_table_statuslabels()

    print("const struct ithoLabels ithoWPUStatusLabels[]{ \t//index".expandtabs(120))
    for idx, label in enumerate(StatusLabelNames):
        try:
            # replace with the "old" handmade translation
            desc, slug = handmadelabels.StatusLabels[idx]
        except IndexError:
            # new key/value!
            desc, slug = Labels[label]
            print('// new label: ', desc, slug)
        if show_index:
            print(f'    {{"{desc}", "{slug}"}},\t//{idx}'.expandtabs(120))
        else:
            print(f'    {{"{desc}", "{slug}"}},')
    print('    };')


#
# SettingLabels        
#




if __name__ == '__main__':
    read_mdb()
    print("//DEBUG: ", fw_versions)
    print("// diff StatusLabels against wpu.h. Only 8_9 11_17 and 18_19 are different. All keys should be the same")
    print_itho_WPU_status_lines()
    print()
    print_ithoWPUStatusLabels(show_index=False)