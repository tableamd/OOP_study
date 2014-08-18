#coding:utf-8
class Kame:
    #コンストラクタ
    def __init__(self, name, kouraColor, lifeTime, sex):
        self.name = name  # 名前
        self.kouraColor = kouraColor  # 甲羅の色
        self.lifeTime = lifeTime  # 寿命
        self.sex = sex  # 性別

    #歩くメソッド
    def walk(self):
        #歩く命令をここに書く 
        print "walking!"
        pass

    #食べるメソッド
    def eat(self):
        #食べる命令をここに書く
        print "eating!"
        pass

    #寝るメソッド
    def sleep(self):
        #寝る命令をここに書く
        print "sleeping!"
        pass