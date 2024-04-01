#PRODUCT = 'WPU' 
PRODUCT = 'Autotemp'
DATABASE = f".\{PRODUCT}.sqlite"


import sqlite3
from collections import defaultdict
import re, slugify


# import "hand translated" StatusLabels
import handmadelabels


# globals

# Read from sqlite file:
# StatusLabels[2][:3]  Labels for firware '2' first 3 rows:
# [(0, 'T_out', 'Buitentemp', '°C', None, None),
# (1, 'T_BoilDwn', 'Boiler laag', '°C', None, None),
# (2, 'T_BoilTop', 'Boiler hoog', '°C', None, None)]
StatusLabels = defaultdict(list)
# Setting labels per firmware version:
SettingsLabels = defaultdict(list)
fw_versions = {} # fw_versions['datalabel'] = [2, 4, ... 34, 37, 41]

# Translated labels, to export into wpu.h
StatusLabelNames = []
SettingLabelNames = []

#
# Read MDB
#

def get_version(s):
    x = re.findall('\d+', s)
    assert len(x) == 1
    return int(x[0])


def read_db(DATABASE=DATABASE):
    # connect to db
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # index by column name
    cur = conn.cursor()

    tables = []
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';");
    for table_info in cur.fetchall():
        if re.match("^(VersieBeheer|Data[Ll]abel|Parameterlijst)", table_info[0]):
            tables.append(table_info[0])
   
    Versies = []
    for table in sorted(tables):
        #print(table)
        
        if re.match("^Parameterlijst", table):
            fw_ver = get_version(table)
            cur.execute(f"SELECT `Index`, `Naam`, `Tekst_NL`, `Tekst_GB`, `Eenheid_NL`, `Eenheid_GB` FROM {table}") 
            rows = cur.fetchall()
            for r in rows:
                if r['Tekst_NL'] is not None: # skip empty line
                    SettingsLabels[fw_ver].append((r['Index'], r['Naam'], r['Tekst_NL'], r['Eenheid_NL'], r['Tekst_GB'], r['Eenheid_GB']))
            SettingsLabels[fw_ver].sort()         
        if re.match("^Data[Ll]abel", table):
            fw_ver = get_version(table)
            cur.execute(f"SELECT `Index`, `Naam`, `Tekst_NL`, `Tekst_GB`, `Eenheid_NL`, `Eenheid_GB` FROM {table}") 
            rows = cur.fetchall()
            for r in rows:
                StatusLabels[fw_ver].append((r['Index'], r['Naam'], r['Tekst_NL'], r['Eenheid_NL'], r['Tekst_GB'], r['Eenheid_GB']))
            StatusLabels[fw_ver].sort()
        if re.match("^VersieBeheer", table):
            cur.execute(f"SELECT `VersieNummer`, `DataLabel`, `ParameterLijst` FROM {table}")
            rows = cur.fetchall()
            for r in rows:
                Versies.append((r['VersieNummer'], r['DataLabel'], r['ParameterLijst']))      
                
    DataLabels = {}
    SettingLabels = {}
    Hardware = []
    if len(Versies) == 0:
        # geen Versies tabel
        #print('// NO VERSION INFORMATION FOUND !!!')
        for versie in sorted(StatusLabels.keys()):
            Versies.append((versie, versie, versie))

    for versie in Versies:
        fw, datalabel, setting = versie
        DataLabels[int(fw)] = int(datalabel)
        SettingLabels[int(fw)] = int(setting)
        Hardware.append(int(fw))

    # fw_versions is global
    fw_versions['datalabels'] = sorted(set([int(x) for x in DataLabels.values()]))  # unique
    fw_versions['settings'] = sorted(set([int(x) for x in SettingLabels.keys()]))  
    fw_versions['fw_vs_datalabels'] = DataLabels
    fw_versions['fw_vs_settinglabels'] = SettingLabels
    fw_versions['hardware'] = sorted(Hardware)
   

def ithowifi_slugify(s):
    return str(slugify.slugify(s)).replace('degc', 'c').replace('/', '_')
    

#
# StatusLabels
# 
def itho_status_line(fw_ver, l):
    # const uint8_t itho_WPUstatus42[]{0, 1, 255};
    indices_str = ', '.join(str(x) for x in l)
    return f'const uint8_t itho_{PRODUCT}status{fw_ver}[]{{{indices_str}, 255}};'


# Generate the index tables 'itho_WPUstatus' from the parameter tables
def print_itho_status_lines():
    # print: ... const uint8_t itho_WPUstatusxx[]{0, 1, ..., 255};
    for fw_ver in fw_versions['datalabels']:
        fw_ver = int(fw_ver)
        #print(fw_ver)
        label_list = []
        for label in StatusLabels[fw_ver]:
            idx, name, _,_,_,_ = label
            #print(idx, name)
            if name not in StatusLabelNames:
                StatusLabelNames.append(name)
            list_idx = StatusLabelNames.index(name)
            label_list.append(list_idx)
        print(itho_status_line(fw_ver, label_list))


def create_lookup_table_statuslabels():
    Labels = {}

    # create lookup tabel for Statuslabels, based on most recent firmware
    for fw in fw_versions['datalabels']:
        for label in StatusLabels[fw]:
            idx, name, nl_tekst, nl_unit, gb_tekst, gb_unit = label
            #print(name, gb_tekst, gb_unit)
            if gb_tekst is None:
                gb_tekst = nl_tekst
                gb_unit = nl_unit
            if gb_unit is None:
                unit = ""
            else:
                unit = " ("+gb_unit+")"
            desc = gb_tekst.capitalize()
            desc += unit
            # create a slug. Hand generated slugs use C instead of degc for temperature units
            slug = ithowifi_slugify(desc)
            Labels[name] = (desc.replace('/', '_'), slug)
    return Labels


def print_ithoStatusLabels(show_index=True):
    # print the StatusLabels, import the handmade translations first
    #  generate new one from tekst_gb if new

    # Lookup table 'Naam' -> ('tekst_gb', 'eenheid_gb')
    Labels = create_lookup_table_statuslabels()

    print(f"const struct ithoLabels itho{PRODUCT}StatusLabels[]{{")
    for idx, label in enumerate(StatusLabelNames):
        try:
            # replace with the "old" handmade translation
            desc, slug = handmadelabels.StatusLabels[PRODUCT][idx]
        except IndexError:
            # new key/value!
            desc, slug = Labels[label]
            #print('// new label: ', desc, slug)
        if show_index:
            print(f'    {{"{desc}", "{slug}"}},\t//{idx}'.expandtabs(120))
        else:
            print(f'    {{"{desc}", "{slug}"}},')
    print('    };')



def print_status_map():
    max_fw = max(fw_versions['datalabels'])
    r = f'const uint8_t *itho{PRODUCT}StatusMap[] = {{' 
    for idx in range(max_fw+1):
        r += f"itho_{PRODUCT}status{fw_versions['fw_vs_datalabels'][idx]}, " if idx in fw_versions['hardware'] else 'nullptr, '
    print(r+'};')


#
# SettingLabels        
#
def itho_setting_line(fw_ver, l):
    indices = ', '.join(str(x) for x in l)
    return f'const uint16_t itho_{PRODUCT}setting{fw_ver}[]{{{indices}, 999}};'

def print_itho_settings_lines():
    for fw_ver in fw_versions['settings']:
        fw_ver = int(fw_ver)
        #print(fw_ver)
        label_list = []
        for label in SettingsLabels[fw_ver]:
            idx, name, _, _, _, _ = label
            #print(idx, name)
            if name not in SettingLabelNames:
                SettingLabelNames.append(name)
            list_idx = SettingLabelNames.index(name)
            label_list.append(list_idx)
        print(itho_setting_line(fw_ver, label_list))


def create_lookup_table_settings():
    Labels = {}

    # create lookup tabel for Statuslabels, based on most recent firmware
    for fw in fw_versions['settings']:
        for label in SettingsLabels[fw]:
            idx, name, nl_tekst, nl_unit, gb_tekst, gb_unit = label
            #print(name, gb_tekst, gb_unit)
            if gb_tekst is None:
                gb_tekst = nl_tekst
                gb_unit = nl_unit
            if gb_unit is None:
                unit = ""
            else:
                unit = " ("+gb_unit+")"
            desc = gb_tekst.capitalize()
            desc += unit
            Labels[name] = desc.replace('/', '_')
    return Labels


def print_ithoSettingLabels(show_index=False):
    
    Labels = create_lookup_table_settings()
    print(f"const char *itho{PRODUCT}SettingsLabels[] = {{")
    for idx,label in enumerate(SettingLabelNames):
        desc = Labels[label]
        if show_index:
            print(f"    \"{desc}\",\t//{idx}".expandtabs(70))
        else:
            print(f"    \"{desc}\",")
    print('    };')


def print_settings_map():
    max_fw = max(fw_versions['settings'])
    r = f'const uint16_t *itho{PRODUCT}SettingsMap[] = {{' 
    for idx in range(max_fw+1):
        r += f"itho_{PRODUCT}setting{fw_versions['fw_vs_settinglabels'][idx]}, " if idx in fw_versions['hardware'] else 'nullptr, '
    print(r+'};')

if __name__ == '__main__':
    print("// Product: ", PRODUCT)
    read_db()
    print_itho_settings_lines()
    print()
    print_ithoSettingLabels(show_index=True)
    print()
    print_itho_status_lines()
    print()
    print_ithoStatusLabels(show_index=True)
    print()
    print_settings_map()
    print()
    print_status_map()

