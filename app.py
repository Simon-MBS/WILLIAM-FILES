from flask import Flask, render_template
# create an instance from the class
app =Flask(__name__)
PROJECTS={
    'project-one':{
        'id' : 'project-one',
        'tittle' : 'E-Commerce platform',
        'short_description' : 'A reliable security systems partner',
        'image' : 'p1.webp',
        'technologies' : ['flask', 'React', 'postgreSQL', 'Stripe API '],
        'description' : 'Our security solutions deliver end-to-end protection for commercial, industrial, and residential environments, combining robust hardware with intelligent software.We design, install, and maintain CCTV surveillance systems, access control solutions, biometric time & attendance, alarm systems, electric fences, automatic gates, and turnstile barriers. Each solution is customized through site surveys and risk assessments to ensure maximum coverage, reliability, and compliance. Our systems support remote monitoring, real-time alerts, and centralized management, enabling clients to control access, deter threats, and improve operational efficiency. Backed by professional installation and ongoing maintenance, we provide secure, scalable, and future-ready security infrastructure.',
        'features' : [
            'user authentication and authorization',
            'Product catalogue with search and filtering',
            'Shopping cart and checkout system',
            'Stripe payment integration',
            'Admin dashboard for inventory management',
            'order tracking and email notification'
        ],
        'challenges' : 'The main challenge was implementing a source payment flow while maintaining',
        'github' : 'https://github.com/',
        'live_demo' : 'https://github.com/Simon-MBS/PORTFOLIO'

    },
    'project-two':{
        'id' : 'project-two',
        'tittle' : 'GYM Management System',
        'short_description' : 'A colaborative task amangement tool for Gyms',
        'image' : 'p2.jpg',
        'technologies' : ['flask', 'React', 'postgreSQL', 'Stripe API '],
        'description' : 'Our Gym management solutions deliver end-to-end protection for commercial, industrial, and residential environments, combining robust hardware with intelligent software.We design, install, and maintain CCTV surveillance systems, access control solutions, biometric time & attendance, alarm systems, electric fences, automatic gates, and turnstile barriers. Each solution is customized through site surveys and risk assessments to ensure maximum coverage, reliability, and compliance. Our systems support remote monitoring, real-time alerts, and centralized management, enabling clients to control access, deter threats, and improve operational efficiency. Backed by professional installation and ongoing maintenance, we provide secure, scalable, and future-ready security infrastructure.',
        'features' : [
            'Real time member management',
            'Product catalogue with search and filtering',
            'Gym class categories',
            'Milti payment integration',
            'Admin dashboard for inventory management',
            'personnalised gym member management'
        ],
        'challenges' : 'The main challenge was implementing a source payment flow',
        'github' : 'https://github.com/',
        'live_demo' : 'https://github.com/Simon-MBS/PORTFOLIO'

    }
}
#routes/
@app.route('/')
def index():
    return render_template('index.html')
#other routes
# about rouete

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():

    #portifolio details
    projects = [ #pass the simplified project data here
        {
            'id' : project['id'],
            'tittle' : project['tittle'],
            'description' : project['short_description'],
            'image' : project['image']
        }
        

        for project in PROJECTS.values()
    ]


    return render_template('portfolio.html',projects=projects)

# add a rouet to access each project by ID
@app.route('/project/<project_id>')
def project_details(project_id):
    # get a specific project
    project= PROJECTS.get(project_id)
    if project is None:
        abort(404)
    return render_template('project_details.html', project=project)
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)