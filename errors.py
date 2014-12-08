
class ErrorMsg(object):
    def __init__(self, message, line, column):
        self.msg = message
        self.line = line
        self.column = column

    def __str__(self):
        return "Error: {0} (line: {1}, position: {2})".format( self.msg, self.line, self.column )

class WarningMsg(object):
    def __init__(self, message, line, column):
        self.msg = message
        self.line = line
        self.column = column

    def __str__(self):
        return "Warning: {0} (line: {1}, position: {2})".format( self.msg, self.line, self.column )
