import pandas as pd
R = R = '/Volumes/bootcamp/default/raw_2025_26/'
path = 'matches_2025_26.parquet'

m = pd.read_parquet(R + path)





# 1. Analiza rezultata utakmica

    # 1.1 Pronaći sve utakmice u kojima su oba tima postigla bar po jedan gol.

        # len(m.loc[(m['home_goals'] > 0) & m['away_goals'] > 0])
        m.loc[(m['home_goals'] > 0) & m['away_goals'] > 0][['match_id', 'home_team', 'home_goals','away_team', 'away_goals']]

        # Imamo 127 utakmica u kojima su obe ekipe zatresle mrežu protivnika



    # 1.2.Pronaći sve utakmice u kojima je domaćin pobedio sa tačno jednim golom razlike.

        # len(m.loc[(m['home_goals'] - m['away_goals']) == 1][['match_id', 'home_team', 'home_goals','away_team', 'away_goals']])
        m.loc[(m['home_goals'] - m['away_goals']) == 1][['match_id', 'home_team', 'home_goals','away_team', 'away_goals']]
        
        # Imamo 105 utakmica u kojima je domaći tim pobedio sa tačno jednim golom razlike



    # 1.3.Koliko utakmica je završeno rezultatom 0:0?

        # len(m.loc[(m['home_goals'] == 0) & (m['away_goals'] == 0)])
        m.loc[(m['home_goals'] == 0) & (m['away_goals'] == 0)]

        # Imamo 26 uktamica koje su završene rezultatom 0:0



    # 1.4.Prikazati 10 utakmica sa najviše ukupno postignutih golova.

        m['total_goals'] = m['home_goals'] + m['away_goals']
        m.nlargest(10, 'total_goals')[['match_id', 'home_team', 'home_goals','away_team', 'away_goals', 'total_goals']]





 # 2. Analiza jednog tima

    # Za tim po izboru (m['home_team'].unique() -> WFT):


    # 2.1.Prikazati sve utakmice u kojima je učestvovao.

        mp = m.loc[(m['home_team'] == 'WFT') | (m['away_team'] == 'WFT')]
        len(mp)


        # Ekipa WFT odigrala je 38 utakmica u sezoni 2025/26



    # 2.2.Koliko je puta pobedio, izgubio i odigrao nerešeno?

        mp.loc[((mp['home_team'] == 'WFT') & (mp['home_goals'] > mp['away_goals'])) | ((mp['away_team'] == 'WFT') & (mp['away_goals'] > mp['home_goals'])), 'result'] = 'WIN'
        mp.loc[mp['home_goals'] == mp['away_goals'], 'result'] = 'DRAW'
        mp.loc[((mp['home_team'] == 'WFT') & (mp['home_goals'] < mp['away_goals'])) | ((mp['away_team'] == 'WFT') & (mp['away_goals'] < mp['home_goals'])), 'result'] = 'LOSS'

        # mp['result']
        mp['result'].value_counts()

        # Ekipa WFT u sezoni 2025/26 iz meča je izašla kao pobednik na 13 utakmica,
        # isto toliko je bilo nerešenih ishoda, dok je imala jedan manje poraz, 12.



    # 2.3.Koliko je golova postigao kao domaćin, a koliko kao gost?

        mp.loc[mp['home_team'] == 'WFT', 'home_goals'].sum()
        mp.loc[mp['away_team'] == 'WFT', 'away_goals'].sum()

        # Ekipa WFT imala je bolji uspeh u utakmicama kod kuće, gde je postigla 27 golova,
        # dok je "na strani" zatresla mrežu domačina svega 18 puta.
    


    # 2.4.Pronaći utakmicu u kojoj je postigao najviše golova.

        max_ag = mp.loc[mp['away_team'] == 'WFT'].nlargest(1, 'away_goals')
        max_hg = mp.loc[mp['home_team'] == 'WFT'].nlargest(5, 'home_goals')

        pd.concat([max_hg, max_ag])[['match_id', 'home_team', 'home_goals','away_team', 'away_goals']]

        # Ekipa WFT na jednom meču postigla je najviše 3 gola
        # i taj uspeh ostvarila na čak šest susreta, 
        # pet puta kao domaćin i jednom kao gost.
    




# 3. Analiza stadiona

    # 3.1.Prikazati sve različite stadione na kojima su odigrane utakmice.

        m['stadium'].unique()
    


    # 3.2.Pronaći stadion na kojem je odigrano najviše utakmica.

        m['stadium'].value_counts().sort_values(ascending = False)

        # Deluje mi da je na svim stadionima odigrano po 19 utakmica?
    


    # 3.3.Za svaki stadion izračunati prosečnu posećenost.

        m[['stadium', 'attendance']].groupby('stadium').mean().round(2)

    

    # 3.4.Prikazati pet stadiona sa najvećom prosečnom posećenošću.

        m[['stadium', 'attendance']].groupby('stadium').mean().round(2).nlargest(5, 'attendance')