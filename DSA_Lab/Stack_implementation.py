stack_list= []

while(True):
    print("1.Push\n2.Pop\n3.View top element\n4. size of current stack\nany other key to exit")
    x = int(input())
    
    if(x == 1):
        print("\n enter number to be inserted:")
        i = int(input())
        stack_list.append(i)
        print("\n current stack is", stack_list)
        
    elif(x == 2):
        stack_list.pop()
        print("\n current stack is", stack_list)
    elif(x == 3):
        if(len(stack_list) == 0):
            print("\nstack empty\n")
        else:
            y  = stack_list[-1]
            print("Top element is: ", y)
    elif(x == 4):
        print("\n Current length is:",len(stack_list))
    else:
        break