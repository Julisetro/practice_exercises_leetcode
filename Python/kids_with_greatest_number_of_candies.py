"""Solución al problema de leetcode titulado: Kids With the Greatest Number of Candies"""

class Solution(object):
    """Clase de la solución"""
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """Función que genera una listea boleana como resultado segun las especificaciones
        del problema"""
        n = len(candies)
        if n >= 2 and n <= 100:
            maxCandies = max(candies)
            answer = []
            for _ in candies:
                answer.append(_ + extraCandies >= maxCandies)
            return answer   
        return print("La longitud de la lista no es la adecuada")

if __name__ == "__main__":
    Solution().kidsWithCandies(candies= [1,1,5], extraCandies= 3)
