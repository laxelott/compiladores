from pprint import pprint
from yaml import load, dump
from enum import Enum
import re
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Node:
    name = ''
    def __init__(self, value) -> None:
        self.value = value
    def match(str) -> str:
        return ''
    def __str__(self) -> str:
        return repr(self.value)

def parseLexical(lexicalFileName) -> tuple[list[Node]]:
    identifiers = []
    with open(lexicalFileName) as file:
        lexical = load(file.buffer, Loader=Loader)
        tokens = lexical['tokens']
        tokenOrder = lexical['options']['tokenOrder']
        showOnly = lexical['options']['showOnly']
        ignore = lexical['options']['ignore']
    nodeList = {}
    ignoreList = []
    showList = []
    for token in tokens:
        if token in tokenOrder:
            identifiers.append(token)
            
            flags = 0        
            body = {
                'name': tokens[token]['name'],
            }
            if 'flags' in tokens[token]['match']:
                flagsRaw = tokens[token]['match']['flags']
                for flag in flagsRaw:
                    if flag == 'multiline':
                        flags = flags|re.MULTILINE
                    elif flag == 'ignore case':
                        flags = flags|re.IGNORECASE
                    elif flag == 'dotall':
                        flags = flags|re.DOTALL
            
            if 'elements' in tokens[token]:
                body['elements'] = Enum('elements', tokens[token]['elements'])
                def match(str) -> str:
                    print(tokens[token])
                    elementList = [item.value for item in tokens[token]['elements']]
                    for item in elementList:
                        found = re.search(
                            tokens[token]['match']['regex'].replace('{ITEM}', item),
                            str,
                            flags=flags
                        )
                        if found:
                            return item
                    return ''
            else:
                def match(str):
                    if match := re.search(
                        tokens[token]['match']['regex'],
                        str,
                        flags=flags
                    ):
                        return match.group(0)
                    else:
                        return ''

            body['match'] = match
            
            node = type(token, (Node, ), body)
            nodeList[token] = node
            if token in ignore:
                ignoreList.append(node)
            if token in showOnly:
                showList.append(node)
    retList = []
    for token in tokenOrder:
        retList.append(nodeList[token])
    return retList, ignoreList, showList

def parseSyntax(syntaxFileName, nodeList):
    with open("syntax.yaml") as file:
        syntax = load(file.buffer, Loader=Loader)
    for pattern in syntax['patterns']:
        print(pattern)
        print(syntax[pattern])
