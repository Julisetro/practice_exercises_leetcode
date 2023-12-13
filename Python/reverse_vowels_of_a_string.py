"""Solución al problema de leetcode titulado: Reverse Vowels of a String """

class Solution:
    """Solución"""
    def reverseVowels(self, s: str) -> str:
        """Invierte las vocales de una palabra"""
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        #Usamos el metodo de dos punteros. Realizamos un bucle
        #hasta que el puntero start ya no sea menor que el puntero end
        while start < end:
            #Movemos el puntero start hacia el final de la cadena
            #hasta que apunte a una vocal
            #Para ello utilizamos el metodo .find() donde si word[start] no es una vocal devuelve -1
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            #De la misma forma lo hacemos para el puntero end. Lo movemos hacia el inicio
            #hasta que apunte a una vocal
            while end > start and vowels.find(word[end]) == -1:
                end -= 1
            #Intercambianos las vocales encontradas
            word[start], word[end] = word[end], word[start]
            #Movemos los punteros para la siguiente ireación
            start += 1
            end -= 1
        return "".join(word)


if __name__ == "__main__":
    print(Solution().reverseVowels(s= "buenas"))

