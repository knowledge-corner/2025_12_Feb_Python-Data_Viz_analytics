from flask import Flask, render_template, Response
import io
import seaborn as sns
import matplotlib.pyplot as plt
from mpg import df

plt.rcParams["figure.figsize"] = (4, 3)
plt.rcParams['xtick.labelsize'] = 'x-small'
plt.rcParams['ytick.labelsize'] = 'x-small'
plt.rcParams['xtick.color'] = 'darkslategrey'
plt.rcParams['ytick.color'] = 'darkslategrey'
plt.rcParams['legend.fontsize'] = 'x-small'  
plt.rcParams['legend.edgecolor'] = 'darkslategrey'

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/bar_chart.png")
def bar_chart():
    fig = plt.figure()
    sns.barplot(data = df, x = "origin", y = "horsepower", errorbar=None, hue = "origin", palette="viridis")

    output= io.BytesIO()
    fig.savefig(output, format = "png")
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype="image/png")

@app.route("/scatter_chart.png")
def scatter_chart():
    fig = plt.figure()
    sns.scatterplot(data = df, x = 'weight', y= "mpg")

    output= io.BytesIO()
    fig.savefig(output, format = "png")
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype="image/png")

@app.route("/box_chart.png")
def box_chart():
    fig = plt.figure()
    sns.boxplot(data = df, x = "origin", y = "mpg", hue = "origin", palette="pastel")

    output= io.BytesIO()
    fig.savefig(output, format = "png")
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype="image/png")


if __name__ == "__main__":
    app.run()