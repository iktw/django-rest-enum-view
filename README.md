# django-rest-enum-view
Extends django enumerify

Requirements
-
* pip install djangorestframework
* pip install django-enumerify

Usage
-
```
class MyEnumView(EnumView):
    enum_class = MyEnumClass
    fields = ('i18n', 'content_key', 'css_class')
```

Response
-
```
[
    {
        "i18n": "Default",
        "id": 0,
        "content_key": "my_content_key",
        "css_class": "hello_world"
    },
]
```
