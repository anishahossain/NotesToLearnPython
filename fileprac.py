def input_shows():
    shows = open(file_input)
    shows_list = []
    create_list = shows.readlines()
    for items in create_list:
        item = items.strip('\n')
        if item.isdigit() == False:
            shows_list.append(item)
    return shows_list
def input_file(file_input):

    shows = open(file_input)
    create_list = shows.readlines()
    seasons = None  # not a list
    shows_dict = {}

    for items in create_list:
        item = items.strip('\n')
        if item.isdigit() == True:
            seasons = int(item)  # not added to a list just assigned like a normal variable
            if seasons not in shows_dict:
                shows_dict[seasons] = []
        else:
            shows_dict[seasons].append(item)
    return shows_dict


def output_results(shows_dict, output_keys_file):
    with open(output_keys_file, 'w') as file:
        for seasons, shows in sorted(shows_dict.items(), reverse=True):
            file.write(f"{seasons}: {'; '.join(shows)}\n")

def output_shows(shows_list, output_titles_file):
    with open(output_titles_file, 'w') as nf:
        for shows in sorted(shows_list, reverse=True):
            nf.write(f'{shows}\n')

file_input = input()

shows_dict = input_file(file_input)
output_keys_file = 'output_keys.txt'
output_titles_file = 'output_titles.txt'
output_results(shows_dict, output_keys_file)# have to define since not a global variable
shows_list = input_shows()
output_shows(shows_list, output_titles_file)

# ['20 : Gunsmoke', '30 : The Simpsons', '10 : Will & Grace', '14 : Dallas', '20 : Law & Order', '12 : Murder, She Wrote']
