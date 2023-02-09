#process 1:take input from user.
operand1=input('please enter number1:')
operand2=input('please enter number2:')
operator=input('enter the operator:')
operand1=int(operand1)
operand2=int(operand2)
result=' '
if operator == '+':
  result=operand1+operand2
elif operator=='-':
  result=operand1-operand2
elif operator=='*':
  result=operand1*operand2
elif operator=='/':
  result=operand1/operand2
else:
  result ='not defined'
print('the result is:',result)