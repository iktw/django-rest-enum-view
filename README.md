# django-rest-enum-view
Extends django enumerify

Requirements
-
* pip install django-enumerify

Usage
-
```
class MyEnumView(EnumView):
    enum_class = MyEnumClass
```

Response
-
```
[
    {
        "i18n": "Default",
        "id": 0
    },
]
```
