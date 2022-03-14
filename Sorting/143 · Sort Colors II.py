class Solution_rainbow_sort:
    
    def sortColors2(self, colors, k):
        
        self.color_partition(colors, 0, len(colors)-1, 1, k)
        
    def color_partition(self, colors, start, end, lo, hi):
        
        if lo == hi or start == end:
            return
        
        k = (lo+hi) // 2
        
        pivot = colors[end]
        left, right = start, end 
        while left <= right:
            while left <= right and colors[left] <= k:
                left += 1 
            while left <= right and colors[right] > k:
                right -= 1 
                
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1 
                
        self.color_partition(colors, start, right, lo, k)
        self.color_partition(colors, left, end, k+1, hi)