install.packages("plotly")
library(plotly)
plot_ly(seattle,x=day,y=temperature,type='scatter',mode='lines')
install.packages("leaflet")
library(leaflet)
library(dplyr)
leaflet()%>%
  addTiles()%>%
  addMarkers(lng = 75.37,lat = 12.10,popup="Location")