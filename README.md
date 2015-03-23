#summary Инструкция

= Как пользоваться скриптом =

  # Скачайте и установите [http://python.org/ Python 2.5] или старше, например [http://python.org/ftp/python/2.5.4/python-2.5.4.msi отсюда].
  # Скачайте скрипт [http://viu.googlecode.com/files/viu.rar отсюда] и распакуйте в любую папку (например, в *D:\viu*).
  # Скачайте и распакуйте в ту же папку библиотеку [http://code.google.com/p/uimge/ uimge] например отсюда: http://uimge.googlecode.com/files/guimge-0.1.2-0.zip
  # Также скачайте и установите [http://sourceforge.net/projects/virtualdubmod/files/VirtualDubMod/VirtualDubMod_1_5_10_2_All_inclusive.zip VirtualDubMod] (в файлах *getframesnum.bat* и *getframeavs.bat* из папки скрипта замените "D:\Progs\VirtualDubMod_1_5_10_2_All_inclusive" на свой путь, а также *D:\viu* на путь к папке куда вы распаковали скрипт) и [http://avisynth.org AviSynth].
  # Всё! Скрипт практически готов к работе, осталось лишь изменить значения нескольких параметров в файле *viu.py* на ваши и запустить этот файл двойным щелчком или из консоли:
{{{
python.exe viu.py
}}}

После того как скрипт отработает, он запишет результат в файл *out.txt* в виде BB-кода.

= Параметры =

  * *start_n = 2145* - кадр с которого начинать, это необходимо для продолжения если скрипт (а точнее, ffmpeg или VirtualDub) зависнет, в начале лучше установить 0.
  * *first_frame_time = 5* - через сколько секунд после начала видео начинать снимать скриншоты, по-умолчанию 5.
  * *frames_num = 5* - кол-во скриншотов с одного видео, по-умолчанию 5.
  * *video_folder = "J:\Music\Video\Scooter\Live"* - папка с видео, замените на свою.
  * *screenshots_folder = "screenshots"* - временная папка для скриншотов.
  * *viu_log = "viu_log.txt"* - лог файл.
