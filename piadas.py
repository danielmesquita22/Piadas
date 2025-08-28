
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class PiadaApp(App):
	def build(self):
		self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
		self.label = Label(text='Clique no botão para ver uma piada!', font_size=22, halign='center', valign='middle')
		self.label.bind(size=self.label.setter('text_size'))
		self.btn = Button(text='Nova Piada', size_hint=(1, 0.2), font_size=20)
		self.btn.bind(on_release=self.mostrar_piada)
		self.layout.add_widget(self.label)
		self.layout.add_widget(self.btn)
		return self.layout

	def mostrar_piada(self, instance):
		try:
			resp = requests.get('https://official-joke-api.appspot.com/random_joke', timeout=5)
			if resp.status_code == 200:
				data = resp.json()
				piada = f"{data['setup']}\n\n{data['punchline']}"
				self.label.text = piada
			else:
				self.label.text = 'Erro ao buscar piada.'
		except Exception as e:
			self.label.text = 'Erro de conexão.'

if __name__ == '__main__':
	PiadaApp().run()
