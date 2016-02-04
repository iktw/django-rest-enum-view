from rest_framework.views import APIView
from rest_framework.response import Response


class EnumView(APIView):
    permission_classes = []
    fields = ('i18n', )

    def get(self, *args, **kwargs):
        enums = self.enum_class.get_as_tuple_list()
        context = []

        for enum in enums:
            _id = enum[1]
            enum_context = {'id': _id}

            for field in self.fields:
                enum_context[field] = getattr(self.enum_class, field)[_id]

            context.append(enum_context)

        return Response(context)
