from rest_framework.views import APIView
from rest_framework.response import Response


class EnumView(APIView):
    permission_classes = []

    def get(self, *args, **kwargs):
        enums = self.enum_class.get_as_tuple_list()

        context = []
        for enum in enums:
            _id = enum[1]
            i18n = self.enum_class.i18n[_id]

            context.append({
                'id': _id,
                'i18n': i18n,
            })

        return Response(context)
