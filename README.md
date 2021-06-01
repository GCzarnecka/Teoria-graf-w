# Analiza algorytmu Bellmana-Forda

**Jakie problemy rozwiązuje?**
* Służy do rozwiązywania problemu najkrótszych ścieżek, w którym wagi na krawędziach mogą być ujemne
* Algorytm ten zwraca wartość logiczną, czy istnieje cykl o ujemnej wadze, który jest osiągalny ze źródła
* Jeśli taki cykl istnieje, to w grafie tym nie można obliczyć najkrótszych ścieżek
* Jeśli takiego cyklu nie ma, algorytm oblicza najkrótsze ścieżki i ich wagi
* Opiera się na metodzie relaksacji
* Można wykorzystać go do znalezienia ujemnego cyklu w grafie
* W przeciwieństwie do algorytmu Dijkstry można go wykonywać na grafach z wagami ujemnymi
* Wykorzystywany w protokole RIP (Routing Information Protocol)



---



## Co to jest Routing Information Protocol?
**Routing Information Protocol** jest protokołem dynamicznego trasowania wykorzystującym ilość przeskoków jako metrykę w celu odnalezienia najlepszego połączenia między źródłową i docelową siecią. Protokół ten jest oparty na zestawie algorytmów wektorowych. Do swojego działania wykorzystuje port 520.


Ilość przeskoków określa liczbę routerów występujących między źródłową siecią, a docelową siecią. Ścieżka o najniższej liczbie przeskoków jest wybierana jako najlepsza trasa. Cechą charakterystyczną tego protokołu jest to, że posiada on maksymalną liczbę dozwolonych przeskoków – 15. Wraz z 16 przeskokiem uznaje się, że sieć docelowa jest nieosiągalna.

#### Dodatkowe cechy charakterystyczne protokołu:
* Informacje o trasach są wysyłane w stałych odstępach czasowych - domyślnie w odstępie co 30 sekund.
* Aktualizacje trasowania są rozgłaszane tylko do routerów sąsiednich (routing on rumours)
#### Aplikacje w routingu
**Etapy**
1. Każdy węzeł oblicza dystans pomiędzy sobą i wszystkimi innymi węzłami i zapisuje tę informację w postaci tabeli.
2. Każdy węzeł wysyła swoją tablicę do wszystkich węzłów sąsiednich.
3. Kiedy węzeł otrzymuje tablicę odległości od sąsiadów, oblicza najkrótsze trasy do wszystkich innych węzłów i aktualizuje własną tabelę, aby odzwierciedlić wszelkie zmiany. 
