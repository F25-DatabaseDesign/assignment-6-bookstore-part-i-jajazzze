from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

categories = [
    [1,"Romantic Stories"],
    [2,"Detective Fiction"],
    [3,"Action & Fantasy"],
    [4,"Science Fiction"]
]


# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

books = [
    # Romantic
    [1, 1, "Pride and Prejudice", "Jane Austen", "9780000001001", 9.99, "pride_and_prejudice", 1],
    [2, 1, "Gone with the Wind", "Margaret Mitchell", "9780000001002", 11.99, "gone_with_the_wind", 0],
    [3, 1, "Wuthering Heights", "Emily Brontë", "9780000001003", 10.49, "wuthering_heights", 0],
    [4, 1, "Romeo and Juliet", "William Shakespeare", "9780000001004", 8.25, "romeo_and_juliet", 1],

    # Detective
    [5, 2, "The Hound of the Baskervilles", "Arthur Conan Doyle", "9780000002001", 8.50, "hound_of_the_baskervilles", 1],
    [6, 2, "Murder on the Orient Express", "Agatha Christie", "9780000002002", 10.75, "murder_on_the_orient_express", 0],
    [7, 2, "The Woman in White", "Wilkie Collins", "9780000002003", 9.40, "the_woman_in_white", 0],
    [8, 2, "The Maltese Falcon", "Dashiell Hammett", "9780000002004", 8.95, "the_maltese_falcon", 1],

    # Fantasy & Classics
    [9, 3, "Moby-Dick", "Herman Melville", "9780000003001", 12.00, "moby_dick", 0],
    [10, 3, "The Odyssey", "Homer", "9780000003002", 14.25, "the_odyssey", 1],
    [11, 3, "Tarzan of the Apes", "Edgar Rice Burroughs", "9780000003003", 9.75, "tarzan_of_the_apes", 1],
    [12, 3, "The Lord of the Rings", "J.R.R. Tolkien", "9780000003004", 15.99, "the_lord_of_the_rings", 0],

    # Sci-Fi
    [13, 4, "Journey to the Center of the Earth", "Jules Verne", "9780000004001", 9.50, "journey_to_the_center_of_the_earth", 0],
    [14, 4, "Frankenstein", "Mary Shelley", "9780000004002", 8.75, "frankenstein", 1],
    [15, 4, "The Time Machine", "H.G. Wells", "9780000004003", 7.99, "the_time_machine", 0],
    [16, 4, "We", "Yevgeny Zamyatin", "9780000004004", 9.20, "we", 1]
]



# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template("index.html",categories = categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    category_id = request.args.get("categoryId", type=int)

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [
        #for loop that filter the whole booklist to match the category user clicked
        b for b in books if b[1] == category_id
        ]

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template(
        "category.html",
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )
    

# we'll link this for project 2 to an sqlite3 database using flask's get_db() function
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('search','')
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template

if __name__ == "__main__":
    app.run(debug = True)
