Aplikacija omogućuje korisnicima monitoriranje njihove prehrane, pomoću osnovnih CRUD operacija.

**CRUD funkcije**

1. Dodaj obrok -> Dodavanje novog obroka putem POST zahtjeva
2. Pregeld unesenih obroka -> Pregled svih obroka putem GET zahtjeva
3. Uredivanje unesenih obroka -> Uredivanje unesenih obroka putem PUT zahtjeva
4. Brisanje obroka -> Brisanje unesenih obroka putem DELETE zahtjeva

Takoder, postoje i funkcionalnosti kao stu su vizualizacija obroka, te uvid kada je audit polje kreirano i zadnji puta azurirano

**Pokretanje aplikacije**

Kako bi sve radilo ispravno, slijedite ove korake. Preduvjet pokretanja aplikacije je da imate Docker Desktop instaliran na vasim računalima ili laptopima. Potom, naravno treba preuzeti komponente u ovom repozitoriju. Za ovaj korak postoji dosta opcija, ali kako biste bili 100% sigurni da ste sve obavili kako treba predlažem kreiranje novog direktorija, navigirajte do njega i klonirajte u njega ovaj repozitorij: Primjer mkdir vas_direktorij -> cd .../vas_direktorij -> git clone https://github.com/spahicadis/is-pracenje-prehrane.git Jednom kada je ovo uspjesno obavljeno u istom direktoriju moramo stoviriti Docker image pomocu naredbe: docker build -t prehrana/is-flask:0.0.1.RELEASE. U trenutnom direktoriju smo kreirali Docker image sada kada imamo Docker image, možemo dignuti kontejner naredbom: : docker container run -d -p 5000:8080 prehrana/is-flask:0.0.1.RELEASE. Ovime smo pokrenuli Docker kontejner koji sluša na portu 8080, izgraden je na temelju Docker image-a koju smo stvorili prije. Sada kada je kontejner dignut mozemo pristupiti aplikaciji preko weba, dovoljno je napisati localhost:8080. Sada imate pristup aplikaciji i možete isprobati njezinu funkcionalnost.
