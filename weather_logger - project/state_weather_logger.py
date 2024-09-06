import csv
from statistics import mean

# File to store weather data
FILE_NAME = 'state_weather_data.csv'

def log_weather(location, temperature, humidity):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([location, temperature, humidity])

def view_logs():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\nLocation    | Temperature | Humidity")
            print("-------------------------------------")
            for row in reader:
                print(f"{row[0]}    | {row[1]}°C         | {row[2]}%")
    except FileNotFoundError:
        print("No weather data found yet.")

def get_stats_by_location(location):
    temperatures = []
    humidities = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == location:
                    temperatures.append(float(row[1]))
                    humidities.append(float(row[2]))
        if temperatures:
            avg_temp = mean(temperatures)
            avg_humidity = mean(humidities)
            print(f"\nStatistics for {location}:")
            print(f"Average Temperature: {avg_temp:.2f}°C")
            print(f"Average Humidity: {avg_humidity:.2f}%")
        else:
            print("No data found for the specified location.")
    except FileNotFoundError:
        print("No weather data found yet.")

def main():
    while True:
        print("\nState Weather Statistics Logger")
        print("1. Log Weather Data")
        print("2. View All Logs")
        print("3. Get Statistics by Location")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            location = input("Enter location: ")
            temperature = input("Enter temperature (°C): ")
            humidity = input("Enter humidity (%): ")
            log_weather(location, temperature, humidity)
            print("Weather data logged successfully.")
        elif choice == '2':
            view_logs()
        elif choice == '3':
            location = input("Enter location to get statistics for: ")
            get_stats_by_location(location)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
