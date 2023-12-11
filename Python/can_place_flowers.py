"""Solucón al problema de leetcode titulado: Can Place Flowers"""
class Solution:
    """Clase de la solución"""
    def canPlaceFlowers (self, flowerbed: list[int], n: int) -> bool:
        """Función que contiene la logica del ejercicio"""
        count = 0
        # Nos moveremos a travez de la lista flowerbed por medio de su index
        # dentro de un rango de numeros que va de cero hasta la longitud de la lista.
        for i, flowerbeds in enumerate(flowerbed):
            #Checkeamos si el index esta disponible

            if flowerbed[i] == 0:
                #Checkeamos si los index adyacentes estan tambien disponibles
                empy_plots = (i == 0 or (flowerbed[i-1] == 0)) and (
                    (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0))
                if empy_plots:
                    flowerbed[i] = 1
                    count += 1
        return count >= n


if __name__ == "__main__":
    Solution().canPlaceFlowers(flowerbed=[1,0,0,0,1], n= 1)
