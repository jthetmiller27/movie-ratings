import csv
 
def read_csv_data_set(file_name):
    '''
    Read a data set from a CSV file.
 
    Parameters
    ----------
    file_name : string
        Name of the CSV file in the current folder.
 
    Returns
    -------
    data_set : List of dictionaries.
        Data set.
 
    '''
    # Create a list to be the return value.
    data_set = []
    with open('./' + file_name) as file:
        file_csv = csv.DictReader(file)
        # Put each row into the return list.
        for row in file_csv:
            data_set.append(row)
    return data_set

def is_rating_ok(rating):
    #is it a number?
    try:
        rating = int(rating)
    except Exception:
        return False
    #check range
    if rating < 1 or rating > 5:
        return False
    return True

def is_record_ok(record):
    #code to validate movie name
    movie_name = record['Title']
    if movie_name == '' or movie_name == None:
        return False
    #code to validate movie genre
    movie_genre = record['Genre']
    movie_genre = movie_genre.strip().lower()
    if movie_genre != 'romance' and movie_genre != 'action' and movie_genre != 'scifi':
        return False
    #code to validate critic rating
    critic_rating = record['Critic rating']
    if not is_rating_ok(critic_rating):
        return False
    #code to validate viewer rating
    viewer_rating = record['Viewer rating']
    if not is_rating_ok(viewer_rating):
        return False
    return True

def count_valid_records(records):
    valid_records = 0 
    for record in records:
        if is_record_ok(record):
            valid_records += 1
    return valid_records
  
#processing
movie_ratings = read_csv_data_set('movie-ratings.csv')

valid_records = count_valid_records(movie_ratings)

#find total critic and viewer rating
total_critic = 0
total_viewer = 0
for movie in movie_ratings:
    if is_record_ok(movie):
        total_critic += int(movie['Critic rating'])
        total_viewer += int(movie['Viewer rating'])

#find average critic and viewer rating
average_critic = total_critic / valid_records 
average_viewer = total_viewer / valid_records
    
#output
print('Number of records read: ' + str(len(movie_ratings)))
print('Number of valid records: ' + str(valid_records))
print('Average critic rating: ' + str(average_critic))
print('Average viewer rating: ' + str(average_viewer))