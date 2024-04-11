def extractName(rawShow: str) -> 'Option[str]':
    bracketOpen = rawShow.find('(')
    if bracketOpen > 0:
        return Some(rawShow[:bracketOpen].strip())
    else:
        return None

class Some:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Some({self.value})'
        
print("Debug: Running extractName with 'Mad Men (2007-2015)'", extractName('Mad Men (2007-2015)'))