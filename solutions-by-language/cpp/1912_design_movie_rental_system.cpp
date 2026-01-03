#include <bits/stdc++.h>
using namespace std;

class MovieRentingSystem {
    unordered_map<int, set<pair<int,int>>> available; // movie -> {(price, shop)}
    set<tuple<int,int,int>> rented; // {(price, shop, movie)}
    unordered_map<long long,int> priceMap; // (shop,movie) -> price

    long long key(int shop, int movie) {
        return ((long long)shop << 20) | movie;
    }

public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for (auto &e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            available[movie].insert({price, shop});
            priceMap[key(shop,movie)] = price;
        }
    }

    vector<int> search(int movie) {
        vector<int> res;
        auto &s = available[movie];
        for (auto it = s.begin(); it != s.end() && res.size() < 5; ++it)
            res.push_back(it->second);
        return res;
    }

    void rent(int shop, int movie) {
        int price = priceMap[key(shop,movie)];
        available[movie].erase({price, shop});
        rented.insert({price, shop, movie});
    }

    void drop(int shop, int movie) {
        int price = priceMap[key(shop,movie)];
        rented.erase({price, shop, movie});
        available[movie].insert({price, shop});
    }

    vector<vector<int>> report() {
        vector<vector<int>> res;
        for (auto it = rented.begin(); it != rented.end() && res.size() < 5; ++it) {
            auto [price, shop, movie] = *it;
            res.push_back({shop, movie});
        }
        return res;
    }
};