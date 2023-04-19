
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
      return MED[(S, T)]
    if (T, S) in MED:
      return MED[(T, S)]

    if (S == ""): #S is empty, number of operations required is the remaining length of T
      return(len(T))
    elif (T == ""): #same as above but switch S and T
      return(len(S))
    else:
      if (S[0] == T[0]): #entries are equal, no operation required
        return fast_MED(S[1:], T[1:], MED)
      else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        replace = fast_MED(S[1:], T[1:], MED)
        result = 1 + min(insert, delete, replace)
        
    MED[(S, T)] = result
    return result

def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
      return MED[(S, T)]
    if (T, S) in MED:
      return MED[(T, S)]
    
    if (S == ""):
        return ('-' * len(T), T)
    elif (T == ""):
        return (S, '-' * len(S))
    else:
      if (S[0] == T[0]):
        align = fast_align_MED(S[1:], T[1:], MED)
        return (S[0] + align, T[0] + align)
      else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        replace = fast_MED(S[1:], T[1:], MED)

        if (min(replace, insert, delete) == insert):
            align = fast_align_MED(S, T[1:], MED)
            return ('-' + align, T[0] + align)
        elif (min(replace, insert, delete) == delete):
            align = fast_align_MED(S[1:], T, MED)
            return (S[0] + align, '-' + align)
        elif (min(replace, insert, delete) == replace):
            align = fast_align_MED(S[1:], T[1:], MED)
            return (S[0] + align, T[0] + align)

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
