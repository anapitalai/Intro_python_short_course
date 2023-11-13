"""
Some functions for determination or errors in the automatic level.
"""

def error(bs_to_a:float,fs_to_b:float,beyond_b,bs_a:float):
    """
    A function that calulates the error in the automatic level,first arguement is the backsight
    from Point A,second is the foresight from B,third is the backsight from B and last 
    is the foresight from B.
    """
    total_bs=bs_to_a + beyond_b
    total_fs= fs_to_b + bs_a
    calc_err = total_fs - total_bs
    return round(calc_err,4)


