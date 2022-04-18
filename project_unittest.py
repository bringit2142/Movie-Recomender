import project_1 as proj
#create a movie object
mv = proj.Movie(5, "movie 3", "comedy", ["a","b","c"])

if mv.movie_id == 5:
    print("success, movie object created")
else:
    print("failed, movie object not created")

#Create a reccomendations object
rec=proj.Recommendations()
mv2 = proj.Movie(6, "movie 3", "comedy", ["a","b","c"])
rec.add_recommendation(mv2, ["Netflix", "Amazon"])

if(rec.rec_list[0][0] == mv2):
    print("Success, Rec obj created")
else:
    print("Rec object Failed")
    
#Call Create_dataset() check if it gets a response 
df = proj.create_dataset()
if df.empty:
    print('Dataset creation failed')
else:
    print('Dataset created uccessfully')
    

#test the streaming service 
svc = proj.get_streaming_svc_list(mv2)
if svc == ["Netflix","Amazon"]:
    print("svc success")
else:
    print("svc fail")
    
#Test the get reccomendation movie
mvlist = proj.get_recommendation_movie(mv2)
if len(mvlist) != 0:
    print("rec list success")
else:
    print("rec list fail")
