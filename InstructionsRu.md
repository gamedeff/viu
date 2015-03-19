# Как пользоваться скриптом #

  1. Скачайте и установите [Python 2.5](http://python.org/) или старше, например [отсюда](http://python.org/ftp/python/2.5.4/python-2.5.4.msi).
  1. Скачайте скрипт [отсюда](http://viu.googlecode.com/files/viu.rar) и распакуйте в любую папку (например, в **D:\viu**).
  1. Скачайте и распакуйте в ту же папку библиотеку [uimge](http://code.google.com/p/uimge/) например отсюда: http://uimge.googlecode.com/files/guimge-0.1.2-0.zip
  1. Также скачайте и установите [VirtualDubMod](http://sourceforge.net/projects/virtualdubmod/files/VirtualDubMod/VirtualDubMod_1_5_10_2_All_inclusive.zip) (в файлах **getframesnum.bat** и **getframeavs.bat** из папки скрипта замените "D:\Progs\VirtualDubMod\_1\_5\_10\_2\_All\_inclusive" на свой путь, а также **D:\viu** на путь к папке куда вы распаковали скрипт) и [AviSynth](http://avisynth.org).
  1. Всё! Скрипт практически готов к работе, осталось лишь изменить значения нескольких параметров в файле **viu.py** на ваши и запустить этот файл двойным щелчком или из консоли:
```
python.exe viu.py
```

После того как скрипт отработает, он запишет результат в файл **out.txt** в виде BB-кода.

# Параметры #

  * **start\_n = 2145** - кадр с которого начинать, это необходимо для продолжения если скрипт (а точнее, ffmpeg или VirtualDub) зависнет, в начале лучше установить 0.
  * **first\_frame\_time = 5** - через сколько секунд после начала видео начинать снимать скриншоты, по-умолчанию 5.
  * **frames\_num = 5** - кол-во скриншотов с одного видео, по-умолчанию 5.
  * **video\_folder = "J:\Music\Video\Scooter\Live"** - папка с видео, замените на свою.
  * **screenshots\_folder = "screenshots"** - временная папка для скриншотов.
  * **viu\_log = "viu\_log.txt"** - лог файл.