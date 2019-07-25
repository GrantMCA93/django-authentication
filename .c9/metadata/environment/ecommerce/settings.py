{"filter":false,"title":"settings.py","tooltip":"/ecommerce/settings.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":82,"column":0},"end":{"row":95,"column":21},"action":"remove","lines":["# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","","","# Password validation"],"id":64},{"start":{"row":82,"column":0},"end":{"row":98,"column":21},"action":"insert","lines":["# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }","","","","# Password validation"]}]]},"ace":{"folds":[],"scrolltop":977.5999755859375,"scrollleft":0,"selection":{"start":{"row":84,"column":0},"end":{"row":84,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":66,"state":"start","mode":"ace/mode/python"}},"timestamp":1564021627567,"hash":"674eeee517b12622ffb54c84a00eb4400bd78c45"}