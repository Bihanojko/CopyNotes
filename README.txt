Copy Notes

1. a) Do slo�ky CopyNotes z tohoto zipu p�esunout soubory, ze kter�ch a do kter�ch se budou pozn�mky kop�rovat. 
   b) Druhou variantou je p�esunout soubory ze slo�ky CopyNotes do slo�ky, ve kter� se nach�z� notes.*.xml soubor na��tan� 
   do hry. V�hodou je, �e se notes.*.xml soubor pro p�id�n� pozn�mek nemus� p�esunovat tam a zp�t.

2. V souboru "logins.txt" nahradit [insert_login] sv�m loginem (loginem z n�zvu souboru, do kter�ho chceme data kop�rovat). 
   Na dal��m ��dku nahradit [second_login] loginem, kter� je v n�zvu toho souboru, ze kter�ho chceme kop�rovat data.
   Pokud chceme data kop�rovat ze dvou a v�ce soubor�, pro ka�d� dal�� soubor p�id�me ��dek ve tvaru: "copy_from_login=[login]
".

P��klad: Pro kop�rov�n� do souboru s loginem "vagy" ze soubor� s loginy 
"mirda", "merisi" a "poker_king" by vypadal soubor "logins.txt" takto:

user_login=vagy
copy_from_login=mirda
copy_from_login=merisi
copy_from_login=poker_king

3. Spustit CopyNotes.exe. V�t�inou to trv� p�r des�tek sekund, z�le�� na velikosti a po�tu xml soubor�. Po skon�en�
   pr�ce skriptu se vyp�e, �e byly pozn�mky �sp�n� zkop�rov�ny a stiskem libovoln� kl�vesy se okno zav�e.