import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the training data
df = pd.read_csv('golf_ball_data.csv')

# Split the data into features and labels
X = df[['gender', 'handicap', 'driver_ball_speed', 'price_range']]
y = df['recommended_ball']

# Train a random forest classifier on the data
model = RandomForestClassifier()
model.fit(X, y)

# Ask the user for their information
gender = input('What is your gender (male/female)? ')
handicap = int(input('What is your golf handicap? '))
driver_ball_speed = int(input('What is your driver ball speed (in mph)? '))
price_range = int(input('What is your price range (1-5)? '))
current_ball = input('What golf ball do you currently use? ')
like_current_ball = input('Do you like your current golf ball (yes/no)? ')

# If the user likes their current golf ball, add it to the training data
if like_current_ball == 'yes':
    new_data = {'gender': [gender], 'handicap': [handicap], 'driver_ball_speed': [driver_ball_speed], 'price_range': [price_range], 'recommended_ball': [current_ball]}
    new_df = pd.DataFrame(data=new_data)
    df = df.append(new_df, ignore_index=True)
    X = df[['gender', 'handicap', 'driver_ball_speed', 'price_range']]
    y = df['recommended_ball']
    model.fit(X, y)

# Make a prediction based on the user's information
prediction = model.predict([[gender, handicap, driver_ball_speed, price_range]])

# Recommend a golf ball to the user
print(f'We recommend using the {prediction[0]} golf ball.')
