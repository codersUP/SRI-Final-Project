
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND LPAREN NOT OR RPAREN TERMexpr : expr AND exprexpr : expr OR exprexpr : termexpr : LPAREN expr RPARENexpr : NOT termexpr : NOT LPAREN expr RPARENterm : TERM'
    
_lr_action_items = {'LPAREN':([0,3,4,6,7,10,],[3,3,10,3,3,3,]),'NOT':([0,3,6,7,10,],[4,4,4,4,4,]),'TERM':([0,3,4,6,7,10,],[5,5,5,5,5,5,]),'$end':([1,2,5,9,11,12,13,15,],[0,-3,-7,-5,-1,-2,-4,-6,]),'AND':([1,2,5,8,9,11,12,13,14,15,],[6,-3,-7,6,-5,6,6,-4,6,-6,]),'OR':([1,2,5,8,9,11,12,13,14,15,],[7,-3,-7,7,-5,7,7,-4,7,-6,]),'RPAREN':([2,5,8,9,11,12,13,14,15,],[-3,-7,13,-5,-1,-2,-4,15,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,3,6,7,10,],[1,8,11,12,14,]),'term':([0,3,4,6,7,10,],[2,2,9,2,2,2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr AND expr','expr',3,'p_expr_and','query_parser.py',6),
  ('expr -> expr OR expr','expr',3,'p_expr_or','query_parser.py',16),
  ('expr -> term','expr',1,'p_expr_term','query_parser.py',26),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr_par','query_parser.py',36),
  ('expr -> NOT term','expr',2,'p_expr_not','query_parser.py',46),
  ('expr -> NOT LPAREN expr RPAREN','expr',4,'p_expr_not_par','query_parser.py',56),
  ('term -> TERM','term',1,'p_term','query_parser.py',66),
]
