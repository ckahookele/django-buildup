from django.conf.urls import patterns, url
urlpatterns = patterns('', url(r'^$', 'buildup.views.hello', name='hello'),
                       url(r'^time/$', 'buildup.views.time', name='time'),
                       url(r'^random/$', 'buildup.views.random', name = 'random'),
                       url(r'^hello/(?P<yourname>.+)/$', 'buildup.views.hello_name', name = 'hello_name'),
                       url(r'^speak/(?P<sentence>.+)/$', 'buildup.views.sentence', name = 'sentence'),
                       
                       url(r'^hello_template/(?P<yourname>\w+)/$', 'buildup.views.hello_template', name = 'hello_template'),
                       url(r'^time_template/$', 'buildup.views.time_template', name='time_template'),
                       url(r'^random_template/$', 'buildup.views.random_template', name = 'random_template'),
                       url(r'^speak_template/(?P<sentence>.+)/$', 'buildup.views.speak_template', name = 'speak_template'),
                       url(r'^facts/$', 'buildup.views.all_facts', name = 'all_facts')
                       url(r'^facts/new/$', 'buildup.views.new_fact', name='new_fact')
                      )
                           