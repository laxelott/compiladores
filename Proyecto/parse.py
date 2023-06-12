from enums import *
from syntax import Token
from pprint import pprint
import inspect

class ParserError(Exception):
    pass

class PatternFinder:
    CONDITION_PATTERN = 1
    CONDITION_VALUE = 2
    CONDITION_TYPE = 3
    CONDITION_FUNCTION = 4
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
        elif inspect.isclass(step['match']):
            return self.CONDITION_TYPE
        elif callable(step['match']):
            return self.CONDITION_FUNCTION
        else:
            return False

    def runNext(self, step):
        if 'next' in step:
            return self.findRegularDefinition(step['next'])
        else:
            return []
        

    def processMatch(self, step):
        result = [self.tokens[0].node]
        del self.tokens[0]
        
        self.runNext(step)
        
        if 'final' in step:
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
            if len(result) > 0:
                self.runNext(step)
        elif condition == self.CONDITION_FUNCTION:
            result = self.findRegularDefinition(step['match']())
            if (len(result) == 0 and step['required']):
                return False
            if len(result) > 0:
                self.runNext(step)
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
                raise ParserError("Parser Error: invalid 'match'!")
            
            if (stepResult := self.processStep(step, condition)) == False:
                self.printTokens()
                raise ParserError(f"Error: {step['error']}!")
            
            result.extend(stepResult)
            
            if self.FINAL:
                self.FINAL = False
                break
            
        return result

    def printTokens(self):
        print("--- TOKENS:")
        for token in self.tokens:
            print(token.__str__())
