from fasthtml.common import *
import os

# Create static directory if it doesn't exist
os.makedirs('static', exist_ok=True)

# Initialize app with static directory
app, rt = fast_app(static_dir='static')

# Common headers
def get_headers():
    return [
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Title("High Order Software | Consulting Services"),
        Link(rel="icon", href="/static/favicon.ico", type="image/x-icon"),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"),
        Style("""
            .hero {
                background-color: #f8f9fa;
                padding: 5rem 0;
                margin-bottom: 2rem;
            }
            .service-card {
                height: 100%;
                transition: transform 0.3s;
            }
            .service-card:hover {
                transform: translateY(-5px);
            }
        """),
        Script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js")
    ]

# Service data
services = [
    ("LLM Productization", "Turn AI research into scalable, production-ready products and services."),
    ("Speech to Text Analysis", "Advanced speaker diarization and transcription solutions."),
    ("Cloud Architecture", "Scalable, resilient cloud infrastructure design and implementation."),
    ("Marketing Automation", "Email marketing systems and customer journey optimization."),
    ("Financial Market Analysis", "S&P 500 and broader market trend analysis and visualization."),
    ("Air Quality APIs", "Development of reliable air quality data collection and reporting systems."),
    ("Career Consulting", "Technical career guidance and professional development planning."),
    ("Enterprise IT Architecture", "Strategic technology planning and implementation for large organizations."),
    ("IoT Solutions", "Device management and cloud integration for connected systems.")
]

@rt('/')
def index():
    return Html(
        *get_headers(),
        Body(
            # Hero Section
            Div(
                Div(
                    Img(src="/static/public/hos.png", alt="High Order Software Logo", cls="mb-3", style="max-height: 360px;"),
                    H1("High Order Software", cls="display-4 fw-bold"),
                    P("Advanced Software Solutions for Complex Business Challenges", cls="lead"),
                    P("Led by:", cls="mt-3"),
                    P("David Russell, Partner and Lead Developer", cls="mb-0"),
                    P("A.G. Russell, Partner and Enterprise IT Architect", cls="mb-3"),
                    cls="container"
                ),
                cls="hero text-center"
            ),
            # Services Section
            Div(
                H2("Our Services", cls="text-center mb-4"),
                Div(
                    *[Div(
                        Div(
                            Div(
                                H5(service[0], cls="card-title"),
                                P(service[1], cls="card-text"),
                                cls="card-body"
                            ),
                            cls="card service-card shadow-sm"
                        ),
                        cls="col-md-4"
                    ) for service in services],
                    cls="row g-4"
                ),
                cls="container mb-5"
            ),
            # Call to Action
            Div(
                Div(
                    H3("Ready to transform your business?"),
                    P("Contact us to discuss how High Order Software can help with your next project."),
                    A("Get in touch", href="mailto:david@davidrussell.dev", cls="btn btn-primary mt-2"),
                    cls="col text-center py-4"
                ),
                cls="container"
            ),
            # Footer
            Div(
                Div(
                    P("© 2025 High Order Software. All rights reserved."),
                    cls="container text-center"
                ),
                cls="bg-dark text-white mt-5 py-4"
            )
        )
    )

@rt('/favicon.ico')
def favicon():
    if not os.path.exists('static/favicon.ico'):
        with open('static/favicon.ico', 'wb') as f:
            f.write(b'')
    return FileResponse('static/favicon.ico')

@rt('/installHook.js.map')
def install_hook_map():
    if not os.path.exists('static/installHook.js.map'):
        with open('static/installHook.js.map', 'wb') as f:
            content = b'{"version":3,"file":"installHook.js","sourceRoot":"","sources":[],"names":[],"mappings":""}'
            f.write(content)
    return FileResponse('static/installHook.js.map')

# Start the server
serve()