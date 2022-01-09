def run():
    affirmation = input('Do you want analyze the ratings? ')
    total_qualified = 0
    approved = 0
    average = 0
    sum_average = 0
    
    while affirmation == 's':
        check = int(input('Enter the calification: '))
        total_qualified += 1
        
        if check > 4:
            approved += 1
            sum_average += check
        
        affirmation = input('Enter "s" for continued or other key for end: ')

    approved_percent = (approved / total_qualified) * 100
    average = sum_average /   approved    
    
    print(f'The percent of approved is {approved_percent}% and the average is {average}')      
            
if __name__ == '__main__':
    run()