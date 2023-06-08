from enums import *
from syntax import Token

class ParserError(Exception):
    pass

class PatternFinder:
    CONDITION_PATTERN = 1
    CONDITION_VALUE = 2
    CONDITION_TYPE = 3
    FINAL = False
    
    tokens: list[Token]
    pattern: list[dict]
    def __init__(self, tokens) -> list:
        self.tokens = tokens
    
    def getCondition(self, step):
        if not 'match' in step:
            return False
        
        if type(step['match']) is list:
            return self.CONDITION_PATTERN
        elif type(step['match']) is str:
            return self.CONDITION_VALUE
        elif issubclass(step['match'], Node):
            return self.CONDITION_TYPE
        else:
            return False

    def processMatch(self, step):
        result = [self.tokens[0].node]
        del self.tokens[0]
        if 'next' in step:
            result.extend(self.findRegularDefinition(step['next']))
        elif 'final' in step:
            if step['final']:
                self.FINAL = True
        return result

    def processStep(self, step, condition):
        if len(self.tokens) == 0:
            return []
        
        if condition == self.CONDITION_PATTERN:
            result = self.findRegularDefinition(step['match'])
            if (len(result) == 0 and step['required']):
                return False
        elif condition == self.CONDITION_VALUE:
            if (self.tokens[0].node.value == step['match']):
                result = self.processMatch(step)
            elif step['required']:
                return False
            else:
                result = []
        elif condition == self.CONDITION_TYPE:
            if (type(self.tokens[0].node) is step['match']):
                result = self.processMatch(step)
            elif step['required']:
                return False
            else:
                result = []
        else:
            return False
    
        if 'looping' in step and result:
            if step['looping']:
                while(loopResult := self.processStep(step, condition)):
                    result.extend(loopResult)
    
        return result

    def findRegularDefinition(self, pattern):
        if len(self.tokens) == 0:
            return []
        
        result = []
        for step in pattern:
            if not (condition := self.getCondition(step)):
                raise ParserError("Parser Error: match required!")
            
            if (stepResult := self.processStep(step, condition)) == False:
                raise ParserError(f"Error: {step['error']}!")
            
            result.extend(stepResult)
            
            if self.FINAL:
                self.FINAL = False
                break
            
        return result
