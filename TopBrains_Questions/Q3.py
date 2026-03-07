class Solution:
    def low_stock_products(self, inventory):
        result = []
        #Write your code here
        for i in inventory:
            if inventory[i] < 10:
                result.append(i)
       
        return result