# from django import forms


# class ListTextWidget(forms.TextInput):
#     def __init__(self, data_list, name, *args, **kwargs):
#         super(ListTextWidget, self).__init__(*args, **kwargs)
#         self._name = name
#         self._list = data_list
#         self.attrs.update({'list': 'list__%s' % self._name})
#         self.attrs.update(
#             {'placeholder': 'e.g. Part-time job, My Bank Account'})

#     def render(self, name, value, attrs=None, renderer=None):
#         text_html = super(ListTextWidget, self).render(
#             name, value, attrs=attrs)
#         data_list = '<datalist id="list__%s">' % self._name
#         for item in self._list:
#             data_list += '<option value="%s">' % item
#         data_list += '</datalist>'

#         return (text_html + data_list)
