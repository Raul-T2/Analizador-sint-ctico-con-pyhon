
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ID IDENTIFICADOR INT LLAVE_DERECHA LLAVE_IZQUIERDA MAIN PARENTESIS_DERECHA PARENTESIS_IZQUIERDA PUNTO_Y_COMAprogram : INT MAIN PARENTESIS_IZQUIERDA PARENTESIS_DERECHA LLAVE_IZQUIERDA declarations LLAVE_DERECHAdeclarations : INT IDENTIFICADOR PUNTO_Y_COMA\n                    | INT IDENTIFICADOR PUNTO_Y_COMA declarations'
    
_lr_action_items = {'INT':([0,6,11,],[2,7,7,]),'$end':([1,10,],[0,-1,]),'MAIN':([2,],[3,]),'PARENTESIS_IZQUIERDA':([3,],[4,]),'PARENTESIS_DERECHA':([4,],[5,]),'LLAVE_IZQUIERDA':([5,],[6,]),'IDENTIFICADOR':([7,],[9,]),'LLAVE_DERECHA':([8,11,12,],[10,-2,-3,]),'PUNTO_Y_COMA':([9,],[11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([6,11,],[8,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> INT MAIN PARENTESIS_IZQUIERDA PARENTESIS_DERECHA LLAVE_IZQUIERDA declarations LLAVE_DERECHA','program',7,'p_program','app.py',39),
  ('declarations -> INT IDENTIFICADOR PUNTO_Y_COMA','declarations',3,'p_declarations','app.py',43),
  ('declarations -> INT IDENTIFICADOR PUNTO_Y_COMA declarations','declarations',4,'p_declarations','app.py',44),
]
