import random
decision_table = {
            #best move 1 Player_Number=1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            #best move 2 Player_Number=2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (1, 3), (3, 1), (3, 3)]), "KILLER_MOVE"),
            '[[1. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 1.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [1. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 1.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [1. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 1.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [1. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 1.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [1. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]]': ((2,  2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 1.]]': ((2,  2), "KILLER_MOVE"),
            #best move 3 Player_Number=1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 3), (3, 1)]), "KILLER_MOVE"), #1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (3, 3)]), "KILLER_MOVE"), #2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (3, 3)]), "KILLER_MOVE"), #3
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 3), (3, 1)]), "KILLER_MOVE"), #4
            #best move 4 Player_Number=2
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 1), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 3), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 3), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 1), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 3), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 1), "KILLER_MOVE"), #3.2  
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 1), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 3), "KILLER_MOVE"), #4.2
            #best move 5 Player_Number=1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #3.2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #4.2
            #best move 6 Player_Number=2
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 1. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 1. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 1. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #3.2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 1. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE")  #4.2
        } #decisions tabel