import random
from basketball.country import *

def random_name(name = 'full'):

  first_names = ["James", "Jim", "John", "Johnny", "Jon", "Robert", "Rob", "Bob", "Mike", "Mikey", "Michael", "William", "Will", "Bill", "David", "Dave", "Joseph", "Charles", "Charlie", "Thomas", "Tom", "Daniel", "Dan", "Matthew", "Matt", "Anthony", "Ant",
    "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth", "George", "Joshua", "Brian", "Edward", "Kevin", "Ronald", "Gerald"
    "Timothy", "Jason", "Jeffrey", "Frank", "Scott", "Eric", "Stephen", "Jerry", "Gregory", "Raymond", "Samuel", "Patrick",
    "Benjamin", "Walter", "Dennis", "Douglas", "Henry", "Peter", "Carl", "Arthur", "Ryan", "Roger", "Joe", "Juan", "Jack",
    "Albert", "Jonathan", "Justin", "Terry", "Gerald", "Keith", "Willie", "Lawrence", "Ralph", "Nicholas", "Roy", "Ben",
    "Bruce", "Brandon", "Adam", "Harry", "Fred", "Wayne", "Billy", "Steve", "Louis", "Jeremy", "Aaron", "Randy", "Howard",
    "Eugene", "Carlos", "Russell", "Bobby", "Victor", "Martin", "Ernest", "Phillip", "Craig", "Alan", "Shawn", "Chris",
    "Johnny", "Earl", "Jimmy", "Antonio", "Danny", "Bryan", "Tony", "Luis", "Mike", "Stanley", "Leonard", "Nathan",
    "Dale", "Manuel", "Rodney", "Curtis", "Norman", "Allen", "Marvin", "Vincent", "Glenn", "Jeffery", "Travis", "Jeff",
    "Chad", "Jacob", "Lee", "Melvin", "Alfred", "Kyle", "Francis", "Bradley", "Jesus", "Herbert", "Frederick", "Ray",
    "Joel", "Edwin", "Don", "Eddie", "Ricky", "Troy", "Randall", "Barry", "Alexander", "Bernard", "Leroy", "Micheal",
    "Leroy", "Micheal", "Byron", "Colin", "Daryl", "Jaime", "Joey", "Arturo", "Lance", "Roderick", "Stuart", "Cecil",
    "Duane", "Homer", "Malcolm", "Murray", "Roland", "Sterling", "Edgar", "Max", "Miles", "Alvin", "Cedric", "Elijah",
    "Elias", "Ezekiel", "Gavin", "Grayson", "Jaden", "Jaylen", "Josiah", "Kai", "Kaiden", "Kaleb", "Kingston", "Kyrie",
    "Liam", "Mason", "Noah", "Roman", "Ryan", "Sebastian", "Xavier", "Zion", "Andre", "Darius", "Deandre", "Devon",
    "Dwayne", "Jamal", "Jamel", "Javon", "Lamont", "Marquis", "Maurice", "Monte", "Nigel", "Omar", "Quentin", "Reginald",
    "Tevin", "Tyrone", "Tyrese", "Tyson", "Xavier", "DeAndre", "DeMarcus", "Draymond", "Jamal", "Jamel", "Javon", "Lamont",
                 "Marquis", "Maurice", "Monte", "Nigel", "Omar",
    "Quentin", "Reginald", "Tevin", "Tyrone", "Tyrese", "Tyson", "Xavier", "Andre", "Darius", "Devon", "Dwayne", "Malik",
    "Jermaine", "Darnell", "Terrell", "LaMarcus", "Marcellus", "Jerome", "Rashad", "Jalen", "Trevon", "Devonte", "Shaquille",
    "Terrence", "Donte", "Darrell", "Latrell", "Tariq", "Marlon", "Demetrius", "Jabari", "Derrick", "Cedric", "Tyrone", "Lorenzo",
    "Darryl", "Dion", "Darian", "Deshawn", "Montrell", "Jamarcus", "Antoine", "Jamar", "Marquise", "Terrance", "Deshon",
    "Davon", "Dwight", "Jevon", "Tyrell", "Jovon", "Darius", "Malcolm", "Tremaine", "Marlon", "Davonte", "Keenan", "Devan",
    "Marcell", "Travon", "Dashawn", "Denzel", "D'Andre", "Daquan", "Demarcus", "Demarco", "Damion", "Damon", "Damarion",
    "Daquan", "Dandre", "Davion", "Devontae", "Jaquez", "Darian", "Tyrin", "Tajuan", "Deante", "Derick", "Jeramie",
    "Jemar", "Jerell", "Lemar", "Lemarcus", "Ladarrius", "Jarell", "Tysheem", "Devaughn", "Deondre", "Devaun", "Dontae",
    "Demonte", "Tequan", "Deaundre", "Dajuan", "Dajon", "Tavon", "Tyshaun", "Devin", "Jamir", "Jahiem", "Darien", "Deven",
    "Devion", "Damar", "Dajuan", "Jaelin", "Dontavious", "Devlin", "Dantrell", "Dejon", "Devlin", "Torey", "Devonta",
    "Tyrique", "Tevin", "Teon", "Daimon", "Dashaun", "Tayshaun", "Tayvon", "Dameon", "Damond", "Jaelen", "Jaeden",
    "Desean", "Jalen", "Jerel", "Jaheim", "Jahmir", "Daevon", "Damein", "Jaheem", "Jaylon", "Jaquavious",
    "Jaquan", "Jaquez", "Jayceon", "Jaydan", "Jaydin", "Jahari", "Jakhari", "Jahmir", "Jameir", "Bucket"]

  last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas",
    "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis",
    "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams",
    "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker",
    "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy",
    "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James",
    "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman",
    "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster",
    "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham",
    "Sullivan", "Wallace", "Woods", "Cole", "West", "Jordan", "Owens", "Reynolds", "Fisher", "Ellis", "Harrison",
    "Gibson", "Mcdonald", "Cruz", "Marshall", "Ortiz", "Gomez", "Murray", "Freeman", "Wells", "Webb", "Simpson",
    "Stevens", "Tucker", "Porter", "Hunter", "Hicks", "Crawford", "Henry", "Boyd", "Mason", "Morales", "Kennedy",
    "Warren", "Dixon", "Ramos", "Reyes", "Burns", "Gordon", "Shaw", "Holmes", "Rice", "Robertson", "Hunt", "Black",
    "Daniels", "Palmer", "Mills", "Nichols", "Grant", "Knight", "Ferguson", "Rose", "Stone", "Hawkins", "Dunn",
    "Perkins", "Hudson", "Spencer", "Gardner", "Stephens", "Payne", "Pierce", "Berry", "Matthews", "Arnold", "Wagner",
    "Willis", "Ray", "Watkins", "Olson", "Carroll", "Duncan", "Snyder", "Hart", "Cunningham", "Bradley", "Lane",
    "Andrews", "Ruiz", "Harper", "Fox", "Riley", "Armstrong", "Carpenter", "Weaver", "Greene", "Lawrence", "Elliott",
    "Chavez", "Sims", "Austin", "Peters", "Kelley", "Franklin", "Lawson", "Fields", "Gutierrez", "Ryan", "Schmidt",
    "Carr", "Vasquez", "Castillo", "Wheeler", "Chapman", "Oliver", "Montgomery", "Richards", "Williamson", "Johnston",
    "Banks", "Meyer", "Bishop", "Mccoy", "Howell", "Alvarez", "Morrison", "Hansen", "Fernandez", "Garza", "Harvey",
    "Little", "Burton", "Stanley", "Nguyen", "George", "Jacobs", "Reid", "Kim", "Fuller", "Lynch", "Dean", "Gilbert",
    "Garrett", "Romero", "Welch", "Larson", "Frazier", "Burke", "Hanson", "Day", "Mendoza", "Moreno", "Bowman",
    "Medina", "Fowler", "Brewer", "Hoffman", "Carlson", "Silva", "Pearson", "Holland", "Douglas", "Fleming", "Jensen",
    "Vargas", "Byrd", "Davidson", "Hopkins", "May", "Terry", "Herrera", "Wade", "Soto", "Walters", "Curtis", "Neal",
    "Caldwell", "Lowe", "Jennings", "Barnett", "Graves", "Jimenez", "Horton", "Shelton", "Barrett", "Obrien", "Castro",
    "Sutton", "Gregory", "Mckinney", "Lucas", "Miles", "Craig", "Rodriquez", "Chambers", "Holt", "Lambert", "Fletcher",
    "Watts", "Bates", "Hale", "Rhodes", "Pena", "Beck", "Newman", "Haynes", "Mcdaniel", "Mendez", "Bush", "Vaughn",
    "Parks", "Dawson", "Santiago", "Norris", "Hardy", "Love", "Steele", "Curry", "Powers", "Schultz", "Barker", "Guzman",
    "Page", "Munoz", "Ball", "Keller", "Chandler", "Weber", "Leonard", "Walsh", "Lyons", "Ramsey", "Wolfe", "Schneider",
    "Mullins", "Benson", "Sharp", "Bowen", "Daniel", "Barber", "Cummings", "Hines", "Baldwin", "Griffith", "Valdez",
    "Hubbard", "Salazar", "Reeves", "Warner", "Stevenson", "Burgess", "Santos", "Tate", "Cross", "Garner", "Mann",
    "Mack", "Moss", "Thornton", "Dennis", "Mcgee", "Farmer", "Delgado", "Aguilar", "Vega", "Glover", "Manning", "Cohen",
    "Harmon", "Rodgers", "Robbins", "Newton", "Todd", "Blair", "Higgins", "Ingram", "Reese", "Cannon", "Strickland",
    "Townsend", "Potter", "Goodwin", "Walton", "Rowe", "Hampton", "Ortega", "Patton", "Swanson", "Joseph", "Francis",
    "Goodman", "Maldonado", "Yates", "Becker", "Erickson", "Hodges", "Rios", "Conner", "Adkins", "Webster", "Norman",
    "Malone", "Hammond", "Flowers", "Cobb", "Moody", "Quinn", "Blake", "Maxwell", "Pope", "Floyd", "Osborne",
    "Paul", "McCarthy", "Guerrero", "Lindsey", "Estrada", "Sandoval", "Gibbs", "Tyler", "Gross", "Fitzgerald", "Stokes",
    "Doyle", "Sherman", "Saunders", "Wise", "Colon", "Gill", "Alvarado", "Greer", "Padilla", "Simon", "Waters",
    "Nunez", "Ballard", "Schwartz", "McBride", "Houston", "Christensen", "Klein", "Pratt", "Briggs", "Parsons", "Mclaughlin",
    "Zimmerman", "French", "Buchanan", "Moran", "Copeland", "Roy", "Pittman", "Brady", "Mccormick", "Holloway",
    "Brock", "Poole", "Frank", "Logan", "Owen", "Bass", "Marsh", "Drake", "Wong", "Jefferson", "Park", "Morton",
    "Abbott", "Sparks", "Patrick", "Norton", "Huff", "Clayton", "Massey", "Lloyd", "Figueroa", "Carson", "Bowers",
    "Roberson", "Barton", "Tran", "Lamb", "Harrington", "Casey", "Boone", "Cortez", "Clarke", "Mathis", "Singleton",
    "Wilkins", "Cain", "Bryan", "Underwood", "Hogan", "Mckenzie", "Collier", "Luna", "Phelps", "Mcguire", "Allison",
    "Bridges", "Wilkerson", "Nash", "Summers", "Atkins", "Wilcox", "Pitts", "Conley", "Marquez", "Burnett", "Richard",
    "Cochran", "Chase", "Davenport", "Hood", "Gates", "Clay", "Ayala", "Sawyer", "Roman", "Vazquez", "Dickerson",
    "Hodge", "Acosta", "Flynn", "Espinoza", "Nicholson", "Monroe", "Wolf", "Morrow", "Kirk", "Randall", "Anthony",
    "Whitaker", "Oconnor", "Skinner", "Ware", "Molina", "Kirby", "Huffman", "Bradford", "Charles", "Gilmore", "Dominguez",
    "O'Neal", "Bruce", "Lang", "Combs", "Kramer", "Heath", "Hancock", "Gallagher", "Gaines", "Shaffer", "Short", "Wiggins",
    "Bailey", "Foster", "Brooks", "Reed", "Barnes",
    "Kelly", "Roberts", "Morris", "Russell", "Murphy", "Evans", "Butler", "Fisher", "Cook", "Howard", "Coleman",
    "Hayes", "Kowalski", "Blake", "Sorensen", "Robertson", "Reid","Robinson", "Moore", "Green", "Carter", "Wright", "Young",
    "Hall", "Mitchell", "King", "Adams", "Nelson", "Parker", "Bailey", "Stewart", "Cooper", "Hill", "Phillips", "Ross",
    "Washington", "Long", "Marshall", "Douglas", "Dalton", "Everly", "Fitzgerald", "Harrington", "Jefferson",
    "Kensington", "Montgomery", "Prescott", "Reynolds", "Thackeray", "Wellington", "Bannister", "Calloway", "Davenport",
    "Fairchild", "Hawthorne", "Kensington", "Livingston", "Maxwell", "Norwood", "Pemberton", "Quincy", "Radcliffe",
    "Sutherland", "Tremaine", "Waverly", "Whitaker", "Winslow", "Worthington", "Wycliffe", "Colt", "Orange", "Reat", "Snearl", "Usoro", "Bombaro", "Clyborne", "Concord", "Featheringham", "Hoig", "Javernick"]

  russian_first = [
    "Alexander", "Andrei", "Anton", "Artem", "Boris", "Daniil", "Dmitri", "Evgeni", "Igor", "Ilya",
    "Ivan", "Konstantin", "Maxim", "Mikhail", "Nikita", "Nikolai", "Oleg", "Pavel", "Roman", "Sergei",
    "Stanislav", "Vadim", "Valentin", "Viktor", "Vladimir", "Yaroslav", "Yevgeny", "Yuri", "Zakhar"
  ]

  russian_sur = ["Ivanov", "Petrov", "Popov", "Dimitrov", "Georgiev", "Stefanov", "Andreev", "Angelov", "Ivanov", "Smirnov",
                 "Kuznetsov", "Popov", "Sokolov", "Lebedev", "Kozlov", "Novikov", "Morozov", "Petrov", "Volkov", "Solovyov",
                 "Vasilyev", "Zaytsev", "Pavlov", "Semyonov", "Golubev", "Vinogradov", "Bogdanov", "Vorobev", "Fedorov",
                 "Mikhailov", "Grigoriev", "Titov", "Davydov", "Kuzmin", "Yakovlev", "Romanov", "Makarov", "Ryzhkov", "Sergeev",
                 "Simakov", "Frolov", "Andreev", "Sorokin", "Sokolov", "Karpov", "Gorbachev", "Medvedev", "Orlov", "Nikitin",
                 "Osipov", "Lazarev", "Rodionov", "Kalinin", "Kiselev", "Zaitsev", "Kotov", "Golovin", "Belyaev", "Belov",
                 "Tikhonov", "Bondarenko", "Savchenko", "Alekseev", "Savin", "Nikitin", "Filatov", "Andreev", "Mironov",
                 "Sorokin", "Kovalev", "Zakharov", "Orekhov", "Gerasimov", "Belyakov", "Belikov"]

  balkan_first = [
    "Aleksandar", "Bogdan", "Dimitar", "Goran", "Jovana", "Luka", "Marko", "Milan", "Nikola", "Petar",
    "Stefan", "Viktor", "Vladimir", "Zoran", "Andrej", "Bojana", "Damjan", "Filip", "Gordana", "Igor",
    "Nemanja", "Oliver", "Teodora", "Uroš", "Željko", "Branimir", "Dragan", "Grgur", "Ilija", "Krunoslav",
    "Marin", "Ognjen", "Roko", "Tin", "Zlatko"
]

  balkan_sur = ["Nikolic", "Kovac", "Jovanovic", "Kostic", "Stojanovic", "Markovic", "Milosevic", "Stankovic", "Radovic",
                 "Pavlovic", "Vukovic", "Jovic", "Milic", "Djokic", "Nikolic", "Petrovic", "Ivanovic", "Vukovic", "Stojanovic",
                 "Jovanovic", "Markovic", "Kovac", "Todorovic", "Pavlovic", "Maric", "Simic", "Lukic", "Knezevic", "Nedic", "Radic",
                 "Stankovic", "Vulic", "Antic", "Mitic", "Savic", "Ristic", "Popovic", "Andric", "Bogdanovic", "Kuzmanovic", "Pantic",
                 "Rajkovic", "Babic", "Pezic", "Vujic", "Nedic", "Peric", "Nedic", "Lazic", "Djordjevic", "Dabic", "Lukic",
                 "Marinkovic", "Pajic", "Ilic", "Vasic", "Zivkovic", "Tomic", "Maksimovic", "Stevanovic", "Velickovic", "Mijatovic",
                 "Ristic", "Boskovic", "Milosevic", "Sekulic", "Pavlovic", "Ilic", "Bajic", "Vulic", "Sredojevic", "Marjanovic",
                 "Milenkovic", "Mitrovic", "Stefanovic", "Dimitrovic", "Kostic", "Zdravkovic", "Simeunovic", "Matic", "Arsic",
                 "Radovanovic", "Trifunovic", "Vladic", "Zivkovic", "Djordjevic", "Stefanovic"]

  se_asian_first = ["Ali", "Amir", "Hassan", "Ibrahim", "Mohammed", "Mohammed", "Muhammad", "Muhammad", "Omar", "Yusuf"]

  levantine_first = ["Jad", "Karim", "Mohammad", "Mohammed", "Muhammad", "Muhammad", "Rami", "Youssef"]

  gulf_first = ["Faisal", "Jaber", "Khalid", "Mahmoud", "Mohammed", "Mohammed", "Muhammad", "Muhammad", "Rashid", "Yousef"]

  maghrebi_first = ["Amine", "Hassan", "Ismail", "Mohammed", "Mohammed", "Muhammad", "Muhammad", "Yusuf"]

  egyptian_first = ["Amir", "Hassan", "Ibrahim", "Mohammed", "Mohammed", "Muhammad", "Muhammad", "Omar", "Yusuf"]

  sudan_first = ["Abdul", "Amir", "Hassan", "Ibrahim", "Mohammed", "Mohammed", "Muhammad", "Muhammad", "Omar", "Yusuf"]

  se_asian_sur = ["Aziz", "Basri", "Faisal", "Hamid", "Hassan", "Hussein", "Ibrahim", "Jamal", "Khalid", "Malik",
                  "Mohammed", "Mustafa", "Rahman", "Salleh", "Sultan", "Syed", "Yusof", "Zain", "Abadi", "Adnan",
                  "Bahar", "Din", "Hanif", "Kadir", "Lutfi", "Nasir", "Razak", "Sani", "Tahir", "Umar", "Wahid",
                  "Yasin", "Zahari", "Zubir"]

  levantine_sur = ["Khoury", "Shaheen", "Daher", "Nasrallah", "Abi Farraj", "Haddad", "Al-Masri", "Amir", "Dawood",
                    "Hanna", "Jawhar", "Karam", "Mansour", "Nader", "Rizk", "Sabbagh", "Tawil", "Zuabi"]

  gulf_sur = ["Al-Saud", "Al-Thani", "Al-Maktoum", "Al-Khalifa", "Al-Majid", "Al-Abdullah", "Al-Rashid", "Al-Ghamdi",
              "Al-Marri", "Al-Sabah", "Al-Zahrani", "Al-Nasser", "Al-Balushi", "Al-Harthy", "Al-Muhairi",
              "Al-Sulaiti", "Al-Zayed"]

  maghrebi_sur = ["Ben Youssef", "Belhadj", "Bouzid", "Cherif", "El Amrani", "Kadiri", "Slimani", "Alaoui", "Ammar",
              "Chaabane", "Djelloul", "Hammami", "Nouri", "Rouissi", "Zemouri"]

  egyptian_sur = ["Abdel-Meguid", "El-Sayed", "Mahmoud", "Hassan", "Gaber", "El-Din", "Gawad", "Badawi", "El-Khatib",
              "Farag", "Hegazi", "Kamel", "Lotfy", "Mekki", "Saad", "Sobhy", "Zaki"]

  sudan_sur = [ "Abdel-Rahman", "Abu Baker", "Hamad", "Ismail", "Khalifa", "Omar", "Salih", "Taha", "Adam", "Ali",
            "Bashir", "Eisa", "Fadl", "Ghazali", "Hussein", "Idris", "Musa", "Younis", "Abdullahi"]

  french_african_first = ["Amadou", "Aïssatou", "Moussa", "Amina", "Ousmane", "Mariam", "Ismael", "Fatou",
                          "Ibrahima", "Aïcha", "Mamadou", "Coumba", "Adama", "Awa", "Sekou", "Kadiatou",
                          "Oumar", "Hawa", "Alassane", "Salimatou", "Daouda", "Astou", "Modibo", "Nafissatou",
                          "Issa"]

  french_african_sur = ["Diallo", "Diop", "Dabo", "Traore", "Faye", "Ndiaye", "Sylla", "Thiam", "Camara",
                    "Cisse", "Sow", "Kouyate", "Kante", "Diawara", "Bamba", "Dembele", "Doumbia", "Sanogo",
                    "Toure", "Kone", "Keita", "Sidibe", "Sangare", "Diarra", "Diabate", "Tandia", "Kamara",
                    "Sylla", "Diagne", "Niang", "Sagna", "Sambou", "Djiba", "Mbaye", "Fall", "Sall", "Diagne",
                    "Dione", "Gueye", "Niane", "Djiby", "Diong", "Zouma", "Gaye", "Keita"]

  english_african_first = ["Kwame", "Nia", "Malik", "Aisha", "Jomo", "Ayana", "Kofi", "Fatima", "Jabari", "Naima",
                            "Amin", "Nyla", "Idris", "Amara", "Zuri", "Aiden", "Zara", "Nasir", "Sanaa", "Amir",
                            "Sade", "Kaden", "Nia", "Khalil", "Imani"]

  english_african_sur = ["Adeyemi", "Obi", "Okafor", "Okeke", "Nwankwo", "Eze", "Ogunbiyi", "Ogundele", "Olowe",
                      "Osagie", "Uzoma", "Okonkwo", "Olabode", "Adebayo", "Olajuwon", "Akinwale", "Odusanya",
                      "Oyebanjo", "Adegoke", "Ajayi", "Ogbonna", "Akintola", "Oluwole", "Omondi", "Oduor",
                      "Nyong'o", "Adeleke", "Adeola", "Odumodu", "Chukwu", "Mensah", "Yao", "Addo", "Asante",
                      "Ayew", "Boateng", "Dankwa", "Dzifa", "Mensah", "Osei", "Owusu", "Quansah", "Tetteh",
                      "Amoah", "Ansah", "Koomson", "Ampadu", "Adu", "Annan", "Arthur", "Gyan", "Aidoo", "Nkoudou",
                      "Ngoh", "Tchakounte", "Fotso", "Eto'o", "Ngo'o", "Mvondo", "Mbappe", "Fokam", "Njoh",
                      "Ndamukong", "Biya", "Moukandjo", "Bongonda", "Olinga", "Onguene", "Abanda", "Bassogog",
                      "Milla", "Mboma"]

  east_african_first = ["Abdi", "Lina", "Musa", "Zahra", "Solomon", "Sara", "Asad", "Nadia", "Isaiah", "Alia",
                        "Yusuf", "Amina", "Elijah", "Zainab", "Ezekiel", "Layla", "Yohannes", "Samira", "Haile",
                        "Najma", "Imani", "Tendai", "Ayubu", "Habiba", "Jamal"]

  east_african_sur = ["Kamau", "Mwangi", "Njoroge", "Kariuki", "Gitonga", "Odhiambo", "Macharia", "Kiarie",
                  "Wanjiku", "Kimani", "Omondi", "Musyoka", "Akinyi", "Odhiambo", "Ogutu", "Ogola", "Odongo",
                  "Achieng", "Kagwe", "Juma", "Mbatha", "Njuguna", "Njeri", "Mwaura", "Nzuki", "Nyambura",
                  "Kimathi", "Okoth", "Mburu", "Kibet"]

  southern_african_first = ["Tariro", "Zanele", "Kwazi", "Thandi", "Bongani", "Ayanda", "Thabo", "Nomvula",
                            "Mandla", "Nokuthula", "Musa", "Thandeka", "Sipho", "Lindiwe", "Mzwandile", "Zinhle",
                            "Enoch", "Khanyisile", "Ndabezinhle", "Nandi", "Siyabonga", "Lerato", "Tatenda",
                            "Noluthando", "Mthokozisi"]

  southern_african_sur = ["Ndlovu", "Dube", "Moyo", "Mkhize", "Zulu", "Khumalo", "Mabaso", "Zuma", "Mthembu",
                      "Mokoena", "Motloung", "Maseko", "Nkosi", "Nkuna", "Moloi", "Molefe", "Mokwena",
                      "Modise", "Tladi", "Khoza", "Mphela", "Phiri", "Mofokeng", "Magagula", "Ndhlovu",
                      "Sibanda", "Lekwane", "Letsebe", "Mokone", "Makwela"]

  china_first = [
    "Wei", "Jian", "Xin", "Lei", "Chen", "Hao", "Yi", "Xiang", "Peng", "Zhong", "Jing", "Gang", "Shan", "Yan", "Yang",
    "Tao", "Jun", "Hui", "Ming", "Wei", "Qiang", "Li", "Bo", "Feng", "Sheng", "Bin", "Chao", "Tian", "Zheng", "Hong",
    "Jin", "Kang", "Yu", "Cheng", "Yong", "Hua", "Xue", "Zhi", "Rui", "Xu", "Dong", "Lin", "Jiang", "Ren", "Mao",
    "Zhang", "Guo", "Xian", "Rong", "Shi", "Nan", "Fu", "Zhen", "Liang", "Bao", "Min"
  ]

  japan_first = [
      "Haruki", "Kaito", "Yuto", "Sota", "Riku", "Hiroto", "Yuki", "Yuma", "Haru", "Sora", "Ryota", "Kota", "Ren",
      "Ryo", "Hayato", "Kazuki", "Shota", "Takumi", "Yusei", "Tatsuki", "Takeru", "Kakeru", "Ryusei", "Yuito",
      "Yosuke", "Naoki", "Kohei", "Tomoya", "Kota", "Sho", "Shun", "Keita", "Takeru", "Hiroshi", "Yamato", "Yusuke",
      "Masaki", "Kenta", "Yoshiki", "Kosei", "Hinata", "Sosuke", "Yusaku", "Daiki", "Ryosuke", "Koichi", "Tomoaki",
      "Takahiro", "Kotaro", "Shuto", "Satoshi", "Junya", "Hiroki", "Kensuke"
  ]

  korea_first = [
      "Jihoon", "Minjoon", "Seojin", "Yeonwoo", "Siwon", "Taehyun", "Donghyun", "Jisung", "Minseok", "Hyunwoo",
      "Sungmin", "Jiwon", "Jungwoo", "Sanghoon", "Taeho", "Dongwook", "Jaehyun", "Seojun", "Yongmin", "Chanwoo",
      "Seojin", "Jinwoo", "Minhyuk", "Jaewon", "Kyunghoon", "Dongmin", "Joonho", "Woohyun", "Seungwoo", "Kyungsoo",
      "Jinseok", "Seokjin", "Hyungjun", "Younghoon", "Kyungwoo", "Sangwoo", "Hoon", "Junho", "Hyeonseok", "Sihoon",
      "Dohyun", "Byungchul", "Hoseok", "Taewoo", "Dongwon", "Yunseong", "Seungho", "Yonghyun", "Sunghyun", "Hyunjoon",
      "Hyeonwoo", "Junsik"
  ]

  india_first = [
      "Arjun", "Aryan", "Aditya", "Rahul", "Rohan", "Siddharth", "Vikram", "Amit", "Anish", "Deepak", "Gaurav", "Karan",
      "Manish", "Nikhil", "Pranav", "Ravi", "Rohit", "Sandeep", "Satish", "Shivam", "Sumit", "Vijay", "Aakash", "Arun",
      "Ashish", "Dhruv", "Ganesh", "Hari", "Jatin", "Kunal", "Naveen", "Pawan", "Rajat", "Rajesh", "Sanjay", "Santosh",
      "Tarun", "Umesh", "Varun", "Vivek", "Yash", "Abhinav", "Amar", "Anand", "Ankit", "Ashok", "Dinesh", "Gopal", "Hitesh",
      "Kamal", "Mohan", "Narendra", "Pradeep"
  ]

  china_sur = [
      "Li", "Wang", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Lin", "Sun", "Xu", "Ma", "Gao", "Hu", "Luo",
      "He", "Li", "Shi", "Lu", "Wu", "Wu", "Zhou", "Yu", "Feng", "Peng", "Jiang", "Tang", "Wei", "Xie", "Song", "Qian",
      "Dong", "Han", "Yuan", "Yu", "Tian", "Yao", "Pan", "Mao", "Long", "Zou", "Cao", "Xiao", "Qin", "Shen", "Zeng",
      "Xiong", "Fu", "Meng", "Wei", "Lu", "Jin", "Cheng", "Yin", "Jiang", "Du"
  ]

  japan_sur = [
      "Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Ito", "Yamamoto", "Nakamura", "Kobayashi", "Saito",
      "Kimura", "Yoshida", "Yamada", "Nakajima", "Kato", "Yamaguchi", "Matsumoto", "Inoue", "Mori", "Ikeda",
      "Hashimoto", "Abe", "Kondo", "Ishikawa", "Okada", "Kawasaki", "Fujita", "Kojima", "Miyazaki", "Nakano",
      "Ogawa", "Hayashi", "Shimizu", "Shibata", "Tamura", "Sakamoto", "Matsuda", "Hasegawa", "Fujita", "Aoki",
      "Ota", "Miura", "Kojima", "Morita", "Fujimoto", "Ishii", "Takagi", "Kubo", "Nishimura", "Fukuda", "Matsui",
      "Nakayama", "Harada", "Ono", "Yano", "Yoshikawa", "Sakai", "Yamashita"
  ]

  korea_sur = [
      "Kim", "Lee", "Park", "Choi", "Jung", "Kang", "Yoon", "Han", "Jeong", "Chung", "Yang", "Lim", "Shin", "Seo",
      "Hong", "Song", "Kwon", "Jo", "Ko", "Oh", "Kang", "Lee", "Nam", "Seong", "Im", "Eom", "Cheon", "Bae", "Bak",
      "Seok", "Jeon", "Hwang", "Chon", "Hahn", "Cha", "An", "Jeong", "Gim", "Ha", "Gu", "Yeo", "Won", "No", "Yu",
      "Go", "Yun", "Chwe", "Choo", "Son", "Han", "So", "Han", "Sin", "Chae", "Sim", "Do"
  ]

  india_sur = [
    "Patel", "Sharma", "Singh", "Kumar", "Mehta", "Jain", "Shah", "Gupta", "Verma", "Rao", "Reddy", "Malhotra",
    "Yadav", "Shukla", "Chauhan", "Sharma", "Rajput", "Jha", "Sinha", "Mishra", "Srivastava", "Pandey", "Saxena",
    "Choudhary", "Deshmukh", "Pawar", "Bhatia", "Agrawal", "Biswas", "Khan", "Rao", "Dixit",
    "Roy", "Naidu", "Chopra", "Das", "Kulkarni", "Pandey", "Goswami", "Nair", "Chakraborty", "Sarkar", "Dutta",
    "Banerjee", "Menon", "Iyer", "Shetty", "Nambiar", "Sethi", "Gupta", "Sinha", "Kaur", "Raj", "Rathod"
]

  scand_first = [
    "Erik", "Lars", "Anders", "Johan", "Henrik", "Sven", "Oskar", "Emil", "Gustav", "Frederik", "Oliver", "Axel",
    "Niklas", "Kristian", "Oscar", "Daniel", "Mikkel", "Sebastian", "Benjamin", "Christian", "Anton", "Jonas", "Mathias",
    "Viktor", "Lucas", "Simon", "Isak", "Max", "Noah", "Marcus", "Carl", "Elias", "Julius", "Philip", "William", "Hugo",
    "Joakim", "Alexander", "Martin", "Nils", "Jakob", "Kasper", "Victor", "Peter", "Adam", "Gabriel", "Tobias", "David",
    "Elias", "Samuel", "Fredrik", "Leo", "Henning", "Jonathan", "Mads", "August", "Matthias", "Lukas", "Benjamin",
    "Malthe", "Rasmus", "Theo", "Jesper", "Sebastian", "Sofus", "Silas", "Sander", "Albert", "Marius", "Filip", "Bastian",
    "Frederik", "Lasse", "Mikkel", "Nikolaj", "Jannik", "Johannes", "Nicolai", "Thomas", "Simon", "Christian", "Magnus"]

  scand_sur = [
    "Hansen", "Jensen", "Andersen", "Nielsen", "Pedersen", "Kristensen", "Olsen", "Petersen", "Madsen", "Jorgensen",
    "Christensen", "Sorensen", "Rasmussen", "Johansen", "Moller", "Mortensen", "Larsen", "Svendsen", "Hermansen", "Thomsen",
    "Lund", "Eriksen", "Mikkelsen", "Mortensen", "Rasmussen", "Lund", "Christiansen", "Berg", "Larsson", "Svensson",
    "Gustafsson", "Johansson", "Eriksson", "Nilsson", "Karlsson", "Andersson", "Persson", "Olsson", "Lindberg", "Lindstrom",
    "Lindqvist", "Bergström", "Sjoberg", "Gustavsson", "Holm", "Holmgren", "Soderberg", "Bengtsson", "Jonsson", "Carlsson",
    "Pettersson", "Hansson", "Mattsson"
]

  sa_hisp_first = [
    "Juan", "Carlos", "Luis", "Miguel", "Jose", "Antonio", "Manuel", "Javier", "Pedro", "Francisco", "Ricardo", "Mario",
    "Angel", "Gabriel", "Alejandro", "Sergio", "Rafael", "Fernando", "Pablo", "Andres", "Hector", "Daniel", "Victor",
    "Alberto", "Eduardo", "Roberto", "Ramon", "Emilio", "Jorge", "Ernesto", "Adrian", "Arturo", "Diego", "Marco",
    "Israel", "Felipe", "Gustavo", "Nelson", "Oscar", "Rodrigo", "Salvador", "Cesar", "Hugo", "Leonardo", "Enrique",
    "Emmanuel", "Alonso", "Alexis", "Raul", "Maximiliano", "Mauricio", "Cristian", "Bruno", "Ignacio", "Elias",
    "Sebastian", "Renato", "Federico", "Ismael", "Matias", "Julian", "Erick", "Raul", "Mariano", "Guillermo", "Nicolás",
    "Hernan", "Kevin", "Ezequiel", "Ariel", "Ivan", "Cristobal", "Bryan", "Martin", "Luciano", "Santiago", "Axel",
    "Agustin", "Gonzalo", "Joel", "Lorenzo", "Emanuel", "Alan", "Gaston", "Raul", "Esteban", "Joaquin", "Damian",
    "Leonel", "Benjamin", "Fabian", "Alejandro", "Juan Carlos", "Juan Pablo", "Jose Antonio", "Jose Luis", "Jesus",
    "Ricardo", "Carlos Alberto", "Antonio", "Miguel Angel", "Luis Alberto", "Carlos Manuel", "Francisco Javier",
    "Jose Manuel", "Miguel Angel", "Juan Jose"
  ]

  spain_first = [
      "Antonio", "Manuel", "Jose", "Francisco", "David", "Juan", "Javier", "Jose Antonio", "Jose Manuel", "Miguel",
      "Angel", "Francisco Javier", "Alejandro", "Rafael", "Pedro", "Jose Luis", "Daniel", "Jesus", "Juan Carlos",
      "Luis", "Fernando", "Juan Jose", "Pablo", "Miguel Angel", "Sergio", "Alberto", "Carlos", "Juan Antonio", "Diego",
      "Fernando", "Jorge", "Ramon", "Victor", "Ruben", "Adrian", "Enrique", "Ricardo", "Juan Manuel", "Julian", "Mario",
      "Luis Miguel", "Marcos", "Francisco Jose", "Mariano", "Gabriel", "Andres", "Emilio", "Victor Manuel", "Roberto",
      "Angel", "Alvaro", "Joan", "Jaime", "Ignacio", "Ivan", "Gonzalo", "Eduardo", "Agustin", "Cristian", "Raul",
      "Emmanuel", "Hector", "Eugenio", "Federico", "Cesar", "Oscar", "Tomas", "Felix", "Lorenzo", "Juan Francisco",
      "Guillermo", "Alex", "Xavier", "Luis Fernando", "Jordi", "Raul", "Marcelo", "Borja", "Salvador", "Ismael",
      "Jaime", "Gregorio", "Nicolas", "Angel Luis", "Bruno", "Eloy", "Esteban", "Patricio", "Rogelio", "Abel",
      "Sebastian", "Jesus Maria", "Victoriano", "Baltasar", "Jacinto", "Xavi", "Anselmo", "Ramiro", "Vidal", "Gorka",
      "Telmo", "Feliciano", "Teodoro", "Eligio", "Vicente", "Iker", "Genaro", "Bonifacio", "Celestino", "Isidro",
      "Adolfo", "Olegario", "Eulogio", "Gustavo", "Valentin", "Teofilo", "Epifanio", "Placido", "Javier Antonio",
      "Julio Cesar", "Pedro Antonio", "Juan Ramon", "Angel Luis", "Ismael", "Manuel Jesus", "Jesus Manuel", "Jesus Maria",
      "Juan Antonio"
  ]

  sa_hisp_sur = [
      "Silva", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Perez", "Martinez", "Gomez", "Ramos", "Chavez", "Morales",
      "Hernandez", "Torres", "Garcia", "Santos", "Ortega", "Vargas", "Mendoza", "Reyes", "Alvarez", "Rojas", "Cruz", "Nunez",
      "Castillo", "Medina", "Delgado", "Ramirez", "Pacheco", "Guerrero", "Vega", "Flores", "Leon", "Herrera", "Navarro",
      "Campos", "Jimenez", "Ibanez", "Rios", "Soto", "Valencia", "Pena", "Montoya", "Cardenas", "Escobar", "Fuentes",
      "Acosta", "Velasquez", "Zamora", "Carvajal", "Serrano", "Cortez", "Aguilar", "Gutierrez", "Molina", "Camacho",
      "Estrada", "Arroyo", "Calderon", "Palacios", "Rocha", "Miranda", "Osorio", "Roman", "Cabrera", "Bautista", "Paredes",
      "Figueroa", "Santiago", "Lara", "Avila", "Mendez", "Villarreal", "Mercado", "Carrillo", "Maldonado", "Olivera",
      "Arias", "Sepulveda", "Pinto", "Espinoza", "Benitez", "Luna", "Cordova", "Cisneros", "Castañeda", "Delgado"
  ]

  spain_sur = [
      "Garcia", "Gonzalez", "Rodriguez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez", "Martin", "Jimenez",
      "Ruiz", "Hernandez", "Diaz", "Moreno", "Alvarez", "Romero", "Morales", "Ortega", "Delgado", "Castro", "Silva",
      "Santos", "Castillo", "Gimenez", "Vargas", "Rojas", "Mendoza", "Ramos", "Pacheco", "Fuentes", "Herrera", "Cruz",
      "Carmona", "Cabrera", "Carrasco", "Nieto", "Moya", "Reyes", "Ibanez", "Soto", "Vicente", "Vega", "Rios", "Roman",
      "Esteban", "Valero", "Blanco", "Serrano", "Lara", "Marin", "Prieto", "Roldan", "Soler", "Guerrero", "Mesa",
      "Redondo", "Velasco", "Toledo", "Rubio", "Cortes", "Bautista", "Paredes", "Figueroa", "Santiago", "Lorenzo",
      "Saez", "Valencia", "Navarro", "Rivas", "Crespo", "Rico", "Oliver", "Mendez", "Molina", "Otero", "Avila",
      "Bellido", "Marquez", "Benitez", "Carrillo", "Gallardo", "Pardo", "Camacho", "Cuevas", "Quintana", "Gallego"
  ]

  french_first = [
    "Lucas", "Louis", "Gabriel", "Adam", "Hugo", "Raphael", "Leo", "Arthur", "Paul", "Nathan", "Ethan", "Theo", "Tom",
    "Maxime", "Antoine", "Noah", "Jules", "Baptiste", "Enzo", "Mathis", "Valentin", "Matteo", "Alexandre", "Nolan",
    "Sacha", "Timeo", "Thomas", "Leo", "William", "Evan", "Benjamin", "Alexis", "Eliott", "Remi", "Simon", "Victor",
    "Augustin", "Pierre", "Noe", "Yanis", "Tristan", "Gaspard", "Robin", "Maxence", "Elias", "Ethan", "Oscar", "Thibault",
    "Julien", "Come", "Clement", "Corentin", "Romain", "Matheo", "Samuel", "Martin", "Noel", "Adrien", "Thomas", "Louis",
    "Gaspard", "Augustin", "Jean", "Hugues", "Thibaut", "Pierre", "Guillaume", "Charles", "Luc", "Paul", "Philippe",
    "Jacques", "Francois", "Henri", "Antoine", "Alexandre", "David", "Michel", "Jean-Baptiste", "Nicolas", "Vincent",
    "Matthieu", "Joseph", "Olivier", "Sebastien", "Emmanuel", "Bertrand", "Frederic", "Patrick"
  ]

  french_sur = [
    "Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", "Simon",
    "Laurent", "Lefevre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier", "Morel", "Girard",
    "Andre", "Lefebvre", "Mercier", "Dupont", "Lambert", "Bonnet", "Francois", "Martinez", "Legrand", "Garnier",
    "Faure", "Rousseau", "Blanc", "Guerin", "Muller", "Henry", "Riviere", "Lucas", "Jean", "Dumont", "Lecomte",
    "Lopez", "Fontaine", "Chevalier", "Colin", "Marchand", "Aubry", "Renard", "Bourgeois", "Roger", "Roy", "Dupuis",
    "Noel", "Lemoine", "Gaillard", "Philippe", "Leclerc", "Barbier", "Dupuy", "Perrin", "Morin", "Dufour", "Clement",
    "Bailly", "Robin", "Lemoigne", "Cousin", "Boucher", "Leduc", "Leblanc", "Renaud", "Dumas", "Blanchard", "Leclercq",
    "Guillaume", "Lebrun", "Caron", "Guillot", "Julien", "Prevost", "Collet", "Masson", "Fabre", "Leroux", "Maillard",
    "Vidal", "Lamy", "Marchal", "Delaunay", "David", "Delaurent", "Huet", "Herve", "Leroux", "Loiseau", "Cordier",
    "Aubert", "Bourgeois", "Lebon", "Charles", "Lefort", "Roy", "Marchand", "Dupuis", "Lefebvre", "Benoit", "Picard",
    "Colin", "Perrot", "Brun", "Garnier", "Vasseur"
  ]

  german_first = [
    "Max", "Ben", "Paul", "Jonas", "Finn", "Lukas", "Leon", "Felix", "Luca", "Noah", "Tim", "Moritz", "Jan", "Julian",
    "Elias", "Simon", "Nico", "Philipp", "Dominik", "David", "Niklas", "Alexander", "Tom", "Tobias", "Eric", "Daniel",
    "Fabian", "Jannik", "Oskar", "Christian", "Marc", "Andreas", "Markus", "Marvin", "Sebastian", "Stefan", "Nils",
    "Oliver", "Florian", "Matthias", "Kai", "Sven", "Leonard", "Thomas", "Hannes", "Jonathan", "Timon", "Fiete", "Henrik",
    "Bennet", "Torben", "Nikolai", "Jakob", "Raphael", "Lennard", "Malte", "Mathis", "Jannis", "Johann", "Jannes",
    "Joschua", "Karsten", "Kevin", "Kilian", "Lennart", "Linus", "Ludwig", "Luis", "Magnus", "Mario", "Marvin",
    "Matteo", "Maurice", "Mika", "Mirko", "Moritz", "Nikita", "Niklas", "Nils", "Noel", "Ole", "Pascal", "Patrick",
    "Paul", "Peer", "Philipp", "Pierre", "Quentin", "Rafael", "Ramon", "Richard", "Robert"
]

  german_sur = [
    "Schmidt", "Schneider", "Fischer", "Meyer", "Weber", "Schulz", "Wagner", "Becker", "Hoffmann", "Schafer", "Koch",
    "Bauer", "Richter", "Klein", "Wolf", "Schroder", "Neumann", "Schwarz", "Zimmermann", "Braun", "Kruger",
    "Hofmann", "Hartmann", "Lange", "Schmitt", "Werner", "Schmitz", "Krause", "Meier", "Lehmann", "Schmid", "Schulze",
    "Maier", "Kohler", "Herrmann", "Konig", "Walter", "Mayer", "Huber", "Kaiser", "Fuchs", "Peters", "Lang",
    "Scholz", "Moller", "Weiss", "Jung", "Hahn", "Vogel", "Friedrich", "Keller", "Gunther", "Frank", "Berger",
    "Roth", "Beck", "Lorenz", "Baumann", "Franke", "Albrecht", "Schuster", "Simon", "Ludwig", "Bohm", "Winter",
    "Kraus", "Martin", "Schumacher", "Kramer", "Vogt", "Stein", "Jager", "Otto", "Sommer", "Gross", "Seidel",
    "Heinrich", "Brandt", "Haas", "Schreiber", "Graf", "Schulte", "Dietrich", "Ziegler", "Kuhn", "Pohl", "Engel",
    "Horn", "Bergmann", "Voigt", "Busch", "Thomas", "Sauer", "Arnold", "Wolff", "Pfeiffer", "Herzog", "Schumann",
    "Frey", "Beyer", "Seifert", "Maurer", "Moeller", "Geiger", "Gross", "Riedel", "Kirchner", "Kramer", "Reuter",
    "Barth", "Witt", "Ullrich", "Freitag", "Beckmann", "Lutz", "Schultz", "Reichert", "Kunz", "Schütz", "Hesse"
  ]

  italian_first = [
    "Luca", "Leonardo", "Gabriele", "Alessandro", "Mattia", "Francesco", "Lorenzo", "Andrea", "Matteo", "Giovanni",
    "Simone", "Antonio", "Marco", "Davide", "Christian", "Federico", "Riccardo", "Filippo", "Raffaele", "Nicola",
    "Daniele", "Pietro", "Enrico", "Giuseppe", "Stefano", "Vincenzo", "Michele", "Massimo", "Alessio", "Mario",
    "Sergio", "Giacomo", "Paolo", "Salvatore", "Angelo", "Carmine", "Roberto", "Alberto", "Fabio", "Emanuele", "Diego",
    "Giorgio", "Alessandro", "Emilio", "Gianluca", "Samuele", "Tommaso", "Nicolo", "Omar", "Cristian", "Gianmarco",
    "Ettore", "Elia", "Rocco", "Lorenzo", "Gianluigi", "Manuel", "Renato", "Vittorio", "Dario", "Gianfranco", "Valerio",
    "Luigi", "Mauro", "Adriano", "Carlo", "Gino", "Guido", "Luciano", "Giovanni", "Bruno", "Dante", "Nino", "Elio",
    "Aldo", "Ottavio", "Alberto", "Sandro", "Eugenio", "Loris", "Santo", "Silvio", "Vito", "Ugo", "Renzo", "Fabrizio"
  ]

  italian_sur = [
      "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco", "Bruno",
      "Gallo", "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi", "Moretti", "Barbieri",
      "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", "Longo", "Gentile",
      "Valentini", "Pellegrini", "Donati", "Gatti", "Palmieri", "Sanna", "Fabbri", "Serra", "Ferri", "Battaglia",
      "Martino", "Guerra", "Rossetti", "Piras", "Farina", "D'Amico", "Damiani", "Mazza", "Bellini", "Riva", "De Santis",
      "Lupo", "Cattaneo", "De Angelis", "D'Angelo", "Bruni", "Sartori", "Sorrentino", "D'Amato", "Amato", "Romani",
      "Rusconi", "Marchetti", "Testa", "Villa", "Salvatore", "Silvestri", "Ruggiero", "De Rosa", "Negri", "Pace",
      "Carbone", "Rizzi", "Benedetti", "Grasso", "Bianco", "Gallo", "Riva", "De Santis", "D'Amico", "Ferri", "Marino",
      "Mazza", "Piras", "Pellegrini", "Romani", "Romano", "Rusconi", "Russo", "Sanna", "Santoro", "Serra", "Sorrentino",
      "Testa", "Valentini", "Villa"
  ]

  portuguese_sur = [
    "Silva", "Santos", "Ferreira", "Pereira", "Oliveira", "Costa", "Rodrigues", "Martins", "Gomes", "Lopes", "Almeida",
    "Ribeiro", "Carvalho", "Cunha", "Sousa", "Moreira", "Mendes", "Nunes", "Vieira", "Monteiro", "Cardoso", "Rocha",
    "Araujo", "Fonseca", "Ramos", "Castro", "Pinto", "Fernandes", "Gonçalves", "Machado", "Santana", "Neves", "Morais",
    "Coelho", "Jesus", "Barbosa", "Marques", "Soares", "Reis", "Antunes", "Teixeira", "Correia", "Alves", "Pires",
    "Freitas", "Campos", "Borges", "Azevedo", "Nogueira", "Lourenço", "Simoes", "Andrade", "Dias", "Paiva", "Barros",
    "Cruz", "Figueiredo", "Faria", "Miranda", "Guerreiro", "Melo", "Amaral", "Pinheiro", "Leal", "Saraiva", "Bento",
    "Esteves", "Vargas", "Batista", "Salgado", "Veiga", "Goulart", "Tavares", "Gomes", "Cabral", "Raposo", "Peixoto",
    "Cavalcante", "Freire", "Branco", "Cesar", "Rosa", "Macedo", "Vieira", "Caldeira", "Coutinho", "Camacho", "Amarante",
    "Moura", "Carmo", "Santiago", "Matias", "Dias"
  ]

  portuguese_first = [
    "Joao", "Manuel", "Antonio", "Francisco", "Paulo", "Pedro", "Luis", "Miguel", "Carlos", "Jorge", "Rui", "Jose",
    "Nuno", "Andre", "Bruno", "Fernando", "Sergio", "Ricardo", "Daniel", "Ricardo", "Artur", "Alberto", "Alexandre",
    "Goncalo", "Hugo", "Mario", "Raul", "Leonardo", "Guilherme", "Joaquim", "Diogo", "Eduardo", "Ivan", "Rafael",
    "Tomas", "Fabio", "Vitor", "Salvador", "Tiago", "Gabriel", "Alex", "Samuel", "Filipe", "Julio", "Cristiano",
    "Vasco", "Isaac", "Adriano", "Americo", "Renato", "Rogerio", "Ruben", "Javier", "Xavier", "Elias", "Emanuel",
    "Rodrigo", "Noe", "Juliao", "Celestino", "Bernardo", "Constantino", "Dinis", "Leandro", "Micael", "Simao", "Lucas",
    "Israel", "Alan", "Cesar", "Gustavo", "Clemente", "Rui", "Joel", "Augusto", "Helder", "Ernesto", "Gualter", "Afonso",
    "Diego", "Milton", "Delfim", "Sandro", "Josue", "Anibal", "Maximiano", "Rodolfo",
    "Eusebio", "Lazaro", "Maximiano", "Rodolfo"
  ]

  turkish_sur = [
    "Yilmaz", "Ozturk", "Demir", "Saya", "Sahin", "Celik", "Arslan", "Aksoy", "Ozdemir", "Dogan", "Balik", "Kaplan", "Mehmet"
  ]

  turkish_first = [
    "Ahmet", "Ali", "Avi", "Mustafa", "Emir", "Yusuf", "Ayaz", "Bayram", "Altan", "Alp", "Omer", "Aslan", "Kerem", "Goktug", "Metehan"
  ]

  if name == 'full':

    c = random.choices(range(8), weights=[80,1,4,2,3,2,4,4], k=1)[0]

    # english
    if c == 0:
      country = random.choices([USA, CAN, AUS, NZL, ENG], weights=[453, 25, 12, 1, 2], k=1)[0]
      if random.choices([0,1],weights=[98,2],k=1)[0] == 0:
        return random.choice(first_names) + ' ' + random.choice(last_names), country
      else:
        return random.choice(first_names) + ' ' + random.choice(last_names) + '-' + random.choice(last_names), country

    # russian
    elif c == 1:
      country = random.choices([USA, RUS, UKR, POL], weights=[20, 10, 12, 5], k=1)[0]
      if random.choice(range(10)) < 2:
        c2 = random.choices(range(5),weights=[196,1,1,1,1],k=1)[0]
        if c2 == 0:
          return random.choice(first_names) + ' ' + random.choice(russian_sur), country
        elif c2 == 1:
          return random.choice(first_names) + ' ' + random.choice(russian_sur) + '-' + random.choice(last_names), country
        elif c2 == 2:
          return random.choice(first_names) + ' ' + random.choice(last_names) + '-' + random.choice(russian_sur), country
        elif c2 == 3:
          return random.choice(russian_first) + ' ' + random.choice(russian_sur) + '-' + random.choice(last_names), country
        else:
          return random.choice(russian_first) + ' ' + random.choice(last_names) + '-' + random.choice(russian_sur), country
      else:
        return random.choice(russian_first) + ' ' + random.choice(russian_sur), country

    # balkan
    elif c == 2:
      country = random.choices([USA, SRB, CRO, MON, BOS, SLV], weights=[20, 40, 25, 7, 8, 13], k=1)[0]
      if random.choice(range(10)) < 1:
        c2 = random.choices(range(5),weights=[196,1,1,1,1],k=1)[0]
        if c2 == 0:
          return random.choice(first_names) + ' ' + random.choice(balkan_sur), country
        elif c2 == 1:
          return random.choice(first_names) + ' ' + random.choice(balkan_sur) + '-' + random.choice(last_names), country
        elif c2 == 2:
          return random.choice(first_names) + ' ' + random.choice(last_names) + '-' + random.choice(balkan_sur), country
        elif c2 == 3:
          return random.choice(balkan_first) + ' ' + random.choice(balkan_sur) + '-' + random.choice(last_names), country
        else:
          return random.choice(balkan_first) + ' ' + random.choice(last_names) + '-' + random.choice(balkan_sur), country
      else:
        return random.choice(balkan_first) + ' ' + random.choice(balkan_sur), country

    # south asian / middle east
    elif c == 3:
      c2 = random.choice(range(30))
      if c2 < 1:
        return random.choice(se_asian_first) + ' ' + random.choice(se_asian_sur), IRN
      elif c2 < 2:
        return random.choice(gulf_first) + ' ' + random.choice(gulf_sur), SAU
      elif c2 < 11:
        return random.choice(levantine_first) + ' ' + random.choice(levantine_sur), random.choices([JOR, ISR, LBN], [1, 4, 4], k=1)[0]
      elif c2 < 12:
        return random.choice(maghrebi_first) + ' ' + random.choice(maghrebi_sur), TUN
      elif c2 < 13:
        return random.choice(egyptian_first) + ' ' + random.choice(egyptian_sur), EGY
      elif c2 < 19:
        return random.choice(sudan_first) + ' ' + random.choice(sudan_sur), SSD
      elif c2 < 23:
        return random.choice(turkish_first) + ' ' + random.choice(turkish_sur), TUR
      else:
        c3 = random.choice(range(2))
        if c3 == 0:
          return random.choice(first_names) + ' ' + random.choice(levantine_sur), random.choices([USA, JOR, ISR, LBN], [7, 1, 4, 4], k=1)[0]
        else:
          return random.choice(first_names) + ' ' + random.choice(sudan_sur), random.choices([USA, SSD], [1, 2], k=1)[0]

    # african
    elif c == 4:
      c2 = random.choice(range(10))
      if c2 < 3:
        return random.choice(french_african_first) + ' ' + random.choice(french_african_sur), random.choices([FRA, SEN], [1, 3], k=1)[0]
      elif c2 < 7:
        return random.choice(english_african_first) + ' ' + random.choice(english_african_sur), random.choices([USA, NGA], [1, 5], k=1)[0]
      elif c2 < 8:
        return random.choice(east_african_first) + ' ' + random.choice(east_african_sur), CAM
      elif c2 < 9:
        return random.choice(southern_african_first) + ' ' + random.choice(southern_african_sur), DRC
      else:
        c3 = random.choice(range(4))
        if c3 == 0:
          return random.choice(first_names) + ' ' + random.choice(french_african_sur), random.choices([USA, FRA, SEN], [1, 1, 1], k=1)[0]
        elif c3 == 1:
          c4 = random.choices(range(5),weights=[90,4,2,2,2],k=1)[0]
          if c4 == 0:
            return random.choice(first_names) + ' ' + random.choice(english_african_sur), random.choices([USA, NGA], [1, 1], k=1)[0]
          elif c4 == 1:
            return random.choice(first_names) + ' ' + random.choice(english_african_sur) + '-' + random.choice(last_names), random.choices([USA, NGA], [1, 1], k=1)[0]
          elif c4 == 2:
            return random.choice(first_names) + ' ' + random.choice(last_names) + '-' + random.choice(english_african_sur), random.choices([USA, NGA], [1, 1], k=1)[0]
          elif c4 == 3:
            return random.choice(english_african_first) + ' ' + random.choice(english_african_sur) + '-' + random.choice(last_names), random.choices([USA, NGA], [1, 3], k=1)[0]
          else:
            return random.choice(english_african_first) + ' ' + random.choice(last_names) + '-' + random.choice(english_african_sur), random.choices([USA, NGA], [1, 3], k=1)[0]
        elif c3 == 2:
          return random.choice(first_names) + ' ' + random.choice(east_african_sur), random.choices([USA, CAM], [1, 1], k=1)[0]
        else:
          return random.choice(first_names) + ' ' + random.choice(southern_african_sur), random.choices([USA, DRC], [1, 1], k=1)[0]

    # east asian
    elif c == 5:
      c2 = random.choice(range(10))
      if c2 < 3:
        return random.choice(china_first) + ' ' + random.choice(china_sur), CHN
      elif c2 == 3:
        return random.choice(japan_first) + ' ' + random.choice(japan_sur), JPN
      elif c2 == 4:
        return random.choice(korea_first) + ' ' + random.choice(korea_sur), KOR
      elif c2 == 5:
        return random.choice(india_first) + ' ' + random.choice(india_sur), IND
      else:
        c3 = random.choice(range(6))
        if c3 < 3:
          return random.choice(first_names) + ' ' + random.choice(china_sur), random.choices([USA, CHN], [1, 1], k=1)[0]
        elif c3 == 3:
          return random.choice(first_names) + ' ' + random.choice(japan_sur), random.choices([USA, JPN], [1, 1], k=1)[0]
        elif c3 == 4:
          return random.choice(first_names) + ' ' + random.choice(korea_sur), random.choices([USA, KOR], [1, 1], k=1)[0]
        else:
          return random.choice(first_names) + ' ' + random.choice(india_sur), random.choices([USA, IND], [1, 1], k=1)[0]

    # hispanic
    elif c == 6:
      c2 = random.choice(range(6))
      if c2 < 3:
        return random.choice(sa_hisp_first) + ' ' + random.choice(sa_hisp_sur), random.choices([ARG, DOM, PUE, VEN, MEX, COL, URU, CHI], [15, 10, 7, 2, 3, 1, 1, 1], k=1)[0]
      elif c2 == 3:
        return random.choice(spain_first) + ' ' + random.choice(spain_sur), ESP
      else:
        c3 = random.choice(range(3))
        if c3 == 0:
          return random.choice(first_names) + ' ' + random.choice(spain_sur), random.choices([USA, ESP], [1, 1], k=1)[0]
        else:
          return random.choice(first_names) + ' ' + random.choice(sa_hisp_sur), random.choices([USA, ARG, DOM, PUE, VEN, MEX, COL, URU, CHI], [20, 15, 10, 7, 2, 3, 1, 1, 1], k=1)[0]

    # western european
    else:
      c2 = random.choice(range(10))
      if c2 < 1:
        return random.choice(scand_first) + ' ' + random.choice(scand_sur), random.choices([LAT, LTH, SWE, POL, FIN, DEN], [10, 15, 5, 5, 5, 1], k=1)[0]
      elif c2 < 3:
        return random.choice(french_first) + ' ' + random.choice(french_sur), random.choices([FRA, BEL, CAN], [50, 7, 10], k=1)[0]
      elif c2 < 5:
        return random.choice(german_first) + ' ' + random.choice(german_sur), random.choices([GER, LAT, LTH, POL], [50, 10, 10, 5], k=1)[0]
      elif c2 < 7:
        return random.choice(italian_first) + ' ' + random.choice(italian_sur), ITA
      elif c2 < 8:
        return random.choice(portuguese_first) + ' ' + random.choice(portuguese_sur), random.choices([POR, BRA, ANG, CBV], [2, 18, 1, 1], k=1)[0]
      else:
        c3 = random.choice(range(5))
        if c3 == 0:
          return random.choice(first_names) + ' ' + random.choice(scand_sur), random.choices([USA, LAT, LTH, SWE, POL, FIN, DEN], [20, 10, 15, 5, 5, 5, 1], k=1)[0]
        elif c3 == 1:
          return random.choice(first_names) + ' ' + random.choice(french_sur), random.choices([USA, FRA, BEL, CAN], [20, 30, 7, 30], k=1)[0]
        elif c3 == 2:
          return random.choice(first_names) + ' ' + random.choice(german_sur), random.choices([USA, GER, LAT, LTH, POL], [20, 50, 10, 10, 5], k=1)[0]
        elif c3 == 3:
          return random.choice(first_names) + ' ' + random.choice(italian_sur), random.choices([USA, ITA], [1, 1], k=1)[0]
        else:
          return random.choice(first_names) + ' ' + random.choice(portuguese_sur), random.choices([USA, POR, BRA, ANG, CBV], [10, 2, 18, 1, 1], k=1)[0]
  else:
    return random.choice(first_names)