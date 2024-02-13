#Create a dictionary representing a library catalogue.
# Each book should have a title, author, and publication year.

library_catalogue=[
    {
       "title":"A Little Book for Little Children ",
        "auther":"Thomas White",
        "publication_year":1702
    },
    {
      "title":"A Description of Three Hundred Animals",
      "auther":" Thomas Boreman",
      "publication_year":1730
    },
    {
        "title":"Sacred Dramas",
        "auther":"Hannah More",
        "publication_year":1782
    }
]
for x in library_catalogue:
    print("title:",x["title"])
    print(f"auther:{x["auther"]}")
    print(f"publication year:{x["publication_year"]}")
    print("-------------------")
