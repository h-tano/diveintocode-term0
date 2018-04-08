course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}


def find_person(want_to_find_person):
    #   各コースで在籍判定および結果の表示を行う
    if type(want_to_find_person) == set:
        want_to_find_person = set(want_to_find_person)
    else:
        print("入力をset形式にしてください。")
        print("例：{'Aさん','Bさん'}")
        return None

    for course_name in course_dict.keys():
        # コースに探したい人が在籍しているか積を取って確認する
        result = course_dict[course_name] & want_to_find_person
        # 探したい人が何人在籍しているかを調べる
        number = len(result)
        # 探したい人の在籍人数が０人なら"〇〇さんは在籍していません"と表示する
        if number == 0:
            print("{}に{}は在籍していません。".format(course_name, want_to_find_person))
        # 探したい人の在籍人数が１人かつ探したい人の人数が複数名なら"〇〇さんのみ在籍しています"と表示する
        elif number == 1 and len(want_to_find_person) > 1:
            print("{}に{}のみ在籍しています。".format(course_name, result))
        # 探したい人の在籍人数が2人以上なら"〇〇さんは在籍しています"と表示する
        else:
            print("{}に{}は在籍しています。".format(course_name, result))


def main():
    want_to_find_person = ['Cさん', 'Aさん']
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
