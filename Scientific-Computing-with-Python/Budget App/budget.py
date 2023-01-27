class Category:

  all_category = []

  def __init__(self, name: str):
    self.name = name
    self.balance = 0
    self.ledger = []

  def deposit(self, depo_amount:float, depo_description = ""):
    
    #verifying amount should be positive number
    assert depo_amount >= 0, f'{depo_amount} is a negative number!'

    #assign to self object
    self.depo_amount = depo_amount
    self.depo_description = depo_description

    #append ledger attribute
    self.ledger.append({'amount':self.depo_amount,'description':self.depo_description})
    self.balance = self.balance + self.depo_amount
  
  def withdraw(self, withdraw_amount:float, withdraw_description = ""):
    
    #verifying amount should be positive number
    assert withdraw_amount >= 0, f'{withdraw_amount} is a negative number'

    #assign to self object
    if self.balance < withdraw_amount:
      return False
    else:
      self.withdraw_amount = -withdraw_amount
      self.withdraw_description = withdraw_description 
      self.balance = self.balance + self.withdraw_amount
      #append ledger
      self.ledger.append({'amount':self.withdraw_amount, 'description':self.withdraw_description})
      return True
    

  def get_balance(self):
    return self.balance

  def transfer(self, transfer_amount, category):
    
    #verify amount should be more than zero
    assert transfer_amount >= 0, f'{transfer_amount} is less than zero'

    #assign to self objects
    if self.balance < transfer_amount:
      return False
    else:
      self.transfer_amount = transfer_amount
      transfer_to_description = 'Transfer to {}'.format(category.name)
      transfer_from_description = 'Transfer from {}'.format(self.name)
      self.withdraw(transfer_amount, transfer_to_description)
      category.deposit(transfer_amount, transfer_from_description)
      return True 
    
  def check_funds(self, amount):
    return amount <= self.balance 

  def __str__(self):
    title = '{:*^30}'.format(self.name)
    content = ""
    total = "Total: {}".format(self.balance)

    for item in self.ledger:
      content += "{:<23}{:>7.2f}\n".format(item['description'][:23], item['amount'])

    return '{}\n{}{}'.format(title,content,total)

def create_spend_chart(categories:list):

  total_spent = 0
  category_spent = 0
  percentage_spent = []
  category_names = []
  number_of_categories = len(categories)
  
  #extract the percentage for each category and calculate height
  for each in categories: 
    for item in each.ledger: 
      if item['amount'] < 0: 
        category_spent += abs(item['amount'])
    total_spent += category_spent
    category_spent = 0

  for each in categories:
    for item in each.ledger: 
      if item['amount'] < 0: 
        category_spent += abs(item['amount'])
    percentage = int(category_spent / total_spent*100)
    percentage_spent.append(percentage)
    category_spent = 0
    

  #extract name of each category
  for each in categories: 
    category_names.append([x for x in each.name])

  #create chart
  chart = "Percentage spent by category\n"
  
  #start from the top, the algorithm for printing the chart is by comparing the percentage of each category   with the 'y-axis' that we create, starting from 100 down to 0 with decremental of 10 per each loop. if the   value of the percentage is higher or equal to the value of the 'y-axis', we will print "o" and print blank   space otherwise.
  for x in range(100,-10,-10):
    chart += '{:>3}|'.format(str(x))
    for y in percentage_spent:
      if y >= x:
        chart += ' o '
      else:
        chart += '   '
    chart+= ' \n'
  chart += 4*' ' + 3*number_of_categories*'-' + '-\n    '

  #print the name vertically
  n = 0
  maxLength = max(map(len, category_names))
  for x in range(maxLength):
    for each in category_names:
      if x < len(each):
        chart += " {} ".format(each[x])
      else:
        chart += '   '
    chart+=' \n    '
  
  return chart

  
  

  
    
    
  

    
    
