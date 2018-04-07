WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

def output_schedule(study_time_list):
    '''今週の勉強予定を出力します'''
    #曜日リスト内の何番目の曜日を扱うかを表す変数
    day_count = 0
    #教科リスト内の何番目の教科を扱うかを表す変数
    subject = 1
    #教科の数を取得
    number_of_subjects = len(SUBJECT_LIST)
    #曜日ごとに予定を出力する
    for day in WEEK_LIST:
        #その日の勉強時間の値を取得
        study_times = study_time_list[day_count]
        #勉強時間が１時間以上あれば授業の科目を表示する
        if study_times != 0:
            print("{}曜日は、{}時間勉強する予定です。".format(day,study_times))
            for hour in range(study_times):
                print("{}限目 {}".format(hour+1,SUBJECT_LIST[subject]))
                subject = (subject + 1) % number_of_subjects
        #勉強時間が０の日は休みと表示する
        else:
            print("{}曜日は、お休みです。".format(day))
        day_count += 1

def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()
