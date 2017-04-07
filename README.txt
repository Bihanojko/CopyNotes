Copy Notes

1. a) Do složky CopyNotes z tohoto zipu pøesunout soubory, ze kterých a do kterých se budou poznámky kopírovat. 
   b) Druhou variantou je pøesunout soubory ze složky CopyNotes do složky, ve které se nachází notes.*.xml soubor naèítaný 
   do hry. Výhodou je, že se notes.*.xml soubor pro pøidání poznámek nemusí pøesunovat tam a zpìt.

2. V souboru "logins.txt" nahradit [insert_login] svým loginem (loginem z názvu souboru, do kterého chceme data kopírovat). 
   Na dalším øádku nahradit [second_login] loginem, který je v názvu toho souboru, ze kterého chceme kopírovat data.
   Pokud chceme data kopírovat ze dvou a více souborù, pro každý další soubor pøidáme øádek ve tvaru: "copy_from_login=[login]
".

Pøíklad: Pro kopírování do souboru s loginem "vagy" ze souborù s loginy 
"mirda", "merisi" a "poker_king" by vypadal soubor "logins.txt" takto:

user_login=vagy
copy_from_login=mirda
copy_from_login=merisi
copy_from_login=poker_king

3. Spustit CopyNotes.exe. Vìtšinou to trvá pár desítek sekund, záleží na velikosti a poètu xml souborù. Po skonèení
   práce skriptu se vypíše, že byly poznámky úspìšnì zkopírovány a stiskem libovolné klávesy se okno zavøe.