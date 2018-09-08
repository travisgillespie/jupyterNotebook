# Explore-and-Summarize-Data
Udacity Data Analysis Project 4

## Project Overview
This project uses R to apply exploratory data analysis techniques, explore relationships in one variable to multiple variables, and explore a selected data set for distributions, outliers, plus anomalies.

**Data Sets**<br>
The data set contains 1,599 red wines, and includes 12 variables that represent chemical properties and quality of the wine. At least 3 wine experts rated the quality of each wine, providing a rating between 0 (very bad) and 10 (very excellent).

**What do I need to install?**<br>
In order to complete the project, you will need to install R. You can download and install R from the Comprehensive R Archive Network (CRAN).

After installing R, you will need to download and install R Studio. Choose the appropriate installation for your operating system.

Finally, you will need to install a few packages. We recommend opening R Studio and installing the following packages using the command line.

<pre>
install.packages("ggplot2", dependencies = T)
install.packages("knitr", dependencies = T)
install.packages("dplyr", dependencies = T)
install.packages("RColorBrewer", dependencies = T)
install.packages("corrplot", dependencies = T)
</pre>

For more information on installing R packages, please refer to Installing R Packages on R Bloggers.

**Why this Project?**<br>
Exploratory Data Analysis (EDA) is the numerical and graphical examination of data characteristics and relationships before formal, rigorous statistical analyses are applied.

EDA can lead to insights, which may uncover to other questions, and eventually predictive models. It also is an important “line of defense” against bad data and is an opportunity to notice that your assumptions or intuitions about a data set are violated.

**What will I learn?**<br>
After completing the project, you will:
- Understand the distribution of a variable and to check for anomalies and outliers
- Learn how to quantify and visualize individual variables within a data set by using appropriate plots such as scatter plots, histograms, bar charts, and box plots
- Explore variables to identify the most important variables and relationships within a data set before building predictive models; calculate correlations, and investigate conditional means
- Learn powerful methods and visualizations for examining relationships among multiple variables, such as reshaping data frames and using aesthetics like color and shape to uncover more information
