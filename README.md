# Seminaarityö: LeetCode with Python

## Johdanto

Tämän seminaarityön ideana on kehittää omaa algoritmista ajattelua ja samalla syventää Python-osaamista käytännön kautta. LeetCode tarjoaa monipuolisia ohjelmointitehtäviä eri aihealueista ja vaikeustasoista ja se on suosittu alusta työnhakuun valmistautuessa tai oman osaamisen testaamisessa.

Tehtävien valinnassa käytin apuna tekoälyä, jonka avulla sain koottua mahdollisimman monipuolisen ja tasapainoisen tehtäväkokonaisuuden. Halusin mukaan erilaisia haasteita, joissa pääsee harjoittelemaan esimerkiksi taulukoita ja merkkijonoja, hakualgoritmeja, tietorakenteita ja dynaamista ohjelmointia. Näin sain rakennettua kokonaisuuden, joka kehittää teknistä osaamista, mutta myös ongelmanratkaisukykyä sekä loogista ajattelua.

Kaikki tehtävät on toteutettu Pythonilla ja pyrin kirjoittamaan ratkaisuni mahdollisimman selkeästi sekä tehokkaasti oman osaamiseni mukaan. Tehtävät on jaettu kolmeen vaikeustasoon: helppoihin, keskivaikeisiin ja vaikeisiin. Päätin ottaa itselleni haasteeksi suorittaa 15 helppoa, 5 keskivaikeaa, sekä yhden vaikean tehtävän. Jokaiseen tehtävään on lisätty pohdinta tehtävästä: mitä opin sekä mitä haasteita tuli vastaan. Tehtävän yhteydestä löytyy myös kuva alkuperäisestä tehtävänannosta, jotta kokonaisuus olisi mahdollisimman ymmärrettävä. Itse tehtävät on tallennettuna erikseen omissa kansioissaan ja niihin löytyy myös linkki jokaisen tehtävän yhteydessä. Tehtäviin on myös toteutettu toimiva versio, eli muokattu pelkkaa koodia mitä kirjoitin LeetCode:en ja tämän muokatun koodin pystyy suorittamaan. Siihen on lisätty samaa esimerkkidataa, kuin itse LeetCode -alustalla.

## Tehtävät

### Helpot tehtävät (13 kpl)

**1. Two Sum** ([LeetCode](https://leetcode.com/problems/two-sum/), [Ratkaisu](./1_easy/two_sum.py))
   
   ![](./images/two_sum.png)

   **Miten tein tehtävän:**
      
   Tein tehtävän brute force -taktiikalla eli kahdella sisäkkäisellä silmukalla. Nämä käyvät läpi kaikki mahdolliset luvut ja etsivät parin, jonka summa on yhtä kuin annettu `target`. Kirjoitin ratkaisun Pythonilla.

   **Miten meni:**

   Ensimmäisellä yrityksellä sain `IndentationError` -virheen. Toisella yrityksellä sain koodin suorittamaan ilman virheitä, mutta se palautti tyhjän listan. Kolmannella yrityksellä vaihdoin hieman lähestymistapaa, mutta sisennys meni taas pieleen. Lopulta sain kuitenkin toimivan ratkaisun. Jo ensimmäisestä tehtävästä tuli olo, että miten voi olla näin vaikeaa, vaikka tämän pitäisi olla tasoltaan helppo. Asiaa auttoi muiden kommenttien lukeminen. Tästä Tajusin, että on tosi yleistä aloittaessa kokea samaa turhautumista ja osaamattomuuden tunnetta. 

   **Mitä tehtävästä jäi käteen:**

   - Pythonin sisennys on erittäin tarkkaa – pienikin virhe voi estää koodin ajon kokonaan.

   - On tärkeää lukea virheilmoitukset tarkasti ja etsiä niistä vihjeitä.

   - Vaikka brute force -ratkaisu toimii, ymmärsin, että tehtävän voi ratkaista myös tehokkaammin esimerkiksi HashMapin avulla.

   **Mitä voisin tehdä toisin seuraavalla kerralla:**

   - Suunnitella ratkaisun paremmin ennen koodin kirjoittamista.

   - Käyttää hyväksi materiaaleja sekä dokumentaatioita

   - Idean ymmärrettäessä kokeeilla.

---

**2. Palindrome Number** ([LeetCode](https://leetcode.com/problems/palindrome-number/), [Ratkaisu](./1_easy/palindrome_number.py))
   
   ![](./images/palindrome_number.png)

   **Miten tein tehtävän:**

   Tehtävänä oli tarkistaa, onko annettu kokonaisluku palindromi eli sama etu- ja takaperin luettuna. Muunsin kokonaisluvun merkkijonoksi ja vertasin sitä käännettyyn versioon `x[::-1]`. Jos ne ovat samat, luku on palindromi.

   **Miten meni:**

   Tehtävä oli melko suoraviivainen ja sain sen toimimaan nopeammin kuin `Two Sum` -tehtävän. Jouduin vähän tutkimaan netiste miten Pythonin merkkijonoja voidaan kääntää ja ratkaisu `[::-1]` oli helppo ja tehokas tapa ratkaista tehtävä. 

   **Mitä tehtävästä jäi käteen:**

   - Palindromin tarkistaminen onnistuu näppärästi kääntämällä merkkijono `[::-1]` -operaattorilla.

   - Koodia voi usein tiivistää ja tehdä selkeämmäksi poistamalla tarpeettomat ehtorakenteet. Toisaalta joskus tiivein koodi ei ole selkeintä vaikka se olisikin tehokkainta.  

   **Mitä voisin tehdä toisin seuraavalla kerralla:**

   - Tiivistää koodia heti alussa mahdollisimman yksinkertaiseksi, ratkaisussani if-rakenne oli turha ja olisin voinut toteuttaa tehtävän esimerkiksi näin:

   ``` python
   def isPalindrome(self, x: int) -> bool:
    return str(x) == str(x)[::-1]
   ```
---

**3. Merge Two Sorted Lists** ([LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/), [Ratkaisu](./1_easy/merge_two_sorted_lists.py))
   
   ![](./images/merge_two_sorted_lists.png)

**Miten tein tehtävän:**
Tarkoituksena oli yhdistää kaksi järjestettyä listaa yhdeksi uudeksi järjestetyksi listaksi. Käytin `dummy_node`:a, jonka kautta rakensin uuden listan. Kävin läpi molempia listoja rinnakkain ja lisäsin pienemmän arvon omaavan noden uudelle listalle.

**Miten meni:**

Tehtävä tuntui hieman monimutkaiselta, koska "linked list" -rakenne ei ollut entuudestaan tuttu ja erilainen kuin tavalliset listat. Kävin etsimässä apua tehtävän ratkaisuun ja löysin, että joku oli käyttänyt `dummy_node`:a. Aloin pelleilemään tällä, jonka avulla pääsin vihdoin käyttämään tätä uuden listan tekemiseen. Tehtävä alkoi pikkuhiljaa sujumaan, mutta kyllä sen tekemisessä aika kauan meni.

**Mitä tehtävästä jäi käteen:**

- Dummy-noden käyttö on tehokas tapa yksinkertaistaa linkitetyn listan rakentamista.

- Linkitettyjä listoja käsitellessä täytyy olla tarkkana next-osoittimien kanssa, ettei lista vahingossa katkea.

- Harjoittelin myös ehdollista sijoittamista `current_node.next = list1 if list1 else list2` viimeisten solmujen liittämiseen.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Luoda piirtämällä itselle visuaalinen kaavio ymmärtämisen helpottamiseksi.

---

**4. Valid Parentheses** ([LeetCode](https://leetcode.com/problems/valid-parentheses/), [Ratkaisu](./1_easy/valid_parentheses.py))
   
   ![](./images/valid_parentheses.png)

**Miten tein tehtävän:**

Tehtävänä oli tarkistaa, ovatko annetun merkkijonon sulut oikein sulkeutuneet sekä oikeassa järjestyksessä. Käytin pinoa `stack`, johon lisätään aukeavat sulut ja poistetaan ne, kun vastaava sulkeva sulku löytyy. Lopussa tarkistetaan, että se on tyhjä.

**Miten meni:**

Tehtävä tuntui loogisemmalta kuin aiemmat ja sain sen toimimaan jonkinnäköisesti melko nopeasti, toki ratkaisu ei ollut oikein heti alussa. Jouduin katsomaan vinkkiä, jossa sanottiin, että käytä pinoa. En ollu heti varma miten se toimii, joten menin tutkailemaan sitä netistä. Pinon käytön ymmärtäessäni tehtävän ratkaiseminen meni sujuvasti. Tehtävä ei aiheuttanut sen suurempia ongelmia, mitä pienellä googlaamisella ei pystyisi selvittämään. 

**Mitä tehtävästä jäi käteen:**

- Opin mikä on `stack` ja miten sitä voi käyttää rakenteiden käsittelemiseen, kun on kyseessä avausten sekä sulkujen seuraaminen.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Harjoitella lisää `stack` -rakenteen käyttöä.

---

**5. Best Time to Buy and Sell Stock** ([LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [Ratkaisu](./1_easy/best_time_to_buy_and_sell_stock.py))
   
   ![](./images/best_time_to_buy_and_sell_stock.png)

**Miten tein tehtävän:**

Tarkoituksena oli löytää suurin mahdollinen voitto ostamalla osake yhtenä päivänä ja myymällä se myöhempänä päivänä. Käytin kahta muuttujaa: `max_profit` seuraamaan suurinta mahdollista voittoa sekä `min_price` seuraamaan halvinta hintaa tähän asti.

**Miten meni:**

Ensin yritin pakottaa `brute force` ratkaisua kahdella silmukalla, mutta lopetin sen nopeasti, sillä halusin löytää ratkaisun, joka toimisi pelkästään yhdellä. Löysin vihdoin miten pystyn päivittämään minimihintaa samalla listaa läpi käymässä, joka tuntui hyvältä. Tosin, matka tyssäsi muutamaan klassiseen `IndentationError` -virheeseen.

**Mitä tehtävästä jäi käteen:**

- Opin käyttämään `float('inf')` alkutilan asettamiseen.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Miettiä rauhassa ennen ratkaisun yrittämistä.

---

**6. Richest Customer Wealth** ([LeetCode](https://leetcode.com/problems/richest-customer-wealth/), [Ratkaisu](./1_easy/richest_customer_wealth.py))
   
   ![](./images/richest_customer_wealth.png)

**Miten tein tehtävän:**

Tässä tehtävässä laskettiin jokaiselle asiakkaalle hänen kaikkien tiliensä summat ja valittiin niistä suurin. Käytin `sum()` -funktiota yhdistettynä `max()` -funktioon, joka käy kaikki asiakkaat läpi.

**Miten meni:**

Tehtävä oli selkeä ja mukava tehdä. Ratkaisu onnistui kerralla, ja oli kiva huomata, kuinka tehokas yhdistelmä `sum()` ja `max()` oli tähän.

**Mitä tehtävästä jäi käteen:**

- Opin lisää `sum()` ja `max()` -funktioiden käyttämisestä

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Kokeilla vaikka miten voisin saada myös rikkaimman asiakkaan indeksin, enkä pelkästään summan.

---

**7. Climbing Stairs** ([LeetCode](https://leetcode.com/problems/climbing-stairs/), [Ratkaisu](./1_easy/climbing_stairs.py))
   
   ![](./images/climbing_stairs.png)

**Miten tein tehtävän:**

Piti selvittää, kuinka monta erilaista tapaa on kiivetä `n` portaan ylös, kun voi ottaa yhden tai kaksi porrasta per askel. Jokainen uusi askelma on edellisten kahden summa. Käytin kahta muuttujaa `first_step` ja `second_step`, joita päivitin silmukassa.

**Miten meni:**

Edellisen tehtävän jälkeen tämä tehtävä oli rentouttavampi, sillä ei tarvinnut opetella kokonaan uusia algoritmejä. Aluksi yritin tehdä rekursiivisen ratkaisun, mutta sen sijaan päädyin dynaamisen ohjelmoinnin ratkaisuun. Tämä ratkaisu toimi yhdellä silmukalla ja oli mukava huomata, että ratkaisu oli myös siisti ja tehokas.

**Mitä tehtävästä jäi käteen:**

- Opin käyttämään kahta muuttujaa peräkkäisten arvojen säilyttämiseen.

- Opin ajattelemaan dynaamista ohjelmointia yksinkertaisessa kontekstissa.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Piirtää esimerkiksi taulukon n-arvoista ja vastauksista hahmoittaakseni laskennan visuaalisesti.

---

**8. Binary Search** ([LeetCode](https://leetcode.com/problems/binary-search/), [Ratkaisu](./1_easy/binary_search.py))
   
   ![](./images/binary_search.png)

**Miten tein tehtävän:**

Tehtävässä piti etsiä tietty luku `target` järjestetystä listasta. Käytin binäärihakua `binary search`, jossa tarkastellaan keskikohtaa ja puolitetaan etsintäaluetta joka kierroksella sen perusteella, onko kohdeluku suurempi vai pienempi.

**Miten meni:**

Tehtävä itsessään oli selkeä, mutta aluksi unohdin päivittää `left` ja `right` arvot oikein, jolloin loin silmukan, joka jäi pyörimään loputtomasti. Mietin mikä on vikana ja pitkän etsimisen jälkeen tajusin käyttää `//` (kokonaislukujako) ja päivittää rajat oikein, jonka jälkeen ratkaisu hyväksyttiin.

**Mitä tehtävästä jäi käteen:**

- Opin binäärihaun toiminnan ja miten se perustuu listan puolittamiseen.

- Opin laskemaan keskikohdan oikein: `(left + right) // 2`.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Kokeilla vaikka rekursiivista versiota binäärihausta.

---

**9. Ransom Note** ([LeetCode](https://leetcode.com/problems/ransom-note/), [Ratkaisu](./1_easy/ransom_note.py))
   
   ![](./images/ransom_note.png)

**Miten tein tehtävän:**

Tehtävässä tarkistettiin, voiko `ransomNote` -merkkijonon merkit muodostaa `magazine` -merkkijonosta. Käytin `Counter` -luokkaa, joka laskee merkkien esiintymismäärät molemmissa merkkijonoissa. Tämän jälkeen vertasin, että `magazine` sisältää riittävästi kunkin merkin määrää.

**Miten meni:**

Tehtävä meni yllättävän hyvin. Ratkaisu oli yksinkertainen sekä `Counter` -luokan käyttäminen nopeutti merkkien laskemista. Ei tullut suurempia ongelmia muutakuin yleiset syntax-virheet.

**Mitä tehtävästä jäi käteen:**

- Opin käyttämään `Counter` -luokkaa, jonka avulla voidaan laskea merkkien määrät nopeasti.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Harjoituksen vuoksi voisin yrittää kehittää ratkaisun käyttämättä `Counter` -luokkaa.

---

**10. Reverse Linked List** ([LeetCode](https://leetcode.com/problems/reverse-linked-list/), [Ratkaisu](./1_easy/reverse_linked_list.py))
   
   ![](./images/reverse_linked_list.png)


**Miten tein tehtävän:**

Tässä tehtävässä haluttiin kääntää `linked list`. Käytin kolmea apumuuttujaa: `previous_node`, `current_node` ja `next_node`. Kävin listan läpi ja käänsin jokaisen noden next-osoittimen, jolloin lista kääntyi.

**Miten meni:**

Tehtävä oli aluksi hieman haastava, koska linkitetyt listat eivät ole yhtä tuttuja kuin tavalliset listat. Mutta ymmärsin nopeasti, kuinka solmujen linkit käännetään. Ratkaisu onnistui hyvin, eikä tullut suuria ongelmia. 

**Mitä tehtävästä jäi käteen:**

- Periaatteet miten linkitetyt listat toimivat.

- Miten kääntää simppeli linkitetty lista yksi node kerrallaan.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Seuraavalla kerralla olisin voinut tehdä tämän tehtävän ennen tehtävää "merge two sorted lists". Tämä olisi säästänyt päänsärkyä, sillä koin tämän tehtävän olevan simppelimpi.

---

**11. First Unique Character in a String** ([LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/), [Ratkaisu](./1_easy/first_unique_character_in_a_string.py))
   
   ![](./images/first_unique_character_in_a_string.png)


**Miten tein tehtävän:**

Tehtävässä käytin `Counter` -luokkaa, jolla laskin kuinka monta kertaa kukin merkki esiintyy merkkijonossa. Kävin sitten merkkijonon läpi ja tarkistin ensimmäisen merkin, joka esiintyy vain kerran.

**Miten meni:**

 Tehtävä meni aika sujuvasti, sillä olin käyttänyt jo `Counter`:ia aikaisemmassa tehtävässä. Joten se oli siis tuttu ja pystyin pystyin hyödyntämään samaa ajattelutapaa.

**Mitä tehtävästä jäi käteen:**

- Miten yhdistää järkevästi `enumerate` -funktion sekä `Counter` -luokan

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Sama kehitys kuin aikaisemmin, tehdä tehtävä käyttämättä `Counter` -luokkaa.

---

**12. Intersection of Two Arrays II** ([LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/), [Ratkaisu](./1_easy/intersection_of_two_arrays2.py))
   
   ![](./images/intersection_of_two_arrays2.png)

**Miten tein tehtävän:**

Tässä tehtävässä käytin `Counter` -luokkaa laskemaan kummankin listan alkioiden määrän. Kävin sitten toisen listan läpi ja tarkistin löytyykö alkio ensimmäisestä listasta. Jos löytyi, lisäsin sen tulokseen ja vähensin laskuria yhdellä.

**Miten meni:**

Tehtävä sujui hyvin, sillä `Counter` -luokka on tullut jo tutuksi muutaman edellisen tehtävän yhteydessä. On kiva huomata tehtäviä tehdessä, kun käyttää samoja rakenteita sekä luokkia, niin tuntuu, että oikeasti asiat jää paremmin päähän ja vaikuttavat enemmän ja enemmän tutuilta joka kerta.

**Mitä tehtävästä jäi käteen:**

- Syvensin `Counter` -luokan käyttöä

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Kokeilla toista ratkaisutapaa, esim käyttämällä kahta `pointer`:ia

---

**13. Move Zeroes** ([LeetCode](https://leetcode.com/problems/move-zeroes/), [Ratkaisu](./1_easy/move_zeroes.py))
   
   ![](./images/move_zeroes.png)

**Miten tein tehtävän:**

Tehtävässä oli tarkoitus siirtää nollat listan loppuun ja toteutin tämän käyttämällä indeksimuuttujaa `non_zero_index`, joka piti kirjaa mihin seuraava numero, joka ei ole nolla sijoitetaan. Tein aina siirron kun vastaan tullut numero ei ollut nolla.

**Miten meni:**

 Alussa ajattelin käyttää vain toista listaa, mutta sitten huomasin, että tehtävä vaatii "in-place" ratkaisua. Muutin lähestymistapaa ja onnistuin tekemään toimivan ratkaisun. Vaikka itsessään tehtävä oli yksinkertainen, tuntui että minulla meni siihen aivan liian kauan aikaa.

**Mitä tehtävästä jäi käteen:**

- Vahvistin omaa osaamista `for`-silmukoiden sekä indeksien käyttämisessä.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Testata toista lähestymistapaa ja vaikka siirtää kaikki ei nollat eteen ja täyttää loppu lista nollilla. 

---

### Keskivaikeat tehtävät (3 kpl)

**1. Maximum Subarray** ([LeetCode](https://leetcode.com/problems/maximum-subarray/), [Ratkaisu](./2_medium/maximum_subarray.py))
   
   ![](./images/maximum_subarray.png)

**Miten tein tehtävän:**

Tehtävässä piti löytää suurimman summan muodostava peräkkäinen `subarray`. Käytin Kadanen Algoritmia, joka toimii pitämällä kirjaa kahdesta arvosta, tässä tapauksessa: `max_current_sum` ja `max_global_sum`. Jokaisessa vaiheessa tarkastellaan, kannattaako jatkaa nykyistä summaa vai aloittaa uusi.

**Miten meni:**

Rehellisesti en ollut kuullut Kadanen algoritmista ennen, joten jouduin tutkimaan mitä se tekee. Aluksi oli vaikea ymmärtää, miksi vertaillaan `max(nums[i], max_current + nums[i])` Kirjoitin sen käsin paperille, jonka jälkeen se vähän alkoi hahmottua. Koodin sai lopulta toimimaan pitkän vääntämisen jälkeen.

**Mitä tehtävästä jäi käteen:**

- Opin miten Kadanen algoritmi toimii käytännössä.

- Ymmärsin, että aina ei tarvitse tallentaa kaikkia alitaulukkoja ja riittää vain parhaan tallentaminen

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Tutustua lisää jatkuvaan päivitykseen liittyviin algoritmeihin. 

---

**2. Longest Substring Without Repeating Characters** ([LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [Ratkaisu](./2_medium/longest_substring_without_repeating_characters.py))
   
   ![](./images/longest_substring_without_repeating_characters.png)

**Miten tein tehtävän:**

Tehtässä oli tarkoituksena löytää mahdollisimman pitkä osa merkkijonosta ilman toistuvia merkkejä. Toteutin tehtävän "Sliding Window" -tekniikkaa käyttäen, jossa pidin yllä `left` ja `right` pointeria sekä `set` -rakennetta.

**Miten meni:**

Aloitin tehtävän tekemisen `brute force` tekniikalla, mutta se osoittautui huonoksi vaihtoehdoksi. Sen jälkeen lähdin tutkimaan miten tehtävä olisi mahdollista suorittaa ja törmäsin "Sliding window" -tekniikkaan. Tehtävän hahmottaminen oli silti vähän vaikeaa ja jouduin jättämään sen kesken, sillä aivot löivät vaan ihan tyhjää. Palasin illemalla tehtävän pariin ja piirsin paperille esimerkin miten ratkaisu voisi toimia, joka auttoi vähän hahmottamaan tilannetta. Lopulta sain tehtyä ratkaisun, joka tuotti oikean vastauksen.

**Mitä tehtävästä jäi käteen:**

- Tutustuin "Sliding window" -tekniikkaan.

- Harjoittelin `set`:in käyttöä.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Pitää tarpeeksi nopeasti tauko, jos tehtävän tekeminen ei vain kulje. Usein aika auttaa ajattelemisen kanssa.

---

**3. Group Anagrams** ([LeetCode](https://leetcode.com/problems/group-anagrams/), [Ratkaisu](./2_medium/group_anagrams.py))
   
   ![](./images/group_anagrams.png)

**Miten tein tehtävän:**

Tehtävässä oli tarkoituksena ryhmitellä listan sanat anagrammien mukaan. Toteutin tehtävän vertaamalla sanojen aakkosjärjestykseen laitettuja versioita ja keräämällä ne yhteen `defaultdict` -rakenteen avulla.

**Miten meni:**

Aluksi mietin monimutkaisempaa lähestymistapaa laskemalla kirjainmääriä, mutta päädyin aakkosjärjestykseen perustuvaan ideaan, joka yksinkertaisti ratkaisun. `defaultdict` -rakenne teki koodista siistin ja lyhyen. 

**Mitä tehtävästä jäi käteen:**

- Anagrammien tunnistus on helpompaa, kun kirjaimet on järjestetty aakkosjärjestykseen.

- Tutustuin ja käytin `defaultdict` -rakennetta.

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Miettiä suoraan mahdollisimman yksinkertainen lähestymistapa.

---

### Vaikea tehtävä

**1. Median of Two Sorted Arrays** ([LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/), [Ratkaisu](./3_hard/median_of_two_sorted_arrays.py))
   
   ![](./images/median_of_two_sorted_arrays.png)

**Miten tein tehtävän:**

Yhdistin molemmat annetut listat yhdeksi `nums` ja laittelin uuden listan `sorted()`
-funktiolla. Sen jälkeen tarkistin listan pituuden: pariton vaiko parillinen, jonka perusteella palautin mediaanin, joko keskimmäisenä arvona TAI kahden keskimmäisen numeron keskiarvona. 

**Miten meni:**

Lähestyin tehtävää ensin ns. optimaalisella tavalla eli binäärihakua hyödyntävällä `O(log(min(n, m)))` ratkaisulla. Luin useita kertoja tehtävän kuvauksen sekä tutkin materiaaleja ja yritin hahmottaa indeksien liikuttelua kahden taulukon välillä, mutta kokonaisuus tuntui vain liian monimutkaiselta ja aivot olivat ihan sekaisin. Lopulta päätin palata keräämään ajatuksiani ja päätin ratkaista tehtävän yksinkertaisemmalla tavalla yhdistämällä listat ja lajittelemalla ne. Tämä palautti motivaation, sillä sain ratkaisun toimimaan ja aloin ymmärtämään mediaanin logiikkaa.

**Mitä tehtävästä jäi käteen:**

- Ymmärsin mediaanin määritelmän ja sen käsittelyn parillisessa vs. parittomassa listassa.

- Harjoittelin listojen yhdistämistä ja lajittelua Pythonissa.

- Muistin, että joskus kannattaa lähteä liikkeelle yksinkertaisella ratkaisulla ja lähteä vasta sitten optimoimaan, kun osaa asiaa paremmin. 

**Mitä voisin tehdä toisin seuraavalla kerralla:**

- Tämä ratkaisu ei täytä tehtävän varsinaista vaatimusta tehokkaasta `O(log(min(n, m)))` aikavaativuudesta, mutta sitä voisi miettiä ja kehittää ratkaisua. 

## Yhteenveto

Seminaarityön aloittaessani olin itsevarma omista taidoistani ja uskoin pystyväni ratkaista haasteita ilman mitään ongelmia. Voin sanoa, että ensimmäistä tehtävää tehdessä tämä itsevarmuus hävisi niin nopeasti kuin oli ilmaantunutkin. Tavoitteena oli ratkaista 15 helppoa, 5 keskivaikeaa sekä 1 vaikea LeetCode-haaste, mutta todellisuudessa ratkaisin 13 helppoa, 3 keskivaikeaa ja 1 vaikean haasteen. Vaikka alkuperäiseen tavoitteeseen en siis päässyt, voin sanoa oppineeni valtavasti uutta Pythonin käytöstä sekä kehittänyt omaa algoritmista ajattelua. Tehtävien tekeminen osoitti, että ne eivätkään olleet niin helppoja kuin olin olettanut ja ongelmanratkaisussa tarvitaan paljon kärsivällisyyttä, huolellisuutta sekä ulkopuolista apua ja uusia lähestymistapoja.

Työn tekeminen sai minut miettimään ohjelmointia syvemmin ja tajusin, että haasteiden tekeminen ei ollut pelkkää koodin kirjoittamista, vaan jatkuvaa testaamista, virheiden jäljittämistä (näitä tuli ja paljon) sekä ratkaisun muotoilua. Ymmärsin kuinka tärkeää on lukea ja tulkita virheilmoituksia tarkasti.

Kaiken kaikkiaan voin sanoa, että olen positiivisesti yllättynyt seminaarityön tekemisestä: kokemust oli haastava, mutta samalla todella opettavainen. Vaikka alkuperäinen suunnitelma ei ihan toteutunut, niin mielestäni tärkeämpää on se, mitä uutta opin matkan varrella. Ymmärrykseni ohjelmoinnista on laajentunut ja ongelmanratkaisutaitoni ovat kehittyneet. Sain harjoiteltua jo tutumpia aiheita syvemmin sekä sain käsityksen missä on vielä paljon kehitettävää. Oli kiva seurata omaa etenemistä konkreettisesti ja varmasti aion tulevaisuudessakin syventyä algoritmeihin enemmän ja jatkaa LeetCode-haasteiden tekemistä!

> Kaikki tehtävät ja ratkaisut löytyvät tästä GitHub-repositoriosta.

