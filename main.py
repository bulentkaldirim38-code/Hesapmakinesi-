        # 2. Ana Giriş Ekranı
        self.ekran = TextInput(
            multiline=False, 
            readonly=True, 
            halign="right", 
            font_size=45, 
            background_color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )
        self.main_layout.add_widget(self.ekran)

        # 3. Butonlar (Izgara Düzeni)
        tus_takimi = GridLayout(cols=4, spacing=10, size_hint=(1, 0.5))

        butonlar = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for tus in butonlar:
            btn = Button(
                text=tus, 
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                background_normal='',
                background_color=(0.2, 0.6, 0.8, 1) if tus in self.operators or tus == '=' else (0.4, 0.4, 0.4, 1)
            )
            btn.bind(on_press=self.on_button_press)
            tus_takimi.add_widget(btn)

        self.main_layout.add_widget(tus_takimi)
        return self.main_layout

    def on_button_press(self, instance):
        mevcut_metin = self.ekran.text
        tus_metni = instance.text

        if tus_metni == 'C':
            self.ekran.text = ""
        elif tus_metni == '=':
            try:
                # Hesaplama yap ve geçmişe ekle
                sonuc = str(eval(mevcut_metin))
                gecmis_satiri = f"{mevcut_metin} = {sonuc}\n"
                self.gecmis_listesi.append(gecmis_satiri)
                
                # Geçmiş ekranını güncelle
                self.gecmis_ekrani.text = "".join(self.gecmis_listesi[-5:]) # Son 5 işlemi göster
                self.ekran.text = sonuc
            except Exception:
                self.ekran.text = "Hata!"
        else:
            # Üst üste operatör gelmesini engelle
            if mevcut_metin and tus_metni in self.operators and mevcut_metin[-1] in self.operators:
                return
            self.ekran.text += tus_metni

if __name__ == '__main__':
    HesapMakinesi().run()
