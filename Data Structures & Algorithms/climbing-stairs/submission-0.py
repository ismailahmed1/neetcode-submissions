class Solution:
    def climbStairs(self, n: int) -> int:
        currentStep = 0 
        previousStep = 1

        for i in range (n - 1, -1, -1):
            totalSteps = currentStep + previousStep
            currentStep = previousStep
            previousStep = totalSteps
        

        return totalSteps

