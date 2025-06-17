from flask import Flask , request , render_template , send_file
import os
from werkzeug.utils import secure_filename
from pdfreader import extract_text_from_pdf
from preprocessing import preprocess
from scoring import rank_resumes

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET","POST"])
def index():
    ranks = []
    if request.method == "POST":
        job_desc = request.form["job_description"]
        job_desc_processed = preprocess(job_desc) 
        
        resume_texts = []
        filenames = []
        
        for file in request.files.getlist("resumes"):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            file.save(path)
            text = extract_text_from_pdf(path)
            processed = preprocess(text)
            resume_texts.append(processed)
            filenames.append(filename)
            
        scores = rank_resumes(resume_texts , job_desc_processed)
        ranks = sorted(zip(filenames,scores), key=lambda x: x[1], reverse= True)
    return render_template("index.html",ranks=ranks)
if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER , exist_ok= True)
    app.run(debug=True)       
            