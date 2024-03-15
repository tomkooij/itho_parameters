PRODUCT = 'WPU' 
DATABASE = f".\{PRODUCT}.mdb"

try:
    from password import PASSWORD
except ImportError:
    print('Please fill in the password in password.py')
    PASSWORD = 'foobar'

# Win32 specific?
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'


import pyodbc, re
from collections import defaultdict
import slugify


# import "hand translated" StatusLabels
import handmadelabels


# globals

# Read from mdb file:
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


def read_mdb(DRV=DRV, DATABASE=DATABASE, PASSWORD=PASSWORD):
    # connect to db
    conn = pyodbc.connect(f'DRIVER={DRV};DBQ={DATABASE};PWD={PASSWORD}')
    conn.setencoding("UTF-8")
    conn.setdecoding(pyodbc.SQL_CHAR, encoding="UTF-8")
    cur = conn.cursor()


    tables = []
    for table_info in cur.tables(tableType="TABLE"):
        if re.match("^(VersieBeheer|Data[Ll]abel|Parameterlijst)", table_info.table_name):
            tables.append(table_info.table_name)
    Versies = []

    for table in sorted(tables):
        #print(table)
        
        if re.match("^Parameterlijst", table):
            fw_ver = get_version(table)
            cur.execute(f"select Index, Naam, Tekst_NL, Tekst_GB, Eenheid_NL, Eenheid_GB from {table}") 
            rows = cur.fetchall()
            for r in sorted(rows):
                SettingsLabels[fw_ver].append((r.Index, r.Naam, r.Tekst_NL, r.Eenheid_NL, r.Tekst_GB, r.Eenheid_GB))
        if re.match("^Data[Ll]abel", table):
            fw_ver = get_version(table)
            cur.execute(f"select Index, Naam, Tekst_NL, Tekst_GB, Eenheid_NL, Eenheid_GB from {table}")
            rows = cur.fetchall()
            for r in sorted(rows):
                StatusLabels[fw_ver].append((r.Index, r.Naam, r.Tekst_NL, r.Eenheid_NL, r.Tekst_GB, r.Eenheid_GB))          
        if re.match("^VersieBeheer", table):
            cur.execute(f"select VersieNummer, DataLabel, ParameterLijst from {table}")
            rows = cur.fetchall()
            for r in sorted(rows):
                Versies.append((r.VersieNummer, r.DataLabel, r.ParameterLijst))        
                
    DataLabels = {}
    SettingLabels = {}
    Hardware = []

    for versie in Versies:
        fw, datalabel, setting = versie
        DataLabels[int(fw)] = int(datalabel)
        SettingLabels[int(fw)] = int(setting)
        Hardware.append(int(fw))

    # fw_versions is global
    fw_versions['datalabels'] = sorted([int(x) for x in DataLabels.values()])
    fw_versions['settings'] = sorted([int(x) for x in SettingLabels.values()])
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
    print('    }; // EDIT THIS!')



def print_status_map():
    max_fw = max(fw_versions['datalabels'])
    r = f'const uint8_t *itho{PRODUCT}StatusMap[] = {{' 
    for idx in range(max_fw+1):
        r += f"itho_{PRODUCT}status{fw_versions['fw_vs_datalabels'][idx]}, " if idx in fw_versions['hardware'] else 'nullptr, '
    print(r+'}; // EDIT THIS!')   


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
    print('    }; // EDIT THIS!')


def print_settings_map():
    max_fw = max(fw_versions['settings'])
    r = f'const uint16_t *itho{PRODUCT}SettingsMap[] = {{' 
    for idx in range(max_fw+1):
        r += f"itho_{PRODUCT}setting{fw_versions['fw_vs_settinglabels'][idx]}, " if idx in fw_versions['hardware'] else 'nullptr, '
    print(r+'}; // EDIT THIS!')   

if __name__ == '__main__':
    print("//DEBUG: ", PRODUCT)
    read_mdb()
    #print("//DEBUG: ", fw_versions)
    print_itho_settings_lines()
    print()
    print_ithoSettingLabels(show_index=True)
    print()
    print_itho_status_lines()
    print()
    print_ithoStatusLabels(show_index=False)
    print()
    print_settings_map()
    print()
    print_status_map()
