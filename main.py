import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView

class DeutschFunPro(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        
        # تحميل البيانات
        with open('dictionary.json', 'r', encoding='utf-8') as f:
            self.dictionary = json.load(f)
        with open('all_lessons.json', 'r', encoding='utf-8') as f:
            self.lessons = json.load(f)
            
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # العنوان الرئيسية
        title = MDLabel(
            text="DeutschFun Pro 🇩🇪",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height=50
        )
        
        sub_title = MDLabel(
            text=f"القاموس: {len(self.dictionary)} كلمة | الدروس: {len(self.lessons)} درساً",
            halign="center",
            font_style="Subtitle1",
            size_hint_y=None,
            height=30
        )
        
        # قائمة العرض
        scroll = MDScrollView()
        list_view = MDList()
        
        # إضافة أول 20 كلمة للعرض التجريبي في الواجهة
        for word in self.dictionary[:20]:
            item = OneLineListItem(text=f"{word['german']} - {word['arabic']}")
            list_view.add_widget(item)
            
        scroll.add_widget(list_view)
        
        layout.add_widget(title)
        layout.add_widget(sub_title)
        layout.add_widget(scroll)
        screen.add_widget(layout)
        
        return screen

if __name__ == "__main__":
    DeutschFunPro().run()
