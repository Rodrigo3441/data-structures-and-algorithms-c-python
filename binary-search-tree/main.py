from bst import *

root = None

for i in [10, 23, 44, 9, 5, 32, 49, 78, 77, 54]:
    root = insert(root, i)

while True:
    inorder(root)
    print()
    
    print('Please select your desired procedure:')
    print('1- Insert a node')
    print('2- Search a node')
    print('3- Find max node')
    print('4- Find min node')
    print('5- Find height')
    print('6- Delete a node')
    print('7- Go out')

    option = int(input())

    match option:
        case 1:
            print('Enter the number you want to enter:')
            value = int(input())
            insert(root, value)
            
        case 2:
            print('Enter the number you want to search:')
            value = int(input())
            search(root, value)
            
        case 3:
            print(find_max(root))
            
        case 4:
            print(find_min(root))
  

        case 5:
            print(find_height(root))

        case 6:
            print('Enter the number you want to delete:')
            value = int(input())
            delete_node(root, value)

        case 7:
            break
            
