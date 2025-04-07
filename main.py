# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# =============================================================================

def main():
    # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        }
    }

    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        header = file.readline()
        for line in file:
            line = line.strip()
            columns = line.split(',')
            user_id = columns[0]
            algorithm = columns[1]
            session_duration = int(columns[2])
            happiness_rating = int(columns[3])

            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                print(f"Unknown algorithm: {algorithm}")

    # TODO: Calculate averages for each algorithm
    # For each algorithm in the stats dictionary:
    #   - Calculate avg_happiness = total_happiness / session_count
    #   - Calculate avg_duration = total_duration / session_count
    #   - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration'
    for algorithm in stats:
        avg_happiness = int(stats[algorithm]["total_happiness"]) / int(stats[algorithm]["session_count"])
        avg_duration = int(stats[algorithm]["total_duration"]) / int(stats[algorithm]["session_count"])
        stats[algorithm]["avg_happiness"] = avg_happiness
        stats[algorithm]["avg_duration"] = avg_duration

    # TODO: Determine the algorithm with the highest average happiness rating
    # Initialize variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values
    highest_avg_happiness = 0
    highest_avg_happiness_algo = ""
    for algorithm in stats:
        if int(stats[algorithm]['avg_happiness']) > highest_avg_happiness:
            highest_avg_happiness = stats[algorithm]['avg_happiness']
    highest_avg_happiness_algo = stats[algorithm]

    # TODO: Determine the algorithm with the longest average session duration
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values
    longest_duration = 0
    longest_duration_algo = ""
    for algorithm in stats:
        if int(stats[algorithm]['avg_duration']) > longest_duration:
            longest_duration = stats[algorithm]['avg_duration']
    longest_duration_algo = stats[algorithm]

    # TODO: Print the report
    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output

    print("Euphoria User Engagement Analysis Report")
    print("-" * 50)
    print("")
    print("Average Happiness Rating per Algorithm:")
    print(f"- JoyStream: {stats["JoyStream"]["avg_happiness"]:.2f}")
    print(f"- SerenityFlow: {stats["SerenityFlow"]["avg_happiness"]:.2f}")
    print(f"- DeepPulse: {stats["DeepPulse"]["avg_happiness"]:.2f}")
    print("")
    print("Total Session Count per Algorithm:")
    print(f"- JoyStream: {stats["JoyStream"]["session_count"]}")
    print(f"- SerenityFlow: {stats["SerenityFlow"]["session_count"]}")
    print(f"- DeepPulse: {stats["DeepPulse"]["session_count"]}")
    print("")
    print("Average Session Duration per Algorithm:")
    print(f"- JoyStream: {stats["JoyStream"]["avg_duration"]:.2f} minutes")
    print(f"- SerenityFlow: {stats["SerenityFlow"]["avg_duration"]:.2f} minutes")
    print(f"- DeepPulse: {stats["DeepPulse"]["avg_duration"]:.2f} minutes")
    print("")
    print("Highest Average Happiness Rating:")
    print(f"{highest_avg_happiness_algo} with an average happiness rating of {highest_avg_happiness:.2f}")
    print("")
    print("Longest Average Session Duration:")
    print(f"{longest_duration_algo} with a duration length of {longest_duration:.2f}")
    


if __name__ == "__main__":
    main()