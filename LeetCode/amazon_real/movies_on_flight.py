"""
You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.

Example 1:

Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)
"""
def foo(flightDuration, movieDuration):
    # Write your code here
    # movie should finish before 30 minutes so target is
    target = flightDuration - 30
    indices_map = {}
    max_val = -1
    indices = [-1, -1]
    for idx, movie_duration in enumerate(movieDuration):
        if movie_duration not in indices_map:
            indices_map[target - movie_duration] = idx
        else:
            if movie_duration > max_val or target - movie_duration > max_val:
                indices[0] = indices_map[movie_duration]
                indices[1] = idx
                max_val = max(movie_duration, target - movie_duration)
    return indices


# movieDurations = [90, 85, 75, 60, 120, 150, 125]
# flightDurations = 290
movieDurations = [30, 40, 20, 10, 15]
flightDurations = 100
print(foo(flightDurations, movieDurations))