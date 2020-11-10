class Person:
    def rewriteInscription(self, inscription, new):
        inscription.update(new)

class Inscription:
    def __init__(self, text):
        self.text = text
    def update(self, newText):
        self.text = newText
    def get(self):
        return self.text

#Make inscription object first time
inscription = Inscription('Here we go')
print(inscription.get())
#Make rewriter
person = Person()
#Update inscription
person.rewriteInscription(inscription, 'Here we go again')

print(inscription.get())