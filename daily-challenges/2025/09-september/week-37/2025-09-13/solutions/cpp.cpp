class Solution {
public:
    int maxFreqSum(string str) {
        int arr[26] = {0};

        for (char ch : str) {
            arr[ch - 'a']++;
        }

        int freq1 = 0, freq2 = 0;
        for (int i = 0; i < 26; i++) {
            if (i == 'a' - 'a' || i == 'e' - 'a' || i == 'i' - 'a' || i == 'o' - 'a' || i == 'u' - 'a') {
                if (freq1 < arr[i]) {
                    freq1 = arr[i];
                }
            } else {
                if (freq2 < arr[i]) {
                    freq2 = arr[i];
                }
            }
        }

        return freq1 + freq2;
    }
};