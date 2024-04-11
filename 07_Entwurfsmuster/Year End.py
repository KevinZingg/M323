
def extractYearEnd(rawShow: str) -> 'Option[int]':
    dash = rawShow.find('-')
    bracketClose = rawShow.find(')')
    if dash != -1 and bracketClose > dash + 1:
        yearStr = rawShow[dash + 1:bracketClose]
        if yearStr.isdigit():
            return Some(int(yearStr))
    return None

class Some:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Some({self.value})'
        
print("Debug: Running extractYearEnd with 'Mad Men (2007-2015)'", extractYearEnd('Mad Men (2007-2015)'))
