empty = [0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0]

cross = [1, 0, 0, 0, 0, 0, 0, 1,
         0, 1, 0, 0, 0, 0, 1, 0,
         0, 0, 1, 0, 0, 1, 0, 0,
         0, 0, 0, 1, 1, 0, 0, 0,
         0, 0, 0, 1, 1, 0, 0, 0,
         0, 0, 1, 0, 0, 1, 0, 0,
         0, 1, 0, 0, 0, 0, 1, 0,
         1, 0, 0, 0, 0, 0, 0, 1]

question_mark = [0, 0, 0, 1, 1, 1, 0, 0,
                 0, 0, 1, 0, 0, 0, 1, 0,
                 0, 0, 1, 0, 0, 0, 1, 0,
                 0, 0, 0, 0, 0, 1, 0, 0,
                 0, 0, 0, 0, 1, 0, 0, 0,
                 0, 0, 0, 0, 1, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 1, 0, 0, 0]

arrow_left = [0, 0, 0, 1, 0, 0, 0, 0,
              0, 0, 1, 1, 0, 0, 0, 0,
              0, 1, 1, 1, 0, 0, 0, 0,
              1, 1, 1, 1, 1, 1, 1, 0,
              1, 1, 1, 1, 1, 1, 1, 0,
              0, 1, 1, 1, 0, 0, 0, 0,
              0, 0, 1, 1, 0, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0, 0]

arrow_right = [0, 0, 0, 0, 1, 0, 0, 0,
               0, 0, 0, 0, 1, 1, 0, 0,
               0, 0, 0, 0, 1, 1, 1, 0,
               0, 1, 1, 1, 1, 1, 1, 1,
               0, 1, 1, 1, 1, 1, 1, 1,
               0, 0, 0, 0, 1, 1, 1, 0,
               0, 0, 0, 0, 1, 1, 0, 0,
               0, 0, 0, 0, 1, 0, 0, 0]

one = [0, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 1, 1, 0, 0, 0,
       0, 0, 1, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0]

two = [0, 0, 1, 1, 1, 1, 0, 0,
       0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 1, 1, 1, 1, 0, 0,
       0, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 1, 1, 1, 1, 0, 0]

three = [0, 0, 1, 1, 1, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 1, 1, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 1, 1, 1, 1, 0, 0]

four = [0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0]

five = [0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0]

six = [0, 0, 1, 1, 1, 1, 0, 0,
       0, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 1, 1, 1, 1, 0, 0,
       0, 0, 1, 0, 0, 1, 0, 0,
       0, 0, 1, 0, 0, 1, 0, 0,
       0, 0, 1, 1, 1, 1, 0, 0]

seven = [0, 0, 1, 1, 1, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 1, 0, 0]

eight = [0, 0, 1, 1, 1, 1, 0, 0,
         0, 0, 1, 0, 0, 1, 0, 0,
         0, 0, 1, 0, 0, 1, 0, 0,
         0, 0, 1, 1, 1, 1, 0, 0,
         0, 0, 1, 0, 0, 1, 0, 0,
         0, 0, 1, 0, 0, 1, 0, 0,
         0, 0, 1, 0, 0, 1, 0, 0,
         0, 0, 1, 1, 1, 1, 0, 0]

nine = [0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0]

zero = [0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0]

letter_a = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0]

letter_b = [0, 0, 1, 1, 1, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 0, 0, 0]

letter_c = [0, 0, 0, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0]

letter_d = [0, 0, 1, 1, 1, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 0, 0, 0]

letter_e = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0]

letter_f = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0]

letter_g = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0]

letter_h = [0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0]

letter_i = [0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0]

letter_j = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 0, 1, 1, 0, 0, 0]

letter_k = [0, 0, 1, 0, 0, 0, 1, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 1, 0, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 1, 0]

letter_l = [0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0]

letter_m = [0, 1, 0, 0, 0, 0, 1, 0,
            0, 1, 1, 0, 0, 1, 1, 0,
            0, 1, 0, 1, 1, 0, 1, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 0, 1, 0]

letter_n = [0, 1, 0, 0, 0, 0, 1, 0,
            0, 1, 1, 0, 0, 0, 1, 0,
            0, 1, 1, 1, 0, 0, 1, 0,
            0, 1, 0, 1, 1, 0, 1, 0,
            0, 1, 0, 1, 1, 0, 1, 0,
            0, 1, 0, 0, 1, 1, 1, 0,
            0, 1, 0, 0, 0, 1, 1, 0,
            0, 1, 0, 0, 0, 0, 1, 0]

letter_o = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0]

letter_p = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0]

letter_q = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0]

letter_r = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0]

letter_s = [0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0]

letter_t = [0, 1, 1, 1, 1, 1, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0]

letter_u = [0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0]

letter_v = [0, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 1, 0,
            0, 0, 1, 0, 0, 0, 1, 0,
            0, 0, 0, 1, 0, 0, 1, 0,
            0, 0, 0, 1, 0, 1, 0, 0,
            0, 0, 0, 1, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 1, 0, 0, 0]

letter_w = [1, 0, 0, 0, 0, 0, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1,
            0, 1, 1, 0, 0, 0, 0, 1,
            0, 1, 1, 0, 0, 0, 1, 0,
            0, 0, 1, 0, 1, 0, 1, 0,
            0, 0, 1, 0, 1, 0, 1, 0,
            0, 0, 1, 1, 0, 1, 1, 0]

letter_x = [1, 0, 0, 0, 0, 0, 0, 1,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 0, 0, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            1, 0, 0, 0, 0, 0, 0, 1]

letter_y = [1, 0, 0, 0, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 1, 0, 0,
            0, 0, 1, 0, 1, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0]

letter_z = [1, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 0,
            0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1]


def get_score_frame(number: int):
    if number == 1:
        return one
    elif number == 2:
        return two
    elif number == 3:
        return three
    elif number == 4:
        return four
    elif number == 5:
        return five
    elif number == 6:
        return six
    elif number == 7:
        return seven
    elif number == 8:
        return eight
    elif number == 9:
        return nine
    elif number == 0:
        return zero
    return empty


def get_letter_frame(letter):
    if letter == 'a':
        return letter_a
    elif letter == 'e':
        return letter_e
    elif letter == 'g':
        return letter_g
    elif letter == 'k':
        return letter_k
    elif letter == 'n':
        return letter_n
    elif letter == 'o':
        return letter_o
    elif letter == 'p':
        return letter_p
    elif letter == 's':
        return letter_s
    return empty


# Alternative zu 'get_letter_frame'
def letter_to_frame(letter):
    return {
        'a': letter_a,
        'b': empty,
        'c': empty,
        'd': empty,
        'e': letter_e,
        'f': empty,
        'g': letter_g,
        'h': empty,
        'i': empty,
        'j': empty,
        'k': letter_k,
        'l': empty,
        'm': empty,
        'n': letter_n,
        'o': letter_o,
        'p': letter_p,
        'q': empty,
        'r': empty,
        's': letter_s,
        't': empty,
        'u': empty,
        'v': empty,
        'w': empty,
        'x': empty,
        'y': empty,
        'z': empty
    }[letter]


# Alternative zu 'get_score_frame'
def number_to_frame(number):
    return {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        0: zero
    }[number % 10]
