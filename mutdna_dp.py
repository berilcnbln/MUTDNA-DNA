#include <iostream>
#include <vector>
#include <algorithm>

int dp_function(const std::string& s) {
    int n = s.length();

    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(4, 0));

    for (int i = 1; i <= n; ++i) {
        if (s[i - 1] == 'B') {
            dp[i][0] = std::min(dp[i - 1][3] + 1, dp[i - 1][2] + 1);
            dp[i][1] = std::min(dp[i - 1][3], dp[i - 1][2] + 2);
        } else {
            dp[i][0] = std::min(dp[i - 1][0], dp[i - 1][1] + 2);
            dp[i][1] = std::min(dp[i - 1][0] + 1, dp[i - 1][1] + 1);
        }

   
        dp[i][2] = dp[i][0];
        dp[i][3] = dp[i][1];
    }

    return dp[n][0];
}

int main() {
 
    int length;
    std::cin >> length;


    std::string user_input;
    std::cin >> user_input;

  
    if (user_input.length() != static_cast<size_t>(length)) {
        std::cout << "" << std::endl;
    } else {
        
        int result = dp_function(user_input);

    
        std::cout << "" << result << std::endl;
    }

    return 0;
}
