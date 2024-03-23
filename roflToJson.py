import json


def extract_json_like_data(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()  
        
    decoded_content = content.decode('utf-8', 'ignore')
    
    try:
        start_index = decoded_content.index('[{')
        end_index = decoded_content.index('}]', start_index) + 2 
        json_like_data = decoded_content[start_index:end_index]
        return json_like_data
    except ValueError as e:
        return f"Specified pattern not found: {e}"

# Replace 'your_file_path_here' with the path to your .rofl file
file_path = "your_file_path_here"
specific_json_like_data = extract_json_like_data(file_path)
json_like_string = specific_json_like_data.replace("\\","")


def parse_unknown_structure_json_string(json_string):
    objects = []
    pos = 0
    while pos < len(json_string):
        try:
            obj, end = json.JSONDecoder().raw_decode(json_string[pos:])
            objects.append(obj)
            pos += end
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
    return objects

parsed_objects = parse_unknown_structure_json_string(json_like_string)

total_seconds = int(parsed_objects[0][0]['TIME_PLAYED'])
minutes = total_seconds // 60
seconds = total_seconds % 60

time_played = f"{minutes:02d}:{seconds:02d}"
print(time_played)

for player in parsed_objects[0]:
    print(f"{player['PUUID']} \n{player['SKIN']} | KDA: {player['CHAMPIONS_KILLED']} / {player['NUM_DEATHS']} / {player['ASSISTS']} | {player['MINIONS_KILLED']} minions | {player['GOLD_EARNED']} gold | Role: {player['INDIVIDUAL_POSITION']} | {player['VISION_SCORE']} vision score | Win {player['WIN']}")




