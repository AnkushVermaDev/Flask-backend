from flask import Flask , jsonify, request




books_data  = [

{"id":1,"title":"java coding " , "Price":677},
{"id":2,"title":"fundamental of computing" , "Price":990},

]


app = Flask(__name__)


@app.route('/booksIndex',methods=['get'])

def getName():
    return books_data


# POST REQUEST WITH THE HELP OF 

@app.route('/uploadBook',methods=['post'] )

def uploadFunc():
    new_book  = {'id':len(books_data)+1, "title":request.json['title'],  "Price" : request.json['Price']}
    books_data.append(new_book)
    return new_book


if __name__ == '__main__':
    app.run(debug=True)