from django.http import HttpResponse
import datetime


def current_datetime(request):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Date and Time</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                line-height: 1.6;
            }}
            header {{
                background-color: #f4f4f4;
                padding: 10px 20px;
                border-bottom: 2px solid #ccc;
            }}
            footer {{
                margin-top: 20px;
                text-align: center;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to My Testing Page</h1>
            <p>It is a simple page for testing purposes.</p>
        </header>
        <main>
            <p>The current time is: <strong id="time"></strong>.</p>
            <script>
                function updateTime() {{
                    const now = new Date();
                    const timeString = now.toLocaleTimeString();
                    document.getElementById('time').innerText = timeString;
                }}
                setInterval(updateTime, 1000); // Update every second
            </script>
            <section>
                <h2>Sample Content</h2>
                <p>This is a paragraph for testing styles and layout.</p>
                <ul>
                    <li>Test item 1</li>
                    <li>Test item 2</li>
                    <li>Test item 3</li>
                </ul>
            </section>
        </main>
        <footer>
            <p>Testing Page &copy 2024</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html)
