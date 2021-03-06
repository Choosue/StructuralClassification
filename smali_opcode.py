#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HCG_FILE_NAME = 'directed_hcg_19bit.json'
# CG_FILE_NAME = 'directed_cg_19bit.json'

# INSTRUCTION_CLASS_COLOR = {
#     'nop': 0,
#     'move': 1,
#     'return': 2,
#     'const': 3,
#     'monitor': 4,
#     'check': 5,
#     'array': 6,
#     'new': 7,
#     'throw': 8,
#     'goto': 9,
#     'switch': 10,
#     'cmp': 11,
#     'if': 12,
#     'get': 13,
#     'put': 14,
#     'invoke': 15,
#     'cal': 16,
#     'convert': 17,
#     'exec': 18
# }

# INSTRUCTION_CLASSES = [
#     'nop',
#     'move',
#     'return',
#     'const',
#     'monitor',
#     'check',
#     'array',
#     'new',
#     'throw',
#     'goto',
#     'switch',
#     'cmp',
#     'if',
#     'get',
#     'put',
#     'invoke',
#     'cal',
#     'convert',
#     'exec'
# ]

# INSTRUCTION_SET_COLOR = {
#     'sput': 14,
#     'monitor-enter': 4,
#     'move/16': 1,
#     'double-to-float': 17,
#     'int-to-double': 17,
#     'aput': 14,
#     'rem-int/2addr': 16,
#     'rem-long/2addr': 16,
#     'iget-char': 13,
#     'invoke-polymorphic': 15,
#     'invoke-virtual-quick': 15,
#     'div-float': 16,
#     'aget-boolean': 13,
#     'iget-char-quick': 13,
#     'shl-int': 16,
#     'add-int/2addr': 16,
#     'or-int/lit8': 16,
#     'aput-byte': 14,
#     'ushr-long/2addr': 16,
#     'iput-quick': 14,
#     'rem-int/lit8': 16,
#     'aget-byte': 13,
#     'sput-char': 14,
#     'iput-wide-quick': 14,
#     'iget-object': 13,
#     'iput': 14,
#     'sget': 13,
#     'if-lez': 12,
#     'add-double': 16,
#     'mul-double/2addr': 16,
#     'invoke-interface/range': 15,
#     'goto/32': 9,
#     'iget-wide': 13,
#     'div-float/2addr': 16,
#     'move-result-wide': 1,
#     'shr-long': 16,
#     'move-object': 1,
#     'invoke-direct': 15,
#     'iput-byte': 14,
#     'move/from16': 1,
#     'div-int/lit8': 16,
#     'float-to-int': 17,
#     'if-eq': 12,
#     'add-float/2addr': 16,
#     'aget-char': 13,
#     'iput-wide': 14,
#     'execute-inline': 18,
#     'iput-boolean': 14,
#     'aput-wide': 14,
#     'long-to-double': 17,
#     'move-wide/from16': 1,
#     'return': 2,
#     'float-to-long': 17,
#     'int-to-float': 17,
#     'sget-boolean': 13,
#     'and-long': 16,
#     'iput-byte-quick': 14,
#     'xor-int/lit16': 16,
#     'iget-short-quick': 13,
#     'and-long/2addr': 16,
#     'iput-short-quick': 14,
#     'aget-wide': 13,
#     'neg-double': 16,
#     'sput-object': 14,
#     'nop': 0,
#     'const-wide/high16': 3,
#     'invoke-super-quick': 15,
#     'fill-array-data': 6,
#     'sget-byte': 13,
#     'sub-int': 16,
#     'ushr-int': 16,
#     'mul-int/lit16': 16,
#     'packed-switch-payload': 10,
#     'or-int/2addr': 16,
#     'invoke-super': 15,
#     'double-to-long': 17,
#     'mul-int/lit8': 16,
#     'neg-int': 16,
#     'const-wide/32': 3,
#     'move-wide': 1,
#     'if-gez': 12,
#     'aget-short': 13,
#     'goto': 9,
#     'int-to-byte': 17,
#     'div-double': 16,
#     'if-nez': 12,
#     'sub-long': 16,
#     'iput-object-volatile': 14,
#     'invoke-virtual-quick/range': 15,
#     'rsub-int': 16,
#     'shr-int/2addr': 16,
#     'iget-byte-quick': 13,
#     'return-void-barrier': 2,
#     'invoke-super/range': 15,
#     'mul-int': 16,
#     'const/16': 3,
#     'div-int': 16,
#     'throw-verification-error': 8,
#     'instance-of': 5,
#     'not-int': 16,
#     'sget-object': 13,
#     'mul-double': 16,
#     'iput-object-quick': 14,
#     'aget': 13,
#     'new-instance': 7,
#     'mul-long/2addr': 16,
#     'or-long': 16,
#     'add-long': 16,
#     'aput-short': 14,
#     'ushr-int/2addr': 16,
#     'shr-long/2addr': 16,
#     'iput-char': 14,
#     'add-double/2addr': 16,
#     'move-result-object': 1,
#     'int-to-long': 17,
#     'iput-char-quick': 14,
#     'xor-int/lit8': 16,
#     'sput-object-volatile': 14,
#     'sput-byte': 14,
#     'if-eqz': 12,
#     'div-int/2addr': 16,
#     'if-lt': 12,
#     'shr-int': 16,
#     'if-gtz': 12,
#     'not-long': 16,
#     'long-to-int': 17,
#     'invoke-virtual/range': 15,
#     'invoke-virtual': 15,
#     'add-int/lit8': 16,
#     'int-to-short': 17,
#     'iget': 13,
#     'const/high16': 3,
#     'iget-byte': 13,
#     'xor-long/2addr': 16,
#     'double-to-int': 17,
#     'rem-double/2addr': 16,
#     'mul-float': 16,
#     'add-float': 16,
#     'throw': 8,
#     'sput-wide-volatile': 14,
#     'float-to-double': 17,
#     'iput-short': 14,
#     'array-payload': 6,
#     'invoke-object-init/range': 15,
#     'iget-wide-volatile': 13,
#     'const': 3,
#     'cmpl-double': 11,
#     'neg-float': 16,
#     'shl-long': 16,
#     'iput-object': 14,
#     'sput-wide': 14,
#     'add-long/2addr': 16,
#     'div-long': 16,
#     'move-result': 1,
#     'invoke-static': 15,
#     'xor-long': 16,
#     'div-int/lit16': 16,
#     'sput-boolean': 14,
#     'sub-float': 16,
#     'aput-char': 14,
#     'shl-int/lit8': 16,
#     'check-cast': 5,
#     'array-length': 6,
#     'filled-new-array/range': 6,
#     'sub-double/2addr': 16,
#     'and-int/lit8': 16,
#     'return-wide': 2,
#     'move-object/16': 1,
#     'filled-new-array': 6,
#     'iget-object-quick': 13,
#     'rem-int/lit16': 16,
#     'mul-long': 16,
#     'if-ltz': 12,
#     'rem-float': 16,
#     'and-int': 16,
#     'invoke-direct-empty': 15,
#     'sub-long/2addr': 16,
#     'const/4': 3,
#     'aget-object': 13,
#     'iput-wide-volatile': 14,
#     'const-class': 3,
#     'move-exception': 1,
#     'const-string': 3,
#     'sget-object-volatile': 13,
#     'rsub-int/lit8': 16,
#     'add-int/lit16': 16,
#     'long-to-float': 17,
#     'rem-long': 16,
#     'xor-int': 16,
#     'if-gt': 12,
#     'sput-volatile': 14,
#     'invoke-static/range': 15,
#     'invoke-interface': 15,
#     'packed-switch': 10,
#     'neg-long': 16,
#     'or-int/lit16': 16,
#     'div-double/2addr': 16,
#     'goto/16': 9,
#     'iget-object-volatile': 13,
#     'if-ge': 12,
#     'invoke-direct/range': 15,
#     'sget-wide': 13,
#     'cmpg-double': 11,
#     'iget-short': 13,
#     'return-object': 2,
#     'sput-short': 14,
#     'cmpl-float': 11,
#     'invoke-polymorphic/range': 15,
#     'iget-volatile': 13,
#     'rem-double': 16,
#     'sparse-switch-payload': 10,
#     'return-void': 2,
#     'iget-boolean-quick': 13,
#     'shl-int/2addr': 16,
#     'ushr-int/lit8': 16,
#     'sget-char': 13,
#     'iput-boolean-quick': 14,
#     'move': 1,
#     'xor-int/2addr': 16,
#     'const-wide/16': 3,
#     'cmpg-float': 11,
#     'monitor-exit': 4,
#     'div-long/2addr': 16,
#     'if-ne': 12,
#     'if-le': 12,
#     'move-object/from16': 1,
#     'or-long/2addr': 16,
#     'sget-wide-volatile': 13,
#     'rem-float/2addr': 16,
#     'const-string/jumbo': 3,
#     'iget-quick': 13,
#     'add-int': 16,
#     'iget-wide-quick': 13,
#     'sub-float/2addr': 16,
#     'iget-boolean': 13,
#     'cmp-long': 11,
#     'iput-volatile': 14,
#     'aput-boolean': 14,
#     'sub-int/2addr': 16,
#     'sget-short': 13,
#     'move-wide/16': 1,
#     'return-void-no-barrier': 2,
#     'shl-long/2addr': 16,
#     'rem-int': 16,
#     'or-int': 16,
#     'and-int/lit16': 16,
#     'sparse-switch': 10,
#     'invoke-super-quick/range': 15,
#     'mul-float/2addr': 16,
#     'new-array': 6,
#     'aput-object': 14,
#     'shr-int/lit8': 16,
#     'ushr-long': 16,
#     'const-wide': 3,
#     'and-int/2addr': 16,
#     'sub-double': 16,
#     'sget-volatile': 13,
#     'int-to-char': 17,
#     'mul-int/2addr': 16,
#     'execute-inline/range': 18
# }

HCG_FILE_NAME = 'directed_hcg_15bit.json'
CG_FILE_NAME = 'directed_cg_15bit.json'

INSTRUCTION_CLASS_COLOR = {
    'nop': 0,
    'move': 1,
    'return': 2,
    'monitor': 3,
    'test': 4,
    'new': 5,
    'throw': 6,
    'jump': 7,
    'branch': 8,
    'arrayop': 9,
    'instanceop': 10,
    'staticop': 11,
    'invoke': 12,
    'unop': 13,
    'binop': 14
} 

INSTRUCTION_CLASSES = [
    'nop',
    'move',
    'return',
    'monitor',
    'test',
    'new',
    'throw',
    'jump',
    'branch',
    'arrayop',
    'instanceop',
    'staticop',
    'invoke',
    'unop',
    'binop'
]

INSTRUCTION_SET_COLOR = {
    'nop': 0,
    'move': 1,
    'move/from16': 1,
    'move/16': 1,
    'move-wide': 1,
    'move-wide/from16': 1,
    'move-wide/16': 1,
    'move-object': 1,
    'move-object/from16': 1,
    'move-object/16': 1,
    'move-result': 1,
    'move-result-wide': 1,
    'move-result-object': 1,
    'move-exception': 1,
    'return-void': 2,
    'return': 2,
    'return-wide': 2,
    'return-object': 2,
    'const/4': 1,
    'const/16': 1,
    'const': 1,
    'const/high16': 1,
    'const-wide/16': 1,
    'const-wide/32': 1,
    'const-wide': 1,
    'const-wide/high16': 1,
    'const-string': 1,
    'const-string/jumbo': 1,
    'const-class': 1,
    'monitor-enter': 3,
    'monitor-exit': 3,
    'check-cast': 4,
    'instance-of': 4,
    'array-length': 1,
    'new-instance': 5,
    'new-array': 5,
    'filled-new-array': 1,
    'filled-new-array/range': 1,
    'fill-array-data': 1,
    'fill-array-data-payload': 1,
    'throw': 6,
    'goto': 7,
    'goto/16': 7,
    'goto/32': 7,
    'packed-switch': 7,
    'packed-switch-payload': 7,
    'sparse-switch': 7,
    'sparse-switch-payload': 7,
    'cmpl-float': 7,
    'cmpg-float': 7,
    'cmpl-double': 7,
    'cmpg-double': 7,
    'cmp-long': 7,
    'if-eq': 8,
    'if-ne': 8,
    'if-lt': 8,
    'if-ge': 8,
    'if-gt': 8,
    'if-le': 8,
    'if-eqz': 8,
    'if-nez': 8,
    'if-ltz': 8,
    'if-gez': 8,
    'if-gtz': 8,
    'if-lez': 8,
    'aget': 9,
    'aget-wide': 9,
    'aget-object': 9,
    'aget-boolean': 9,
    'aget-byte': 9,
    'aget-char': 9,
    'aget-short': 9,
    'aput': 9,
    'aput-wide': 9,
    'aput-object': 9,
    'aput-boolean': 9,
    'aput-byte': 9,
    'aput-char': 9,
    'aput-short': 9,
    'iget': 10,
    'iget-wide': 10,
    'iget-object': 10,
    'iget-boolean': 10,
    'iget-byte': 10,
    'iget-char': 10,
    'iget-short': 10,
    'iput': 10,
    'iput-wide': 10,
    'iput-object': 10,
    'iput-boolean': 10,
    'iput-byte': 10,
    'iput-char': 10,
    'iput-short': 10,
    'sget': 11,
    'sget-wide': 11,
    'sget-object': 11,
    'sget-boolean': 11,
    'sget-byte': 11,
    'sget-char': 11,
    'sget-short': 11,
    'sput': 11,
    'sput-wide': 11,
    'sput-object': 11,
    'sput-boolean': 11,
    'sput-byte': 11,
    'sput-char': 11,
    'sput-short': 11,
    'invoke-virtual': 12,
    'invoke-super': 12,
    'invoke-direct': 12,
    'invoke-static': 12,
    'invoke-interface': 12,
    'invoke-virtual/range': 12,
    'invoke-super/range': 12,
    'invoke-direct/range': 12,
    'invoke-static/range': 12,
    'invoke-interface/range': 12,
    'neg-int': 13,
    'not-int': 13,
    'neg-long': 13,
    'not-long': 13,
    'neg-float': 13,
    'neg-double': 13,
    'int-to-long': 13,
    'int-to-float': 13,
    'int-to-double': 13,
    'long-to-int': 13,
    'long-to-float': 13,
    'long-to-double': 13,
    'float-to-int': 13,
    'float-to-long': 13,
    'float-to-double': 13,
    'double-to-int': 13,
    'double-to-long': 13,
    'double-to-float': 13,
    'int-to-byte': 13,
    'int-to-char': 13,
    'int-to-short': 13,
    'add-int': 14,
    'sub-int': 14,
    'mul-int': 14,
    'div-int': 14,
    'rem-int': 14,
    'and-int': 14,
    'or-int': 14,
    'xor-int': 14,
    'shl-int': 14,
    'shr-int': 14,
    'ushr-int': 14,
    'add-long': 14,
    'sub-long': 14,
    'mul-long': 14,
    'div-long': 14,
    'rem-long': 14,
    'and-long': 14,
    'or-long': 14,
    'xor-long': 14,
    'shl-long': 14,
    'shr-long': 14,
    'ushr-long': 14,
    'add-float': 14,
    'sub-float': 14,
    'mul-float': 14,
    'div-float': 14,
    'rem-float': 14,
    'add-double': 14,
    'sub-double': 14,
    'mul-double': 14,
    'div-double': 14,
    'rem-double': 14,
    'add-int/2addr': 14,
    'sub-int/2addr': 14,
    'mul-int/2addr': 14,
    'div-int/2addr': 14,
    'rem-int/2addr': 14,
    'and-int/2addr': 14,
    'or-int/2addr': 14,
    'xor-int/2addr': 14,
    'shl-int/2addr': 14,
    'shr-int/2addr': 14,
    'ushr-int/2addr': 14,
    'add-long/2addr': 14,
    'sub-long/2addr': 14,
    'mul-long/2addr': 14,
    'div-long/2addr': 14,
    'rem-long/2addr': 14,
    'and-long/2addr': 14,
    'or-long/2addr': 14,
    'xor-long/2addr': 14,
    'shl-long/2addr': 14,
    'shr-long/2addr': 14,
    'ushr-long/2addr': 14,
    'add-float/2addr': 14,
    'sub-float/2addr': 14,
    'mul-float/2addr': 14,
    'div-float/2addr': 14,
    'rem-float/2addr': 14,
    'add-double/2addr': 14,
    'sub-double/2addr': 14,
    'mul-double/2addr': 14,
    'div-double/2addr': 14,
    'rem-double/2addr': 14,
    'add-int/lit16': 14,
    'rsub-int': 14,
    'mul-int/lit16': 14,
    'div-int/lit16': 14,
    'rem-int/lit16': 14,
    'and-int/lit16': 14,
    'or-int/lit16': 14,
    'xor-int/lit16': 14,
    'add-int/lit8': 14,
    'rsub-int/lit8': 14,
    'mul-int/lit8': 14,
    'div-int/lit8': 14,
    'rem-int/lit8': 14,
    'and-int/lit8': 14,
    'or-int/lit8': 14,
    'xor-int/lit8': 14,
    'shl-int/lit8': 14,
    'shr-int/lit8': 14,
    'ushr-int/lit8': 14
}