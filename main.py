from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Arka plan rengini ayarlayalım (Opsiyonel)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class HesapMakinesi(App):
    def build(self):
        self.operators = [',', '.', '-', '+', '/', '*', '%']
        self.gecmis_listesi = []

        # Ana Düzen (Dikey)
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # 1. Geçmiş Ekranı (Kaydırılabilir)
        self.scroll = ScrollView(size_hint=(1, 0.3))
        self.gecmis_ekrani = Label(
            text="",
            color=(0.3, 0.3, 0.3, 1),
            font_size='15sp',
            halign='right',
            valign='bottom',
            size_hint_y=None
        )
        self.gecmis_ekrani.bind(texture_size=self.gecmis_ekrani.setter('size'))
        self.scroll.add_widget(self.gecmis_ekrani)
        self.main_layout.add_widget(self.scroll)

        # 2. Ana Giriş Ekranı
        self.ekran = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size='40sp',
            size_hint=(1, 0.2),
            background_color=(1, 1, 1, 1)
        )
        self.main_layout.add_widget(self.ekran)

        # 3. Butonlar (Izgara Düzeni)
        self.buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.5))
        
        butonlar = [
            '.', 'AC', 'C', '/',   
            '1', '2', '3', '*',
            '4', '5', '6', '-',
            '7', '8', '9', '+',
            ',', '0', '%', '='
        ]

        for buton in butonlar:
            btn = Button(
                text=buton,
                font_size='20sp',
                background_normal='',
                background_color=(0.8, 0.8, 0.8, 1),
                color=(0, 0, 0, 1)
            )
            btn.bind(on_press=self.on_button_click)
            self.buttons_layout.add_widget(btn)

        self.main_layout.add_widget(self.buttons_layout)
        return self.main_layout

    def on_button_click(self, instance):
        tus = instance.text
        mevcut = self.ekran.text

        if tus == 'AC':
            self.ekran.text = ""
        elif tus == 'C':
            self.ekran.text = mevcut[:-1]
        elif tus == '=':
            self.hesapla()
        else:
            # Operatör Kontrolü
            if mevcut and tus in self.operators and mevcut[-1] in self.operators:
                return
            if not mevcut and tus in self.operators and tus != '-':
                return
            self.ekran.text += tus

    def hesapla(self):
        islem = self.ekran.text.replace(',', '.')
        if not islem or islem[-1] in self.operators:
            return

        try:
            sonuc = str(eval(islem))
            # Geçmişe ekle
            self.gecmis_listesi.append(f"{islem} = {sonuc}")
            if len(self.gecmis_listesi) > 20:
                self.gecmis_listesi.pop(0)
            
            self.gecmis_ekrani.text = "\n".join(self.gecmis_listesi)
            self.ekran.text = sonuc
        except Exception:
            self.ekran.text = "Hata"

if __name__ == "__main__":
    HesapMakinesi().run()
