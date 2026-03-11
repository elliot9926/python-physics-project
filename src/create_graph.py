import matplotlib
matplotlib.use('Agg') # Force matplotlib to disable its UI, or else it throws an error
import matplotlib.pyplot as plt

class GraphHelper:
    def __init__(self):
        pass
    
    @staticmethod
    def draw_graph(x_axis, y_axis):
        plt.scatter(x_axis, y_axis)

        plt.xlabel("Time (Days)")
        plt.ylabel("Average distance between bodies (meters)")
        plt.title("Average distance between bodies in the system over time")

        plt.savefig("output/scatter_plot.png", dpi=300, bbox_inches='tight')

        plt.close()