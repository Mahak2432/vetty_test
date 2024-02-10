from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/') 
def read_file():
   
    file_name = request.args.get('file', 'file1.txt')
    print(file_name)
   
    start_line = int(request.args.get('start_line', 0))
    end_line = int(request.args.get('end_line', -1))
    
    try:
       
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
          lines = file.readlines()


     
        if end_line > len(lines) or end_line == -1:
            end_line = len(lines)

        # Get content between start_line and end_line
        lines = lines[start_line:end_line]


        return render_template('file_content.html', lines=lines)

    except Exception as e:
      
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
