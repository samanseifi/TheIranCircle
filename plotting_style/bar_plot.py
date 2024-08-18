import matplotlib.pyplot as plt
from matplotlib import font_manager

def create_economist_style_barh_plot(data, label_column, value_column, title, subtitle, source, x_labels, x_ticks, output_file, farsi_font=None):
    """
    Creates a horizontal bar chart in the style described, with optional Farsi font support.

    Parameters:
        data (pd.DataFrame): DataFrame containing the data to plot.
        label_column (str): The name of the column to use for labels (e.g., 'country').
        value_column (str): The name of the column to use for values (e.g., 'gdp_trillions').
        title (str): The main title of the plot.
        subtitle (str): The subtitle of the plot.
        source (str): The source text to be displayed on the plot.
        x_labels (list): Custom labels for the x-axis.
        x_ticks (list): Custom ticks for the x-axis.
        output_file (str): Path to save the output image.
        farsi_font (str): Path to the Farsi font file. If provided, this font will be used.
    """
    # Setup plot size.
    fig, ax = plt.subplots(figsize=(3, 6))

    # Load Farsi font if provided
    if farsi_font:
        font_prop = font_manager.FontProperties(fname=farsi_font)
    else:
        font_prop = None

    # Create grid 
    ax.grid(which="major", axis='x', color='#758D99', alpha=0.6, zorder=1)

    # Remove splines
    ax.spines[['top', 'right', 'bottom']].set_visible(False)

    # Make left spine slightly thicker
    ax.spines['left'].set_linewidth(1.1)

    # Sort and select the top 9 rows based on the value_column
    data = data.sort_values(by=value_column)[-9:]

    # Plot data
    ax.barh(data[label_column], data[value_column], color='#006BA2', zorder=2)

    # Set custom labels for x-axis
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, fontproperties=font_prop)

    # Reformat x-axis tick labels
    ax.xaxis.set_tick_params(labeltop=True,      # Put x-axis labels on top
                             labelbottom=False,  # Set no x-axis labels on bottom
                             bottom=False,       # Set no ticks on bottom
                             labelsize=11,       # Set tick label size
                             pad=-1)             # Lower tick labels a bit

    # Reformat y-axis tick labels
    ax.set_yticklabels(data[label_column],        # Set labels again
                       ha='left',                # Set horizontal alignment to left
                       fontproperties=font_prop) # Apply Farsi font if specified
    ax.yaxis.set_tick_params(pad=100,            # Pad tick labels so they don't go over y-axis
                             labelsize=11,       # Set label size
                             bottom=False)       # Set no ticks on bottom/left

    # Shrink y-lim to make plot a bit tighter
    ax.set_ylim(-0.5, len(data)-0.5)

    # Add in line and tag
    ax.plot([-.35, .87],                 # Set width of line
            [1.02, 1.02],                # Set height of line
            transform=fig.transFigure,   # Set location relative to plot
            clip_on=False, 
            color='#E3120B', 
            linewidth=.6)
    ax.add_patch(plt.Rectangle((-.35, 1.02),        # Set location of rectangle by lower left corner
                               0.12,               # Width of rectangle
                               -0.02,              # Height of rectangle. Negative so it goes down.
                               facecolor='#E3120B', 
                               transform=fig.transFigure, 
                               clip_on=False, 
                               linewidth=0))

    # Add in title and subtitle
    ax.text(x=-.35, y=.96, s=title, transform=fig.transFigure, ha='left', fontsize=13, weight='bold', alpha=.8, fontproperties=font_prop)
    ax.text(x=-.35, y=.925, s=subtitle, transform=fig.transFigure, ha='left', fontsize=11, alpha=.8, fontproperties=font_prop)

    # Set source text
    ax.text(x=-.35, y=.08, s=source, transform=fig.transFigure, ha='left', fontsize=9, alpha=.7, fontproperties=font_prop)

    # Export plot as high resolution PNG
    plt.savefig(output_file,             # Set path and filename
                dpi=300,                 # Set dots per inch
                bbox_inches="tight",     # Remove extra whitespace around plot
                facecolor='white')       # Set background color to white
    plt.show()

