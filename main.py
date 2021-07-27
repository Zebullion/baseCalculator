from tkinter import Tk, Entry, Label,Button
from tkinter.font import Font
a = 12
b=13
# wn = window
#entryExp = enter expression
def main():
  wn = Tk()
  wn.title('Base Calculator')

  fontStyle = Font(family = 'Times New Roman',size = 20)

  entryExp = Entry(master=wn,width = 25,font=fontStyle)
  labelEq = Label(master=wn, text = ' = ',font=fontStyle)
  labelResult = Label(master=wn,text='0',font=fontStyle)
  buttonCalc = Button(master=wn, text = 'Calculate',font=fontStyle, 
                      command=lambda : calculate(entryExp,labelResult))

  entryExp.grid(row = 0, column = 0)
  labelEq.grid(row=0,column=1)
  buttonCalc.grid(row=1)
  labelResult.grid(row=0,column=2)

  wn.mainloop()


def calculate(expression, LabelResult):
  """Evaluate the expression in the entry widget
  Update the label with the result on row 0.
  """

  e = expression.get()
  eParts = splitUp(e)
  print(eParts)
  newE = rebuildExpression(eParts)
  result = eval(newE)
  LabelResult['text'] = result


def splitUp(expression) ->list:
  """ Break the Expression into its parts and return list:
  [Left Number, Right Number, Operator] or [Number]
  """

  parts = []


  if '*' in expression:
    parts = expression.split('*')
    parts.append('*')

  elif '/' in expression:
    parts = expression.split('/')
    parts.append('/')

  elif '-' in expression:
    parts = expression.split('-')
    parts.append('-')

  elif '+' in expression:
    parts = expression.split('+')
    parts.append('+')


  return parts
  



def rebuildExpression(parts):
  """Converts all numbers to decimal and returns the expression with
  the decimal numbers.
  """
  pass


if __name__ == '__main__':
  main()
