import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# I needed some sample data to train the model on
# It makes random numbers for things like study hours and stuff
def load_data(n=100):
    np.random.seed(42)

    # Let's generate the study hours first
    study_hours=np.random.uniform(0,10,n)
    # Then attendance, I think this range makes sense
    attendance=np.random.uniform(50,100,n)
    # Sleep hours, people need sleep
    sleep_hours=np.random.uniform(4,9,n)
    # And previous scores, from low to high
    previous_score=np.random.uniform(30,90,n)

    # Now calculate the score
    # I looked up some studies and came up with these weights
    # Study hours should matter a lot, attendance too, sleep is important, and past performance
    score=(1.8*study_hours+0.7*attendance+1.0*sleep_hours+0.5*previous_score+np.random.normal(0,3,n)) 
    
    score=np.clip(score,0,100) #keeping the score within the boundaries

    # Stick it all in a dataframe
    data=pd.DataFrame({"study_hours":study_hours,"attendance":attendance,"sleep_hours":sleep_hours,"previous_score":previous_score,"score":score})

    return data

# Simple function to train the model
def train_model(X_train,y_train):
    model = LinearRegression()
    model.fit(X_train,y_train)
    return model

# This checks how well the model did
def evaluate_model(model,X_test,y_test):
    predictions=model.predict(X_test)
    mae=mean_absolute_error(y_test,predictions)
    r2=r2_score(y_test,predictions)

    # Just print the metrics
    print("Mean Absolute Error:",round(mae,2))
    print("R² Score:",round(r2,2))

# Function to ask the user for input
def get_user_input():
    try:
        # Prompt for each input
        study_hours=float(input("Enter study hours per day: "))
        attendance=float(input("Enter attendance percentage: "))
        sleep_hours=float(input("Enter sleep hours per day: "))
        previous_score=float(input("Enter previous exam score: "))
        return study_hours,attendance,sleep_hours,previous_score
    except ValueError:
        # Handle bad input
        print("Invalid Input! Please enter numeric values.")
        return None, None, None, None

# Validate that the inputs are valid
def validate_input(study_hours,attendance,sleep_hours,previous_score):
    # Check if study hours are okay
    if not (0<=study_hours<=24):
        print("Study hours must be between 0 and 24")
        return False
    # Same for attendance
    if not (0<=attendance<=100):
        print("Attendance must be between 0 and 100")
        return False
    # Sleep hours
    if not (0<=sleep_hours<= 24):
        print("Sleep hours must be between 0 and 24")
        return False
    # Previous score
    if not (0<=previous_score<=100):
        print("Previous score must be between 0 and 100")
        return False
    return True

# Predicting the score of the user
def predict_score(model,study_hours,attendance,sleep_hours,previous_score):
    # Make a dataframe for the prediction
    input_data=pd.DataFrame({"study_hours":[study_hours],"attendance":[attendance],"sleep_hours":[sleep_hours],"previous_score":[previous_score]})
    predicted_score=model.predict(input_data)
    # Keep it in bounds
    predicted_score=np.clip(predicted_score[0],0,100)
    # Print it out nicely
    print("Predicted Score:",round(predicted_score, 2))



# Main function
def main():
    # Get the data
    data=load_data(200)

    # Set up X and y
    X=data[["study_hours", "attendance", "sleep_hours", "previous_score"]]
    y=data["score"]

    # Split for training and testing
    X_train,X_test,y_train,y_test=train_test_split(X, y,test_size=0.2,random_state=42)

    # Train and evaluate
    model=train_model(X_train,y_train)
    evaluate_model(model,X_test,y_test)

    # Train again on full data
    model.fit(X,y)

    # Now the loop for user predictions
    while True:
        # Get user inputs
        study_hours,attendance,sleep_hours,previous_score=get_user_input()

        # Skip if invalid
        if study_hours is None:
            continue

        # If good, predict
        if validate_input(study_hours,attendance,sleep_hours,previous_score):
            predict_score(model,study_hours,attendance,sleep_hours,previous_score)

        # Check if we want to continue
        choice=input("Do you want to predict your score again? (y/n): ")
        if choice.lower()!='y':
            print("Exiting program...See you soon")
            break
# Program run
if __name__=="__main__":
    main()
    