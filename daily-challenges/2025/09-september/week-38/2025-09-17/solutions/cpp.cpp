#include <bits/stdc++.h>
using namespace std;

class FoodRatings {
    unordered_map<string, string> foodToCuisine;
    unordered_map<string, int> foodToRating;
    unordered_map<string, set<pair<int,string>>> cuisineSets; // (-rating, name)

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        int n = foods.size();
        for (int i = 0; i < n; ++i) {
            const string &f = foods[i];
            const string &c = cuisines[i];
            int r = ratings[i];
            foodToCuisine[f] = c;
            foodToRating[f] = r;
            cuisineSets[c].insert({-r, f});
        }
    }

    void changeRating(string food, int newRating) {
        string c = foodToCuisine[food];
        int old = foodToRating[food];
        auto &s = cuisineSets[c];
        s.erase({-old, food});
        s.insert({-newRating, food});
        foodToRating[food] = newRating;
    }

    string highestRated(string cuisine) {
        auto &s = cuisineSets[cuisine];
        return s.begin()->second;
    }
};