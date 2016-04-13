second_table = LOAD 'my_match_history.json' 
    USING JsonLoader(
    barracks_status_dire: string,
 	match_id: long, radiant_win: string ,
  	barracks_status_radiant': int,
   	cluster': int,
    first_blood_time': int,
     dire_score': int,
      duration': int,
       game_mode': int,
        lobby_type': int,
         tower_status_dire': int,
          leagueid': int, 
          engine': int,
           radiant_score': int,
           human_players': int,
            start_time': int,
             match_seq_num': long,
              tower_status_radiant': int,
              negative_votes': int, 
              positive_votes': int,
              players': [{gold_spent': int, gold': int, deaths': int, hero_damage': int, last_hits': int, player_slot': int, denies': int, tower_damage': int, hero_id': int, xp_per_min': int, account_id': int, kills': int, leaver_status': int, hero_healing': int, assists': int, gold_per_min': int, level': int, item_4': int, item_5': int, item_2': int, item_3': int, item_0': int, item_1': int}],
                 flags': int}});

dump second_table;






