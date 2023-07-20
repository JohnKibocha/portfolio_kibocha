from models import Skill

# Create 10 records for the skills model
Skill.objects.create(
    name='Android Development',
    progress=80,
    projects=[
        {'name': 'Judiciary Management System', 'url': 'https://judiciary.com'},
        {'name': 'Fitness Tracker', 'url': 'https://fit.com'},
        {'name': 'Weather App', 'url': 'https://weather.com'}
    ],
    tools=['Java', 'Android Studio', 'Firebase', 'Google Maps API']
)

Skill.objects.create(
    name='Web Development',
    progress=70,
    projects=[
        {'name': 'Blog Site', 'url': 'https://blog.com'},
        {'name': 'E-commerce Site', 'url': 'https://shop.com'},
        {'name': 'Social Media Site', 'url': 'https://social.com'}
    ],
    tools=['HTML', 'CSS', 'JavaScript', 'Django', 'Bootstrap']
)

Skill.objects.create(
    name='Machine Learning',
    progress=60,
    projects=[
        {'name': 'Image Classification', 'url': 'https://image.com'},
        {'name': 'Sentiment Analysis', 'url': 'https://sentiment.com'},
        {'name': 'Recommendation System', 'url': 'https://recommend.com'}
    ],
    tools=['Python', 'TensorFlow', 'Keras', 'Scikit-learn', 'Pandas']
)

Skill.objects.create(
    name='Data Science',
    progress=50,
    projects=[
        {'name': 'Data Visualization', 'url': 'https://visual.com'},
        {'name': 'Data Cleaning', 'url': 'https://clean.com'},
        {'name': 'Data Analysis', 'url': 'https://analyze.com'}
    ],
    tools=['Python', 'NumPy', 'Matplotlib', 'Seaborn', 'Jupyter Notebook']
)

Skill.objects.create(
    name='Game Development',
    progress=40,
    projects=[
        {'name': 'Platformer Game', 'url': 'https://platform.com'},
        {'name': 'Shooter Game', 'url': 'https://shoot.com'},
        {'name': 'Puzzle Game', 'url': 'https://puzzle.com'}
    ],
    tools=['C#', 'Unity', 'Blender', 'Photoshop']
)

Skill.objects.create(
    name='UI/UX Design',
    progress=30,
    projects=[
        {'name': 'Mobile App Design', 'url': 'https://mobile.com'},
        {'name': 'Web App Design', 'url': 'https://web.com'},
        {'name': 'Logo Design', 'url': 'https://logo.com'}
    ],
    tools=['Figma', 'Sketch', 'Adobe XD']
)

Skill.objects.create(
    name='Blockchain Development',
    progress=20,
    projects=[
        {'name': 'Cryptocurrency Exchange',
'url':
'https://crypto.com'},
        {'name':
'Smart Contract Development',
'url':
'https://smart.com'},
        {'name':
'Decentralized Application',
'url':
'https://dapp.com'}
    ],
    tools=['Solidity','Ethereum','Truffle','Web3.js']
)

Skill.objects.create(
    name='Cybersecurity',
    progress=10,
    projects=[
        {'name':'Penetration Testing',
'url':
'https://penetrate.com'},
        {'name':'Malware Analysis',
'url':
'https://malware.com'},
        {'name':'Ethical Hacking',
'url':
'https://hack.com'}
    ],
    tools=['Kali Linux','Metasploit','Wireshark','Nmap']
)

Skill.objects.create(
    name='Cloud Computing',
    progress=90,
    projects=[
        {'name':'Cloud Storage',
'url':
'https://storage.com'},
        {'name':'Cloud Hosting',
'url':
'https://hosting.com'},
        {'name':'Cloud Computing',
'url':
'https://compute.com'}
    ],
    tools=['AWS','Google Cloud','Azure','Docker','Kubernetes']
)

Skill.objects.create(
    name='Artificial Intelligence',
    progress=100,
    projects=[
        {'name':'Natural Language Processing',
'url':
'https://nlp.com'},
        {'name':'Computer Vision',
'url':
'https://vision.com'},
        {'name':'Speech Recognition',
'url':
'https://speech.com'}
    ],
    tools=['Python','PyTorch','OpenCV','NLTK','SpaCy']
)
