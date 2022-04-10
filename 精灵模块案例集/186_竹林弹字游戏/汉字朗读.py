import pyttsx3
# 初始化， 必须要有奥
engine = pyttsx3.init()

engine.say('语音合成开始')
engine.say('我会说中文了，开森，开森')

#注意，没有本句话是没有声音的
engine.runAndWait()
