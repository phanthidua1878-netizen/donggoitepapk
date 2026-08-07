from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class StudyApp(App):

  def build(self):
    layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
    self.label = Label(
        text='Chào bạn! Chọn môn học để AI ra bài tập:', font_size=18
    )
    layout.add_widget(self.label)

    subjects = ['Toán học', 'Ngữ văn', 'Tiếng Anh', 'Vật lý']
    for sub in subjects:
      btn = Button(text=sub, size_hint_y=None, height=50)
      btn.bind(on_press=self.on_subject_click)
      layout.add_widget(btn)

    return layout

  def on_subject_click(self, instance):
    self.label.text = (
        f'AI đang tạo bài tập môn: {instance.text} cho lớp của bạn...'
    )


if __name__ == '__main__':
  StudyApp().run()