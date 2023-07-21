import os
from dotenv import load_dotenv
import unittest
from unittest import TestCase

import requests

from functions import sort_courses_by_duration, top_3_popular_name, unique_name, get_ydisk_folder

load_dotenv()


class TestUnique(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupTestUnique")

    def setUp(self):
        print('setUp')
        self.persons = [
            ['Александр Иванов', 'Денис Иванов', 'Анна Иванова'],
            ['Александр Петров', 'Денис Носков'],
            ['Анна Петрова']
        ]

    def tearDown(self):
        print('tearDown\n')

    @classmethod
    def tearDownClass(cls):
        print("tearDownTestUnique")

    def test_compliance(self):
        print('test_compliance')
        result = unique_name(self.persons)
        expected = 'Уникальные имена преподавателей: Александр, Анна, Денис'
        self.assertEqual(result, expected)

    @unittest.expectedFailure
    def test_wrong_name_failure(self):
        print('test_wrong_name_failure')
        persons = [
            ['Александр Иванов', 'Денис Иванов', 'Анна Иванова'],
            ['Александр Петров', 'Денис Носков'],
            [1]
        ]
        result = unique_name(persons)
        expected = 'Уникальные имена преподавателей: Александр, Анна, Денис'
        self.assertEqual(result, expected)


class TestTop3(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupTestTop3")

    @classmethod
    def tearDownClass(cls):
        print("tearDownTestTop3\n")

    def test_compliance(self):
        persons = [
            ['Александр Иванов', 'Денис Иванов', 'Анна Иванова'],
            ['Александр Петров', 'Денис Носков'],
            ['Александр Петров']
        ]
        result = 'Александр: 3 раз(а), Денис: 2 раз(а), Анна: 1 раз(а)'
        expected = top_3_popular_name(persons)
        self.assertEqual(result, expected)

    def test_each_two(self):
        persons = [
            ['Александр Иванов', 'Денис Иванов', 'Анна Иванова'],
            ['Александр Петров', 'Денис Носков'],
            ['Анна Петрова']
        ]
        result = ['Александр: 2 раз(а)', 'Анна: 2 раз(а)', 'Денис: 2 раз(а)']
        expected = top_3_popular_name(persons)
        expected = expected.split(", ")
        expected = sorted(expected)
        self.assertEqual(result, expected)

    @unittest.expectedFailure
    def test_wrong_name_failure(self):
        persons = [
            ['Александр Иванов', 'Денис Иванов', 'Анна Иванова'],
            ['Александр Петров', 'Денис Носков'],
            [1]
        ]
        result = ['Александр: 2 раз(а)', 'Анна: 2 раз(а)', 'Денис: 2 раз(а)']
        expected = top_3_popular_name(persons)
        expected = expected.split(", ")
        expected = sorted(expected)
        self.assertEqual(result, expected)


class TestSortCourses(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupTesSortCourses")

    @classmethod
    def tearDownClass(cls):
        print("tearDownTestSortCourses\n")

    def setUp(self):
        print('setUp')
        self.courses = ['Phyton', 'Java', 'Frontend']
        self.wrong_courses = ['Phyton', ':-)', 3]
        self.mentors = [
            ['Александр Иванов', 'Денис Иванов', 'Анна Иванова'],
            ['Александр Петров', 'Денис Носков'],
            ['Анна Петрова']
        ]
        self.wrong_mentors = [
            ['Александр Иванов', 'Денис Иванов', 'Анна Иванова'],
            ['Александр Петров', 'Денис Носков'],
            [1]
        ]
        self.durations = [12, 6, 8]
        self.wrong_durations = ['двенадцать', 6, 8]

    def tearDown(self):
        print('tearDown\n')

    def test_compliance(self):
        print('test_compliance')
        result = sort_courses_by_duration(self.courses, self.mentors, self.durations)
        expended = ['Java - 6 месяцев', 'Frontend - 8 месяцев', 'Phyton - 12 месяцев']

        self.assertEqual(result, expended)

    @unittest.expectedFailure
    def test_failure_month(self):
        print('test_failure_month')
        result = sort_courses_by_duration(self.courses, self.mentors, self.wrong_durations)
        expended = ['Java - 6 месяцев', '3 - 8 месяцев', 'Phyton - двенадцать месяцев']

        self.assertEqual(result, expended)

    def test_wrong_courses(self):
        print('test_wrong_courses')
        result = sort_courses_by_duration(self.wrong_courses, self.mentors, self.durations)
        expended = [':-) - 6 месяцев', '3 - 8 месяцев', 'Phyton - 12 месяцев']

        self.assertEqual(result, expended)

    def test_wrong_name(self):
        print('test_wrong_name')
        result = sort_courses_by_duration(self.courses, self.wrong_mentors, self.durations)
        expended = ['Java - 6 месяцев', 'Frontend - 8 месяцев', 'Phyton - 12 месяцев']

        self.assertEqual(result, expended)


class TestYDFolder(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupTestYDFolder")

    def setUp(self):
        print('setUp')
        self.token = os.getenv('TOKEN')
        self.path = 'Folder'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def tearDown(self):
        print('tearDown\n')

    @classmethod
    def tearDownClass(cls):
        print("tearDownTestYDFolder\n")

    def test_1_status_code(self):
        print('test_exist_folder_status_code')
        get_ydisk_folder(self.token, self.path)
        url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + self.path
        response = requests.get(url=url, headers=self.headers)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_2_in_list_dir(self):
        print('test_exist_folder_in_list_dir')
        url = 'https://cloud-api.yandex.net/v1/disk/resources?path=%2F'
        response = requests.get(url=url, headers=self.headers)
        result = response.json()
        folders = [i['name'] for i in result['_embedded']['items']]
        self.assertIn(self.path, folders)

    def test_3_wrong_token(self):
        print('test_3_wrong_token')
        token = '123456'
        result = get_ydisk_folder(token, self.path)
        expended = 401
        self.assertEqual(result, expended)

    def test_4_wrong_name(self):
        print('test_3_wrong_name')
        path = ''
        result = get_ydisk_folder(self.token, path)
        expended = 400
        self.assertEqual(result, expended)
