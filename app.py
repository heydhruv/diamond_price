from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline
# from src.pipeline.training_pipeline import 
app=Flask(__name__)

@app.route('/')
def home():


    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':

        return render_template('form.html')
    else:
        data=CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            color=request.form.get('color'),
            cut=request.form.get('cut'),
            clarity=request.form.get('clarity'),

        )
        final_df=data.get_my_as_dataframe()

        prediction_pipeline=PredictPipeline()
        pred=prediction_pipeline.predict(final_df)

        results=round(pred[0],2)

        return render_template('result.html',final_result=results)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)