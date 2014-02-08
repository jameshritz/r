#This module is a set of dictionaries that allow the data in the files to be mapped
# and to be aggregated in more familiar or summarized ways.




# So we can create view of races strictly by age groupings

ASR = {'AOF': '2 Year Old Fillies ONLY' ,\
	   'AON': '2 Year Olds ONLY',\
	   'BOF': '3 Year Old Fillies ONLY' ,\
	   'BON': '3 Year Olds ONLY',\
	   'BUC': '3 Year Olds & Up Colts & Geldings Only',\
	   'BUM': '3 Year Old & Up Mares & Fillies',\
	   'BUN': '3 Year Old & Up',\
	   'COF': '4 Year Old Fillies Only',\
	   'CON': '4 Year Olds Only',\
	   'CUM': '4 Year Old & Up Mares',\
	   'CUN': '4 Year Olds & Up' }

# So we can create view of races strictly by gender

gender_only = {'AOF': 'Females',\
	   'AON': 'Mixed',\
	   'BOF': 'Females' ,\
	   'BON': 'Mixed',\
	   'BUC': 'Males',\
	   'BUM': 'Females',\
	   'BUN': 'Mixed',\
	   'COF': 'Females',\
	   'CON': 'Mixed',\
	   'CUM': 'Females',\
	   'CUN': 'Mixed' }



age_only = {'AOF': '2yo ONLY' ,\
	   'AON': '2yo ONLY',\
	   'BOF': '3yo ONLY' ,\
	   'BON': '3yo ONLY',\
	   'BUC': '3yo+',\
	   'BUM': '3yo+',\
	   'BUN': '3yo+',\
	   'COF': '4yo ONLY',\
	   'CON': '4yo ONLY',\
	   'CUM': '4yo+',\
	   'CUN': '4yo+' }


Dist = { 440:'2F', 1430:'6.5F', 1760:'1M',\
        1320:'6F', 1870:'1-1/16M', 1210:'5.5 F',\
        1540:'7F', 1980:'1-1/8M', 1100:'5F',\
        2200:'1-1/4M', 2640:'1-1/2M', 3080:'1-3/4M'}

# Points of Call in Miles

poc = {0:'0', 440:'1/4Mi', 330:'3/16Mi', 880:'1/2Mi', 1760:'1M',\
       660:'3/8Mi', 1320:'3/4Mi',2200:'1-1/4Mi',2640:'1-1/2Mi',\
       1100:'5/8Mi'}
       
filestructure = ['t_track','t_date','t_race','t_post position','t_entry','t_distance',\
't_surface','reserved1','t_race type','t_age/sex restrictions',\
't_race_classification','t_purse','t_claimprice','t_claiming_price_horse',\
't_track_record','t_race_conditions','t_lasix_list','t_bute_list','t_coupled_list',\
't_mutuel_list','simulcast_host_track_code','simulcast_host_track_race','t_breed_type',\
't_nasal_strip_chg','t_allweather_surface_flag','reserved26','reserved27',\
't_trainer','t_trainer_cm_sts','t_trainer_cm_wins','t_trainer_cm_places',\
't_trainer_cm_shows','t_jockey','t_apprentice_wgt_allow','t_jockey_cm_sts',\
't_jockey_cm_wins','t_jockey_cm_places','t_jockey_cm_shows','t_owner',\
'ownersilks','main_track_only_ae','reserved42','t_prog_no','t_morn_line_odds',\
'horse_name','year_of_birth','horse_foaling_month','reserved48',\
'sex','horse_color','t_weight','sire','siresire','dam','damsire',\
'breeder','bredin','t_program_post_position','reserved59','reserved60','reserved61',\
't_med_new','t_med_old','t_equip_chg','h_dst_lt_starts','h_dst_lt_wins',\
'h_dst_lt_places','h_dst_lt_shows','h_dst_lt_earnings','h_trk_lt_starts',\
'h_trk_lt_wins','h_trk_lt_places','h_trk_lt_shows','h_trk_lt_earnings',\
'h_turf_lt_starts','h_turf_lt_wins','h_turf_lt_places','h_turf_lt_shows',\
'h_turf_lt_earnings','h_wet_lt_starts','h_wet_lt_wins','h_wet_lt_places',\
'h_wet_lt_shows','h_wet_lt_earnings','cy','h_cy_lt_starts','h_cy_lt_wins',\
'h_cy_lt_places','h_cy_lt_shows','h_cy_lt_earnings','py','h_py_lt_starts',\
'h_py_lt_wins','h_py_lt_places','h_py_lt_shows','h_py_lt_earnings',\
'h_lt_starts','h_lt_wins','h_lt_places','h_lt_shows','h_lt_earnings',\
'workoutdate1','workoutdate2','workoutdate3','workoutdate4','workoutdate5',\
'workoutdate6','workoutdate7','workoutdate8','workoutdate9','workoutdate10',\
'workoutdate11','workoutdate12','worktime1','worktime2','worktime3','worktime4',\
'worktime5','worktime6','worktime7','worktime8','worktime9','worktime10',\
'worktime11','worktime12','worktrack1','worktrack2','worktrack3','worktrack4',\
'worktrack5','worktrack6','worktrack7','worktrack8','worktrack9','worktrack10',\
'worktrack11','worktrack12','workdist1','workdist2','workdist3','workdist4',\
'workdist5','workdist6','workdist7','workdist8','workdist9','workdist10',\
'workdist11','workdist12','workcon1','workcon2','workcon3','workcon4',\
'workcon5','workcon6','workcon7','workcon8','workcon9','workcon10',\
'workcon11','workcon12','workdesc1','workdesc2','workdesc3','workdesc4',\
'workdesc5','workdesc6','workdesc7','workdesc8','workdesc9','workdesc10',\
'workdesc11','workdesc12','workmt1','workmt2','workmt3','workmt4',\
'workmt5','workmt6','workmt7','workmt8','workmt9','workmt10','workmt11',\
'workmt12','workcount1','workcount2','workcount3','workcount4',\
'workcount5','workcount6','workcount7','workcount8','workcount9',\
'workcount10','workcount11','workcount12','workrank1','workrank2','workrank3',\
'workrank4','workrank5','workrank6','workrank7','workrank8','workrank9','workrank10',\
'workrank11','workrank12','run_style','quirin','reserved212','reserved213',\
'2f_pace_par','4f_pace_par','6f_pace_par','speed_par','late_pace_par',\
'tj_starts','tj_365_wins','tj_365_places','tj_365_shows','tj_365_roi',\
'dayssincelastrace','racecon1','racecon2','racecon3','racecon4','racecon5',\
'racecon6','h_aw_lt_starts','h_aw_lt_wins','h_aw_lt_places','h_aw_lt_shows',\
'h_aw_lt_earnings','h_aw_lt_bris_speed','reserved237','t_low_claiming_price',\
't_statebred_flag','wager1','wager2','wager3','wager4',\
'wager5','wager6','wager7','wager8','wager9','reserved249','reserved250',\
'bris_prime_power_rating','reserved252','reserved253','reserved254','reserved255',\
'p_rdate1','p_rdate2','p_rdate3','p_rdate4','p_date5',\
'p_rdate6','p_rdate7','p_rdate8','p_rdate9','p_rdate10',\
'dayssince1','dayssince2','dayssince3','dayssince4',\
'dayssince5','dayssince6','dayssince7','dayssince8','dayssince9','reserved275',\
'trackcode1','trackcode2','trackcode3','trackcode4','trackcode5','trackcode6',\
'trackcode7','trackcode8','trackcode9','trackcode10','bristrackcode1',\
'bristrackcode2','bristrackcode3','bristrackcode4','bristrackcode5',\
'bristrackcode6','bristrackcode7','bristrackcode8','bristrackcode9',\
'bristrackcode10','p_race1','p_race2','p_race3','p_race4','p_race5',\
'p_race6','p_race7','p_race8','p_race9','p_race10','p_tackcon1',\
'p_tackcon2','p_tackcon3','p_tackcon4','p_tackcon5','p_tackcon6',\
'p_tackcon7','p_tackcon8','p_tackcon9','p_tackcon10','p_dst1','p_dst2',\
'p_dst3','p_dst4','p_dst5','p_dst6','p_dst7','p_dst8','p_dst9','p_dst10',\
'p_surf1','p_surf2','p_surf3','p_surf4','p_surf5','p_surf6','p_surf7',\
'p_surf8','p_surf9','p_surf10','p_chute1','p_chute2','p_chute3',\
'p_chute4','p_chute5','p_chute6','p_chute7','p_chute8','p_chute9','p_chute10',\
'p_entrants1','p_entrants2','p_entrants3','p_entrants4','p_entrants5',\
'p_entrants6','p_entrants7','p_entrants8','p_entrants9','p_entrants10',\
'p_postpos1','p_postpos2','p_postpos3','p_postpos4','p_postpos5',\
'p_postpos6','p_postpos7','p_postpos8','p_postpos9','p_postpos10','p_equip1',\
'p_equip2','p_equip3','p_equip4','p_equip5','p_equip6','p_equip7','p_equip8',\
'p_equip9','p_equip10','p_racename1','p_racename2','p_racename3',\
'p_racename4','p_racename5','p_racename6','p_racename7','p_racename8',\
'p_racename9','p_racename10','p_med1','p_med2','p_med3','p_med4','p_med5',\
'p_med6','p_med7','p_med8','p_med9','p_med10','p_comment1','p_comment2',\
'p_comment3','p_comment4','p_comment5','p_comment6','p_comment7',\
'p_comment8','p_comment9','p_comment10','p_winner1','p_winner2','p_winner3',\
'p_winner4','p_winner5','p_winner6','p_winner7','p_winner8','p_winner9',\
'p_winner10','p_place1','p_place2','p_place3','p_place4','p_place5',\
'p_place6','p_place7','p_place8','p_place9','p_place10','p_show1',\
'p_show2','p_show3','p_show4','p_show5','p_show6','p_show7','p_show8',\
'p_show9','p_show10','p_win_wt1','p_win_wt2','p_win_wt3','p_win_wt4',\
'p_win_wt5','p_win_wt6','p_win_wt7','p_win_wt8','p_win_wt9',\
'p_win_wt10','p_plc_wt1','p_plc_wt2','p_plc_wt3','p_plc_wt4','p_plc_wt5',\
'p_plc_wt6','p_plc_wt7','p_plc_wt8','p_plc_wt9','p_plc_wt10','p_shw_wt1',\
'p_shw_wt2','p_shw_wt3','p_shw_wt4','p_shw_wt5','p_shw_wt6','p_shw_wt7',\
'p_shw_wt8','p_shw_wt9','p_shw_wt10','p_win_margin1','p_win_margin2',\
'p_win_margin3','p_win_margin4','p_win_margin5','p_win_margin6',\
'p_win_margin7','p_win_margin8','p_win_margin9','p_win_margin10',\
'p_plc_margin1','p_plc_margin2','p_plc_margin3','p_plc_margin4','p_plc_margin5',\
'p_plc_margin6','p_plc_margin7','p_plc_margin8','p_plc_margin9','p_plc_margin10',\
'p_shw_margin1','p_shw_margin2','p_shw_margin3','p_shw_margin4','p_shw_margin5',\
'p_shw_margin6','p_shw_margin7','p_shw_margin8','p_shw_margin9','p_shw_margin10',\
'p_extracomment1','p_extracomment2','p_extracomment3','p_extracomment4',\
'p_extracomment5','p_extracomment6','p_extracomment7','p_extracomment8',\
'p_extracomment9','p_extracomment10 ','p_wt1','p_wt2','p_wt3','p_wt4',\
'p_wt5','p_wt6','p_wt7','p_wt8','p_wt9','p_wt10','p_odds1','p_odds2',\
'p_odds3','p_odds4','p_odds5','p_odds6','p_odds7','p_odds8','p_odds9',\
'p_odds10','p_entry1','p_entry2','p_entry3','p_entry4','p_entry5',\
'p_entry6','p_entry7','p_entry8','p_entry9','p_entry10 ',\
'p_race_classification1','p_race_classification2','p_race_classification3',\
'p_race_classification4','p_race_classification5','p_race_classification6',\
'p_race_classification7','p_race_classification8','p_race_classification9',\
'p_race_classification10','p_claim_price1','p_claim_price2','p_claim_price3',\
'p_claim_price4','p_claim_price5','p_claim_price6','p_claim_price7',\
'p_claim_price8','p_claim_price9','p_claim_price10','p_purse1','p_purse2',\
'p_purse3','p_purse4','p_purse5','p_purse6','p_purse7','p_purse8',\
'p_purse9','p_purse10','p_start_call_position1','p_start_call_position2',\
'p_start_call_position3','p_start_call_position4','p_start_call_position5',\
'p_start_call_position6','p_start_call_position7','p_start_call_position8',\
'p_start_call_position9','p_start_call_position10','p_first_call_position1',\
'p_first_call_position2','p_first_call_position3','p_first_call_position4',\
'p_first_call_position5','p_first_call_position6','p_first_call_position7',\
'p_first_call_position8','p_first_call_position9','p_first_call_position10',\
'p_second_call_position1','p_second_call_position2','p_second_call_position3',\
'p_second_call_position4','p_second_call_position5','p_second_call_position6',\
'p_second_call_position7','p_second_call_position8','p_second_call_position9',\
'p_second_call_position10','p_gate_call_position1','p_gate_call_position2',\
'p_gate_call_position3','p_gate_call_position4','p_gate_call_position5',\
'p_gate_call_position6','p_gate_call_position7','p_gate_call_position8',\
'p_gate_call_position9','p_gate_call_position10','p_stretch_position1',\
'p_stretch_position2','p_stretch_position3','p_stretch_position4',\
'p_stretch_position5','p_stretch_position6','p_stretch_position7',\
'p_stretch_position8','p_stretch_position9','p_stretch_position10',\
'p_finish_position1','p_finish_position2','p_finish_position3',\
'p_finish_position4','p_finish_position5','p_finish_position6',\
'p_finish_position7','p_finish_position8','p_finish_position9',\
'p_finish_position10','p_money_position1','p_money_position2',\
'p_money_position3','p_money_position4','p_money_position5',\
'p_money_position6','p_money_position7','p_money_position8',\
'p_money_position9','p_money_position10',\
'p_start_call_btnlngths_ldr_margin1','p_start_call_btnlngths_ldr_margin2',\
'p_start_call_btnlngths_ldr_margin3','p_start_call_btnlngths_ldr_margin4',\
'p_start_call_btnlngths_ldr_margin5','p_start_call_btnlngths_ldr_margin6',\
'p_start_call_btnlngths_ldr_margin7','p_start_call_btnlngths_ldr_margin8',\
'p_start_call_btnlngths_ldr_margin9','p_start_call_btnlngths_ldr_margin10',\
'p_start_call_btnlngths_only1','p_start_call_btnlngths_only2',\
'p_start_call_btnlngths_only3','p_start_call_btnlngths_only4',\
'p_start_call_btnlngths_only5','p_start_call_btnlngths_only6',\
'p_start_call_btnlngths_only7','p_start_call_btnlngths_only8',\
'p_start_call_btnlngths_only9','p_start_call_btnlngths_only10',\
'p_first_call_btnlngths_ldr_margin1','p_first_call_btnlngths_ldr_margin2',\
'p_first_call_btnlngths_ldr_margin3','p_first_call_btnlngths_ldr_margin4',\
'p_first_call_btnlngths_ldr_margin5','p_first_call_btnlngths_ldr_margin6',\
'p_first_call_btnlngths_ldr_margin7','p_first_call_btnlngths_ldr_margin8',\
'p_first_call_btnlngths_ldr_margin9','p_first_call_btnlngths_ldr_margin10',\
'p_first_call_btnlngths_only1','p_first_call_btnlngths_only2',\
'p_first_call_btnlngths_only3','p_first_call_btnlngths_only4',\
'p_first_call_btnlngths_only5','p_first_call_btnlngths_only6',\
'p_first_call_btnlngths_only7','p_first_call_btnlngths_only8',
'p_first_call_btnlngths_only9','p_first_call_btnlngths_only10',\
'p_second_call_btnlngths_ldr_margin1 ','p_second_call_btnlngths_ldr_margin2',\
'p_second_call_btnlngths_ldr_margin3','p_second_call_btnlngths_ldr_margin4',\
'p_second_call_btnlngths_ldr_margin5','p_second_call_btnlngths_ldr_margin6',\
'p_second_call_btnlngths_ldr_margin7','p_second_call_btnlngths_ldr_margin8',\
'p_second_call_btnlngths_ldr_margin9','p_second_call_btnlngths_ldr_margin10',\
'p_second_call_btnlngths_only1','p_second_call_btnlngths_only2',\
'p_second_call_btnlngths_only3','p_second_call_btnlngths_only4',\
'p_second_call_btnlngths_only5','p_second_call_btnlngths_only6',\
'p_second_call_btnlngths_only7','p_second_call_btnlngths_only8',\
'p_second_call_btnlngths_only9','p_second_call_btnlngths_only10',\
'p_bris_race_shape_first_call1','p_bris_race_shape_first_call2',\
'p_bris_race_shape_first_call3','p_bris_race_shape_first_call4',\
'p_bris_race_shape_first_call5','p_bris_race_shape_first_call6',\
'p_bris_race_shape_first_call7','p_bris_race_shape_first_call8',\
'p_bris_race_shape_first_call9','p_bris_race_shape_first_call10','reserved706',\
'reserved707','reserved708','reserved709','reserved710','reserved711',\
'reserved712','reserved713','reserved714','reserved715',\
'p_stretch_btnlngthsldr_margin1','p_stretch_btnlngthsldr_margin2',\
'p_stretch_btnlngthsldr_margin3','p_stretch_btnlngthsldr_margin4',\
'p_stretch_btnlngthsldr_margin5','p_stretch_btnlngthsldr_margin6',\
'p_stretch_btnlngthsldr_margin7','p_stretch_btnlngthsldr_margin8',\
'p_stretch_btnlngthsldr_margin9','p_stretch_btnlngthsldr_margin10',\
'p_stretch_btnlngths_only1','p_stretch_btnlngths_only2',\
'p_stretch_btnlngths_only3','p_stretch_btnlngths_only4',\
'p_stretch_btnlngths_only5','p_stretch_btnlngths_only6','p_stretch_btnlngths_only7',\
'p_stretch_btnlngths_only8','p_stretch_btnlngths_only9','p_stretch_btnlngths_only10',\
'p_finish_btnlngthswnrs_margin1','p_finish_btnlngthswnrs_margin2',\
'p_finish_btnlngthswnrs_margin3','p_finish_btnlngthswnrs_margin4',\
'p_finish_btnlngthswnrs_margin5','p_finish_btnlngthswnrs_margin6',\
'p_finish_btnlngthswnrs_margin7','p_finish_btnlngthswnrs_margin8',\
'p_finish_btnlngthswnrs_margin9','p_finish_btnlngthswnrs_margin10',\
'p_finish_btnlngths_only1','p_finish_btnlngths_only2','p_finish_btnlngths_only3',\
'p_finish_btnlngths_only4','p_finish_btnlngths_only5','p_finish_btnlngths_only6',\
'p_finish_btnlngths_only7','p_finish_btnlngths_only8','p_finish_btnlngths_only9',\
'p_finish_btnlngths_only10','p_bris_race_shape_second_call1',\
'p_bris_race_shape_second_call2','p_bris_race_shape_second_call3',\
'p_bris_race_shape_second_call4','p_bris_race_shape_second_call5',\
'p_bris_race_shape_second_call6','p_bris_race_shape_second_call7',\
'p_bris_race_shape_second_call8','p_bris_race_shape_second_call9',\
'p_bris_race_shape_second_call10','p_bris_2f_pace_fig1','p_bris_2f_pace_fig2',\
'p_bris_2f_pace_fig3','p_bris_2f_pace_fig4','p_bris_2f_pace_fig5',\
'p_bris_2f_pace_fig6','p_bris_2f_pace_fig7','p_bris_2f_pace_fig8',\
'p_bris_2f_pace_fig9','p_bris_2f_pace_fig10','p_bris_4f_pace_fig1',\
'p_bris_4f_pace_fig2','p_bris_4f_pace_fig3','p_bris_4f_pace_fig4',\
'p_bris_4f_pace_fig5','p_bris_4f_pace_fig6','p_bris_4f_pace_fig7',\
'p_bris_4f_pace_fig8','p_bris_4f_pace_fig9','p_bris_4f_pace_fig10',\
'p_bris_6f_pace_fig1','p_bris_6f_pace_fig2','p_bris_6f_pace_fig3',\
'p_bris_6f_pace_fig4','p_bris_6f_pace_fig5','p_bris_6f_pace_fig6',\
'p_bris_6f_pace_fig7','p_bris_6f_pace_fig8','p_bris_6f_pace_fig9',\
'p_bris_6f_pace_fig10','p_bris_8f_pace_fig1','p_bris_8f_pace_fig2',\
'p_bris_8f_pace_fig3','p_bris_8f_pace_fig4','p_bris_8f_pace_fig5',\
'p_bris_8f_pace_fig6','p_bris_8f_pace_fig7','p_bris_8f_pace_fig8',\
'p_bris_8f_pace_fig9','p_bris_8f_pace_fig10','p_bris_10f_pace_fig1',\
'p_bris_10f_pace_fig2','p_bris_10f_pace_fig3','p_bris_10f_pace_fig4',\
'p_bris_10f_pace_fig5','p_bris_10f_pace_fig6','p_bris_10f_pace_fig7',\
'p_bris_10f_pace_fig8','p_bris_10f_pace_fig9','p_bris_10f_pace_fig10',\
'p_bris_late_pace_fig1','p_bris_late_pace_fig2','p_bris_late_pace_fig3',\
'p_bris_late_pace_fig4','p_bris_late_pace_fig5','p_bris_late_pace_fig6',\
'p_bris_late_pace_fig7','p_bris_late_pace_fig8','p_bris_late_pace_fig9',\
'p_bris_late_pace_fig10','reserved826','reserved827','reserved828',\
'reserved829','reserved830','reserved831','reserved832','reserved833',\
'reserved834','reserved835','reserved836','reserved837','reserved838',\
'reserved839','reserved840','reserved841','reserved842','reserved843',\
'reserved844','reserved845','p_bris_speed_rating1','p_bris_speed_rating2',\
'p_bris_speed_rating3','p_bris_speed_rating4','p_bris_speed_rating5',\
'p_bris_speed_rating6','p_bris_speed_rating7','p_bris_speed_rating8',\
'p_bris_speed_rating9','p_bris_speed_rating10','p_speed_rating1',\
'p_speed_rating2','p_speed_rating3','p_speed_rating4','p_speed_rating5',\
'p_speed_rating6','p_speed_rating7','p_speed_rating8','p_speed_rating9',\
'p_speed_rating10','p_track_variant1','p_track_variant2',\
'p_track_variant3','p_track_variant4','p_track_variant5','p_track_variant6',\
'p_track_variant7','p_track_variant8','p_track_variant9','p_track_variant10',\
'p_2f_fraction1','p_2f_fraction2','p_2f_fraction3','p_2f_fraction4',\
'p_2f_fraction5','p_2f_fraction6','p_2f_fraction7','p_2f_fraction8',\
'p_2f_fraction9','p_2f_fraction10','p_3f_fraction1','p_3f_fraction2',\
'p_3f_fraction3','p_3f_fraction4','p_3f_fraction5','p_3f_fraction6',\
'p_3f_fraction7','p_3f_fraction8','p_3f_fraction9','p_3f_fraction10',\
'p_4f_fraction1','p_4f_fraction2','p_4f_fraction3','p_4f_fraction4',\
'p_4f_fraction5','p_4f_fraction6','p_4f_fraction7','p_4f_fraction8',\
'p_4f_fraction9','p_4f_fraction10','p_5f_fraction1','p_5f_fraction2',\
'p_5f_fraction3','p_5f_fraction4','p_5f_fraction5','p_5f_fraction6',\
'p_5f_fraction7','p_5f_fraction8','p_5f_fraction9','p_5f_fraction10',\
'p_6f_fraction1','p_6f_fraction2','p_6f_fraction3','p_6f_fraction4',\
'p_6f_fraction5','p_6f_fraction6','p_6f_fraction7','p_6f_fraction8',\
'p_6f_fraction9','p_6f_fraction10','p_7f_fraction1','p_7f_fraction2',\
'p_7f_fraction3','p_7f_fraction4','p_7f_fraction5','p_7f_fraction6',\
'p_7f_fraction7','p_7f_fraction8','p_7f_fraction9','p_7f_fraction10',\
'p_8f_fraction1','p_8f_fraction2','p_8f_fraction3','p_8f_fraction4',\
'p_8f_fraction5','p_8f_fraction6','p_8f_fraction7','p_8f_fraction8',\
'p_8f_fraction9','p_8f_fraction10','p_10f_fraction1','p_10f_fraction2',\
'p_10f_fraction3','p_10f_fraction4','p_10f_fraction5','p_10f_fraction6',\
'p_10f_fraction7','p_10f_fraction8','p_10f_fraction9','p_10f_fraction10',\
'p_12f_fraction1','p_12f_fraction2','p_12f_fraction3','p_12f_fraction4',\
'p_12f_fraction5','p_12f_fraction6','p_12f_fraction7','p_12f_fraction8',\
'p_12f_fraction9','p_12f_fraction10','p_14f_fraction1','p_14f_fraction2',\
'p_14f_fraction3','p_14f_fraction4','p_14f_fraction5','p_14f_fraction6',\
'p_14f_fraction7','p_14f_fraction8','p_14f_fraction9','p_14f_fraction10',\
'p_16f_fraction1','p_16f_fraction2','p_16f_fraction3','p_16f_fraction4',\
'p_16f_fraction5','p_16f_fraction6','p_16f_fraction7','p_16f_fraction8',\
'p_16f_fraction9','p_16f_fraction10','p_fractone1','p_fractone2',\
'p_fractone3','p_fractone4','p_fractone5','p_fractone6','p_fractone7',\
'p_fractone8','p_fractone9','p_fractone10','p_fracttwo1','p_fracttwo2',\
'p_fracttwo3','p_fracttwo4','p_fracttwo5','p_fracttwo6','p_fracttwo7',\
'p_fracttwo8','p_fracttwo9','p_fracttwo10','p_fractthree1','p_fractthree2',\
'p_fractthree3','p_fractthree4','p_fractthree5','p_fractthree6','p_fractthree7',\
'p_fractthree8','p_fractthree9','p_fractthree10','reserved1016','reserved1017',\
'reserved1018','reserved1019','reserved1020','reserved1021','reserved1022',\
'reserved1023','reserved1024','reserved1025','reserved1026','reserved1027',\
'reserved1028','reserved1029','reserved1030','reserved1031','reserved1032',\
'reserved1033','reserved1034','reserved1035','p_final_time1',\
'p_final_time2','p_final_time3','p_final_time4','p_final_time5',\
'p_final_time6','p_final_time7','p_final_time8','p_final_time9',\
'p_final_time10','p_claimed_code1','p_claimed_code2','p_claimed_code3',\
'p_claimed_code4','p_claimed_code5','p_claimed_code6','p_claimed_code7',\
'p_claimed_code8','p_claimed_code9','p_claimed_code10','p_trainer1',\
'p_trainer2','p_trainer3','p_trainer4','p_trainer5','p_trainer6','p_trainer7',\
'p_trainer8','p_trainer9','p_trainer10','p_jockey1','p_jockey2','p_jockey3',\
'p_jockey4','p_jockey5','p_jockey6','p_jockey7','p_jockey8','p_jockey9',\
'p_jockey10','p_apprentice_wt_allow1','p_apprentice_wt_allow2',\
'p_apprentice_wt_allow3','p_apprentice_wt_allow4','p_apprentice_wt_allow5',\
'p_apprentice_wt_allow6','p_apprentice_wt_allow7','p_apprentice_wt_allow8',\
'p_apprentice_wt_allow9','p_apprentice_wt_allow10','p_race_type1',\
'p_race_type2','p_race_type3','p_race_type4','p_race_type5','p_race_type6',\
'p_race_type7','p_race_type8','p_race_type9','p_race_type10',\
'p_age_and_sex_restrict1','p_age_and_sex_restrict2','p_age_and_sex_restrict3',\
'p_age_and_sex_restrict4','p_age_and_sex_restrict5','p_age_and_sex_restrict6',\
'p_age_and_sex_restrict7','p_age_and_sex_restrict8','p_age_and_sex_restrict9',\
'p_age_and_sex_restrict10','p_statebred1','p_statebred2','p_statebred3',\
'p_statebred4','p_statebred5','p_statebred6','p_statebred7','p_statebred8',\
'p_statebred9','p_statebred10','p_restricted_flag1','p_restricted_flag2',\
'p_restricted_flag3','p_restricted_flag4','p_restricted_flag5',\
'p_restricted_flag6','p_restricted_flag7','p_restricted_flag8',\
'p_restricted_flag9','p_restricted_flag10','p_fav_indicator1','p_fav_indicator2',\
'p_fav_indicator3','p_fav_indicator4','p_fav_indicator5','p_fav_indicator6',\
'p_fav_indicator7','p_fav_indicator8','p_fav_indicator9','p_fav_indicator10',\
'p_front_bandages_indicator1','p_front_bandages_indicator2',\
'p_front_bandages_indicator3','p_front_bandages_indicator4',\
'p_front_bandages_indicator5','p_front_bandages_indicator6',\
'p_front_bandages_indicator7','p_front_bandages_indicator8',\
'p_front_bandages_indicator9','p_front_bandages_indicator10','reserved1146',\
'trainer_cy_sts','trainer_cy_wins','trainer_cy_places','trainer_cy_shows',\
'trainer_cy_roi','trainer_py_sts','trainer_py_wins','trainer_py_places',\
'trainer_py_shows','trainer_py_roi','jockey_cy_sts','jockey_cy_wins',\
'jockey_cy_places','jockey_cy_shows','jockey_cy_roi','jockey_py_sts',\
'jockey_py_wins','jockey_py_places','jockey_py_shows','jockey_py_roi',\
'p_bris_speed_par1','p_bris_speed_par2','p_bris_speed_par3','p_bris_speed_par4',\
'p_bris_speed_par5','p_bris_speed_par6','p_bris_speed_par7','p_bris_speed_par8',\
'p_bris_speed_par9','p_bris_speed_par10','current_sire_stud_fee',\
'best_bris_speed_fast_track','best_bris_speed_turf',\
'best_bris_speed_offtrack','best_bris_speed_distance','p_bar_shoe1',\
'p_bar_shoe2','p_bar_shoe3','p_bar_shoe4','p_bar_shoe5','p_bar_shoe6',\
'p_bar_shoe7','p_bar_shoe8','p_bar_shoe9','p_bar_shoe10',\
'p_companylinecodes1','p_companylinecodes2','p_companylinecodes3',\
'p_companylinecodes4','p_companylinecodes5','p_companylinecodes6',\
'p_companylinecodes7','p_companylinecodes8','p_companylinecodes9',\
'p_companylinecodes10','p_high_claim1','p_high_claim2','p_high_claim3',\
'p_high_claim4','p_high_claim5','p_high_claim6','p_high_claim7',\
'p_high_claim8','p_high_claim9','p_high_claim10','p_low_claim1',\
'p_low_claim2','p_low_claim3','p_low_claim4','p_low_claim5','p_low_claim6',\
'p_low_claim7','p_low_claim8','p_low_claim9','p_low_claim10',\
'auction_price','auction_loc','reserved1224','reserved1225',\
'reserved1226','reserved1227','reserved1228','reserved1229','reserved1230',\
'reserved1231','reserved1232','reserved1233','reserved1234','reserved1235',\
'reserved1236','reserved1237','reserved1238','reserved1239','reserved1240',\
'reserved1241','reserved1242','reserved1243','reserved1244','reserved1245',\
'reserved1246','reserved1247','reserved1248','reserved1249','reserved1250',\
'reserved1251','reserved1252','reserved1253','prior_start_code1',\
'prior_start_code2','prior_start_code3','prior_start_code4','prior_start_code5',\
'prior_start_code6','prior_start_code7','prior_start_code8','prior_start_code9',\
'prior_start_code10','bris_dirt_pedigree_rating','bris_mud_pedigree_rating',\
'bris_turf_pedigree_rating','bris_dist_pedigree_rating','clmdfroma1',\
'clmdfroma2','clmdfroma3','clmdfroma4','clmdfroma5','clmdfroma6','clmdfroma7',\
'clmdfroma8','clmdfroma9','clmdfroma10','clmdfromb1','clmdfromb2','clmdfromb3',\
'clmdfromb4','clmdfromb5','clmdfromb6','clmdfromb7','clmdfromb8','clmdfromb9',\
'clmdfromb10','clmdfromc1','clmdfromc2','clmdfromc3','clmdfromc4','clmdfromc5',\
'clmdfromc6','clmdfromc7','clmdfromc8','clmdfromc9','clmdfromc10','clmdfromd1',\
'clmdfromd2','clmdfromd3','clmdfromd4','clmdfromd5','clmdfromd6','clmdfromd7',\
'clmdfromd8','clmdfromd9','clmdfromd10','clmdfrome1','clmdfrome2','clmdfrome3',\
'clmdfrome4','clmdfrome5','clmdfrome6','clmdfrome7','clmdfrome8','clmdfrome9',\
'clmdfrome10','clmdfromf1','clmdfromf2','clmdfromf3','clmdfromf4','clmdfromf5',\
'clmdfromf6','clmdfromf7','clmdfromf8','clmdfromf9','clmdfromf10',\
'best_bris_speed_life','best_bris_speed_most_recent_yr',\
'best_bris_speed_2nd_most_recent_yr','best_bris_speed_today_track',\
'h_fst_dirt_lt_starts','h_fst_dirt_lt_wins','h_fst_dirt_lt_places',\
'h_fst_dirt_lt_shows','h_fst_dirt_lt_earnings','key_trnr_categ1',\
'key_trnr_categ1_starts','key_trnr_categ1_win%','key_trnr_categ1_itm%',\
'key_trnr_categ1_roi','key_trnr_categ2','key_trnr_categ2_starts',\
'key_trnr_categ2_win%','key_trnr_categ2_itm%','key_trnr_categ2_roi',\
'key_trnr_categ3','key_trnr_categ3_starts','key_trnr_categ3_win%',\
'key_trnr_categ3_itm%','key_trnr_categ3_roi','key_trnr_categ4',\
'key_trnr_categ4_starts','key_trnr_categ4_win%','key_trnr_categ4_itm%',\
'key_trnr_categ4_roi','key_trnr_categ5','key_trnr_categ5_starts',\
'key_trnr_categ5_win%','key_trnr_categ5_itm%','key_trnr_categ5_roi',\
'key_trnr_categ6','key_trnr_categ6_starts','key_trnr_categ6_win%',\
'key_trnr_categ6_itm%','key_trnr_categ6_roi','jky_dis_turf_label',\
'jky_dis_turf_starts','jky_dis_turf_wins','jky_dis_turf_places',\
'jky_dis_turf_shows','jky_dis_turf_roi','jky_dis_turf_earnings',\
'post_times','reserved1375','reserved1376','reserved1377',\
'reserved1378','reserved1379','reserved1380','reserved1381',\
'reserved1382','p_extend_comment1','p_extend_comment2',\
'p_extend_comment3','p_extend_comment4','p_extend_comment5',\
'p_extend_comment6','p_extend_comment7','p_extend_comment8',\
'p_extend_comment9','p_extend_comment10','p_sealed1','p_sealed2',\
'p_sealed3','p_sealed4','p_sealed5','p_sealed6','p_sealed7','p_sealed8',\
'p_sealed9','p_sealed10','p_aw_flag1','p_aw_flag2','p_aw_flag3',\
'p_aw_flag4','p_aw_flag5','p_aw_flag6','p_aw_flag7','p_aw_flag8',\
'p_aw_flag9','p_aw_flag10','tj_meet_starts','tj_meet_wins','tj_meet_places',\
'tj_meet_shows','tj_meet_roi','today_post_time','peqb_abbr_race_cond1',\
'peqb_abbr_race_cond2','peqb_abbr_race_cond3','peqb_abbr_race_cond4',\
'peqb_abbr_race_cond5','peqb_abbr_race_cond6','peqb_abbr_race_cond7',\
'peqb_abbr_race_cond8','peqb_abbr_race_cond9','peqb_abbr_race_cond10',\
'today_eqb_abbr_race_cond','reserved1430','reserved1431','reserved1432',\
'reserved1433','reserved1434','reserved1435']

# These are fields to initially hide/drop from the datafile
# Some I may want to come back and use later.

r = ['wager1','wager2','wager3','wager4','wager5','wager6','wager7','wager8','wager9',\
'reserved1016','reserved1017','reserved1018','reserved1019','reserved1020',\
'reserved1021','reserved1022','reserved1023','reserved1024','reserved1025',\
'reserved1026','reserved1027','reserved1028','reserved1029','reserved1030',\
'reserved1031','reserved1032','reserved1033','reserved1034','reserved1035',\
'reserved1146','reserved1224','reserved1225','reserved1226','reserved1227',\
'reserved1228','reserved1229','reserved1230','reserved1231','reserved1232',\
'reserved1233','reserved1234','reserved1235','reserved1236','reserved1237',\
'reserved1238','reserved1239','reserved1240','reserved1241','reserved1242',\
'reserved1243','reserved1244','reserved1245','reserved1246','reserved1247',\
'reserved1248','reserved1249','reserved1250','reserved1251','reserved1252',\
'reserved1253','reserved1375','reserved1376','reserved1377','reserved1378',\
'reserved1379','reserved1380','reserved1381','reserved1382','reserved1430',\
'reserved1431','reserved1432','reserved1433','reserved1434','reserved1435',\
'reserved212','reserved213','reserved237','reserved249','reserved250','reserved252',\
'reserved253','reserved254','reserved255','reserved26','reserved27','reserved275',\
'reserved42','reserved48','reserved59','reserved60','reserved61','reserved706',\
'reserved707','reserved708','reserved709','reserved710','reserved711','reserved712',\
'reserved713','reserved714','reserved715','reserved826','reserved827','reserved828',\
'reserved829','reserved830','reserved831','reserved832','reserved833','reserved834',\
'reserved835','reserved836','reserved837','reserved838','reserved839','reserved840',\
'reserved841','reserved842','reserved843','reserved844','reserved845',\
'p_winner1', 'p_winner2', 'p_winner3', 'p_winner4', 'p_winner5', 'p_winner6',\
'p_winner7', 'p_winner8', 'p_winner9', 'p_winner10', 'p_place1', 'p_place2',\
'p_place3', 'p_place4', 'p_place5', 'p_place6', 'p_place7', 'p_place8',\
'p_place9', 'p_place10', 'p_show1', 'p_show2', 'p_show3', 'p_show4', 'p_show5',\
'p_show6', 'p_show7', 'p_show8', 'p_show9', 'p_show10', 'p_win_wt1', 'p_win_wt2',\
'p_win_wt3', 'p_win_wt4', 'p_win_wt5', 'p_win_wt6', 'p_win_wt7', 'p_win_wt8',\
'p_win_wt9', 'p_win_wt10', 'p_plc_wt1', 'p_plc_wt2', 'p_plc_wt3', 'p_plc_wt4',\
'p_plc_wt5', 'p_plc_wt6', 'p_plc_wt7', 'p_plc_wt8', 'p_plc_wt9', 'p_plc_wt10',\
'p_shw_wt1', 'p_shw_wt2', 'p_shw_wt3', 'p_shw_wt4', 'p_shw_wt5', 'p_shw_wt6',\
'p_shw_wt7', 'p_shw_wt8', 'p_shw_wt9', 'p_shw_wt10','p_win_margin1','p_win_margin2',\
'p_win_margin3', 'p_win_margin4', 'p_win_margin5', 'p_win_margin6', 'p_win_margin7',\
'p_win_margin8', 'p_win_margin9', 'p_win_margin10', 'p_plc_margin1', 'p_plc_margin2',\
'p_plc_margin3', 'p_plc_margin4', 'p_plc_margin5', 'p_plc_margin6', 'p_plc_margin7',\
'p_plc_margin8', 'p_plc_margin9', 'p_plc_margin10', 'p_shw_margin1', 'p_shw_margin2',\
'p_shw_margin3', 'p_shw_margin4', 'p_shw_margin5', 'p_shw_margin6', 'p_shw_margin7',\
'p_shw_margin8', 'p_shw_margin9', 'p_shw_margin10','reserved1',\
'p_extracomment1','p_extracomment2','p_extracomment3','p_extracomment4',\
'p_extracomment5','p_extracomment6','p_extracomment7','p_extracomment8',\
'p_extracomment9','p_extracomment10 ',\
'clmdfroma1',\
'clmdfroma2','clmdfroma3','clmdfroma4','clmdfroma5','clmdfroma6','clmdfroma7',\
'clmdfroma8','clmdfroma9','clmdfroma10','clmdfromb1','clmdfromb2','clmdfromb3',\
'clmdfromb4','clmdfromb5','clmdfromb6','clmdfromb7','clmdfromb8','clmdfromb9',\
'clmdfromb10','clmdfromc1','clmdfromc2','clmdfromc3','clmdfromc4','clmdfromc5',\
'clmdfromc6','clmdfromc7','clmdfromc8','clmdfromc9','clmdfromc10','clmdfromd1',\
'clmdfromd2','clmdfromd3','clmdfromd4','clmdfromd5','clmdfromd6','clmdfromd7',\
'clmdfromd8','clmdfromd9','clmdfromd10','clmdfrome1','clmdfrome2','clmdfrome3',\
'clmdfrome4','clmdfrome5','clmdfrome6','clmdfrome7','clmdfrome8','clmdfrome9',\
'clmdfrome10','clmdfromf1','clmdfromf2','clmdfromf3','clmdfromf4','clmdfromf5',\
'clmdfromf6','clmdfromf7','clmdfromf8','clmdfromf9','clmdfromf10',\
'key_trnr_categ1',\
'key_trnr_categ1_starts','key_trnr_categ1_win%','key_trnr_categ1_itm%',\
'key_trnr_categ1_roi','key_trnr_categ2','key_trnr_categ2_starts',\
'key_trnr_categ2_win%','key_trnr_categ2_itm%','key_trnr_categ2_roi',\
'key_trnr_categ3','key_trnr_categ3_starts','key_trnr_categ3_win%',\
'key_trnr_categ3_itm%','key_trnr_categ3_roi','key_trnr_categ4',\
'key_trnr_categ4_starts','key_trnr_categ4_win%','key_trnr_categ4_itm%',\
'key_trnr_categ4_roi','key_trnr_categ5','key_trnr_categ5_starts',\
'key_trnr_categ5_win%','key_trnr_categ5_itm%','key_trnr_categ5_roi',\
'key_trnr_categ6','key_trnr_categ6_starts','key_trnr_categ6_win%',\
'key_trnr_categ6_itm%','key_trnr_categ6_roi',\
'p_extend_comment1','p_extend_comment2',\
'p_extend_comment3','p_extend_comment4','p_extend_comment5',\
'p_extend_comment6','p_extend_comment7','p_extend_comment8',\
'p_extend_comment9','p_extend_comment10','p_2f_fraction1','p_2f_fraction2','p_2f_fraction3','p_2f_fraction4',\
'p_2f_fraction5','p_2f_fraction6','p_2f_fraction7','p_2f_fraction8',\
'p_2f_fraction9','p_2f_fraction10','p_3f_fraction1','p_3f_fraction2',\
'p_3f_fraction3','p_3f_fraction4','p_3f_fraction5','p_3f_fraction6',\
'p_3f_fraction7','p_3f_fraction8','p_3f_fraction9','p_3f_fraction10',\
'p_4f_fraction1','p_4f_fraction2','p_4f_fraction3','p_4f_fraction4',\
'p_4f_fraction5','p_4f_fraction6','p_4f_fraction7','p_4f_fraction8',\
'p_4f_fraction9','p_4f_fraction10','p_5f_fraction1','p_5f_fraction2',\
'p_5f_fraction3','p_5f_fraction4','p_5f_fraction5','p_5f_fraction6',\
'p_5f_fraction7','p_5f_fraction8','p_5f_fraction9','p_5f_fraction10',\
'p_6f_fraction1','p_6f_fraction2','p_6f_fraction3','p_6f_fraction4',\
'p_6f_fraction5','p_6f_fraction6','p_6f_fraction7','p_6f_fraction8',\
'p_6f_fraction9','p_6f_fraction10','p_7f_fraction1','p_7f_fraction2',\
'p_7f_fraction3','p_7f_fraction4','p_7f_fraction5','p_7f_fraction6',\
'p_7f_fraction7','p_7f_fraction8','p_7f_fraction9','p_7f_fraction10',\
'p_8f_fraction1','p_8f_fraction2','p_8f_fraction3','p_8f_fraction4',\
'p_8f_fraction5','p_8f_fraction6','p_8f_fraction7','p_8f_fraction8',\
'p_8f_fraction9','p_8f_fraction10','p_10f_fraction1','p_10f_fraction2',\
'p_10f_fraction3','p_10f_fraction4','p_10f_fraction5','p_10f_fraction6',\
'p_10f_fraction7','p_10f_fraction8','p_10f_fraction9','p_10f_fraction10',\
'p_12f_fraction1','p_12f_fraction2','p_12f_fraction3','p_12f_fraction4',\
'p_12f_fraction5','p_12f_fraction6','p_12f_fraction7','p_12f_fraction8',\
'p_12f_fraction9','p_12f_fraction10','p_14f_fraction1','p_14f_fraction2',\
'p_14f_fraction3','p_14f_fraction4','p_14f_fraction5','p_14f_fraction6',\
'p_14f_fraction7','p_14f_fraction8','p_14f_fraction9','p_14f_fraction10',\
'p_16f_fraction1','p_16f_fraction2','p_16f_fraction3','p_16f_fraction4',\
'p_16f_fraction5','p_16f_fraction6','p_16f_fraction7','p_16f_fraction8',\
'p_16f_fraction9','p_16f_fraction10',\
'p_comment1','p_comment2',\
'p_comment3','p_comment4','p_comment5','p_comment6','p_comment7',\
'p_comment8','p_comment9','p_comment10',\
'p_companylinecodes1','p_companylinecodes2','p_companylinecodes3',\
'p_companylinecodes4','p_companylinecodes5','p_companylinecodes6',\
'p_companylinecodes7','p_companylinecodes8','p_companylinecodes9',\
'p_companylinecodes10','p_high_claim1','p_high_claim2','p_high_claim3',\
'p_high_claim4','p_high_claim5','p_high_claim6','p_high_claim7',\
'p_high_claim8','p_high_claim9','p_high_claim10','p_low_claim1',\
'p_low_claim2','p_low_claim3','p_low_claim4','p_low_claim5','p_low_claim6',\
'p_low_claim7','p_low_claim8','p_low_claim9','p_low_claim10',\
'p_race_classification1','p_race_classification2','p_race_classification3',\
'p_race_classification4','p_race_classification5','p_race_classification6',\
'p_race_classification7','p_race_classification8','p_race_classification9',\
'p_race_classification10','prior_start_code1',\
'prior_start_code2','prior_start_code3','prior_start_code4','prior_start_code5',\
'prior_start_code6','prior_start_code7','prior_start_code8','prior_start_code9',\
'prior_start_code10',\
'p_racename1','p_racename2','p_racename3',\
'p_racename4','p_racename5','p_racename6','p_racename7','p_racename8',\
'p_racename9','p_racename10','bristrackcode1',\
'bristrackcode2','bristrackcode3','bristrackcode4','bristrackcode5',\
'bristrackcode6','bristrackcode7','bristrackcode8','bristrackcode9',\
'bristrackcode10',\
'p_race1','p_race2','p_race3','p_race4','p_race5',\
'p_race6','p_race7','p_race8','p_race9','p_race10',\
'racecon1','racecon2','racecon3','racecon4','racecon5',\
'racecon6','t_lasix_list','t_bute_list','t_track_record',\
't_mutuel_list','ownersilks','t_coupled_list','simulcast_host_track_code',\
'simulcast_host_track_race','t_breed_type','horse_color','t_med_old',\
'today_post_time','t_race type','t_race_conditions','t_race_classification']


def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
	import matplotlib.pyplot as plt
	"""
	Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks
	The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
	"""
	ax = axes or plt.gca()
	ax.spines['top'].set_visible(top)
	ax.spines['right'].set_visible(right)
	ax.spines['left'].set_visible(left)
	ax.spines['bottom'].set_visible(bottom)
	
	#turn off all ticks
	ax.yaxis.set_ticks_position('none')
	ax.xaxis.set_ticks_position('none')
	
	#now re-enable visibles
	if top:
		ax.xaxis.tick_top()
	if bottom:
		ax.xaxis.tick_bottom()
	if left:
		ax.yaxis.tick_left()
	if right:
		ax.yaxis.tick_right()

def add_stats(df):
	from math import sqrt
	import scipy.stats
	df['win%'] = (df['win']/df['start'].apply(float))*100
	df['itm%'] = (df['itm']/df['start'].apply(float))*100
	df['var2'] = df['variance'].apply(sqrt)
	df['st%'] = (df['start']/(df['start'].apply(float).sum()))*100
	df['c_freq'] = (scipy.stats.norm(df['f_odds'],df['var2']).cdf(df['win']))*100
	df['roi%'] = ((df.win_payoff-(df.start*2))/(df.start*2))*100
	return df


odds_map = {.05:'1/20',.1:'1/10',.2:'1/5', .3:'1/5',.4:'2/5',\
.5:'1/2',.6:'3/5',.7:'3/5',.8:'4/5',.9:'4/5',1:'1' ,1.1:'1',\
1.2:'6/5',1.3:'6/5',1.4:'7/5',1.5:'3/2',1.6:'8/5',1.7:'8/5',\
1.8:'9/5',1.9:'9/5',2:'2/1',2.1:'2/1',2.2:'2/1',2.3:'2/1',2.4:'2/1',\
2.5:'5/2',2.6:'5/2',2.7:'5/2',2.8:'5/2',2.9:'5/2',\
3:'3/1',3.1:'3/1',3.2:'3/1',3.3:'3/1',3.4:'3/1',\
3.5:'7/2',3.6:'7/2',3.7:'7/2',3.8:'7/2',3.9:'7/2',\
4:'4/1',4.1:'4/1',4.2:'4/1',4.4:'4/1',\
4.5:'9/2',4.6:'9/2',4.7:'9/2',4.8:'9/2',4.9:'9/2',\
5:'5-1',5.1:'5-1',5.2:'5-1',5.3:'5-1',5.4:'5-1',5.5:'5-1',5.6:'5-1',5.7:'5-1',5.8:'5-1',5.9:'5-1',\
6:'6-1',6.1:'6-1',6.2:'6-1',6.3:'6-1',6.4:'6-1',6.5:'6-1',6.6:'6-1',6.7:'6-1',6.8:'6-1',6.9:'6-1',\
7:'7-1',7.1:'7-1',7.2:'7-1',7.3:'7-1',7.4:'7-1',7.5:'7-1',7.6:'7-1',7.7:'7-1',7.8:'7-1',7.9:'7-1',
8:'8-1',8.1:'8-1',8.2:'8-1',8.3:'8-1',8.4:'8-1',8.5:'8-1',8.6:'8-1',8.7:'8-1',8.8:'8-1',8.9:'8-1',\
9:'9-1',9.1:'9-1',9.2:'9-1',9.3:'9-1',9.4:'9-1',9.5:'9-1',9.6:'9-1',9.7:'9-1',9.8:'9-1',9.9:'9-1',\
10:'10-1',10.1:'10-1',10.2:'10-1',10.3:'10-1',10.4:'10-1',10.5:'10-1',10.6:'10-1',10.7:'10-1',10.8:'10-1',10.9:'10-1',\
11:'11-1',11.1:'11-1',11.2:'11-1',11.3:'11-1',11.4:'11-1',11.5:'11-1',11.6:'11-1',\
11.7:'11-1',11.8:'11-1',11.9:'11-1',12:'12-1',12.1:'12-1',12.2:'12-1',12.3:'12-1',\
12.4:'12-1',12.5:'12-1',12.6:'12-1',12.7:'12-1',12.8:'12-1',12.9:'12-1',13:'13-1',\
13.1:'13-1',13.2:'13-1',13.3:'13-1',13.4:'13-1',13.5:'13-1',13.6:'13-1',13.7:'13-1',\
13.8:'13-1',13.9:'13-1',14:'14-1',14.1:'14-1',14.2:'14-1',14.3:'14-1',14.4:'14-1',\
14.5:'14-1',14.6:'14-1',14.7:'14-1',14.8:'14-1',14.9:'14-1',15:'15-1',15.1:'15-1',\
15.2:'15-1',15.3:'15-1',15.4:'15-1',15.5:'15-1',15.6:'15-1',15.7:'15-1',15.8:'15-1',\
15.9:'15-1',16:'16-1',16.1:'16-1',16.2:'16-1',16.3:'16-1',16.4:'16-1',16.5:'16-1',\
16.6:'16-1',16.7:'16-1',16.8:'16-1',16.9:'16-1',17:'17-1',17.1:'17-1',17.2:'17-1',\
17.3:'17-1',17.4:'17-1',17.5:'17-1',17.6:'17-1',17.7:'17-1',17.8:'17-1',17.9:'17-1',\
18:'18-1',18.1:'18-1',18.2:'18-1',18.3:'18-1',18.4:'18-1',18.5:'18-1',18.6:'18-1',\
18.7:'18-1',18.8:'18-1',18.9:'18-1',19:'19-1',19.1:'19-1',19.2:'19-1',19.3:'19-1',\
19.4:'19-1',19.5:'19-1',19.6:'19-1',19.7:'19-1',19.8:'19-1',19.9:'19-1',20:'20-1',\
20.1:'20-1',20.2:'20-1',20.3:'20-1',20.4:'20-1',20.5:'20-1',20.6:'20-1',20.7:'20-1',\
20.8:'20-1',20.9:'20-1',21:'21-1',21.1:'21-1',21.2:'21-1',21.3:'21-1',21.4:'21-1',\
21.5:'21-1',21.6:'21-1',21.7:'21-1',21.8:'21-1',21.9:'21-1',22:'22-1',22.1:'22-1',\
22.2:'22-1',22.3:'22-1',22.4:'22-1',22.5:'22-1',22.6:'22-1',22.7:'22-1',22.8:'22-1',\
22.9:'22-1',23:'23-1',23.1:'23-1',23.2:'23-1',23.3:'23-1',23.4:'23-1',23.5:'23-1',\
23.6:'23-1',23.7:'23-1',23.8:'23-1',23.9:'23-1',24:'24-1',24.1:'24-1',24.2:'24-1',\
24.3:'24-1',24.4:'24-1',24.5:'24-1',24.6:'24-1',24.7:'24-1',24.8:'24-1',24.9:'24-1',\
25:'25-1',25.1:'25-1',25.2:'25-1',25.3:'25-1',25.4:'25-1',25.5:'25-1',25.6:'25-1',\
25.7:'25-1',25.8:'25-1',25.9:'25-1',26:'26-1',26.1:'26-1',26.2:'26-1',26.3:'26-1',\
26.4:'26-1',26.5:'26-1',26.6:'26-1',26.7:'26-1',26.8:'26-1',26.9:'26-1',27:'27-1',\
27.1:'27-1',27.2:'27-1',27.3:'27-1',27.4:'27-1',27.5:'27-1',27.6:'27-1',27.7:'27-1',\
27.8:'27-1',27.9:'27-1',28:'28-1',28.1:'28-1',28.2:'28-1',28.3:'28-1',28.4:'28-1',\
28.5:'28-1',28.6:'28-1',28.7:'28-1',28.8:'28-1',28.9:'28-1',29:'29-1',29.1:'29-1',\
29.2:'29-1',29.3:'29-1',29.4:'29-1',29.5:'29-1',29.6:'29-1',29.7:'29-1',29.8:'29-1',\
29.9:'29-1',30:'30-1',30.1:'30-1',30.2:'30-1',30.3:'30-1',30.4:'30-1',30.5:'30-1',\
30.6:'30-1',30.7:'30-1',30.8:'30-1',30.9:'30-1',31:'31-1',31.1:'31-1',31.2:'31-1',\
31.3:'31-1',31.4:'31-1',31.5:'31-1',31.6:'31-1',31.7:'31-1',31.8:'31-1',31.9:'31-1',\
32:'32-1',32.1:'32-1',32.2:'32-1',32.3:'32-1',32.4:'32-1',32.5:'32-1',32.6:'32-1',\
32.7:'32-1',32.8:'32-1',32.9:'32-1',33:'33-1',33.1:'33-1',33.2:'33-1',33.3:'33-1',\
33.4:'33-1',33.5:'33-1',33.6:'33-1',33.7:'33-1',33.8:'33-1',33.9:'33-1',34:'34-1',\
34.1:'34-1',34.2:'34-1',34.3:'34-1',34.4:'34-1',34.5:'34-1',34.6:'34-1',34.7:'34-1',\
34.8:'34-1',34.9:'34-1',35:'35-1',35.1:'35-1',35.2:'35-1',35.3:'35-1',35.4:'35-1',\
35.5:'35-1',35.6:'35-1',35.7:'35-1',35.8:'35-1',35.9:'35-1',36:'36-1',36.1:'36-1',\
36.2:'36-1',36.3:'36-1',36.4:'36-1',36.5:'36-1',36.6:'36-1',36.7:'36-1',36.8:'36-1',\
36.9:'36-1',37:'37-1',37.1:'37-1',37.2:'37-1',37.3:'37-1',37.4:'37-1',37.5:'37-1',\
37.6:'37-1',37.7:'37-1',37.8:'37-1',37.9:'37-1',38:'38-1',38.1:'38-1',38.2:'38-1',\
38.3:'38-1',38.4:'38-1',38.5:'38-1',38.6:'38-1',38.7:'38-1',38.8:'38-1',38.9:'38-1',\
39:'39-1',39.1:'39-1',39.2:'39-1',39.3:'39-1',39.4:'39-1',39.5:'39-1',39.6:'39-1',\
39.7:'39-1',39.8:'39-1',39.9:'39-1',40:'40-1',40.1:'40-1',40.2:'40-1',40.3:'40-1',\
40.4:'40-1',40.5:'40-1',40.6:'40-1',40.7:'40-1',40.8:'40-1',40.9:'40-1',41:'41-1',\
41.1:'41-1',41.2:'41-1',41.3:'41-1',41.4:'41-1',41.5:'41-1',41.6:'41-1',41.7:'41-1',\
41.8:'41-1',41.9:'41-1',42:'42-1',42.1:'42-1',42.2:'42-1',42.3:'42-1',42.4:'42-1',\
42.5:'42-1',42.6:'42-1',42.7:'42-1',42.8:'42-1',42.9:'42-1',43:'43-1',43.1:'43-1',\
43.2:'43-1',43.3:'43-1',43.4:'43-1',43.5:'43-1',43.6:'43-1',43.7:'43-1',43.8:'43-1',\
43.9:'43-1',44:'44-1',44.1:'44-1',44.2:'44-1',44.3:'44-1',44.4:'44-1',44.5:'44-1',\
44.6:'44-1',44.7:'44-1',44.8:'44-1',44.9:'44-1',45:'45-1',45.1:'45-1',45.2:'45-1',\
45.3:'45-1',45.4:'45-1',45.5:'45-1',45.6:'45-1',45.7:'45-1',45.8:'45-1',45.9:'45-1',\
46:'46-1',46.1:'46-1',46.2:'46-1',46.3:'46-1',46.4:'46-1',46.5:'46-1',46.6:'46-1',\
46.7:'46-1',46.8:'46-1',46.9:'46-1',47:'47-1',47.1:'47-1',47.2:'47-1',47.3:'47-1',\
47.4:'47-1',47.5:'47-1',47.6:'47-1',47.7:'47-1',47.8:'47-1',47.9:'47-1',48:'48-1',\
48.1:'48-1',48.2:'48-1',48.3:'48-1',48.4:'48-1',48.5:'48-1',48.6:'48-1',48.7:'48-1',\
48.8:'48-1',48.9:'48-1',49:'49-1',49.1:'49-1',49.2:'49-1',49.3:'49-1',49.4:'49-1',\
49.5:'49-1',49.6:'49-1',49.7:'49-1',49.8:'49-1',49.9:'49-1',50:'50-1',50.1:'50-1',\
50.2:'50-1',50.3:'50-1',50.4:'50-1',50.5:'50-1',50.6:'50-1',50.7:'50-1',50.8:'50-1',\
50.9:'50-1',51:'51-1',51.1:'51-1',51.2:'51-1',51.3:'51-1',51.4:'51-1',51.5:'51-1',\
51.6:'51-1',51.7:'51-1',51.8:'51-1',51.9:'51-1',52:'52-1',52.1:'52-1',52.2:'52-1',\
52.3:'52-1',52.4:'52-1',52.5:'52-1',52.6:'52-1',52.7:'52-1',52.8:'52-1',52.9:'52-1',\
53:'53-1',53.1:'53-1',53.2:'53-1',53.3:'53-1',53.4:'53-1',53.5:'53-1',53.6:'53-1',\
53.7:'53-1',53.8:'53-1',53.9:'53-1',54:'54-1',54.1:'54-1',54.2:'54-1',54.3:'54-1',\
54.4:'54-1',54.5:'54-1',54.6:'54-1',54.7:'54-1',54.8:'54-1',54.9:'54-1',55:'55-1',\
55.1:'55-1',55.2:'55-1',55.3:'55-1',55.4:'55-1',55.5:'55-1',55.6:'55-1',55.7:'55-1',\
55.8:'55-1',55.9:'55-1',56:'56-1',56.1:'56-1',56.2:'56-1',56.3:'56-1',56.4:'56-1',\
56.5:'56-1',56.6:'56-1',56.7:'56-1',56.8:'56-1',56.9:'56-1',57:'57-1',57.1:'57-1',\
57.2:'57-1',57.3:'57-1',57.4:'57-1',57.5:'57-1',57.6:'57-1',57.7:'57-1',57.8:'57-1',\
57.9:'57-1',58:'58-1',58.1:'58-1',58.2:'58-1',58.3:'58-1',58.4:'58-1',58.5:'58-1',\
58.6:'58-1',58.7:'58-1',58.8:'58-1',58.9:'58-1',59:'59-1',59.1:'59-1',59.2:'59-1',\
59.3:'59-1',59.4:'59-1',59.5:'59-1',59.6:'59-1',59.7:'59-1',59.8:'59-1',59.9:'59-1',\
60:'60-1',60.1:'60-1',60.2:'60-1',60.3:'60-1',60.4:'60-1',60.5:'60-1',60.6:'60-1',\
60.7:'60-1',60.8:'60-1',60.9:'60-1',61:'61-1',61.1:'61-1',61.2:'61-1',61.3:'61-1',\
61.4:'61-1',61.5:'61-1',61.6:'61-1',61.7:'61-1',61.8:'61-1',61.9:'61-1',62:'62-1',\
62.1:'62-1',62.2:'62-1',62.3:'62-1',62.4:'62-1',62.5:'62-1',62.6:'62-1',\
62.7:'62-1',62.8:'62-1',62.9:'62-1',63:'63-1',63.1:'63-1',63.2:'63-1',63.3:'63-1',\
63.4:'63-1',63.5:'63-1',63.6:'63-1',63.7:'63-1',63.8:'63-1',63.9:'63-1',64:'64-1',\
64.1:'64-1',64.2:'64-1',64.3:'64-1',64.4:'64-1',64.5:'64-1',64.6:'64-1',64.7:'64-1',\
64.8:'64-1',64.9:'64-1',65:'65-1',65.1:'65-1',65.2:'65-1',65.3:'65-1',65.4:'65-1',\
65.5:'65-1',65.6:'65-1',65.7:'65-1',65.8:'65-1',65.9:'65-1',66:'66-1',66.1:'66-1',\
66.2:'66-1',66.3:'66-1',66.4:'66-1',66.5:'66-1',66.6:'66-1',66.7:'66-1',66.8:'66-1',\
66.9:'66-1',67:'67-1',67.1:'67-1',67.2:'67-1',67.3:'67-1',67.4:'67-1',67.5:'67-1',\
67.6:'67-1',67.7:'67-1',67.8:'67-1',67.9:'67-1',68:'68-1',68.1:'68-1',68.2:'68-1',\
68.3:'68-1',68.4:'68-1',68.5:'68-1',68.6:'68-1',68.7:'68-1',68.8:'68-1',68.9:'68-1',\
69:'69-1',69.1:'69-1',69.2:'69-1',69.3:'69-1',69.4:'69-1',69.5:'69-1',69.6:'69-1',\
69.7:'69-1',69.8:'69-1',69.9:'69-1',70:'70-1',70.1:'70-1',70.2:'70-1',70.3:'70-1',\
70.4:'70-1',70.5:'70-1',70.6:'70-1',70.7:'70-1',70.8:'70-1',70.9:'70-1',71:'71-1',\
71.1:'71-1',71.2:'71-1',71.3:'71-1',71.4:'71-1',71.5:'71-1',71.6:'71-1',71.7:'71-1',\
71.8:'71-1',71.9:'71-1',72:'72-1',72.1:'72-1',72.2:'72-1',72.3:'72-1',72.4:'72-1',\
72.5:'72-1',72.6:'72-1',72.7:'72-1',72.8:'72-1',72.9:'72-1',73:'73-1',73.1:'73-1',\
73.2:'73-1',73.3:'73-1',73.4:'73-1',73.5:'73-1',73.6:'73-1',73.7:'73-1',73.8:'73-1',\
73.9:'73-1',74:'74-1',74.1:'74-1',74.2:'74-1',74.3:'74-1',74.4:'74-1',74.5:'74-1',\
74.6:'74-1',74.7:'74-1',74.8:'74-1',74.9:'74-1',75:'75-1',75.1:'75-1',75.2:'75-1',\
75.3:'75-1',75.4:'75-1',75.5:'75-1',75.6:'75-1',75.7:'75-1',75.8:'75-1',75.9:'75-1',\
76:'76-1',76.1:'76-1',76.2:'76-1',76.3:'76-1',76.4:'76-1',76.5:'76-1',76.6:'76-1',\
76.7:'76-1',76.8:'76-1',76.9:'76-1',77:'77-1',77.1:'77-1',77.2:'77-1',77.3:'77-1',\
77.4:'77-1',77.5:'77-1',77.6:'77-1',77.7:'77-1',77.8:'77-1',77.9:'77-1',78:'78-1',\
78.1:'78-1',78.2:'78-1',78.3:'78-1',78.4:'78-1',78.5:'78-1',78.6:'78-1',78.7:'78-1',\
78.8:'78-1',78.9:'78-1',79:'79-1',79.1:'79-1',79.2:'79-1',79.3:'79-1',79.4:'79-1',\
79.5:'79-1',79.6:'79-1',79.7:'79-1',79.8:'79-1',79.9:'79-1',80:'80-1',80.1:'80-1',\
80.2:'80-1',80.3:'80-1',80.4:'80-1',80.5:'80-1',80.6:'80-1',80.7:'80-1',80.8:'80-1',\
80.9:'80-1',81:'81-1',81.1:'81-1',81.2:'81-1',81.3:'81-1',81.4:'81-1',81.5:'81-1',\
81.6:'81-1',81.7:'81-1',81.8:'81-1',81.9:'81-1',82:'82-1',82.1:'82-1',82.2:'82-1',\
82.3:'82-1',82.4:'82-1',82.5:'82-1',82.6:'82-1',82.7:'82-1',82.8:'82-1',82.9:'82-1',\
83:'83-1',83.1:'83-1',83.2:'83-1',83.3:'83-1',83.4:'83-1',83.5:'83-1',83.6:'83-1',\
83.7:'83-1',83.8:'83-1',83.9:'83-1',84:'84-1',84.1:'84-1',84.2:'84-1',84.3:'84-1',\
84.4:'84-1',84.5:'84-1',84.6:'84-1',84.7:'84-1',84.8:'84-1',84.9:'84-1',85:'85-1',\
85.1:'85-1',85.2:'85-1',85.3:'85-1',85.4:'85-1',85.5:'85-1',85.6:'85-1',85.7:'85-1',\
85.8:'85-1',85.9:'85-1',86:'86-1',86.1:'86-1',86.2:'86-1',86.3:'86-1',86.4:'86-1',\
86.5:'86-1',86.6:'86-1',86.7:'86-1',86.8:'86-1',86.9:'86-1',87:'87-1',87.1:'87-1',\
87.2:'87-1',87.3:'87-1',87.4:'87-1',87.5:'87-1',87.6:'87-1',87.7:'87-1',87.8:'87-1',\
87.9:'87-1',88:'88-1',88.1:'88-1',88.2:'88-1',88.3:'88-1',88.4:'88-1',88.5:'88-1',\
88.6:'88-1',88.7:'88-1',88.8:'88-1',88.9:'88-1',89:'89-1',89.1:'89-1',89.2:'89-1',\
89.3:'89-1',89.4:'89-1',89.5:'89-1',89.6:'89-1',89.7:'89-1',89.8:'89-1',\
89.9:'89-1',90:'90-1',90.1:'90-1',90.2:'90-1',90.3:'90-1',90.4:'90-1',90.5:'90-1',\
90.6:'90-1',90.7:'90-1',90.8:'90-1',90.9:'90-1',91:'91-1',91.1:'91-1',91.2:'91-1',\
91.3:'91-1',91.4:'91-1',91.5:'91-1',91.6:'91-1',91.7:'91-1',91.8:'91-1',91.9:'91-1',\
92:'92-1',92.1:'92-1',92.2:'92-1',92.3:'92-1',92.4:'92-1',92.5:'92-1',92.6:'92-1',\
92.7:'92-1',92.8:'92-1',92.9:'92-1',93:'93-1',93.1:'93-1',93.2:'93-1',93.3:'93-1',\
93.4:'93-1',93.5:'93-1',93.6:'93-1',93.7:'93-1',93.8:'93-1',93.9:'93-1',94:'94-1',\
94.1:'94-1',94.2:'94-1',94.3:'94-1',94.4:'94-1',94.5:'94-1',94.6:'94-1',94.7:'94-1',\
94.8:'94-1',94.9:'94-1',95:'95-1',95.1:'95-1',95.2:'95-1',95.3:'95-1',95.4:'95-1',\
95.5:'95-1',95.6:'95-1',95.7:'95-1',95.8:'95-1',95.9:'95-1',96:'96-1',96.1:'96-1',\
96.2:'96-1',96.3:'96-1',96.4:'96-1',96.5:'96-1',96.6:'96-1',96.7:'96-1',96.8:'96-1',\
96.9:'96-1',97:'97-1',97.1:'97-1',97.2:'97-1',97.3:'97-1',97.4:'97-1',97.5:'97-1',\
97.6:'97-1',97.7:'97-1',97.8:'97-1',97.9:'97-1',98:'98-1',98.1:'98-1',98.2:'98-1',\
98.3:'98-1',98.4:'98-1',98.5:'98-1',98.6:'98-1',98.7:'98-1',98.8:'98-1',98.9:'98-1',\
99:'99-1',99.1:'99-1',99.2:'99-1',99.3:'99-1',99.4:'99-1',99.5:'99-1',99.6:'99-1',\
99.7:'99-1',99.8:'99-1',99.9:'99-1'}                                       
                                        

odds_order = {'1/20':0,'1/10':1,'1/5':2,'2/5':3,'1/2':4,'3/5':5,'4/5':6,'1':7,'6/5':8,'7/5':9,'3/2':10,'8/5':11,\
'9/5':12,'2/1':13,'5/2':14,'3/1':15,'7/2':16,'4/1':17,'9/2':18,'5-1':19,'6-1':20,'7-1':21,'8-1':22,\
'9-1':23,'10-1':24,'11-1':25,'12-1':26,'13-1':27,'14-1':28,'15-1':29,'16-1':30,'17-1':31,'18-1':32,\
'19-1':33,'20-1':34,'21-1':35,'22-1':36,'23-1':37,'24-1':38,'25-1':39,'26-1':40,'27-1':41,'28-1':42,\
'29-1':43,'30-1':44,'31-1':45,'32-1':46,'33-1':47,'34-1':48,'35-1':49,'36-1':50,'37-1':51,'38-1':52,\
'39-1':53,'40-1':54,'41-1':55,'42-1':56,'43-1':57,'44-1':58,'45-1':59,'46-1':60,'47-1':61,\
'48-1':62,'49-1':63,'50-1':64,'51-1':65,'52-1':66,'53-1':67,'54-1':68,'55-1':69,'56-1':70,\
'57-1':71,'58-1':72,'59-1':73,'60-1':74,'61-1':75,'62-1':76,'63-1':77,'64-1':78,'65-1':79,\
'66-1':80,'67-1':81,'68-1':82,'69-1':83,'70-1':84,'71-1':85,'72-1':86,'73-1':87,'74-1':88,\
'75-1':89,'76-1':90,'77-1':91,'78-1':92,'79-1':93,'80-1':94,'81-1':95,'82-1':96,'83-1':97,\
'84-1':98,'85-1':99,'86-1':100,'87-1':101,'88-1':102,'89-1':103,'90-1':104,'91-1':105,\
'92-1':106,'93-1':107,'94-1':108,'95-1':109,'96-1':110,'97-1':111,'98-1':112,'99-1':113}       