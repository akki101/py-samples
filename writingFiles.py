from datetime import datetime

with open("C:/Users/jc308511/Desktop/Darshan_attendance.txt", 'r') as file:
    A_list = file.readlines()
    with open("C:/Users/jc308511/Desktop/darshan.txt", 'a') as file2:
        count = 1
        for line in A_list:
    
            words = line.split('_')
            
            inputString = f"{words[2]}, {words[3][:6]}"
            parsed_datetime = datetime.strptime(inputString, "%Y%m%d, %H%M%S")
        
            formatted_datetime = parsed_datetime.strftime("%d/%m/%Y %I:%M %p")
            print(parsed_datetime.time())

            if(parsed_datetime.time().hour < 12):
                greet = "MORNING"

            elif(parsed_datetime.time().hour < 20): 
                greet = "AFTERNOON"
            
            else:
                greet = "EVENING"

            file2.write(f"{count}.  Darshan_{words[2]}_{greet}           {formatted_datetime}\n")
            count += 1
