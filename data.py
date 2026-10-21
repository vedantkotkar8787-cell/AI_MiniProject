def load_books():
    return [
        # ==========================================
        # SCI-FI / FANTASY (13 Books)
        # ==========================================
        {
            "title": "Dune",
            "author": "Frank Herbert",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.7,
            "description": "An epic adventure on the desert planet Arrakis blending politics, religion, and ecology."
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Adventurous",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "Bilbo Baggins is whisked away into an epic quest to reclaim the lost Dwarf Kingdom of Erebor."
        },
        {
            "title": "Project Hail Mary",
            "author": "Andy Weir",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thrilling & Fast-paced",
            "length": "Long (>400 pages)",
            "rating": 4.9,
            "description": "A lone astronaut must save Earth from an extinction-level threat in this science-packed thriller."
        },
        {
            "title": "The Name of the Wind",
            "author": "Patrick Rothfuss",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Adventurous",
            "length": "Long (>400 pages)",
            "rating": 4.8,
            "description": "The tale of Kvothe from his childhood in a troupe of traveling players to his years as a notorious wizard."
        },
        {
            "title": "The Hitchhiker's Guide to the Galaxy",
            "author": "Douglas Adams",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Lighthearted & Fun",
            "length": "Short (<200 pages)",
            "rating": 4.5,
            "description": "A hilarious sci-fi comedy following Arthur Dent across the cosmos after Earth is demolished."
        },
        {
            "title": "Foundation",
            "author": "Isaac Asimov",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.6,
            "description": "Dr. Hari Seldon foresees the fall of the Galactic Empire and creates a foundation to save human knowledge."
        },
        {
            "title": "The Way of Kings",
            "author": "Brandon Sanderson",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Adventurous",
            "length": "Long (>400 pages)",
            "rating": 4.9,
            "description": "Epic fantasy masterpiece set on a world battered by violent storms and ancient conflicts."
        },
        {
            "title": "All Systems Red",
            "author": "Martha Wells",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thrilling & Fast-paced",
            "length": "Short (<200 pages)",
            "rating": 4.5,
            "description": "A grumpy, self-hacking security android who just wants to watch soap operas has to protect human clients."
        },
        {
            "title": "The Martian",
            "author": "Andy Weir",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "An astronaut stranded on Mars must use his ingenuity and scientific wit to survive."
        },
        {
            "title": "Hyperion",
            "author": "Dan Simmons",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.6,
            "description": "Seven pilgrims share their haunting tales as they journey toward a terrifying entity known as the Shrike."
        },
        {
            "title": "Red Rising",
            "author": "Pierce Brown",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.7,
            "description": "A wronged man infiltrates the ruling caste of a futuristic color-coded Mars society to seek bloody vengeance."
        },
        {
            "title": "American Gods",
            "author": "Neil Gaiman",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.4,
            "description": "Ex-con Shadow Moon finds himself caught in a brewing war between ancient mythological gods and modern tech deities."
        },
        {
            "title": "The Long Way to a Small, Angry Planet",
            "author": "Becky Chambers",
            "genre": "Sci-Fi / Fantasy",
            "mood": "Lighthearted & Fun",
            "length": "Medium (200-400 pages)",
            "rating": 4.5,
            "description": "A diverse, lovable crew aboard a tunneling spaceship embarks on an exciting multi-year interstellar journey."
        },

        # ==========================================
        # MOTIVATION & MINDSET (15 Books)
        # ==========================================
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "A practical framework for improving every day through tiny, consistent habit changes."
        },
        {
            "title": "Can't Hurt Me",
            "author": "David Goggins",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "Demonstrates how mastering your mind and pushing past pain unlocks true human potential."
        },
        {
            "title": "Make Your Bed",
            "author": "William H. McRaven",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Short (<200 pages)",
            "rating": 4.6,
            "description": "Little things that can change your life... and maybe the world, based on Navy SEAL wisdom."
        },
        {
            "title": "Show Your Work!",
            "author": "Austin Kleon",
            "genre": "Motivation",
            "mood": "Lighthearted & Fun",
            "length": "Short (<200 pages)",
            "rating": 4.4,
            "description": "Ten transformative rules for being found, staying creative, and sharing your passions."
        },
        {
            "title": "The 7 Habits of Highly Effective People",
            "author": "Stephen R. Covey",
            "genre": "Motivation",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.5,
            "description": "A holistic, integrated approach to solving personal and professional problems."
        },
        {
            "title": "Think and Grow Rich",
            "author": "Napoleon Hill",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.4,
            "description": "Classic motivational philosophy exploring the power of personal belief and clear goals."
        },
        {
            "title": "The Compound Effect",
            "author": "Darren Hardy",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Short (<200 pages)",
            "rating": 4.6,
            "description": "Jumpstart your income, your life, and your success with foundational daily choices."
        },
        {
            "title": "Grit: The Power of Passion and Perseverance",
            "author": "Angela Duckworth",
            "genre": "Motivation",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.5,
            "description": "Why the secret to outstanding achievement is not talent, but a special blend of passion and persistence."
        },
        {
            "title": "Mindset: The New Psychology of Success",
            "author": "Carol S. Dweck",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.6,
            "description": "How our attitude toward ability and learning shapes our success in school, work, and life."
        },
        {
            "title": "Awaken the Giant Within",
            "author": "Tony Robbins",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Long (>400 pages)",
            "rating": 4.4,
            "description": "A comprehensive guide to taking control of your emotional, physical, and financial destiny."
        },
        {
            "title": "The 5 Second Rule",
            "author": "Mel Robbins",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Short (<200 pages)",
            "rating": 4.5,
            "description": "A simple, transformative tool to beat hesitation and change your life using a 5-second countdown."
        },
        {
            "title": "Deep Work",
            "author": "Cal Newport",
            "genre": "Motivation",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.6,
            "description": "Rules for focused success in a distracted world by eliminating distractions and entering deep cognitive states."
        },
        {
            "title": "Essentialism",
            "author": "Greg McKeown",
            "genre": "Motivation",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.5,
            "description": "The disciplined pursuit of less to reclaim control of your choices and focus only on what truly matters."
        },
        {
            "title": "Extreme Ownership",
            "author": "Jocko Willink",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "U.S. Navy SEAL leadership principles applied to business and everyday life to drive accountability."
        },
        {
            "title": "The Psychology of Money",
            "author": "Morgan Housel",
            "genre": "Motivation",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "Timeless lessons on wealth, greed, and happiness through short stories exploring human behavior with money."
        },

        # ==========================================
        # MYSTERY / THRILLER (13 Books)
        # ==========================================
        {
            "title": "The Silent Patient",
            "author": "Alex Michaelides",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.5,
            "description": "A shocking psychological thriller about a woman's act of violence against her husband."
        },
        {
            "title": "And Then There Were None",
            "author": "Agatha Christie",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Short (<200 pages)",
            "rating": 4.6,
            "description": "Ten strangers are lured to an isolated island, where a mysterious killer begins eliminating them."
        },
        {
            "title": "The Girl with the Dragon Tattoo",
            "author": "Stieg Larsson",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Long (>400 pages)",
            "rating": 4.6,
            "description": "A disgraced journalist and a computer hacker investigate a decades-old disappearance."
        },
        {
            "title": "Gone Girl",
            "author": "Gillian Flynn",
            "genre": "Mystery / Thriller",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.4,
            "description": "On his fifth wedding anniversary, Nick Dunne's wife Amy mysteriously disappears, turning him into the prime suspect."
        },
        {
            "title": "The Da Vinci Code",
            "author": "Dan Brown",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Long (>400 pages)",
            "rating": 4.3,
            "description": "A murder in Paris leads a symbologist and a cryptologist on a trail of hidden religious secrets."
        },
        {
            "title": "The Guest List",
            "author": "Lucy Foley",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.2,
            "description": "A glamorous celebrity wedding on a remote island turns deadly as dark secrets come to light."
        },
        {
            "title": "The Maid",
            "author": "Nita Prose",
            "genre": "Mystery / Thriller",
            "mood": "Lighthearted & Fun",
            "length": "Medium (200-400 pages)",
            "rating": 4.3,
            "description": "An eccentric hotel maid finds herself embroiled in a murder mystery she is uniquely unequipped to solve."
        },
        {
            "title": "The Thursday Murder Club",
            "author": "Richard Osman",
            "genre": "Mystery / Thriller",
            "mood": "Lighthearted & Fun",
            "length": "Medium (200-400 pages)",
            "rating": 4.4,
            "description": "Four residents in a peaceful retirement village gather weekly to solve unsolved crimes—until a live murder lands on their doorstep."
        },
        {
            "title": "Shutter Island",
            "author": "Dennis Lehane",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.5,
            "description": "Two U.S. marshals investigate the disappearance of a murderess from a hospital for the criminally insane."
        },
        {
            "title": "The Woman in Cabin 10",
            "author": "Ruth Ware",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.1,
            "description": "A journalist on a luxury cruise witnesses a passenger being thrown overboard, but the ship's crew insists everyone is accounted for."
        },
        {
            "title": "The Shadow of the Wind",
            "author": "Carlos Ruiz Zafón",
            "genre": "Mystery / Thriller",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.7,
            "description": "A boy in 1945 Barcelona is drawn into a dark mystery surrounding an elusive author whose books are being systematically destroyed."
        },
        {
            "title": "Defending Jacob",
            "author": "William Landay",
            "genre": "Mystery / Thriller",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.3,
            "description": "An assistant district attorney's world is shattered when his 14-year-old son is charged with the murder of a classmate."
        },
        {
            "title": "The Sanatorium",
            "author": "Sarah Pearse",
            "genre": "Mystery / Thriller",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 3.9,
            "description": "An off-duty detective stays at a remote luxury hotel converted from an old sanatorium, where guests begin turning up dead in a blizzard."
        },

        # ==========================================
        # NON-FICTION / HISTORY (19 Books)
        # ==========================================
        {
            "title": "Sapiens: A Brief History of Humankind",
            "author": "Yuval Noah Harari",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.7,
            "description": "A bold exploration of how Homo sapiens came to rule the Earth through shared myths and culture."
        },
        {
            "title": "Man's Search for Meaning",
            "author": "Viktor E. Frankl",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Short (<200 pages)",
            "rating": 4.8,
            "description": "Psychiatrist Viktor Frankl's memoir detailing his experiences in Nazi concentration camps and his psychological theories."
        },
        {
            "title": "Educated",
            "author": "Tara Westover",
            "genre": "Non-Fiction / History",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.7,
            "description": "A memoir about a young girl who escapes a survivalist family in rural Idaho to earn a PhD from Cambridge."
        },
        {
            "title": "A Brief History of Time",
            "author": "Stephen Hawking",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Short (<200 pages)",
            "rating": 4.6,
            "description": "An exploration of cosmology, from the Big Bang to black holes, written for non-specialist readers."
        },
        {
            "title": "Born a Crime",
            "author": "Trevor Noah",
            "genre": "Non-Fiction / History",
            "mood": "Lighthearted & Fun",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "The provocative, uplifting, and wildly funny memoir of a boy born in South Africa during apartheid."
        },
        {
            "title": "Outliers: The Story of Success",
            "author": "Malcolm Gladwell",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.5,
            "description": "An examination of what makes high-achievers different, focusing on culture, family, and generation."
        },
        {
            "title": "Bad Blood",
            "author": "John Carreyrou",
            "genre": "Non-Fiction / History",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.8,
            "description": "The full inside story of Theranos, the multibillion-dollar biotech startup, by the investigative journalist who broke it."
        },
        {
            "title": "A Short History of Nearly Everything",
            "author": "Bill Bryson",
            "genre": "Non-Fiction / History",
            "mood": "Lighthearted & Fun",
            "length": "Long (>400 pages)",
            "rating": 4.7,
            "description": "A witty and accessible journey through the history of science, from the Big Bang to the rise of civilization."
        },
        {
            "title": "Thinking, Fast and Slow",
            "author": "Daniel Kahneman",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.6,
            "description": "Nobel laureate Daniel Kahneman explains the two systems that drive how we think and make choices."
        },
        {
            "title": "The Wright Brothers",
            "author": "David McCullough",
            "genre": "Non-Fiction / History",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.7,
            "description": "The dramatic story of Wilbur and Orville Wright and how they achieved the world's first successful airplane flight."
        },
        {
            "title": "Killers of the Flower Moon",
            "author": "David Grann",
            "genre": "Non-Fiction / History",
            "mood": "Thrilling & Fast-paced",
            "length": "Medium (200-400 pages)",
            "rating": 4.6,
            "description": "The true story of the Osage Indian murders in the 1920s and the birth of the FBI."
        },
        {
            "title": "Guns, Germs, and Steel",
            "author": "Jared Diamond",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Long (>400 pages)",
            "rating": 4.3,
            "description": "A sweeping inquiry into why human societies developed at vastly different rates across various continents."
        },
        {
            "title": "The Immortal Life of Henrietta Lacks",
            "author": "Rebecca Skloot",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.6,
            "description": "The remarkable story of a poor tobacco farmer whose cancer cells—taken without her knowledge—revolutionized modern medicine."
        },
        {
            "title": "I Am Malala",
            "author": "Malala Yousafzai",
            "genre": "Non-Fiction / History",
            "mood": "Inspiring & Educational",
            "length": "Medium (200-400 pages)",
            "rating": 4.7,
            "description": "The memoir of a young girl shot by the Taliban for advocating girls' education who became the youngest Nobel Peace Prize laureate."
        },
        {
            "title": "Into the Wild",
            "author": "Jon Krakauer",
            "genre": "Non-Fiction / History",
            "mood": "Adventurous",
            "length": "Short (<200 pages)",
            "rating": 4.4,
            "description": "The true, tragic story of Christopher McCandless, a young man who gave up his savings to hitchhike into the Alaskan wilderness."
        },
        {
            "title": "Quiet: The Power of Introverts in a World That Can't Stop Talking",
            "author": "Susan Cain",
            "genre": "Non-Fiction / History",
            "mood": "Thoughtful & Deep",
            "length": "Medium (200-400 pages)",
            "rating": 4.5,
            "description": "An eye-opening look at how society undervalues introverts and how much wisdom and capability they contribute."
        }
    ]
