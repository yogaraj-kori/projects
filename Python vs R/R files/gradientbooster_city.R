## start time to check the execution time

start_time <- Sys.time()

# Load required libraries
library(gbm)  # For Gradient Boosting
library(Metrics)  # For evaluation metrics

# Read the CSV file
data <- read.csv("C:\\Users\\vishw\\DMML TABA\\Output City.csv")

# Check the structure of your data
str(data)


# Split the data into training and testing sets 80-20 split
set.seed(123) # for reproducibility
train_index <- sample(1:nrow(data), 0.8 * nrow(data))
train_data <- data[train_index, ]
test_data <- data[-train_index, ]

# Train the Gradient Boosting model
gbm_model <- gbm(Quads ~ ., data = train_data, n.trees = 100, interaction.depth = 4, shrinkage = 0.1)

# Predict using the trained model
y_predict <- predict(gbm_model, newdata = test_data, n.trees = 100)

library(randomForest)
library(DALEX)

regression_results <- function(y_test, y_predict) {
  # Calculate explained variance manually
  explained_variance <- 1 - var(y_test - y_predict) / var(y_test)
  
  # Other regression metrics
  mean_absolute_error <- mean(abs(y_test - y_predict))
  mse <- mean((y_test - y_predict)^2)
  median_absolute_error <- median(abs(y_test - y_predict))
  r2 <- 1 - (sum((y_test - y_predict)^2) / sum((y_test - mean(y_test))^2))
  
  cat('explained_variance is ', round(explained_variance, 2), '\n')
  cat('r2 is ', round(r2, 4), '\n')
  cat('MAE is ', round(mean_absolute_error, 4), '\n')
  cat('MSE is ', round(mse, 4), '\n')
  cat('RMSE is ', round(sqrt(mse), 4), '\n')
}

regression_results(test_data$Quads, y_predict)

library(ggplot2)

# Create a data frame with actual and predicted values
plot_data <- data.frame(Actual = test_data$Quads, Predicted = y_predict)

# Create the actual vs predicted plot
ggplot2::ggplot(plot_data, aes(x = Actual, y = Predicted)) +
  ggplot2::geom_point() +
  ggplot2::geom_abline(slope = 1, intercept = 0, color = "red", linetype = "dashed") +
  ggplot2::labs(x = "Actual", y = "Predicted", title = "Actual vs Predicted Plot")


residuals <- test_data$Quads - y_predict

residual_plot_data <- data.frame(Predicted = y_predict, Residuals = residuals)
# Create the residual plot
ggplot2::ggplot(residual_plot_data, aes(x = Predicted, y = Residuals)) +
  ggplot2::geom_point() +
  ggplot2::geom_hline(yintercept = 0, color = "red", linetype = "dashed") +
  ggplot2::labs(x = "Predicted", y = "Residuals", title = "Residual Plot")


# Create a Q-Q plot
# Adjust figure margins
par(mar = c(5, 5, 2, 2))  # Set bottom, left, top, and right margins in inches

# Create a Q-Q plot
qqnorm(residuals)
qqline(residuals, col = 2)


end_time <- Sys.time()
execution_time <- end_time - start_time
print(execution_time)