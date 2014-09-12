# coding: utf-8

from django.contrib.auth import login, authenticate
from django.contrib.sessions.models import Session
from django.http import HttpResponse

from authentication.models import User, DEFAULT_PASSWORD
from authentication.utils import send_sms, re_phone

from core.views import BaseView

from redis_connector import redis


class SessionidView(BaseView):
    """"
    View для тестирования авторизации через sessionid в url
    """

    def is_authenticated(self, request):
        if request.user.is_authenticated():
            print('авторизирован id={}'.format(request.user.id))
        else:
            print('не авторизирован')

    def get(self, request):
        self.is_authenticated(request)
        return HttpResponse()

    def post(self, request):
        self.is_authenticated(request)
        return HttpResponse()

    def put(self, request):
        self.is_authenticated(request)
        return HttpResponse()

    def delete(self, request):
        self.is_authenticated(request)
        return HttpResponse()


class PhoneMixin(object):
    def get_phone(self, request):
        phone = request.POST.get('phone')
        if not phone:
            return self.render_internal_error('Empty phone')
        if not re_phone.match(phone):
            return self.render_internal_error('Invalid phone')
        self.phone = phone

    def get_user(self, phone, resend):
        if resend:
            self.sms_code = User().generate_sms_code()
        try:
            user = User.objects.get(phone=phone)
            self.user = user
            if not user.is_active:
                return self.render_internal_error('User is blocked')
        except User.DoesNotExist:
            pass
        if resend:
            redis.setex('nedviga_user_sms_{}'.format(phone), self.sms_code, 300)


class PreLogin(BaseView, PhoneMixin):
    def post(self, request):
        """
        :param request:
        :return:
        По номеру телефона зарегистрированного пользователя отсылает sms с кодом авторизации на этот номер
        Варианты ошибок:
        'Empty phone' - пустой телефон
        'Invalid phone' - неверный формат номера
        'User not registered' - пользователь с таким телефоном не зарегистрирован
        'User is blocked' - пользователь заблокирован
        """
        # TODO - сделать защиту от частой отправки смс
        # TODO - сделать на фронте возможность повторной отправки смс
        result = self.get_phone(request)
        if result:
            return result

        result = self.get_user(self.phone, True)
        if result:
            return result

        send_sms(self.phone, self.sms_code)
        return self.render_empty_success()


class Login(BaseView, PhoneMixin):

    def get_sms_code(self, request):
        sms_code = request.POST.get('key')
        user_sms_code = redis.get('nedviga_user_sms_{}'.format(self.phone))
        if user_sms_code:
            if int(user_sms_code) == int(sms_code):
                if not User.objects.filter(phone=self.phone):
                    self.user = User()
                    self.user.phone = self.phone
                    self.user.set_password(DEFAULT_PASSWORD)
                    self.user.save()
            else:
                return self.render_internal_error('Invalid sms-code')
        else:
            return self.render_internal_error('Sms-code expired')

    def post(self, request):
        """
        :param request:
        :param phone: номер телефона
        :param sms_code: sms код проверки
        :return:
        Авторизует пользователя по номеру телефона и sms-коду
        Варианты ошибок:
        'User not registered' - пользователь с таким телефоном не зарегистрирован
        'User is blocked' - пользователь заблокирован
        'Invalid sms-code' - неверный sms-код авторизации
        """
        result = self.get_phone(request)
        if result:
            return result

        result = self.get_user(self.phone, False)
        if result:
            return result

        result = self.get_sms_code(request)
        if result:
            return result

        # еще раз вытаскиваем юзера, чтобы django его авторизировала, просто User передать нельзя
        self.user = authenticate(phone=self.phone, password=DEFAULT_PASSWORD)

        # удаляем все другие сессии этого пользователя, чтобы был залогинен всегда с одного устройства
        my_old_sessions = Session.objects.all()
        for row in my_old_sessions:
            if row.get_decoded().get("_auth_user_id") == self.user.id:
                row.delete()
        # теперь спокойно логиним
        login(request, self.user)
        return self.render_json_response(data={'sessionid': request.session.session_key})


