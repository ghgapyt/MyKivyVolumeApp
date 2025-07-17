from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
import webbrowser

try:
    from jnius import autoclass
    Context = autoclass('android.content.Context')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity
    audio_service = activity.getSystemService(Context.AUDIO_SERVICE)
    AudioManager = autoclass('android.media.AudioManager')
    android_ok = True
except Exception as e:
    print("AudioManager not available:", e)
    audio_service = None
    AudioManager = None
    android_ok = False

Window.clearcolor = get_color_from_hex("#121212")

class VolumeControl(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        heading = Label(
            text='PKTW.THINKING',
            font_size='34sp',
            bold=True,
            color=get_color_from_hex("#00FFAA"),
            size_hint=(1, None),
            height=60
        )
        self.add_widget(heading)

        insta_btn = Button(
            text='@ig_gap_',
            font_size='20sp',
            background_color=(0, 0, 0, 0),
            color=get_color_from_hex("#44AADD"),
            size_hint=(1, None),
            height=50
        )
        insta_btn.bind(on_press=lambda x: webbrowser.open("https://instagram.com/ig_gap_"))
        self.add_widget(insta_btn)

        self.add_real_slider("Media Volume", AudioManager.STREAM_MUSIC)
        self.add_real_slider("Ringtone Volume", AudioManager.STREAM_RING)
        self.add_real_slider("Alarm Volume", AudioManager.STREAM_ALARM)
        self.add_real_slider("Notification Volume", AudioManager.STREAM_NOTIFICATION)

        footer = Label(
            text='Made with Kivy',
            font_size='16sp',
            color=get_color_from_hex("#AAAAAA"),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(footer)

    def add_real_slider(self, label_text, stream_type):
        title = Label(
            text=label_text,
            font_size='22sp',
            color=get_color_from_hex("#FFFFFF"),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(title)

        if android_ok:
            try:
                max_vol = audio_service.getStreamMaxVolume(stream_type)
                current_vol = audio_service.getStreamVolume(stream_type)
            except Exception as e:
                print("Error getting volume:", e)
                max_vol = 100
                current_vol = 0
        else:
            max_vol = 100
            current_vol = 0

        value_label = Label(
            text=f"{current_vol}/{max_vol}",
            font_size='20sp',
            color=get_color_from_hex("#00FFAA"),
            size_hint=(1, None),
            height=30
        )
        self.add_widget(value_label)

        slider = Slider(
            min=0,
            max=max_vol,
            value=current_vol,
            step=1,
            size_hint=(1, None),
            height=50
        )
        slider.bind(value=lambda instance, val: self.set_volume(stream_type, value_label, val, max_vol))
        self.add_widget(slider)

    def set_volume(self, stream_type, label_widget, value, max_vol):
        v = int(value)
        label_widget.text = f"{v}/{max_vol}"
        if android_ok:
            try:
                audio_service.setStreamVolume(stream_type, v, 0)
            except Exception as e:
                print("Volume change error:", e)

class VolumeApp(App):
    def build(self):
        return VolumeControl()

if __name__ == '__main__':
    VolumeApp().run()
