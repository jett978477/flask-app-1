📝 Application Purpose
The purpose of this application is to provide a real-time, web-based chat environment that mimics the aesthetic and functionality of the original Nintendo DS PictoChat software. It allows multiple users to:

Join specific chat channels (Rooms A, B, C, and D).

Communicate in real-time using WebSockets via Flask-SocketIO.

Customize their identity through a Settings page that allows for name changes and custom text colors.

Monitor network performance through a built-in latency (ping) tracker for every message sent.

Interact with a custom command system (e.g., /help, /ping, /whisper).

🤖 Use of Generative AI
This application was developed with the assistance of Generative AI (Gemini) in the following ways:

System Architecture: AI assisted in designing the file structure to meet specific project requirements, including the use of a base.html template for consistent navigation across the Dashboard and Settings pages.

Real-Time Logic: AI provided the boilerplate code for the SocketIO implementation, specifically handling room "join" events and broadcasting messages with timestamps for latency calculation.

Frontend Styling: AI was used to generate the CSS required to achieve the "PictoChat" aesthetic, including the pixel font integration, scanline background effects, and the vertical room-list layout.

Debugging & Troubleshooting: AI assisted in resolving environment-specific errors, such as ModuleNotFoundError within virtual environments, and helped debug Jinja2 template rendering issues.