"""
File: variables.py
Description: contains features to include in our models.
"""

control_variables = [
    # census households variables
    # 'S_instcement', # should not include this one
    'S_instsanita',
    'S_restsanita',
    'S_constceili',
    'S_restowalls',
    'S_improveany',
    'S_logrent',
    'S_logsell',

    'C_blocksdirtfloor',
    'C_HHdirtfloor',
    'C_child05',
    'C_households',
    'C_people',
    'C_rooms',
    'C_HHpersons',
    # 'C_waterland',
    # 'C_waterhouse',
    'C_waterbath',
    'C_gasheater',
    'C_refrigerator',
    'C_washing',
    'C_telephone',
    'C_vehicle',
    'C_overcrowding',
    'C_poverty',
    'C_illiterate',
    'C_dropouts515',
    'C_employment',
    'C_earnincome',

    # model covariates
    # model 2
    'S_HHpeople',
    'S_headage',
    'S_spouseage',
    'S_headeduc',
    'S_spouseeduc',

    'S_dem1',
    'S_dem2',
    'S_dem3',
    'S_dem4',
    'S_dem5',
    'S_dem6',
    'S_dem7',
    'S_dem8',

    'S_waterland',
    'S_waterhouse',
    'S_electricity',
    'S_hasanimals',
    'S_animalsinside',
    'S_garbage',
    'S_washhands',

    # model 3
    'S_cashtransfers',
    'S_milkprogram',
    'S_foodprogram',
    'S_seguropopular',
]

table_4_outcomes = [
'S_shcementfloor',
'S_cementfloorkit',
'S_cementfloordin',
'S_cementfloorbat',
'S_cementfloorbed',
]

table_6_outcomes = [
'S_satisfloor',
'S_satishouse',
'S_satislife',
'S_cesds',
'S_pss',
]

