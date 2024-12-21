chinese=[
    "请输入正确的文件路径，或更改应用程序的名称。",
    "请输入正确的文件名。",
    "未找到此文件。",
    "没有指定正确的参数。",
    "无法运行此程序"
]

english=[
    "please input a right file path, or change the application's name.",
    "Please input a right filename.",
    "This file was not found.",
    "The correct parameters are not specified.",
    "This program cannot be run."
]

spanish=[
    "Ingrese una ruta de archivo correcta o cambie el nombre de la aplicación",
    "Por favor, introduzca un nombre de archivo correcto",
    "Este archivo no fue encontrado",
    "No se especifican los parámetros correctos"
    "Este programa no se puede ejecutar"
]

french=[
    "« Veuillez saisir un chemin d’accès au fichier droit ou changer le nom de l’application. »",
    "« Veuillez saisir un nom de fichier correct. »",
    "« Ce fichier n’a pas été retrouvé. »",
    "« Les paramètres corrects ne sont pas spécifiés. »",
    "Ce programme ne peut pas être exécuté"
]

russian=[
    "«Пожалуйста, введите правильный путь к файлу или измените имя приложения».",
    "Пожалуйста, введите правильное имя файла.",
    "«Этот файл не был найден».",
    "«Правильные параметры не указаны».",
    "Эта программа не может быть запущена"
]

language={
    'chinese':chinese,      
    'english':english,
    'spanish':spanish,
    'french':french,
    'russian':russian
          }

def inthes(lang,ind):
    try:return language[lang][ind]
    except:return language['english'][ind]