import requests


courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def sort_courses_by_duration(courses, mentors, durations):
    result = []
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for id_cours, course in enumerate(courses_list):
        key = course['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id_cours)
    durations_dict = dict(sorted(durations_dict.items()))
    for keys, values in durations_dict.items():
        for id_dur, course in enumerate(courses_list):
            if id_dur in values:
                result.append(f'{courses_list[id_dur]["title"]} - {keys} месяцев')
    return result


def top_3_popular_name(list_):
    all_list = []
    for group in list_:
        for name in group:
            all_list.append(name)
    all_names_list = []
    for mentor in all_list:
        name = ' '.join(mentor.split(' ')[:-1])
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[0:3]
    return f'{top_3[0][0]}: {top_3[0][1]} раз(а), ' \
           f'{top_3[1][0]}: {top_3[1][1]} раз(а), ' \
           f'{top_3[2][0]}: {top_3[2][1]} раз(а)'


def unique_name(list_):
    all_list = []
    for group in list_:
        for name in group:
            all_list.append(name)
    all_names_list = []
    for mentor in all_list:
        name = ' '.join(mentor.split(' ')[:-1])
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    list.sort(unique_names)
    return f"Уникальные имена преподавателей: {', '.join(unique_names)}"


def get_ydisk_folder(token, ydisk_folder_path):
    """
    Создает папку на яндекс диске методом put.
    :param: ydisk_folder_path: расположение и имя папки
    :return: в случае ошибки - код ошибки
    """
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    params = {"path": ydisk_folder_path}
    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code
