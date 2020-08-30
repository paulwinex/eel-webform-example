import eel
import random


@eel.expose
def evaluate(expr):
    try:
        result = eval(expr)
        return dict(
            result=result,
            error=''
        )
    except Exception as e:
        return dict(
            result='',
            error=str(e)
        )


eel.init('web')

try:
    eel.start('index.html', size=(600, 700))
except (SystemExit, MemoryError, KeyboardInterrupt):
    pass
