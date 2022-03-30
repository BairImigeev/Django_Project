from django.test import TestCase

# Create your tests here.
import datetime
from django.test import TestCase, Client
from userside import models, forms
from django.urls import reverse


class EducatorModelTest(TestCase):

    def setUp(self):
        self.ed = models.educator.objects.create(name='Test Educator')

    def testStr(self):
        self.assertEqual(
            str(self.ed),
            'Test Educator',
        )


class CourseSearchTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.course1 = models.course.objects.create(name='Test Course 1')
        self.course2 = models.course.objects.create(name='Test Course 2')

    def testSearchByName(self):
        response = self.client.get(reverse('userside:course_list'), data={'name': 'Test Course 1'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Test Course 1',
            response.context['object_list'].first().name,
        )

    def testWithoutParams(self):
        response = self.client.get(reverse('userside:course_list'))
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.course.objects.all()),
            'При поиске без параметров должны выводиться все курсы',
        )

    def testSearchCourseByName(self):
        response = self.client.get(reverse('userside:course_list'), data={'name': 'Test Course 1'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Test Course 1',
            response.context['object_list'].first().name,
        )


# class news(forms.MyCourseCreate):
#
#     def clean(self):
#         return {self.mod, self.value}


class MyCreateCourseTestCase(TestCase):

    # def clean(self):
    #     mod = self.cleaned_data['name']
    #     value_hours = mod.length_of_time
    #
    #     return {mod, value_hours}
    #
    # def test_form_date_in_past(self):
    #     date0 = datetime.date.today() - datetime.timedelta(days=1)
    #     date1 = datetime.date.today() - datetime.timedelta(days=1)
    #     days = int(500/2/7*5)
    #     form = forms.MyCourseCreate(data={'name': 'Test_1', 'days': days, 'date_begin': date0, 'date_end': date1})
    #     self.assertFalse(form.is_valid())

    # def test_date_end_in_length(self):
    #     value_hours = 250
    #     days = int(value_hours / 2 / 7 * 5)
    #     date = datetime.date.today() + datetime.timedelta(days=days) + datetime.timedelta(days=1)
    #     form = forms.MyCourseCreate(data={'date_end': date})
    #     self.assertFalse(form.is_valid())

    # def test_renew_form_date_today(self):
    #     date = datetime.date.today()
    #     form = forms.MyCourseCreate(data={'renewal_date': date})
    #     self.assertTrue(form.is_valid())

    # def test_renew_form_date_field_label(self):
    #     form = forms.MyCourseCreate()
    #     self.assertTrue(
    #         form.fields['date_begin'].label is None or
    #         form.fields['date_end'].label == 'date_end')
    pass

