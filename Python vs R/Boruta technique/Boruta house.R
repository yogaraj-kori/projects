library(Boruta)
library(randomForest)

# Import CSV file
data <- read.csv("C:\\Users\\vishw\\DMML TABA\\Output house.csv")



# Apply Boruta with Random Forest
boruta_result <- Boruta(Appliances ~ ., data = data, doTrace = 2)

print(boruta_result)

plot(boruta_result, cex.axis = 0.7, las = 2)
# Extract selected features
selected_features <- getSelectedAttributes(boruta_result)

# Print selected features
print(selected_features)