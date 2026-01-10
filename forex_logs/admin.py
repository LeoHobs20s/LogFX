from django.contrib import admin

from forex_logs.models import Pair, Price

admin.site.register(Pair)
admin.site.register(Price)
