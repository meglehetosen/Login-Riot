# Login-Riot

Készítette: Sasvári Bálint

Bemutató videó:
https://youtu.be/JjU895rn-Z8?si=RlmesoUnZQ144zgF

Az alkalmazás célja a Riot játékokba való belépés megkönnyítése abban az esetben, ha több fiók között kívánunk gyakran váltani. A programot a customtkinter, pyautogui és sqlite3 Python könyvtárak segítségével hoztam létre.

A Gui.py fájl tartalmazza az alkalmazás felhasználói felületét és funkcióit. Az Acc.py modul felelős a biztonságos bejelentkezésért, ami egy lokális SQL adatbázisban tárolja az azonosítókat és az elérési útvonalat. Végül, a legfontosabb funkciók a MainFunctions.py fájlban találhatók, mely egyike az ablak elhelyezkedésétől függetlenül azonosítja és kezelik a bejelentkezéshez szükséges mezőket és gombokat. A másik függvény az alkalmázás megfelelő futásásért felelős, amit a threading module ér el.

A videóban egy tömörített exe fájl fut (Login.exe), melyet a pyinstaller modullal készítettem. Ezt nem lehet feltölteni a fájlméret korlátozása miatt, de a kódom tökéletesen futtatható bármely fejlesztői környezetből.
