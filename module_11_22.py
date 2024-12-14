# Импортируем нужные библиотеки
import inspect
from pprint import pprint

# Объявим функцию
def introspection_info(obj):
  # Создадим пустой словарь значений
  info_dic = {}
  # Отловим ошибки ввода
  try:
    print(f'Исследуем объект {obj}')
  except AttributeError as ex:
    print(f'Ошибка {ex} значение {ex.args}')
  # К какому модулю принадлежит объект
  print('Модуль, к которому объект принадлежит:', inspect.getmodule(obj), sep='\n\t')
  info_dic['Модуль'] = inspect.getmodule(obj)
  # Тип объекта
  print('Тип объекта: ', type(obj), sep='\n\t')
  info_dic['Тип'] = type(obj)
  # Атрибуты объекта
  print('Атрибуты объекта: ', dir(obj), sep='\n\t')
  info_dic['Атрибуты'] = dir(obj)
  # Создадим пустой список методов
  metod_lst = []
  # Пробежим по методам
  for atr_name in dir(obj):
    atr = getattr(obj, atr_name)
    # Если к методу можно обратиться то добавим в лист
    if callable(atr):
      metod_lst.append(atr)
    print(f'Метод - Имя: {atr_name} Тип: {str(type(atr))} Исполняемый: {callable(atr)}')
    info_dic['Методы'] = metod_lst
  # Для функций
  if inspect.isfunction(obj):
    sig_vol = inspect.signature(obj)
    print('Передаваемый в функцию параметры:', sig_vol.parameters, sep='\n\t')
    param_list = []
    # пробежим по параметрам
    for p_name, param in sig_vol.parameters.items():
      # Имя и значение по умолчанию (если есть)
      param_list.append([param.name, param.default])
      info_dic['Параметры'] = param_list
  # Вернем итоговый словарь
  return info_dic

# Исследуем простое число
info = introspection_info(42)
pprint(info)

# Исследуем встроенную функцию print()
info = introspection_info(print)
pprint(info)

# Для теста объявим класс
class TestClass():
  # Класс в данном случае ничего не делает
  pass

# Создадим экземпляр класса
clas_1 = TestClass()

# Проведем инспекцию
info = introspection_info(clas_1)
pprint(info)

