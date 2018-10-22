import sys
import fileinput

def allTrue(cnf, result): 
    for clause in cnf[1:]: # cnf[0] is 'and'
        if len([var for var in clause[1:] if var in result]) == 0: #clause[0' is 'or
            return False
    return True

def negate(result):
    sol = []
    for literal in result:
        if type(literal) is str:
            sol.append(["not", literal])
        else:
            sol.append(literal[1]) #literal[0]='not'
    return sol

def someFalse(cnf, result):
    resultCompliments = negate(result)
    for clause in cnf[1:]:
        if len([var for var in clause[1:] if var not in resultCompliments]) == 0:
            return True
    return False

def pureLiteral(cnf, result):
    #identify a literal l that occurs only in one polarity and set to true
    resultCompliments = negate(result)
    candidates = []
    for clause in cnf[1:]:
        if len([var for var in clause[1:] if var in result]) == 0:
            candidates = candidates + [var for var in clause[1:]]
    candidateCompliments = negate(candidates)
    pure = [var for var in candidates if var not in candidateCompliments]
    for var in pure:
        if var not in result and var not in resultCompliments:
            return var
    return False

def unitClause(cnf, result):
    #find a unit clause Ci =l, and the literal is not in result
    #set l to true
    resultCompliments = negate(result)
    for clause in cnf[1:]:
        remaining = [var for var in clause[1:] if var not in resultCompliments]
        if len(remaining) == 1:
            if remaining[0] not in result:
                return remaining[0]
    return False

def splitSymbol(cnf, result):
    #find a positive literal not in result
    combined = result + negate(result)
    for clause in cnf[1:]:
        for literal in clause[1:]:
            if type(literal) is str and literal not in combined:
                return literal
    return False

def dpll(cnf):
    return dpll_solver(cnf, [])

def dpll_solver(cnf, result):
    #base cases
    #if current solution satisfy sentence, return 
    if allTrue(cnf, result):
        return result
    #if current solution contains all possible literals, cannot split anymore and some clause if false then not satisfiable
    if someFalse(cnf, result):
        return False
    #Pure literal elimination
    pure = pureLiteral(cnf, result)
    if pure:
        return dpll_solver(cnf, result + [pure])
    #Unit propogation
    unit = unitClause(cnf, result)
    if unit:
        return dpll_solver(cnf, result + [unit])
    pick = splitSymbol(cnf, result)
    if pick:
        # try positive
        sol = dpll_solver(cnf, result + [pick])
        if sol:
            return sol
        else:
            # try negative
            sol = dpll_solver(cnf, result + [['not', pick]])
            if sol:
                return sol
            else:
                return False


if __name__ == "__main__":

    sentences = fileinput.input()
    for l in sentences:
	print repr(dpll(eval(l)))
