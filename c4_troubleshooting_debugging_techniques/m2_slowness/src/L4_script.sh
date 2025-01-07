time ./send_reminders.py "2025-01-15|Example|test1" # measure the script speed | one test user
time ./send_reminders.py "2025-01-15|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9" # measure the script speed | nine test users
pprofile3 -f callgrind -o profile.out ./send_reminders.py "2025-01-15|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9" # generate output file
kcachegrind profile.out # gui for looking into profile.out file | see the function calls and time spent in each function

# ref: slow-script-with-expensive-loop lecture
