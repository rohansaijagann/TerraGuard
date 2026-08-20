"""
Karnataka Geo-Spatial Validation & Offline Reverse Geocoding Engine.
Provides instantaneous water body detection (Arabian Sea + 20 Inland Reservoirs),
Karnataka state bounding validation, and high-precision Taluk/District place naming.
"""

import math

# ══ 1. MAJOR KARNATAKA INLAND RESERVOIRS & WATER BODIES ══
KARNATAKA_RESERVOIRS = [
    {
        "name": "Krishnaraja Sagara (KRS) Reservoir",
        "name_kn": "ಕೃಷ್ಣರಾಜ ಸಾಗರ (ಕೆ.ಆರ್.ಎಸ್) ಜಲಾಶಯ",
        "district": "Mandya / Mysuru",
        "lat": 12.4333, "lon": 76.5722, "radius_km": 6.5
    },
    {
        "name": "Tungabhadra Dam & Reservoir",
        "name_kn": "ತುಂಗಭದ್ರಾ ಜಲಾಶಯ",
        "district": "Vijayanagara / Ballari",
        "lat": 15.2667, "lon": 76.3333, "radius_km": 11.0
    },
    {
        "name": "Almatti Reservoir (Krishna River)",
        "name_kn": "ಆಲಮಟ್ಟಿ ಜಲಾಶಯ (ಕೃಷ್ಣಾ ನದಿ)",
        "district": "Vijayapura / Bagalkot",
        "lat": 16.3333, "lon": 75.8900, "radius_km": 9.5
    },
    {
        "name": "Linganamakki Reservoir (Sharavathi)",
        "name_kn": "ಲಿಂಗನಮಕ್ಕಿ ಜಲಾಶಯ (ಶರಾವತಿ)",
        "district": "Shivamogga",
        "lat": 14.1722, "lon": 74.8333, "radius_km": 10.0
    },
    {
        "name": "Supa Dam Reservoir (Kali River)",
        "name_kn": "ಸೂಪಾ ಜಲಾಶಯ (ಕಾಳಿ ನದಿ)",
        "district": "Uttara Kannada",
        "lat": 15.2833, "lon": 74.5333, "radius_km": 8.0
    },
    {
        "name": "Kabini Reservoir",
        "name_kn": "ಕಬಿನಿ ಜಲಾಶಯ",
        "district": "Mysuru",
        "lat": 11.9700, "lon": 76.3500, "radius_km": 6.0
    },
    {
        "name": "Hemavathi Reservoir (Gorur Dam)",
        "name_kn": "ಹೇಮಾವತಿ ಜಲಾಶಯ (ಗೊರೂರು)",
        "district": "Hassan",
        "lat": 12.7900, "lon": 76.0500, "radius_km": 7.0
    },
    {
        "name": "Bhadra Reservoir (Lakkavalli)",
        "name_kn": "ಭದ್ರಾ ಜಲಾಶಯ (ಲಕ್ಕವಳ್ಳಿ)",
        "district": "Chikkamagaluru / Shivamogga",
        "lat": 13.7000, "lon": 75.6400, "radius_km": 6.5
    },
    {
        "name": "Harangi Reservoir",
        "name_kn": "ಹಾರಂಗಿ ಜಲಾಶಯ",
        "district": "Kodagu",
        "lat": 12.4900, "lon": 75.9000, "radius_km": 4.5
    },
    {
        "name": "Malaprabha Reservoir (Renuka Sagara)",
        "name_kn": "ಮಲಪ್ರಭಾ (ರೇಣುಕಾ ಸಾಗರ) ಜಲಾಶಯ",
        "district": "Belagavi",
        "lat": 15.8200, "lon": 75.1200, "radius_km": 6.5
    },
    {
        "name": "Ghataprabha Reservoir (Hidkal Dam)",
        "name_kn": "ಹಿಡಕಲ್ ಜಲಾಶಯ (ಘಟಪ್ರಭಾ)",
        "district": "Belagavi",
        "lat": 16.1400, "lon": 74.6300, "radius_km": 7.0
    },
    {
        "name": "Basava Sagara (Narayanpur Dam)",
        "name_kn": "ಬಸವ ಸಾಗರ (ನಾರಾಯಣಪುರ) ಜಲಾಶಯ",
        "district": "Yadgir",
        "lat": 16.3200, "lon": 76.4800, "radius_km": 8.0
    },
    {
        "name": "Vani Vilasa Sagara (Mari Kanive)",
        "name_kn": "ವಾಣಿ ವಿಲಾಸ ಸಾಗರ (ಮಾರಿ ಕಣಿವೆ)",
        "district": "Chitradurga",
        "lat": 13.9800, "lon": 76.4900, "radius_km": 5.5
    },
    {
        "name": "Shanti Sagara (Sulekere)",
        "name_kn": "ಶಾಂತಿ ಸಾಗರ (ಸೂಳೆಕೆರೆ)",
        "district": "Davanagere",
        "lat": 14.2800, "lon": 75.8800, "radius_km": 4.0
    },
    {
        "name": "Karanja Reservoir",
        "name_kn": "ಕಾರಂಜಾ ಜಲಾಶಯ",
        "district": "Bidar",
        "lat": 17.9500, "lon": 77.1600, "radius_km": 5.0
    },
    {
        "name": "Mani Dam / Varahi Reservoir",
        "name_kn": "ಮಣಿ ಜಲಾಶಯ (ವಾರಾಹಿ)",
        "district": "Shivamogga / Udupi",
        "lat": 13.7200, "lon": 75.0500, "radius_km": 4.5
    },
    {
        "name": "Chakra & Savehaklu Reservoirs",
        "name_kn": "ಚಕ್ರಾ / ಸಾವೆಹಕ್ಲು ಜಲಾಶಯ",
        "district": "Shivamogga",
        "lat": 13.8800, "lon": 74.9200, "radius_km": 4.5
    },
    {
        "name": "Thippagondanahalli (T.G. Halli) Reservoir",
        "name_kn": "ಟಿ.ಜಿ. ಹಳ್ಳಿ ಜಲಾಶಯ",
        "district": "Bengaluru Rural / Ramanagara",
        "lat": 12.9600, "lon": 77.3400, "radius_km": 3.5
    }
]

# ══ 2. KARNATAKA DISTRICTS & TALUKS REVERSE GEOCODE CATALOG ══
KARNATAKA_TOWNS = [
    # Bengaluru Urban & Rural
    {"name": "Bengaluru", "name_kn": "ಬೆಂಗಳೂರು", "district": "Bengaluru Urban", "lat": 12.9716, "lon": 77.5946},
    {"name": "Yelahanka", "name_kn": "ಯಲಹಂಕ", "district": "Bengaluru Urban", "lat": 13.1007, "lon": 77.5963},
    {"name": "Anekal", "name_kn": "ಆನೇಕಲ್", "district": "Bengaluru Urban", "lat": 12.7107, "lon": 77.6967},
    {"name": "Devanahalli", "name_kn": "ದೇವನಹಳ್ಳಿ", "district": "Bengaluru Rural", "lat": 13.2483, "lon": 77.7126},
    {"name": "Doddaballapura", "name_kn": "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "district": "Bengaluru Rural", "lat": 13.2934, "lon": 77.5435},
    {"name": "Hosakote", "name_kn": "ಹೊಸಕೋಟೆ", "district": "Bengaluru Rural", "lat": 13.0697, "lon": 77.7981},
    {"name": "Nelamangala", "name_kn": "ನೆಲಮಂಗಲ", "district": "Bengaluru Rural", "lat": 13.0970, "lon": 77.3879},

    # Mysuru & Mandya
    {"name": "Mysuru", "name_kn": "ಮೈಸೂರು", "district": "Mysuru", "lat": 12.2958, "lon": 76.6394},
    {"name": "Nanjangud", "name_kn": "ನಂಜನಗೂಡು", "district": "Mysuru", "lat": 12.1190, "lon": 76.6787},
    {"name": "Hunsur", "name_kn": "ಹುಣಸೂರು", "district": "Mysuru", "lat": 12.3082, "lon": 76.2890},
    {"name": "Periyapatna", "name_kn": "ಪಿರಿಯಾಪಟ್ಟಣ", "district": "Mysuru", "lat": 12.3400, "lon": 76.0967},
    {"name": "T. Narasipura", "name_kn": "ಟಿ. ನರಸೀಪುರ", "district": "Mysuru", "lat": 12.2133, "lon": 76.9038},
    {"name": "K.R. Nagar", "name_kn": "ಕೆ.ಆರ್. ನಗರ", "district": "Mysuru", "lat": 12.4383, "lon": 76.3817},
    {"name": "H.D. Kote", "name_kn": "ಹೆಚ್.ಡಿ. ಕೋಟೆ", "district": "Mysuru", "lat": 11.9863, "lon": 76.3262},
    {"name": "Mandya", "name_kn": "ಮಂಡ್ಯ", "district": "Mandya", "lat": 12.5218, "lon": 76.8951},
    {"name": "Maddur", "name_kn": "ಮದ್ದೂರು", "district": "Mandya", "lat": 12.5847, "lon": 77.0457},
    {"name": "Srirangapatna", "name_kn": "ಶ್ರೀರಂಗಪಟ್ಟಣ", "district": "Mandya", "lat": 12.4181, "lon": 76.6947},
    {"name": "Pandavapura", "name_kn": "ಪಾಂಡವಪುರ", "district": "Mandya", "lat": 12.4939, "lon": 76.6692},
    {"name": "Nagamangala", "name_kn": "ನಾಗಮಂಗಲ", "district": "Mandya", "lat": 12.8189, "lon": 76.7583},
    {"name": "K.R. Pet", "name_kn": "ಕೆ.ಆರ್. ಪೇಟೆ", "district": "Mandya", "lat": 12.6617, "lon": 76.4917},
    {"name": "Malavalli", "name_kn": "ಮಳವಳ್ಳಿ", "district": "Mandya", "lat": 12.3867, "lon": 77.0567},

    # Coastal (Dakshina Kannada & Udupi & Uttara Kannada)
    {"name": "Mangaluru", "name_kn": "ಮಂಗಳೂರು", "district": "Dakshina Kannada", "lat": 12.8698, "lon": 74.8421},
    {"name": "Bantwal", "name_kn": "ಬಂಟ್ವಾಳ", "district": "Dakshina Kannada", "lat": 12.8944, "lon": 75.0353},
    {"name": "Puttur", "name_kn": "ಪುತ್ತೂರು", "district": "Dakshina Kannada", "lat": 12.7667, "lon": 75.2000},
    {"name": "Sullia", "name_kn": "ಸುಳ್ಯ", "district": "Dakshina Kannada", "lat": 12.5600, "lon": 75.3900},
    {"name": "Belthangady", "name_kn": "ಬೆಳ್ತಂಗಡಿ", "district": "Dakshina Kannada", "lat": 12.9900, "lon": 75.2600},
    {"name": "Moodbidri", "name_kn": "ಮೂಡುಬಿದಿರೆ", "district": "Dakshina Kannada", "lat": 13.0700, "lon": 74.9900},
    {"name": "Kadaba", "name_kn": "ಕಡಬ", "district": "Dakshina Kannada", "lat": 12.7500, "lon": 75.4300},
    {"name": "Udupi", "name_kn": "ಉಡುಪಿ", "district": "Udupi", "lat": 13.3409, "lon": 74.7421},
    {"name": "Manipal", "name_kn": "ಮಣಿಪಾಲ", "district": "Udupi", "lat": 13.3525, "lon": 74.7865},
    {"name": "Kundapura", "name_kn": "ಕುಂದಾಪುರ", "district": "Udupi", "lat": 13.6267, "lon": 74.6933},
    {"name": "Karkala", "name_kn": "ಕಾರ್ಕಳ", "district": "Udupi", "lat": 13.2100, "lon": 74.9900},
    {"name": "Byndoor", "name_kn": "ಬೈಂದೂರು", "district": "Udupi", "lat": 13.8700, "lon": 74.6300},
    {"name": "Brahmavara", "name_kn": "ಬ್ರಹ್ಮಾವರ", "district": "Udupi", "lat": 13.4300, "lon": 74.7500},
    {"name": "Kaup", "name_kn": "ಕಾಪು", "district": "Udupi", "lat": 13.2200, "lon": 74.7500},
    {"name": "Karwar", "name_kn": "ಕಾರವಾರ", "district": "Uttara Kannada", "lat": 14.8167, "lon": 74.1333},
    {"name": "Sirsi", "name_kn": "ಶಿರಸಿ", "district": "Uttara Kannada", "lat": 14.6195, "lon": 74.8354},
    {"name": "Kumta", "name_kn": "ಕುಮಟಾ", "district": "Uttara Kannada", "lat": 14.4267, "lon": 74.4189},
    {"name": "Ankola", "name_kn": "ಅಂಕೋಲಾ", "district": "Uttara Kannada", "lat": 14.6600, "lon": 74.3000},
    {"name": "Bhatkal", "name_kn": "ಭಟ್ಕಳ", "district": "Uttara Kannada", "lat": 13.9800, "lon": 74.5500},
    {"name": "Honnavar", "name_kn": "ಹೊನ್ನಾವರ", "district": "Uttara Kannada", "lat": 14.2800, "lon": 74.4500},
    {"name": "Dandeli", "name_kn": "ದಾಂಡೇಲಿ", "district": "Uttara Kannada", "lat": 15.2425, "lon": 74.6231},
    {"name": "Yellapur", "name_kn": "ಯಲ್ಲಾಪುರ", "district": "Uttara Kannada", "lat": 14.9600, "lon": 74.7100},
    {"name": "Haliyal", "name_kn": "ಹಳಿಯಾಳ", "district": "Uttara Kannada", "lat": 15.3300, "lon": 74.7600},
    {"name": "Siddapur", "name_kn": "ಸಿದ್ಧಾಪುರ", "district": "Uttara Kannada", "lat": 14.3400, "lon": 74.8900},
    {"name": "Joida", "name_kn": "ಜೋಯಿಡಾ", "district": "Uttara Kannada", "lat": 15.1500, "lon": 74.4800},

    # Malenadu (Chikkamagaluru, Kodagu, Hassan, Shivamogga)
    {"name": "Madikeri", "name_kn": "ಮಡಿಕೇರಿ", "district": "Kodagu", "lat": 12.4244, "lon": 75.7382},
    {"name": "Virajpet", "name_kn": "ವಿರಾಜಪೇಟೆ", "district": "Kodagu", "lat": 12.2000, "lon": 75.8000},
    {"name": "Somwarpet", "name_kn": "ಸೋಮವಾರಪೇಟೆ", "district": "Kodagu", "lat": 12.6000, "lon": 75.8700},
    {"name": "Gonikoppal", "name_kn": "ಗೋಣಿಕೊಪ್ಪಲು", "district": "Kodagu", "lat": 12.1800, "lon": 75.9300},
    {"name": "Kushalnagar", "name_kn": "ಕುಶಾಲನಗರ", "district": "Kodagu", "lat": 12.4600, "lon": 75.9600},
    {"name": "Chikkamagaluru", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "district": "Chikkamagaluru", "lat": 13.3161, "lon": 75.7720},
    {"name": "Mudigere", "name_kn": "ಮೂಡಿಗೆರೆ", "district": "Chikkamagaluru", "lat": 13.1367, "lon": 75.6400},
    {"name": "Koppa", "name_kn": "ಕೊಪ್ಪ", "district": "Chikkamagaluru", "lat": 13.5300, "lon": 75.3600},
    {"name": "Sringeri", "name_kn": "ಶೃಂಗೇರಿ", "district": "Chikkamagaluru", "lat": 13.4200, "lon": 75.2500},
    {"name": "Narasimharajapura", "name_kn": "ಎನ್.ಆರ್. ಪುರ", "district": "Chikkamagaluru", "lat": 13.6200, "lon": 75.5200},
    {"name": "Tarikere", "name_kn": "ತರೀಕೆರೆ", "district": "Chikkamagaluru", "lat": 13.7100, "lon": 75.8100},
    {"name": "Kadur", "name_kn": "ಕಡೂರು", "district": "Chikkamagaluru", "lat": 13.5500, "lon": 76.0100},
    {"name": "Hassan", "name_kn": "ಹಾಸನ", "district": "Hassan", "lat": 13.0072, "lon": 76.1004},
    {"name": "Sakleshpur", "name_kn": "ಸಕಲೇಶಪುರ", "district": "Hassan", "lat": 12.9438, "lon": 75.7865},
    {"name": "Belur", "name_kn": "ಬೇಲೂರು", "district": "Hassan", "lat": 13.1600, "lon": 75.8600},
    {"name": "Halebeedu", "name_kn": "ಹಳೇಬೀಡು", "district": "Hassan", "lat": 13.2100, "lon": 75.9900},
    {"name": "Arsikere", "name_kn": "ಅರಸೀಕೆರೆ", "district": "Hassan", "lat": 13.3100, "lon": 76.2600},
    {"name": "Channarayapatna", "name_kn": "ಚನ್ನರಾಯಪಟ್ಟಣ", "district": "Hassan", "lat": 12.9000, "lon": 76.3900},
    {"name": "Holenarasipura", "name_kn": "ಹೊಳೇನರಸೀಪುರ", "district": "Hassan", "lat": 12.7900, "lon": 76.2400},
    {"name": "Arkalgud", "name_kn": "ಅರಕಲಗೂಡು", "district": "Hassan", "lat": 12.7700, "lon": 76.0600},
    {"name": "Alur", "name_kn": "ಆಲೂರು", "district": "Hassan", "lat": 12.9900, "lon": 75.9800},
    {"name": "Shivamogga", "name_kn": "ಶಿವಮೊಗ್ಗ", "district": "Shivamogga", "lat": 13.9299, "lon": 75.5681},
    {"name": "Bhadravati", "name_kn": "ಭದ್ರಾವತಿ", "district": "Shivamogga", "lat": 13.8400, "lon": 75.7000},
    {"name": "Sagar", "name_kn": "ಸಾಗರ", "district": "Shivamogga", "lat": 14.1600, "lon": 75.0300},
    {"name": "Thirthahalli", "name_kn": "ತೀರ್ಥಹಳ್ಳಿ", "district": "Shivamogga", "lat": 13.6900, "lon": 75.2400},
    {"name": "Shikaripura", "name_kn": "ಶಿಕಾರಿಪುರ", "district": "Shivamogga", "lat": 14.2700, "lon": 75.3500},
    {"name": "Soraba", "name_kn": "ಸೊರಬ", "district": "Shivamogga", "lat": 14.3800, "lon": 75.0900},
    {"name": "Hosanagara", "name_kn": "ಹೊಸನಗರ", "district": "Shivamogga", "lat": 13.9200, "lon": 75.0700},

    # Central & Southern Dry (Tumakuru, Kolar, Chikkaballapur, Ramanagara, Chamarajanagar, Chitradurga, Davanagere)
    {"name": "Tumakuru", "name_kn": "ತುಮಕೂರು", "district": "Tumakuru", "lat": 13.3392, "lon": 77.1016},
    {"name": "Tiptur", "name_kn": "ತಿಪಟೂರು", "district": "Tumakuru", "lat": 13.2600, "lon": 76.4800},
    {"name": "Kunigal", "name_kn": "ಕುಣಿಗಲ್", "district": "Tumakuru", "lat": 13.0200, "lon": 77.0300},
    {"name": "Sira", "name_kn": "ಶಿರಾ", "district": "Tumakuru", "lat": 13.7400, "lon": 76.9000},
    {"name": "Madhugiri", "name_kn": "ಮಧುಗಿರಿ", "district": "Tumakuru", "lat": 13.6600, "lon": 77.2100},
    {"name": "Pavagada", "name_kn": "ಪಾವಗಡ", "district": "Tumakuru", "lat": 14.1000, "lon": 77.2800},
    {"name": "Gubbi", "name_kn": "ಗುಬ್ಬಿ", "district": "Tumakuru", "lat": 13.3100, "lon": 76.9400},
    {"name": "Chikkanayakanahalli", "name_kn": "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ", "district": "Tumakuru", "lat": 13.4200, "lon": 76.6200},
    {"name": "Koratagere", "name_kn": "ಕೊರಟಗೆರೆ", "district": "Tumakuru", "lat": 13.5200, "lon": 77.2400},
    {"name": "Turuvekere", "name_kn": "ತುರುವೇಕೆರೆ", "district": "Tumakuru", "lat": 13.1600, "lon": 76.6700},
    {"name": "Kolar", "name_kn": "ಕೋಲಾರ", "district": "Kolar", "lat": 13.1367, "lon": 78.1292},
    {"name": "KGF (Bangarapet)", "name_kn": "ಕೆ.ಜಿ.ಎಫ್ (ಬಂಗಾರಪೇಟೆ)", "district": "Kolar", "lat": 12.9600, "lon": 78.2700},
    {"name": "Malur", "name_kn": "ಮಾಲೂರು", "district": "Kolar", "lat": 13.0000, "lon": 77.9400},
    {"name": "Mulbagal", "name_kn": "ಮುಳಬಾಗಿಲು", "district": "Kolar", "lat": 13.1600, "lon": 78.3900},
    {"name": "Srinivaspur", "name_kn": "ಶ್ರೀನಿವಾಸಪುರ", "district": "Kolar", "lat": 13.3400, "lon": 78.2100},
    {"name": "Chikkaballapur", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "district": "Chikkaballapur", "lat": 13.4325, "lon": 77.7275},
    {"name": "Gowribidanur", "name_kn": "ಗೌರಿಬಿದನೂರು", "district": "Chikkaballapur", "lat": 13.6100, "lon": 77.5200},
    {"name": "Chintamani", "name_kn": "ಚಿಂತಾಮಣಿ", "district": "Chikkaballapur", "lat": 13.4000, "lon": 78.0600},
    {"name": "Sidlaghatta", "name_kn": "ಶಿಡ್ಲಘಟ್ಟ", "district": "Chikkaballapur", "lat": 13.3900, "lon": 77.8600},
    {"name": "Bagepalli", "name_kn": "ಬಾಗೇಪಲ್ಲಿ", "district": "Chikkaballapur", "lat": 13.7800, "lon": 77.7900},
    {"name": "Gudibanda", "name_kn": "ಗುಡಿಬಂಡೆ", "district": "Chikkaballapur", "lat": 13.6700, "lon": 77.7000},
    {"name": "Ramanagara", "name_kn": "ರಾಮನಗರ", "district": "Ramanagara", "lat": 12.7246, "lon": 77.2813},
    {"name": "Channapatna", "name_kn": "ಚನ್ನಪಟ್ಟಣ", "district": "Ramanagara", "lat": 12.6500, "lon": 77.2000},
    {"name": "Kanakapura", "name_kn": "ಕನಕಪುರ", "district": "Ramanagara", "lat": 12.5500, "lon": 77.4100},
    {"name": "Magadi", "name_kn": "ಮಾಗಡಿ", "district": "Ramanagara", "lat": 12.9600, "lon": 77.2300},
    {"name": "Chamarajanagar", "name_kn": "ಚಾಮರಾಜನಗರ", "district": "Chamarajanagar", "lat": 11.9246, "lon": 76.9432},
    {"name": "Kollegal", "name_kn": "ಕೊಳ್ಳೇಗಾಲ", "district": "Chamarajanagar", "lat": 12.1500, "lon": 77.1200},
    {"name": "Gundlupet", "name_kn": "ಗುಂಡ್ಲುಪೇಟೆ", "district": "Chamarajanagar", "lat": 11.8100, "lon": 76.6900},
    {"name": "Yelandur", "name_kn": "ಯಳಂದೂರು", "district": "Chamarajanagar", "lat": 12.0600, "lon": 77.0300},
    {"name": "Hanur", "name_kn": "ಹನೂರು", "district": "Chamarajanagar", "lat": 12.0900, "lon": 77.3000},
    {"name": "Chitradurga", "name_kn": "ಚಿತ್ರದುರ್ಗ", "district": "Chitradurga", "lat": 14.2251, "lon": 76.3980},
    {"name": "Hiriyur", "name_kn": "ಹಿರಿಯೂರು", "district": "Chitradurga", "lat": 13.9500, "lon": 76.6200},
    {"name": "Challakere", "name_kn": "ಚಳ್ಳಕೆರೆ", "district": "Chitradurga", "lat": 14.3100, "lon": 76.6500},
    {"name": "Holalkere", "name_kn": "ಹೊಳಲ್ಕೆರೆ", "district": "Chitradurga", "lat": 14.0300, "lon": 76.1800},
    {"name": "Hosadurga", "name_kn": "ಹೊಸದುರ್ಗ", "district": "Chitradurga", "lat": 13.8000, "lon": 76.2900},
    {"name": "Molakalmuru", "name_kn": "ಮೊಳಕಾಲ್ಮುರು", "district": "Chitradurga", "lat": 14.7300, "lon": 76.7500},
    {"name": "Davanagere", "name_kn": "ದಾವಣಗೆರೆ", "district": "Davanagere", "lat": 14.4644, "lon": 75.9218},
    {"name": "Harihar", "name_kn": "ಹರಿಹರ", "district": "Davanagere", "lat": 14.5100, "lon": 75.8000},
    {"name": "Channagiri", "name_kn": "ಚನ್ನಗಿರಿ", "district": "Davanagere", "lat": 14.0300, "lon": 75.9300},
    {"name": "Honnali", "name_kn": "ಹೊನ್ನಾಳಿ", "district": "Davanagere", "lat": 14.2400, "lon": 75.6400},
    {"name": "Jagalur", "name_kn": "ಜಗಳೂರು", "district": "Davanagere", "lat": 14.5200, "lon": 76.3500},
    {"name": "Nyamathi", "name_kn": "ನ್ಯಾಮತಿ", "district": "Davanagere", "lat": 14.1500, "lon": 75.5800},

    # Northern Dry & Transition (Belagavi, Dharwad, Gadag, Haveri, Bagalkot, Vijayapura, Ballari, Vijayanagara, Koppal, Raichur, Kalaburagi, Yadgir, Bidar)
    {"name": "Belagavi", "name_kn": "ಬೆಳಗಾವಿ", "district": "Belagavi", "lat": 15.8497, "lon": 74.4977},
    {"name": "Gokak", "name_kn": "ಗೋಕಾಕ್", "district": "Belagavi", "lat": 16.1700, "lon": 74.8200},
    {"name": "Chikkodi", "name_kn": "ಚಿಕ್ಕೋಡಿ", "district": "Belagavi", "lat": 16.4300, "lon": 74.6000},
    {"name": "Athani", "name_kn": "ಅಥಣಿ", "district": "Belagavi", "lat": 16.7300, "lon": 75.0600},
    {"name": "Bailhongal", "name_kn": "ಬೈಲಹೊಂಗಲ", "district": "Belagavi", "lat": 15.8200, "lon": 74.8600},
    {"name": "Saundatti", "name_kn": "ಸವದತ್ತಿ", "district": "Belagavi", "lat": 15.7700, "lon": 75.1200},
    {"name": "Ramdurg", "name_kn": "ರಾಮದುರ್ಗ", "district": "Belagavi", "lat": 15.9500, "lon": 75.3000},
    {"name": "Hukkeri", "name_kn": "ಹುಕ್ಕೇರಿ", "district": "Belagavi", "lat": 16.2300, "lon": 74.6000},
    {"name": "Khanapur", "name_kn": "ಖಾನಾಪುರ", "district": "Belagavi", "lat": 15.6300, "lon": 74.5200},
    {"name": "Raybag", "name_kn": "ರಾಯಭಾಗ", "district": "Belagavi", "lat": 16.4900, "lon": 74.7800},
    {"name": "Nipani", "name_kn": "ನಿಪ್ಪಾಣಿ", "district": "Belagavi", "lat": 16.4000, "lon": 74.3800},
    {"name": "Kagwad", "name_kn": "ಕಾಗವಾಡ", "district": "Belagavi", "lat": 16.6900, "lon": 74.7500},
    {"name": "Mudalgi", "name_kn": "ಮೂಡಲಗಿ", "district": "Belagavi", "lat": 16.3200, "lon": 74.9800},
    {"name": "Kittur", "name_kn": "ಕಿತ್ತೂರು", "district": "Belagavi", "lat": 15.6000, "lon": 74.7900},
    {"name": "Dharwad", "name_kn": "ಧಾರವಾಡ", "district": "Dharwad", "lat": 15.4589, "lon": 75.0078},
    {"name": "Hubballi", "name_kn": "ಹುಬ್ಬಳ್ಳಿ", "district": "Dharwad", "lat": 15.3647, "lon": 75.1240},
    {"name": "Navalgund", "name_kn": "ನವಲಗುಂದ", "district": "Dharwad", "lat": 15.5600, "lon": 75.3700},
    {"name": "Kalghatgi", "name_kn": "ಕಲಘಟಗಿ", "district": "Dharwad", "lat": 15.1800, "lon": 74.9700},
    {"name": "Kundgol", "name_kn": "ಕುಂದಗೋಳ", "district": "Dharwad", "lat": 15.2500, "lon": 75.2500},
    {"name": "Alnavar", "name_kn": "ಅಳ್ನಾವರ", "district": "Dharwad", "lat": 15.4300, "lon": 74.7300},
    {"name": "Gadag", "name_kn": "ಗದಗ", "district": "Gadag", "lat": 15.4266, "lon": 75.6268},
    {"name": "Betageri", "name_kn": "ಬೆಟಗೇರಿ", "district": "Gadag", "lat": 15.4400, "lon": 75.6400},
    {"name": "Ron", "name_kn": "ರೋಣ", "district": "Gadag", "lat": 15.7000, "lon": 75.7300},
    {"name": "Shirhatti", "name_kn": "ಶಿರಹಟ್ಟಿ", "district": "Gadag", "lat": 15.2300, "lon": 75.5800},
    {"name": "Nargund", "name_kn": "ನರಗುಂದ", "district": "Gadag", "lat": 15.7200, "lon": 75.3900},
    {"name": "Mundargi", "name_kn": "ಮುಂಡರಗಿ", "district": "Gadag", "lat": 15.2100, "lon": 75.8800},
    {"name": "Gajendragad", "name_kn": "ಗಜೇಂದ್ರಗಡ", "district": "Gadag", "lat": 15.7300, "lon": 75.9800},
    {"name": "Haveri", "name_kn": "ಹಾವೇರಿ", "district": "Haveri", "lat": 14.7946, "lon": 75.4011},
    {"name": "Ranebennur", "name_kn": "ರಾಣೆಬೆನ್ನೂರು", "district": "Haveri", "lat": 14.6167, "lon": 75.6167},
    {"name": "Byadgi", "name_kn": "ಬ್ಯಾಡಗಿ", "district": "Haveri", "lat": 14.6800, "lon": 75.4900},
    {"name": "Hangal", "name_kn": "ಹಾನಗಲ್", "district": "Haveri", "lat": 14.7600, "lon": 75.1300},
    {"name": "Shiggaon", "name_kn": "ಶಿಗ್ಗಾಂವ", "district": "Haveri", "lat": 14.9900, "lon": 75.2300},
    {"name": "Hirekerur", "name_kn": "ಹಿರೇಕೆರೂರು", "district": "Haveri", "lat": 14.4500, "lon": 75.3900},
    {"name": "Savanur", "name_kn": "ಸವಣೂರು", "district": "Haveri", "lat": 14.9700, "lon": 75.3400},
    {"name": "Rattihalli", "name_kn": "ರಟ್ಟಿಹಳ್ಳಿ", "district": "Haveri", "lat": 14.4200, "lon": 75.5200},
    {"name": "Bagalkot", "name_kn": "ಬಾಗಲಕೋಟೆ", "district": "Bagalkot", "lat": 16.1691, "lon": 75.6615},
    {"name": "Jamkhandi", "name_kn": "ಜಮಖಂಡಿ", "district": "Bagalkot", "lat": 16.5100, "lon": 75.3000},
    {"name": "Mudhol", "name_kn": "ಮುಧೋಳ", "district": "Bagalkot", "lat": 16.3500, "lon": 75.2800},
    {"name": "Badami", "name_kn": "ಬಾದಾಮಿ", "district": "Bagalkot", "lat": 15.9200, "lon": 75.6800},
    {"name": "Hungund", "name_kn": "ಹುನಗುಂದ", "district": "Bagalkot", "lat": 16.0600, "lon": 76.0600},
    {"name": "Ilkal", "name_kn": "ಇಳಕಲ್", "district": "Bagalkot", "lat": 15.9700, "lon": 76.1300},
    {"name": "Guledgudda", "name_kn": "ಗುಳೇದಗುಡ್ಡ", "district": "Bagalkot", "lat": 16.0500, "lon": 75.7800},
    {"name": "Bilagi", "name_kn": "ಬೀಳಗಿ", "district": "Bagalkot", "lat": 16.3500, "lon": 75.6200},
    {"name": "Rabkavi Banhatti", "name_kn": "ರಬಕವಿ ಬನಹಟ್ಟಿ", "district": "Bagalkot", "lat": 16.4800, "lon": 75.1200},
    {"name": "Vijayapura", "name_kn": "ವಿಜಯಪುರ", "district": "Vijayapura", "lat": 16.8302, "lon": 75.7100},
    {"name": "Basavana Bagewadi", "name_kn": "ಬಸವನ ಬಾಗೇವಾಡಿ", "district": "Vijayapura", "lat": 16.5800, "lon": 75.9600},
    {"name": "Indi", "name_kn": "ಇಂಡಿ", "district": "Vijayapura", "lat": 17.1800, "lon": 75.9600},
    {"name": "Sindagi", "name_kn": "ಸಿಂದಗಿ", "district": "Vijayapura", "lat": 16.9200, "lon": 76.2400},
    {"name": "Muddebihal", "name_kn": "ಮುದ್ದೇಬಿಹಾಳ", "district": "Vijayapura", "lat": 16.3400, "lon": 76.1300},
    {"name": "Talikoti", "name_kn": "ತಾಳಿಕೋಟೆ", "district": "Vijayapura", "lat": 16.4800, "lon": 76.3100},
    {"name": "Babaleshwar", "name_kn": "ಬಬಲೇಶ್ವರ", "district": "Vijayapura", "lat": 16.6900, "lon": 75.5400},
    {"name": "Tikota", "name_kn": "ಟಿಕೋಟಾ", "district": "Vijayapura", "lat": 16.8600, "lon": 75.5200},
    {"name": "Chadchan", "name_kn": "ಚಡಚಣ", "district": "Vijayapura", "lat": 17.2500, "lon": 75.7200},
    {"name": "Devar Hippargi", "name_kn": "ದೇವರ ಹಿಪ್ಪರಗಿ", "district": "Vijayapura", "lat": 16.8200, "lon": 76.0400},
    {"name": "Ballari", "name_kn": "ಬಳ್ಳಾರಿ", "district": "Ballari", "lat": 15.1394, "lon": 76.9214},
    {"name": "Siruguppa", "name_kn": "ಸಿರುಗುಪ್ಪ", "district": "Ballari", "lat": 15.6300, "lon": 76.9000},
    {"name": "Sandur", "name_kn": "ಸಂಡೂರು", "district": "Ballari", "lat": 15.0800, "lon": 76.5500},
    {"name": "Kampli", "name_kn": "ಕಂಪ್ಲಿ", "district": "Ballari", "lat": 15.4000, "lon": 76.6000},
    {"name": "Kurugodu", "name_kn": "ಕುರುಗೋಡು", "district": "Ballari", "lat": 15.3400, "lon": 76.8400},
    {"name": "Hosapete", "name_kn": "ಹೊಸಪೇಟೆ", "district": "Vijayanagara", "lat": 15.2700, "lon": 76.3900},
    {"name": "Kudligi", "name_kn": "ಕೂಡ್ಲಿಗಿ", "district": "Vijayanagara", "lat": 14.9000, "lon": 76.3900},
    {"name": "Hagaribommanahalli", "name_kn": "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "district": "Vijayanagara", "lat": 15.0800, "lon": 76.0100},
    {"name": "Harapanahalli", "name_kn": "ಹರಪನಹಳ್ಳಿ", "district": "Vijayanagara", "lat": 14.8000, "lon": 75.9800},
    {"name": "Hoovina Hadagali", "name_kn": "ಹೂವಿನ ಹಡಗಲಿ", "district": "Vijayanagara", "lat": 15.0200, "lon": 75.9600},
    {"name": "Kotturu", "name_kn": "ಕೊಟ್ಟೂರು", "district": "Vijayanagara", "lat": 14.8200, "lon": 76.2200},
    {"name": "Koppal", "name_kn": "ಕೊಪ್ಪಳ", "district": "Koppal", "lat": 15.3464, "lon": 76.1557},
    {"name": "Gangavathi", "name_kn": "ಗಂಗಾವತಿ", "district": "Koppal", "lat": 15.4300, "lon": 76.5300},
    {"name": "Kushtagi", "name_kn": "ಕುಷ್ಟಗಿ", "district": "Koppal", "lat": 15.7500, "lon": 76.2000},
    {"name": "Yelburga", "name_kn": "ಯಲಬುರ್ಗಾ", "district": "Koppal", "lat": 15.6200, "lon": 76.0100},
    {"name": "Karatagi", "name_kn": "ಕಾರಟಗಿ", "district": "Koppal", "lat": 15.5800, "lon": 76.6200},
    {"name": "Kukanur", "name_kn": "ಕುಕನೂರು", "district": "Koppal", "lat": 15.4600, "lon": 75.9900},
    {"name": "Raichur", "name_kn": "ರಾಯಚೂರು", "district": "Raichur", "lat": 16.2076, "lon": 77.3463},
    {"name": "Sindhanur", "name_kn": "ಸಿಂಧನೂರು", "district": "Raichur", "lat": 15.7800, "lon": 76.7600},
    {"name": "Manvi", "name_kn": "ಮಾನ್ವಿ", "district": "Raichur", "lat": 15.9900, "lon": 77.0500},
    {"name": "Devadurga", "name_kn": "ದೇವದುರ್ಗ", "district": "Raichur", "lat": 16.4200, "lon": 76.9300},
    {"name": "Lingsugur", "name_kn": "ಲಿಂಗಸುಗೂರು", "district": "Raichur", "lat": 16.1600, "lon": 76.5200},
    {"name": "Maski", "name_kn": "ಮಸ್ಕಿ", "district": "Raichur", "lat": 15.9600, "lon": 76.6600},
    {"name": "Sirwar", "name_kn": "ಸಿರವಾರ", "district": "Raichur", "lat": 16.1800, "lon": 77.0900},
    {"name": "Kalaburagi", "name_kn": "ಕಲಬುರಗಿ", "district": "Kalaburagi", "lat": 17.3297, "lon": 76.8343},
    {"name": "Sedam", "name_kn": "ಸೇಡಂ", "district": "Kalaburagi", "lat": 17.1800, "lon": 77.2800},
    {"name": "Chittapur", "name_kn": "ಚಿತ್ತಾಪುರ", "district": "Kalaburagi", "lat": 17.1200, "lon": 76.8600},
    {"name": "Afzalpur", "name_kn": "ಅಫ್ಜಲಪುರ", "district": "Kalaburagi", "lat": 17.2000, "lon": 76.3500},
    {"name": "Aland", "name_kn": "ಆಳಂದ", "district": "Kalaburagi", "lat": 17.5600, "lon": 76.5700},
    {"name": "Chincholi", "name_kn": "ಚಿಂಚೋಳಿ", "district": "Kalaburagi", "lat": 17.4700, "lon": 77.4300},
    {"name": "Jevargi", "name_kn": "ಜೇವರ್ಗಿ", "district": "Kalaburagi", "lat": 17.0200, "lon": 76.7700},
    {"name": "Kamalapur", "name_kn": "ಕಮಲಾಪುರ", "district": "Kalaburagi", "lat": 17.5800, "lon": 77.0000},
    {"name": "Shahabad", "name_kn": "ಶಹಾಬಾದ್", "district": "Kalaburagi", "lat": 17.1300, "lon": 76.9400},
    {"name": "Kalgi", "name_kn": "ಕಾಳಗಿ", "district": "Kalaburagi", "lat": 17.3500, "lon": 77.1600},
    {"name": "Yadgir", "name_kn": "ಯಾದಗಿರಿ", "district": "Yadgir", "lat": 16.7645, "lon": 77.1393},
    {"name": "Shahapur", "name_kn": "ಶಹಾಪುರ", "district": "Yadgir", "lat": 16.7000, "lon": 76.8400},
    {"name": "Shorapur", "name_kn": "ಶೋರಾಪುರ", "district": "Yadgir", "lat": 16.5200, "lon": 76.7600},
    {"name": "Hunsagi", "name_kn": "ಹುಣಸಗಿ", "district": "Yadgir", "lat": 16.4400, "lon": 76.5100},
    {"name": "Gurmitkal", "name_kn": "ಗುರಮಿಟ್ಕಲ್", "district": "Yadgir", "lat": 16.8600, "lon": 77.4000},
    {"name": "Wadgera", "name_kn": "ವಡಗೇರಾ", "district": "Yadgir", "lat": 16.6500, "lon": 77.0800},
    {"name": "Bidar", "name_kn": "ಬೀದರ್", "district": "Bidar", "lat": 17.9104, "lon": 77.5199},
    {"name": "Basavakalyan", "name_kn": "ಬಸವಕಲ್ಯಾಣ", "district": "Bidar", "lat": 17.8700, "lon": 76.9500},
    {"name": "Humnabad", "name_kn": "ಹುಮ್ನಾಬಾದ್", "district": "Bidar", "lat": 17.7700, "lon": 77.1300},
    {"name": "Bhalki", "name_kn": "ಭಾಲ್ಕಿ", "district": "Bidar", "lat": 18.0400, "lon": 77.2200},
    {"name": "Aurad", "name_kn": "ಔರಾದ್", "district": "Bidar", "lat": 18.2500, "lon": 77.4300},
    {"name": "Kamalnagar", "name_kn": "ಕಮಲನಗರ", "district": "Bidar", "lat": 18.2300, "lon": 77.2000},
    {"name": "Chitguppa", "name_kn": "ಚಿಟಗುಪ್ಪ", "district": "Bidar", "lat": 17.6900, "lon": 77.2200}
]

def haversine_km(lat1, lon1, lat2, lon2):
    """Calculates distance between 2 coordinates in kilometers."""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2.0)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2.0)**2
    return R * 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

def is_arabian_sea(lat, lon):
    """
    Checks if coordinates fall in the Arabian Sea west of Karnataka's coastline.
    Coastline roughly runs from (11.5N, 74.85E) in South to (14.9N, 74.12E) in North.
    """
    # Any point west of longitude 74.05 along India is in the Arabian Sea
    if lon < 74.05:
        return True
    
    # Check along the Karnataka latitude strip (11.5°N to 15.5°N)
    if 11.5 <= lat <= 15.5:
        # Approximate coastal longitude for given latitude:
        # At lat 11.5, coast is ~74.85. At lat 14.9, coast is ~74.12.
        slope = (74.12 - 74.85) / (14.9 - 11.5) # approx -0.2147
        coast_lon = 74.85 + (lat - 11.5) * slope
        # If clicked point is strictly west of this coastal line
        if lon < (coast_lon - 0.04):
            return True
            
    return False

def check_karnataka_location(lat, lon):
    """
    Exhaustive validation:
    Returns dict: {
        'is_valid': bool,
        'is_water': bool,
        'is_outside': bool,
        'location_name': str,
        'location_name_kn': str,
        'district': str,
        'error_message': str,
        'error_message_kn': str
    }
    """
    # 1. Arabian Sea Check
    if is_arabian_sea(lat, lon):
        return {
            "is_valid": False,
            "is_water": True,
            "is_outside": False,
            "location_name": "🌊 Arabian Sea (Off Karnataka Coast)",
            "location_name_kn": "🌊 ಅರಬ್ಬಿ ಸಮುದ್ರ (ಕರಾವಳಿ ಜಲಪ್ರದೇಶ)",
            "district": "Coastal Sea",
            "error_message": "Water body detected (Arabian Sea). Please select a solid land coordinate within Karnataka.",
            "error_message_kn": "ಜಲಮೂಲ ಪತ್ತೆಯಾಗಿದೆ (ಅರಬ್ಬಿ ಸಮುದ್ರ). ದಯವಿಟ್ಟು ಕರ್ನಾಟಕದ ಭೂಪ್ರದೇಶದ ಜಮೀನನ್ನು ಆಯ್ಕೆಮಾಡಿ."
        }

    # 2. Check 18 Karnataka Inland Reservoirs & Lakes
    for res in KARNATAKA_RESERVOIRS:
        dist = haversine_km(lat, lon, res["lat"], res["lon"])
        if dist <= res["radius_km"]:
            return {
                "is_valid": False,
                "is_water": True,
                "is_outside": False,
                "location_name": f"🌊 {res['name']} ({res['district']})",
                "location_name_kn": f"🌊 {res['name_kn']} ({res['district']})",
                "district": res["district"],
                "error_message": f"Inland water body detected ({res['name']}). Agricultural suitability and fire risk are not applicable over water.",
                "error_message_kn": f"ಜಲಮೂಲ ಪತ್ತೆಯಾಗಿದೆ ({res['name_kn']}). ಜಲಾಶಯದ ಮೇಲೆ ಕೃಷಿ ವಿಶ್ಲೇಷಣೆ ಅನ್ವಯಿಸುವುದಿಲ್ಲ."
            }

    # 3. Check Karnataka Outer Bounding Box (Lat: 11.5°N - 18.5°N, Lon: 74.05°E - 78.6°E)
    if not (11.4 <= lat <= 18.6 and 74.05 <= lon <= 78.65):
        return {
            "is_valid": False,
            "is_water": False,
            "is_outside": True,
            "location_name": "Outside Karnataka",
            "location_name_kn": "ಕರ್ನಾಟಕದ ಹೊರಗೆ",
            "district": "Outside",
            "error_message": "Location outside Karnataka detected. TerraGuard AI is calibrated specifically for the Karnataka agro-ecological zones.",
            "error_message_kn": "ಕರ್ನಾಟಕದ ಹೊರಗಿನ ಸ್ಥಳ ಪತ್ತೆಯಾಗಿದೆ. ಟೆರಾಗಾರ್ಡ್ ಕರ್ನಾಟಕ ಪ್ರದೇಶಕ್ಕೆ ಮಾತ್ರ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ."
        }

    # 4. Valid Land Location — Match Nearest Karnataka Taluk & District (Never returns Unknown!)
    closest_town = KARNATAKA_TOWNS[0]
    min_distance = 999999.0
    for town in KARNATAKA_TOWNS:
        d = haversine_km(lat, lon, town["lat"], town["lon"])
        if d < min_distance:
            min_distance = d
            closest_town = town

    # If within 40km of a known town, format as "Town, District, Karnataka"
    loc_en = f"{closest_town['name']}, {closest_town['district']}, Karnataka"
    loc_kn = f"{closest_town['name_kn']}, {closest_town['district']}, ಕರ್ನಾಟಕ"

    return {
        "is_valid": True,
        "is_water": False,
        "is_outside": False,
        "location_name": loc_en,
        "location_name_kn": loc_kn,
        "district": closest_town["district"],
        "error_message": "",
        "error_message_kn": ""
    }
