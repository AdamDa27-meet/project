import flet as ft

def main(page: ft.Page): 

    page.title = "Color Game" 
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    def colorchange(e):
            canvas.bgcolor = e.control.value
            canvas.image = None
            canvas.update()

    def mesg(e):
        comment = user_input.value.strip().lower()

        if comment == "rainbow":
            canvas.bgcolor = "#800080"
            displayed_message.value = "You found the rainbow secret! 🌈"

        elif comment == "green":
            canvas.bgcolor = "#00FF00"
            displayed_message.value = "Green is the best color! 💚"

        elif comment == "hello":
            displayed_message.value = "Hello! Welcome to the Color Game!"

        elif comment:
            displayed_message.value = f"Your comment: {user_input.value}"

        else:
            displayed_message.value = "Please enter a comment."

        canvas.update()
        page.update()

    def title_hover(e):
        if e.data == "true":
            title_text.value = "You found me!"
            title_text.color = "#FF00FF"
        else:
            title_text.value = "Color Game"
            title_text.color = "#0D0F11"

        title_text.update()

    
    user_input = ft.TextField(
        label = ft.Text(
                                  "Leave a comment or suggestion:", 
                                  color = "#0D0F11"),
        color = "#040D16",
        width = 400,
        border_color = "#0D0F11",
        border_width = 2,
    )

    displayed_message = ft.Text(
        "",
        size = 15,
        color = "#000000",
    )

    title_text = ft.Text(
        "Color Game",
        size=35,
        weight=ft.FontWeight.BOLD,
        color="#0D0F11",
        text_align=ft.TextAlign.CENTER,
    )

    canvas = ft.Container(
        expand = True,
        width = 2000,
        bgcolor = '#63D4B4',
        padding = 15,
        border_radius = 15,
        content = ft.Column(
            controls=[
                ft.Container(
                    content=title_text,
                    width=page.width,
                    height=60,
                    alignment=ft.Alignment.CENTER,
                    on_hover=title_hover,
                ),
                
                ft.Text(
                    "Explore the colors and leave a comment.",
                    size = 15,
                    text_align = ft.TextAlign.CENTER,
                    color = "#0D0F11",  
                    ),  
                ft.Dropdown(
                    label = ft.Text(
                          "Choose a background color of your liking", 
                          color = "#0D0F11"),
                    border_color = "#0D0F11",
                    border_width = 2,
                    options = [
                        ft.dropdown.Option("Red", "#FF0000"),
                        ft.dropdown.Option("Green", "#00FF00"),
                        ft.dropdown.Option("Blue", "#0000FF"),
                        ft.dropdown.Option("Yellow", "#FFFF00"),
                        ft.dropdown.Option("Purple", "#800080"),
                        ft.dropdown.Option("Orange", "#FFA500"),
                        ft.dropdown.Option("Pink", "#FFC0CB"),
                        ft.dropdown.Option("Cyan", "#00FFFF"),
                        ft.dropdown.Option("Lime", "#00FF00"),
                        ft.dropdown.Option("Teal", "#008080"),
                        ft.dropdown.Option("White", "#FFFFFF"), 
                    ],
                    width = 2000,
                    on_select = colorchange,
                    value = "000000"
                ),
                user_input,

                ft.Button(
                     content = ft.Text( "Submit", color = "#386899",), 
                     on_click = mesg,

                ),
                displayed_message,

                
                
            ],
            
        )
    )
    

    

    
        
    page.add(
        canvas
          
    )

ft.run(main)