from dash import html

def generate_buttons(button_names):
    buttons = []
    for name in button_names:
        button = html.Button(name, id=f"button-{name}",style={'font-size': '18px', 'padding': '6px 10px','margin-left':'10px','margin-right':'10px'})
        buttons.append(button)
    return buttons