def arithmetic_arranger(problems, show_answer=False):
  
  import re
  list_of_problems = []
  arranged_problems = ""

    # making sure the input is of type list and only takes up to 5 argument
  if len(problems) > 5: 
    return "Error: Too many problems."

  else:
    for problem in problems: 
        
      #standardizing inputs by removing spaces, this will make the program be able to compute with input that are either with space or without.
      problem = problem.replace(" ","")
  
        #rule 1: numbers must only contain digits
      if re.findall('[a-zA-Z]{1,}', problem) != []:
        return "Error: Numbers must only contain digits."
    
        #rule 2: operators must only be addition and substraction
      elif re.findall('(^\d*[+-]{1}[0-9]{1,})', problem) == []:
        return "Error: Operator must be '+' or '-'."
      
        #rule 3: numbers cannot be more than four digits  
      elif re.findall('\d{5,}', problem) != []:
        return 'Error: Numbers cannot be more than four digits.'

        #separating the operators and operands, some datatype processing and store them in a list of tuples for each problem. the tuple will have the format of (operand1, operand2, length of largest number, operator). We will use these data to print them out later. The length of largest number will be used as the spacing number during formatting.
      else: 
        if problem.find('+') > 0:
          operands = problem.split('+')
          operands = [int(x) for x in operands] #convert from string type to integer
          maxnumber = max(operands) #max number is used for required space length during formatting
          operands.append(len(str(maxnumber)))
          operands.append('+')
          list_of_problems.append((tuple(operands)))
            
        elif problem.find('-') > 0:
          operands = problem.split('-')
          operands = [int(x) for x in operands]
          maxnumber = max(operands)
          operands.append(len(str(maxnumber)))
          operands.append('-')
          list_of_problems.append((tuple(operands)))
  
    first_line = ""
    second_line = ""
    dashes = ""
    answer_line = ""

    for problem in list_of_problems:
      
      #formatting. problem[0] = first operand, problem[1] = second operand, problem[2] = highest number, problem[3] = operator
      first_line = first_line + "  {0:>{1}}".format(problem[0],problem[2],problem[3]) + 4*" " 
      second_line = second_line + "{2} {0:>{1}}".format(problem[1],problem[2],problem[3]) + 4*" "
      dashes = dashes + (problem[2]+2)*'-' + 4*" "
      if problem[3] == '+':
        answer = problem[0] + problem[1]
        answer_length = len(str(answer))
        print(answer_length-problem[2])
      else:
        answer = problem[0] - problem[1]
        answer_length = len(str(answer))
        print(answer_length-problem[2])

      #since the answer might have more or less digit than the operands, we need to create different algorithm just to format the answer so that it allign with the rest. To do this, we need to use the formula: answer_length - (difference between answer length and the max number length), this formula gives the required spacing format.
      if answer_length > problem[2]: 
        answer_line = answer_line + "{0:>{1}}".format(str(answer),2*answer_length-problem[2]) + 4*" "
      else:
        answer_line = answer_line + "{0:>{1}}".format(str(answer),answer_length+2) + 4*" "
  
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip() 
    #rstrip used to remove trailing spaces to abide the formats set by the solution requirement. 
  
    if show_answer == True:
      arranged_problems = arranged_problems + "\n" + answer_line.rstrip()
    else:
      pass
      
    return arranged_problems