import pandas as pd
from tqdm import tqdm

df = pd.read_csv('all_data.csv')
print(df[:10])

columns = ("team1", "team2" , "winner", "diff_kills" , "diff_deaths","diff_assists", "diff_doublekills", "diff_triplekills",          
"diff_quadrakills","diff_pentakills"     ,          "diff_team.kpm"         ,        "diff_dragons"      ,           
"diff_heralds"         ,          "diff_barons"    ,               "diff_towers"      ,             "diff_inhibitors"  ,            
"diff_damagetochampions"    ,    "diff_dpm"            ,          "diff_damagetakenperminute"   ,  "diff_damagemitigatedperminute",
"diff_wardsplaced"     ,         "diff_wpm"         ,             "diff_wardskilled"    ,          "diff_wcpm"             ,       
"diff_controlwardsbought"  ,     "diff_visionscore"    ,          "diff_vspm"     ,                "diff_totalgold"     ,          
"diff_earnedgold"    ,           "diff_earned.gpm"           ,    "diff_gspd"       ,              "diff_minionkills"    ,         
"diff_monsterkills"   ,          "diff_monsterkillsownjungle" ,   "diff_monsterkillsenemyjungle" , "diff_cspm"        ,            
"diff_goldat10"        ,         "diff_xpat10"            ,       "diff_csat10"        ,           "diff_goldat15"    ,            
"diff_xpat15"      ,             "diff_csat15")

df_diff = pd.DataFrame(index = range(56164), columns=columns)
df_diff = df_diff.fillna('x')



for i in tqdm(range(0, 56164, 2)):
    if df.loc[i, 'result'] == 1:
        df_diff.loc[i, 'team1'] = df.loc[i, 'team']
        df_diff.loc[i, 'team2'] = df.loc[i+1, 'team']
        df_diff.loc[i, 'winner'] = df_diff.loc[i, 'team1']
        df_diff.loc[i, 'diff_kills'] = df.loc[i, 'kills'] - df.loc[i+1, 'kills']
        df_diff.loc[i, 'diff_deaths'] = df.loc[i, 'deaths'] - df.loc[i+1, 'deaths']
        df_diff.loc[i, 'diff_assists'] = df.loc[i, 'assists'] - df.loc[i+1, 'assists']
        df_diff.loc[i, 'diff_doublekills'] = df.loc[i, 'doublekills'] - df.loc[i+1, 'doublekills']
        df_diff.loc[i, 'diff_triplekills'] = df.loc[i, 'triplekills'] - df.loc[i+1, 'triplekills']
        df_diff.loc[i, 'diff_quadrakills'] = df.loc[i, 'quadrakills'] - df.loc[i+1, 'quadrakills']
        df_diff.loc[i, 'diff_pentakills'] = df.loc[i, 'pentakills'] - df.loc[i+1, 'pentakills']
        df_diff.loc[i, 'diff_team.kpm'] = df.loc[i, 'team.kpm'] - df.loc[i+1, 'team.kpm']
        df_diff.loc[i, 'diff_dragons'] = df.loc[i, 'dragons'] - df.loc[i+1, 'dragons']
        df_diff.loc[i, 'diff_heralds'] = df.loc[i, 'heralds'] - df.loc[i+1, 'heralds']
        df_diff.loc[i, 'diff_barons'] = df.loc[i, 'barons'] - df.loc[i+1, 'barons']
        df_diff.loc[i, 'diff_inhibitors'] = df.loc[i, 'inhibitors'] - df.loc[i+1, 'inhibitors']
        df_diff.loc[i, 'diff_damagetochampions'] = df.loc[i, 'damagetochampions'] - df.loc[i+1, 'damagetochampions']
        df_diff.loc[i, 'diff_dpm'] = df.loc[i, 'dpm'] - df.loc[i+1, 'dpm']
        df_diff.loc[i, 'diff_damagetakenperminute'] = df.loc[i, 'damagetakenperminute'] - df.loc[i+1, 'damagetakenperminute']
        df_diff.loc[i, 'diff_damagemitigatedperminute'] = df.loc[i, 'damagemitigatedperminute'] - df.loc[i+1, 'damagemitigatedperminute']
        df_diff.loc[i, 'diff_wardsplaced'] = df.loc[i, 'wardsplaced'] - df.loc[i+1, 'wardsplaced']
        df_diff.loc[i, 'diff_wpm'] = df.loc[i, 'wpm'] - df.loc[i+1, 'wpm']
        df_diff.loc[i, 'diff_wardskilled'] = df.loc[i, 'wardskilled'] - df.loc[i+1, 'wardskilled']
        df_diff.loc[i, 'diff_wcpm'] = df.loc[i, 'wcpm'] - df.loc[i+1, 'wcpm']
        df_diff.loc[i, 'diff_controlwardsbought'] = df.loc[i, 'controlwardsbought'] - df.loc[i+1, 'controlwardsbought']
        df_diff.loc[i, 'diff_visionscore'] = df.loc[i, 'visionscore'] - df.loc[i+1, 'visionscore']
        df_diff.loc[i, 'diff_vspm'] = df.loc[i, 'vspm'] - df.loc[i+1, 'vspm']
        df_diff.loc[i, 'diff_totalgold'] = df.loc[i, 'totalgold'] - df.loc[i+1, 'totalgold']
        df_diff.loc[i, 'diff_earnedgold'] = df.loc[i, 'earnedgold'] - df.loc[i+1, 'earnedgold']
        df_diff.loc[i, 'diff_earned.gpm'] = df.loc[i, 'earned.gpm'] - df.loc[i+1, 'earned.gpm']
        df_diff.loc[i, 'diff_gspd'] = df.loc[i, 'gspd'] - df.loc[i+1, 'gspd']
        df_diff.loc[i, 'diff_minionkills'] = df.loc[i, 'minionkills'] - df.loc[i+1, 'minionkills']
        df_diff.loc[i, 'diff_monsterkills'] = df.loc[i, 'monsterkills'] - df.loc[i+1, 'monsterkills']
        df_diff.loc[i, 'diff_monsterkillsownjungle'] = df.loc[i, 'monsterkillsownjungle'] - df.loc[i+1, 'monsterkillsownjungle']
        df_diff.loc[i, 'diff_monsterkillsenemyjungle'] = df.loc[i, 'monsterkillsenemyjungle'] - df.loc[i+1, 'monsterkillsenemyjungle']
        df_diff.loc[i, 'diff_cspm'] = df.loc[i, 'cspm'] - df.loc[i+1, 'cspm']
        df_diff.loc[i, 'diff_goldat10'] = df.loc[i, 'goldat10'] - df.loc[i+1, 'goldat10']
        df_diff.loc[i, 'diff_xpat10'] = df.loc[i, 'xpat10'] - df.loc[i+1, 'xpat10']
        df_diff.loc[i, 'diff_csat10'] = df.loc[i, 'csat10'] - df.loc[i+1, 'csat10']
        df_diff.loc[i, 'diff_goldat15'] = df.loc[i, 'goldat15'] - df.loc[i+1, 'goldat15']
        df_diff.loc[i, 'diff_xpat15'] = df.loc[i, 'xpat15'] - df.loc[i+1, 'xpat15']
        df_diff.loc[i, 'diff_csat15'] = df.loc[i, 'csat15'] - df.loc[i+1, 'csat15']

    else:
        df_diff.loc[i, 'team1'] = df.loc[i+1, 'team']
        df_diff.loc[i, 'team2'] = df.loc[i,'team']
        df_diff.loc[i, 'winner'] = df_diff.loc[i, 'team1']
        df_diff.loc[i, 'diff_kills'] = df.loc[i+1, 'kills'] - df.loc[i, 'kills']
        df_diff.loc[i, 'diff_deaths'] = df.loc[i+1, 'deaths'] - df.loc[i, 'deaths']
        df_diff.loc[i, 'diff_assists'] = df.loc[i+1, 'assists'] - df.loc[i, 'assists']
        df_diff.loc[i, 'diff_doublekills'] = df.loc[i+1, 'doublekills'] - df.loc[i, 'doublekills']
        df_diff.loc[i, 'diff_triplekills'] = df.loc[i+1, 'triplekills'] - df.loc[i, 'triplekills']
        df_diff.loc[i, 'diff_quadrakills'] = df.loc[i+1, 'quadrakills'] - df.loc[i, 'quadrakills']
        df_diff.loc[i, 'diff_pentakills'] = df.loc[i+1, 'pentakills'] - df.loc[i, 'pentakills']
        df_diff.loc[i, 'diff_team.kpm'] = df.loc[i+1, 'team.kpm'] - df.loc[i, 'team.kpm']
        df_diff.loc[i, 'diff_dragons'] = df.loc[i+1, 'dragons'] - df.loc[i, 'dragons']
        df_diff.loc[i, 'diff_heralds'] = df.loc[i+1, 'heralds'] - df.loc[i, 'heralds']
        df_diff.loc[i, 'diff_barons'] = df.loc[i+1, 'barons'] - df.loc[i, 'barons']
        df_diff.loc[i, 'diff_inhibitors'] = df.loc[i+1, 'inhibitors'] - df.loc[i, 'inhibitors']
        df_diff.loc[i, 'diff_damagetochampions'] = df.loc[i+1, 'damagetochampions'] - df.loc[i, 'damagetochampions']
        df_diff.loc[i, 'diff_dpm'] = df.loc[i+1, 'dpm'] - df.loc[i+1, 'dpm']
        df_diff.loc[i, 'diff_damagetakenperminute'] = df.loc[i+1, 'damagetakenperminute'] - df.loc[i, 'damagetakenperminute']
        df_diff.loc[i, 'diff_damagemitigatedperminute'] = df.loc[i+1, 'damagemitigatedperminute'] - df.loc[i, 'damagemitigatedperminute']
        df_diff.loc[i, 'diff_wardsplaced'] = df.loc[i+1, 'wardsplaced'] - df.loc[i, 'wardsplaced']
        df_diff.loc[i, 'diff_wpm'] = df.loc[i+1, 'wpm'] - df.loc[i, 'wpm']
        df_diff.loc[i, 'diff_wardskilled'] = df.loc[i+1, 'wardskilled'] - df.loc[i, 'wardskilled']
        df_diff.loc[i, 'diff_wcpm'] = df.loc[i+1, 'wcpm'] - df.loc[i, 'wcpm']
        df_diff.loc[i, 'diff_controlwardsbought'] = df.loc[i+1, 'controlwardsbought'] - df.loc[i, 'controlwardsbought']
        df_diff.loc[i, 'diff_visionscore'] = df.loc[i+1, 'visionscore'] - df.loc[i, 'visionscore']
        df_diff.loc[i, 'diff_vspm'] = df.loc[i+1, 'vspm'] - df.loc[i, 'vspm']
        df_diff.loc[i, 'diff_totalgold'] = df.loc[i+1, 'totalgold'] - df.loc[i, 'totalgold']
        df_diff.loc[i, 'diff_earnedgold'] = df.loc[i+1, 'earnedgold'] - df.loc[i, 'earnedgold']
        df_diff.loc[i, 'diff_earned.gpm'] = df.loc[i+1, 'earned.gpm'] - df.loc[i, 'earned.gpm']
        df_diff.loc[i, 'diff_gspd'] = df.loc[i+1, 'gspd'] - df.loc[i+1, 'gspd']
        df_diff.loc[i, 'diff_minionkills'] = df.loc[i+1, 'minionkills'] - df.loc[i, 'minionkills']
        df_diff.loc[i, 'diff_monsterkills'] = df.loc[i+1, 'monsterkills'] - df.loc[i, 'monsterkills']
        df_diff.loc[i, 'diff_monsterkillsownjungle'] = df.loc[i+1, 'monsterkillsownjungle'] - df.loc[i, 'monsterkillsownjungle']
        df_diff.loc[i, 'diff_monsterkillsenemyjungle'] = df.loc[i+1, 'monsterkillsenemyjungle'] - df.loc[i, 'monsterkillsenemyjungle']
        df_diff.loc[i, 'diff_cspm'] = df.loc[i+1, 'cspm'] - df.loc[i, 'cspm']
        df_diff.loc[i, 'diff_goldat10'] = df.loc[i+1, 'goldat10'] - df.loc[i, 'goldat10']
        df_diff.loc[i, 'diff_xpat10'] = df.loc[i+1, 'xpat10'] - df.loc[i, 'xpat10']
        df_diff.loc[i, 'diff_csat10'] = df.loc[i+1, 'csat10'] - df.loc[i, 'csat10']
        df_diff.loc[i, 'diff_goldat15'] = df.loc[i+1, 'goldat15'] - df.loc[i, 'goldat15']
        df_diff.loc[i, 'diff_xpat15'] = df.loc[i+1, 'xpat15'] - df.loc[i, 'xpat15']
        df_diff.loc[i, 'diff_csat15'] = df.loc[i+1, 'csat15'] - df.loc[i, 'csat15']

indexnames = df_diff[df_diff['team1'] == 'x'].index
print(indexnames)
df_diff = df_diff.drop(indexnames)
df_diff = df_diff.reset_index(drop = True)


df_diff.to_csv(r'data.csv')