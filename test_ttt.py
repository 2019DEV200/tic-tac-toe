import sys
import os
import unittest

sys.path.insert(
  0, os.path.abspath(os.path.join(os.path.dirname(__file__), '·'))
)

import ttt

class BasicTestSuite(unittest.TestCase):

  ClassIsSetup = False

  def setUp(self):
    import sys
    if not self.ClassIsSetup:
      print(sys.version)
      self.ClassIsSetup = True


  def test_validator_invalid_cell(self):
    boards = [
      {
        'board'  : [
          ['X', '·', 'X'],
          ['O', 'X', '·'],
          ['O', 'X', 'O']
        ],
        # request for cell is out of range
        'move' : 'D3'
      },
      {
        'board'  : [
          ['·', 'X', 'X'],
          ['X', 'O', 'X'],
          ['O', '·', 'O']
        ],
        'move' : 'C4'
      },
      {
        'board'  : [
          ['X', '·', 'X'],
          ['·', 'O', '·'],
          ['·', 'X', 'O']
        ],
        'move' : 'B2'
      },
      {
        'board'  : [
          ['O', '·', 'X'],
          ['·', 'X', '·'],
          ['·', 'X', 'O']
        ],
        'move' : 'C1'
      }
    ]

    for item in boards:
      self.assertFalse(ttt.validator(item['board'], item['move']))
  
  def test_validator_valid_cell(self):
    boards = [
      {
        'board'  : [
          ['X', '·', 'X'],
          ['O', 'X', '·'],
          ['O', 'X', 'O']
        ],
        'move' : 'B1'
      },
      {
        'board'  : [
          ['·', 'X', 'X'],
          ['X', 'O', 'X'],
          ['O', '·', 'O']
        ],
        'move' : 'A1'
      },
      {
        'board'  : [
          ['X', '·', 'X'],
          ['·', 'O', '·'],
          ['·', 'X', 'O']
        ],
        'move' : 'C2'
      },
      {
        'board'  : [
          ['O', '·', 'X'],
          ['·', 'X', '·'],
          ['·', 'X', 'O']
        ],
        'move' : 'A3'
      }
    ]

    for item in boards:
      self.assertTrue(ttt.validator(item['board'], item['move']))

  def test_horizontal_boards(self):
    boards = [
      {
        'board'  : [
          ['X', 'X', 'X'],
          ['O', 'O', '·'],
          ['O', 'X', 'O']
        ],
        'winner' : 'X'
      },
      {
        'board'  : [
          ['·', 'X', 'X'],
          ['X', 'O', 'X'],
          ['O', 'O', 'O']
        ],
        'winner' : 'O'
      }
    ]
    
    for item in boards:
      self.assertEqual(ttt.winner(item['board']), item['winner'])


  def test_vertical_boards(self):
    boards = [
      {
        'board'  : [
          ['X', 'O', 'X'],
          ['·', 'O', 'X'],
          ['O', '·', 'X']
        ],
        'winner' : 'X'
      },
      {
        'board'  : [
          ['O', 'X', 'X'],
          ['O', 'O', 'X'],
          ['O', 'X', 'O']
        ],
        'winner' : 'O'
      }
    ]

    for item in boards:
      self.assertEqual(ttt.winner(item['board']), item['winner'])

  
  def test_diagonal_boards(self):
    boards = [
      {
        'board'  : [
          ['O', '·', 'X'],
          ['·', 'X', '·'],
          ['X', '·', 'O']
        ],
        'winner' : 'X'
      },
      {
        'board'  : [
          ['O', 'X', 'X'],
          ['·', 'O', '·'],
          ['X', 'O', 'O']
        ],
        'winner' : 'O'
      }
    ]

    for item in boards:
      self.assertEqual(ttt.winner(item['board']), item['winner'])
  
  def test_draw_boards(self):
    boards = [
      {
        'board'  : [
          ['X', 'O', 'X'],
          ['X', 'O', 'X'],
          ['O', 'X', 'O']
        ],
        'winner' : None
      },
      {
        'board'  : [
          ['O', 'X', 'O'],
          ['O', 'X', 'X'],
          ['X', 'O', 'X']
        ],
        'winner' : None
      }
    ]

    for item in boards:
      self.assertEqual(ttt.winner(item['board']), item['winner'])
        

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(BasicTestSuite)
  ret = not unittest.TextTestRunner(stream=sys.stdout, verbosity=2, buffer=True).run(suite).wasSuccessful()
  sys.exit(ret)