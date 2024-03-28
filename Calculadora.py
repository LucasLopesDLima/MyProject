from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        # Criamos uma lista de operadores e alguns valores úteis que usaremos mais tarde.
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        # Criamos um layout principal (main_layout) com orientação vertical e adicionamos um widget TextInput somente leitura a ele.
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)

        # Criamos uma lista aninhada de listas contendo os botões para a calculadora.
        buttons = [["7", "8", "9", "/"],
                   ["4", "5", "6", "*"],
                   ["1", "2", "3", "-"],
                   [".", "0", "C", "+"]]

        # Iniciamos um loop sobre os botões. Para cada lista aninhada, criamos um BoxLayout com orientação horizontal.
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                # Criamos um botão com o texto da lista e o vinculamos a um manipulador de eventos.
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            # Adicionamos o layout horizontal ao layout principal.
            main_layout.add_widget(h_layout)

        # Criamos um botão igual (=), o vinculamos a um manipulador de eventos e o adicionamos ao layout principal.
        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        # Retornamos o layout principal.
        return main_layout

    def on_button_press(self, instance):
        # Recebe o argumento instance para acessar qual widget chamou a função.
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Limpa o widget solution.
            self.solution.text = ""
        else:
            # Verifica se a solução possui algum valor pré-existente.
            if current and (self.last_was_operator and button_text in self.operators):
                # Não adiciona dois operadores seguidos.
                return
            # Verifica se o primeiro caractere é um operador.
            # Se for, solution não será atualizado.
            # Isso é para evitar que o usuário tenha dois operadores seguidos. Por exemplo, 1 */ não é uma declaração válida.
            elif current == "" and button_text in self.operators:
                # O primeiro valor não pode ser um valor de operador.
                return
            else:
                # Atualiza a solução.
                new_text = current + button_text
                self.solution.text = new_text
                self.last_button = button_text
                self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            # Calcula a solução e atualiza o widget solution.
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == "__main__":
    app = MainApp()
    app.run()
