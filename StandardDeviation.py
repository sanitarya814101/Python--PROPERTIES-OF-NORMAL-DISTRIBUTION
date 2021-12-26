import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

mean = sum(df["math score"])/len(df["math score"])

median = statistics.median(df["math score"])

mode = statistics.mode(df["math score"])

standard_deviation = statistics.stdev(df["math score"])

print("The mean of data is:", mean)
print("The median of data is:", median)
print("The mode of data is:", mode)
print("The standard deviation of data is:", standard_deviation)

sd1_start, sd1_end = standard_deviation, mean + standard_deviation

sd2_start, sd2_end = (standard_deviation * 2), mean + (standard_deviation * 2)

sd3_start, sd3_end = (standard_deviation * 3), mean + (standard_deviation * 3)

fig = ff.create_distplot([df["math score"].tolist()], [
                         "Math Score"], show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.03], mode="lines", name="Mean"))

fig.add_trace(go.Scatter(x=[sd1_start, sd1_start], y=[
              0, 0.03], mode="lines", name="Standard Deviation 01"))

fig.add_trace(go.Scatter(x=[sd1_end, sd1_end], y=[
              0, 0.03], mode="lines", name="Standard Deviation 01"))

fig.add_trace(go.Scatter(x=[sd2_start, sd2_start], y=[
              0, 0.03], mode="lines", name="Standard Deviation 02"))

fig.add_trace(go.Scatter(x=[sd2_end, sd2_end], y=[
              0, 0.03], mode="lines", name="Standard Deviation 02"))

fig.add_trace(go.Scatter(x=[sd3_start, sd3_start], y=[
              0, 0.03], mode="lines", name="Standard Deviation 03"))

fig.add_trace(go.Scatter(x=[sd3_end, sd3_end], y=[
              0, 0.03], mode="lines", name="Standard Deviation 03"))

fig.show()

data_sd1 = [df for df in df["math score"] if df > sd1_start and df < sd1_end]

data_sd2 = [df for df in df["math score"] if df > sd2_start and df < sd2_end]

data_sd3 = [df for df in df["math score"] if df > sd3_start and df < sd3_end]

print("{}% of data lies within first standard deviation".format(
    len(data_sd1) * 100.0/len(df["math score"])))

print("{}% of data lies within first standard deviation".format(
    len(data_sd2) * 100.0/len(df["math score"])))

print("{}% of data lies within first standard deviation".format(
    len(data_sd3) * 100.0/len(df["math score"])))
