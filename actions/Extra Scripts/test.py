import pandas as pd
import os
loc = os.path.join(os.getcwd(), os.path.basename("./output_file.json"))
club_name = "ACM"
data = pd.read_json(loc)  
data = pd.DataFrame(data)
result_data = data.query("Name == @club_name")
if not result_data.empty:
    msg = "Club Name : "+club_name+"\nClub Lead : "+result_data["Club_Lead"].iloc[0]+ "\nClub President : "+result_data["Club_President"].iloc[0]+"\nClub Description : "+result_data["Club_Description"].iloc[0]+"\nInstagram Handle : https://instagram.com/"+result_data["Insta_handle"].iloc[0]
else:
    msg = f"The club you are looking for doesn't seem to exist. Could you please check again"
  
print(len(data["Name"]))